#!/usr/bin/env node
/**
 * Post-process SVG from beautiful-mermaid: replace edge label boxes with text
 * that follows the edge line (textPath). Fixes: upside-down text, centering, font size.
 * Also: shorten polylines that end inside a node so the arrow stays visible;
 * soften font-weight (600→500, 500→400).
 *
 * Usage: node scripts/svg_edge_labels_along_path.mjs -f docs/diagrams/ime.svg -o docs/diagrams/ime.svg
 */

import { readFileSync, writeFileSync } from 'fs';

const EDGE_LABEL_FONT_SIZE_MAX = 11;
const EDGE_LABEL_FONT_SIZE_MIN = 8;
const EDGE_LABEL_CHAR_WIDTH_EM = 0.58;
/** Produženje putanje teksta na oba kraja (0.35 = 35% duljine segmenta svaki krak) – više prostora za labelu */
const EDGE_PATH_EXTEND_RATIO = 0.35;
const EDGE_LABEL_FILL = 'var(--_text)';
const EDGE_LABEL_STYLE_BASE = 'letter-spacing:0.03em';
/** Okvir oko cijelog dijagrama (viewBox) – konzistentan izgled svih SVG-ova */
const FRAME_STROKE = 'var(--_line)';
const FRAME_STROKE_WIDTH = 1;

function parseArgs() {
  const args = process.argv.slice(2);
  let file = null;
  let output = null;
  for (let i = 0; i < args.length; i++) {
    if (args[i] === '-f' && args[i + 1]) file = args[++i];
    else if (args[i] === '-o' && args[i + 1]) output = args[++i];
  }
  return { file, output };
}

function parsePoints(pointsStr) {
  return pointsStr.trim().split(/\s+/).map((s) => s.split(',').map(Number));
}

function dist(a, b) {
  return Math.hypot(b[0] - a[0], b[1] - a[1]);
}

/**
 * Build path for textPath: use only the middle segment of the polyline,
 * oriented so text is not upside down. Returns { d, length }.
 */
function middleSegmentPathDAndLength(pointsStr) {
  const pts = parsePoints(pointsStr);
  if (pts.length < 2) {
    const d = pointsToPathD(pointsStr);
    const len = pts.length >= 2 ? dist(pts[0], pts[1]) : 0;
    const center = pts.length >= 2 ? [(pts[0][0] + pts[1][0]) / 2, (pts[0][1] + pts[1][1]) / 2] : [0, 0];
    return { d, length: len, center };
  }

  const lengths = [];
  let total = 0;
  for (let i = 0; i < pts.length - 1; i++) {
    const L = dist(pts[i], pts[i + 1]);
    lengths.push(L);
    total += L;
  }
  if (total === 0) {
    const c = [(pts[0][0] + pts[1][0]) / 2, (pts[0][1] + pts[1][1]) / 2];
    return { d: `M ${pts[0][0]} ${pts[0][1]} L ${pts[1][0]} ${pts[1][1]}`, length: 0, center: c };
  }

  const mid = total * 0.5;
  let acc = 0;
  let segIndex = 0;
  for (let i = 0; i < lengths.length; i++) {
    acc += lengths[i];
    if (acc >= mid) {
      segIndex = i;
      break;
    }
  }

  let p0 = pts[segIndex];
  let p1 = pts[segIndex + 1];
  let dx = p1[0] - p0[0];
  let dy = p1[1] - p0[1];
  const segmentLength = dist(p0, p1);

  if (dy < 0 || (dy === 0 && dx < 0)) {
    [p0, p1] = [p1, p0];
    dx = -dx;
    dy = -dy;
  }

  const center = [(p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2];

  if (segmentLength <= 0) {
    return { d: `M ${p0[0]} ${p0[1]} L ${p1[0]} ${p1[1]}`, length: 0, center };
  }

  const extendBy = segmentLength * EDGE_PATH_EXTEND_RATIO;
  const ux = dx / segmentLength;
  const uy = dy / segmentLength;
  const q0 = [p0[0] - extendBy * ux, p0[1] - extendBy * uy];
  const q1 = [p1[0] + extendBy * ux, p1[1] + extendBy * uy];
  const extendedLength = segmentLength + 2 * extendBy;
  const d = `M ${q0[0]} ${q0[1]} L ${q1[0]} ${q1[1]}`;
  return { d, length: extendedLength, center };
}

function pointsToPathD(pointsStr) {
  const pts = parsePoints(pointsStr);
  if (pts.length === 0) return '';
  let d = `M ${pts[0][0]} ${pts[0][1]}`;
  for (let i = 1; i < pts.length; i++) d += ` L ${pts[i][0]} ${pts[i][1]}`;
  return d;
}

function parseRectAttrs(attrsStr) {
  const x = attrsStr.match(/\bx="([^"]+)"/);
  const y = attrsStr.match(/\by="([^"]+)"/);
  const w = attrsStr.match(/\bwidth="([^"]+)"/);
  const h = attrsStr.match(/\bheight="([^"]+)"/);
  return {
    x: x ? Number(x[1]) : 0,
    y: y ? Number(y[1]) : 0,
    width: w ? Number(w[1]) : 0,
    height: h ? Number(h[1]) : 0,
  };
}

