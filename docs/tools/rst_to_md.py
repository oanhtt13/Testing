#!/usr/bin/env python3
"""Simple RST -> Markdown converter for Sphinx quickstart files.
Converts meta directives to YAML front-matter, title underlines to Markdown headings,
basic inline code and links, and comments out unknown directives.
"""
import re
import sys
from pathlib import Path


def parse_meta(text):
    # find .. meta:: block
    m = re.search(r"^.. meta::\n((?:[ \t]+:.+\n)*)", text, flags=re.M)
    if not m:
        return {}, text
    block = m.group(1)
    meta = {}
    for line in block.splitlines():
        line = line.strip()
        if line.startswith(':'):
            parts = line[1:].split(':', 1)
            if len(parts) == 2:
                key = parts[0].strip()
                val = parts[1].strip()
                meta[key] = val
    # remove the meta block from text
    text = text[:m.start()] + text[m.end():]
    return meta, text


def convert_title(text):
    # Replace title underlines
    def repl(m):
        title = m.group(1).strip()
        underline = m.group(2)
        ch = underline[0]
        if ch == '=':
            level = 1
        elif ch == '-':
            level = 2
        elif ch == '^':
            level = 3
        else:
            level = 2
        return '\n' + ('#' * level) + ' ' + title + '\n'
    text = re.sub(r"^(.+?)\n([=\-\^~`]+)\n", repl, text, flags=re.M)
    return text


def convert_inline(text):
    # convert ``code`` -> `code`
    text = re.sub(r'``([^`]+)``', r'`\1`', text)
    # convert links: `text <url>`_ -> [text](url)
    text = re.sub(r'`([^`<>]+) <([^>]+)>`_', r'[\1](\2)', text)
    # convert bare URLs? leave as-is
    return text


def convert_directives(text):
    # comment-out unknown directives like .. toctree:: and its options
    def directive_repl(m):
        block = m.group(0)
        # convert indentation to a comment block
        comment = '<!--\n' + block + '-->\n'
        return comment
    text = re.sub(r"^\.\.[ \t].*(?:\n(?:[ \t].*)*)", directive_repl, text, flags=re.M)
    return text


def normalize_whitespace(text):
    # remove trailing spaces and ensure single trailing newline
    text = re.sub(r"[ \t]+\n", r"\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = text.strip() + "\n"
    return text


def to_markdown(path):
    p = Path(path)
    text = p.read_text(encoding='utf-8')
    meta, text = parse_meta(text)
    text = convert_title(text)
    text = convert_inline(text)
    text = convert_directives(text)
    text = normalize_whitespace(text)
    # build YAML front matter if meta present
    fm = ''
    if meta:
        lines = ['---']
        for k, v in meta.items():
            # simple quoting
            v = v.replace('"', '\\"')
            lines.append(f'{k}: "{v}"')
        lines.append('---\n')
        fm = '\n'.join(lines)
    md = fm + text
    out = p.with_suffix('.md')
    out.write_text(md, encoding='utf-8')
    print(f'Converted {p} -> {out}')


if __name__ == '__main__':
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('docs')
    files = list(root.rglob('*.rst'))
    if not files:
        print('No .rst files found')
        sys.exit(0)
    for f in files:
        to_markdown(f)
    sys.exit(0)
