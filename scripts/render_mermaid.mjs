#!/usr/bin/env node
/**
 * Render Mermaid diagrams with beautiful-mermaid (SVG or ASCII).
 * Usage:
 *   node scripts/render_mermaid.mjs -f path/to/diagram.mmd [-o out.svg] [--ascii] [--theme tokyo-night]
 *   echo "graph LR; A --> B" | node scripts/render_mermaid.mjs [--ascii]
 */

import { readFileSync, readFile } from 'fs';
import { createInterface } from 'readline';
import { renderMermaid, renderMermaidAscii, THEMES } from 'beautiful-mermaid';

const BOOK_SVG_VARS = [
  '--bg:#FFFFFF',
  '--fg:#1b2a4a',
  '--line:#5c7caa',
  '--accent:#5c7caa',
  '--surface:#dceefb',
  '--border:#4a86c8',
  '--muted:#6c84a3',
].join(';');

function getStdin() {
  return new Promise((resolve) => {
    const rl = createInterface({ input: process.stdin });
    const lines = [];
    rl.on('line', (line) => lines.push(line));
    rl.on('close', () => resolve(lines.join('\n')));
  });
}

function parseArgs() {
  const args = process.argv.slice(2);
  const out = { file: null, output: null, ascii: false, theme: null };
  for (let i = 0; i < args.length; i++) {
    if (args[i] === '-f' && args[i + 1]) {
      out.file = args[++i];
    } else if (args[i] === '-o' && args[i + 1]) {
      out.output = args[++i];
    } else if (args[i] === '--ascii') {
      out.ascii = true;
    } else if (args[i] === '--theme' && args[i + 1]) {
      out.theme = args[++i];
    }
  }
  return out;
}

function stripFrontmatter(source) {
  if (!source.startsWith('---')) {
    return source;
  }
  const lines = source.split(/\r?\n/);
  if (lines.length < 3 || lines[0].trim() !== '---') {
    return source;
  }
  let end = -1;
  for (let i = 1; i < lines.length; i++) {
    if (lines[i].trim() === '---') {
      end = i;
      break;
    }
  }
  if (end === -1) {
    return source;
  }
  return lines.slice(end + 1).join('\n').trimStart();
}

function stripLeadingDirectives(source) {
  let text = source.trimStart();
  text = text.replace(/^%%\{[\s\S]*?\}%%\s*/m, '');
  return text;
}

function stripHtmlMarkup(source) {
  return source
    .replace(/<br\s*\/?>/gi, ' ')
    .replace(/<\/?(?:i|b|em|strong)>/gi, '');
}

function stripQuotedLabels(source) {
  return source
    .replace(/\[\s*"([^"\n]+?)"\s*\]/g, '[$1]')
    .replace(/\(\(\s*"([^"\n]+?)"\s*\)\)/g, '(($1))')
    .replace(/\(\s*"([^"\n]+?)"\s*\)/g, '($1)')
    .replace(/\{\s*"([^"\n]+?)"\s*\}/g, '{$1}');
}

function trimToDiagramStart(source) {
  const lines = source.split(/\r?\n/);
  const headerRe = /^(?:graph|flowchart|sequenceDiagram|classDiagram|stateDiagram(?:-v2)?|erDiagram|journey|gantt|pie|mindmap|timeline|quadrantChart|gitGraph|block-beta|packet-beta|architecture-beta)\b/i;
  const idx = lines.findIndex((line) => headerRe.test(line.trim()));
  if (idx === -1) {
    return source;
  }
  return lines.slice(idx).join('\n');
}

async function main() {
  const { file, output, ascii, theme } = parseArgs();
  let source = '';
  if (file) {
    source = readFileSync(file, 'utf8');
  } else {
    source = await getStdin();
  }
  if (!source.trim()) {
    console.error('No Mermaid source (use -f <file> or stdin).');
    process.exit(1);
  }

  source = stripFrontmatter(source);
  source = stripLeadingDirectives(source);
  source = stripHtmlMarkup(source);
  source = stripQuotedLabels(source);
  source = trimToDiagramStart(source);

  const themeOpts = theme && THEMES[theme] ? THEMES[theme] : undefined;

  if (ascii) {
    const result = renderMermaidAscii(source, {});
    if (output) {
      const { writeFileSync } = await import('fs');
      writeFileSync(output, result, 'utf8');
    } else {
      console.log(result);
    }
    return;
  }

  let svg = await renderMermaid(source, themeOpts || {});
  svg = svg.replace(
    /style="--bg:#FFFFFF;--fg:#27272A;background:var\(--bg\)"/,
    `style="${BOOK_SVG_VARS};background:var(--bg)"`
  );
  if (output) {
    const { writeFileSync } = await import('fs');
    writeFileSync(output, svg, 'utf8');
  } else {
    console.log(svg);
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