/** True if (px, py) is inside rect (x, y, width, height). */
function pointInRect(px, py, r) {
  return px >= r.x && px <= r.x + r.width && py >= r.y && py <= r.y + r.height;
}

/** Node rects: rect with rx="0" and height 36 (node boxes), exclude huge containers. */
function getNodeRects(svgStr) {
  const rects = [];
  const re = /<rect([^>]*)\srx="0"[^>]*\sry="0"[^>]*\/>/g;
  let m;
  while ((m = re.exec(svgStr)) !== null) {
    const r = parseRectAttrs(m[1]);
    if (r.height >= 35 && r.height <= 50 && r.width >= 50) rects.push(r);
  }
  return rects;
}

const ARROW_GAP = 10;

/** If the polyline's last point is inside a node rect, shorten so it ends just outside. */
function shortenPolylinePoints(pointsStr, nodeRects) {
  const pts = parsePoints(pointsStr);
  if (pts.length < 2 || nodeRects.length === 0) return pointsStr;
  const last = pts[pts.length - 1];
  const prev = pts[pts.length - 2];
  const rx = last[0];
  const ry = last[1];
  for (const r of nodeRects) {
    if (!pointInRect(rx, ry, r)) continue;
    const dx = prev[0] - last[0];
    const dy = prev[1] - last[1];
    const len = Math.hypot(dx, dy) || 1;
    const ux = dx / len;
    const uy = dy / len;
    const candidates = [];
    if (Math.abs(ux) > 1e-6) {
      if (ux < 0) candidates.push((r.x - rx) / ux);
      else candidates.push((r.x + r.width - rx) / ux);
    }
    if (Math.abs(uy) > 1e-6) {
      if (uy < 0) candidates.push((r.y - ry) / uy);
      else candidates.push((r.y + r.height - ry) / uy);
    }
    const tMin = Math.min(...candidates.filter((t) => t > 0));
    if (tMin === Infinity || !(tMin > 0)) continue;
    const exit = [rx + (tMin + ARROW_GAP) * ux, ry + (tMin + ARROW_GAP) * uy];
    const newPts = [...pts.slice(0, -1), exit];
    return newPts.map((p) => `${p[0]},${p[1]}`).join(' ');
  }
  return pointsStr;
}

