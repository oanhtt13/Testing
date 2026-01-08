#!/usr/bin/env python3
"""
Add a Jekyll-style YAML front-matter block to the top of every .html file
in the given directory (defaults to docs/_build/html).
Idempotent: files already starting with '---' are skipped.
"""
import sys
import os
import re
from pathlib import Path

def make_permalink(root, path):
    rel = os.path.relpath(path, root).replace('\\', '/')
    if rel.endswith('index.html'):
        dirpath = rel[:-len('index.html')]
        if not dirpath.startswith('/'):
            dirpath = '/' + dirpath
        if not dirpath.endswith('/'):
            dirpath = dirpath + '/'
        perm = dirpath
    else:
        perm = '/' + rel
    perm = perm.replace('//','/')
    return perm


def get_title(content):
    m = re.search(r'<title>(.*?)</title>', content, re.I | re.S)
    if m:
        t = m.group(1).strip()
        t = re.sub(r"\s+", " ", t)
        return t
    return None


def needs_front_matter(content):
    return not content.lstrip().startswith('---')


def quote_yaml(s):
    if s is None:
        return '""'
    s = s.replace('\\', '\\\\').replace('"', '\\"')
    return '"{}"'.format(s)


def process(root_dir):
    root = Path(root_dir)
    if not root.exists():
        print(f"Error: root directory does not exist: {root}")
        return 2

    for path in sorted(root.rglob('*.html')):
        text = path.read_text(encoding='utf-8')
        if not needs_front_matter(text):
            print(f"Skipping (front-matter exists): {path}")
            continue
        title = get_title(text) or path.stem
        permalink = make_permalink(str(root), str(path))
        fm_lines = [
            '---',
            f'title: {quote_yaml(title)}',
            'layout: default',
            f'permalink: {quote_yaml(permalink)}',
            '---',
            ''
        ]
        new_text = '\n'.join(fm_lines) + text
        path.write_text(new_text, encoding='utf-8')
        print(f'Prepended front-matter to {path}')

    return 0


if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else 'docs/_build/html'
    sys.exit(process(target))
