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

  const svg = await renderMermaid(source, themeOpts || {});
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