function processSvg(svg) {
  let work = svg;
  work = work.replace(/\s*<path id="edge-path-\d+"[^/]*\/>\s*/g, '');

  const nodeRects = getNodeRects(work);

  const polylineRe = /<polyline[^>]*\spoints="([^"]+)"[^>]*\/>/g;
  const polylineMatches = [];
  let m;
  while ((m = polylineRe.exec(work)) !== null) polylineMatches.push({ full: m[0], points: m[1] });

  for (const { full, points } of polylineMatches) {
    const shortened = shortenPolylinePoints(points, nodeRects);
    if (shortened !== points) {
      const newFull = full.split(points).join(shortened);
      work = work.split(full).join(newFull);
    }
  }

  const polylineRe2 = /<polyline[^>]*\spoints="([^"]+)"[^>]*\/>/g;
  const polylines = [];
  while ((m = polylineRe2.exec(work)) !== null) polylines.push(m[1]);

  const pathData = polylines.map((pts) => middleSegmentPathDAndLength(pts));
  const segmentLengths = pathData.map((p) => p.length);
  const segmentCenters = pathData.map((p) => p.center);
  const pathDefs = pathData
    .map((p, i) => `<path id="edge-path-${i}" d="${p.d}" fill="none"/>`)
    .join('\n  ');
  let out = work.replace(/<\/defs>/, `  ${pathDefs}\n</defs>`);

  /** Font size tako da cijela labela stane na segment (duljina * 0.9, cap/floor). */
  const fontForLabel = (polylineIndex, labelLength) => {
    const len = segmentLengths[polylineIndex];
    if (len === undefined || labelLength <= 0) return EDGE_LABEL_FONT_SIZE_MAX;
    const usableLength = len * 0.9;
    const fontSize = usableLength / (labelLength * EDGE_LABEL_CHAR_WIDTH_EM);
    const clamped = Math.max(EDGE_LABEL_FONT_SIZE_MIN, Math.min(EDGE_LABEL_FONT_SIZE_MAX, Math.round(fontSize)));
    return clamped;
  };

  // Match label blocks (rect with rx="4" ry="4" + text); capture rect attrs and text for position-based matching
  const edgeLabelBlockRe = /<rect([^>]*)\srx="4"[^>]*\sry="4"[^>]*\/>\s*<text[^>]*font-size="11"[^>]*fill="var\(--_text-muted\)"[^>]*>([\s\S]*?)<\/text>/g;
  const labelBlocks = [];
  let blockMatch;
  while ((blockMatch = edgeLabelBlockRe.exec(work)) !== null) {
    const rect = parseRectAttrs(blockMatch[1]);
    const centerX = rect.x + rect.width / 2;
    const centerY = rect.y + rect.height / 2;
    labelBlocks.push({
      fullMatch: blockMatch[0],
      center: [centerX, centerY],
      text: blockMatch[2].trim(),
    });
  }

  // Assign each label to the closest polyline (that doesn't have a label yet)
  const assignedPolyline = new Set();
  const blockToPolylineIndex = [];
  for (const block of labelBlocks) {
    let bestIdx = -1;
    let bestDist = Infinity;
    for (let i = 0; i < segmentCenters.length; i++) {
      if (assignedPolyline.has(i)) continue;
      const d = dist(block.center, segmentCenters[i]);
      if (d < bestDist) {
        bestDist = d;
        bestIdx = i;
      }
    }
    if (bestIdx >= 0) {
      assignedPolyline.add(bestIdx);
      blockToPolylineIndex.push(bestIdx);
    } else {
      blockToPolylineIndex.push(0);
    }
  }

  // Replace each label block with textPath on the assigned polyline (use new regex - previous was consumed by exec)
  const edgeLabelBlockRe2 = /<rect([^>]*)\srx="4"[^>]*\sry="4"[^>]*\/>\s*<text[^>]*font-size="11"[^>]*fill="var\(--_text-muted\)"[^>]*>([\s\S]*?)<\/text>/g;
  let blockIdx = 0;
  out = out.replace(edgeLabelBlockRe2, () => {
    const polylineIndex = blockToPolylineIndex[blockIdx] ?? blockIdx;
    const label = labelBlocks[blockIdx]?.text ?? '';
    blockIdx++;
    const fs = fontForLabel(polylineIndex, label.length);
    return `<text font-size="${fs}" font-weight="400" fill="${EDGE_LABEL_FILL}" style="${EDGE_LABEL_STYLE_BASE}"><textPath href="#edge-path-${polylineIndex}" startOffset="50%" text-anchor="middle">${label}</textPath></text>`;
  });

  // Re-process already post-processed SVGs (textPath with our font sizes)
  out = out.replace(
    /<text[^>]*font-size="(?:1[0-9]|[89])"[^>]*><textPath href="#edge-path-(\d+)"[^>]*>([\s\S]*?)<\/textPath><\/text>/g,
    (_, pathId, label) => {
      const i = parseInt(pathId, 10);
      const text = label.trim();
      const fs = fontForLabel(i, text.length);
      return `<text font-size="${fs}" font-weight="400" fill="${EDGE_LABEL_FILL}" style="${EDGE_LABEL_STYLE_BASE}"><textPath href="#edge-path-${pathId}" startOffset="50%" text-anchor="middle">${text}</textPath></text>`;
    }
  );

  // Konzistentan okvir: rect prema viewBox (umetnuto nakon </defs>) – samo ako ga još nema
  const viewBoxMatch = out.match(/\bviewBox=["']([^"']+)["']/);
  if (viewBoxMatch) {
    const parts = viewBoxMatch[1].trim().split(/\s+/);
    if (parts.length >= 4) {
      const [x, y, w, h] = parts.map(Number);
      const afterDefs = out.slice(out.indexOf('</defs>'), out.indexOf('</defs>') + 400);
      const hasFrame = /fill="none"[^>]*stroke="var\(--_line\)"/.test(afterDefs) || /stroke="var\(--_line\)"[^>]*fill="none"/.test(afterDefs);
      if (!hasFrame) {
        const frameRect = `<rect x="${x}" y="${y}" width="${w}" height="${h}" fill="none" stroke="${FRAME_STROKE}" stroke-width="${FRAME_STROKE_WIDTH}"/>`;
        out = out.replace('</defs>', `</defs>\n  ${frameRect}`);
      }
    }
  }

  // Ublaženi font: 600→500 (naslov), 500→400 (čvorovi) da ne izgleda prejako
  out = out.replace(/font-weight="600"/g, 'font-weight="__W5__"');
  out = out.replace(/font-weight="500"/g, 'font-weight="400"');
  out = out.replace(/font-weight="__W5__"/g, 'font-weight="500"');

  return out;
}

function main() {
  const { file, output } = parseArgs();
  if (!file || !output) {
    console.error('Usage: node svg_edge_labels_along_path.mjs -f <input.svg> -o <output.svg>');
    process.exit(1);
  }
  const input = readFileSync(file, 'utf8');
  const result = processSvg(input);
  writeFileSync(output, result, 'utf8');
}

main();
