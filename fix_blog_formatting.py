#!/usr/bin/env python3
"""Fix common formatting issues in Hugo blog posts.

Issues handled:
1. HTML entities in frontmatter (title, description, slug)
2. Partial HTML entities in title (e.g., quot; instead of &quot; or ")
3. Empty markdown headers (## with no text, merged with next line)
4. Frontmatter closing --- followed by content on same line (missing newline)
5. Tab-indented content outside code fences (renders incorrectly as code blocks)
"""

import re
import sys
from pathlib import Path

POSTS_DIR = Path('/home/user/larrynung.github.io/content/posts')

# Full HTML entity mappings
FULL_ENTITIES = {
    '&quot;': '"',
    '&lsquo;': '‘',
    '&rsquo;': '’',
    '&ldquo;': '“',
    '&rdquo;': '”',
    '&amp;': '&',
    '&ndash;': '–',
    '&mdash;': '—',
    '&hellip;': '…',
    '&apos;': "'",
    '&lt;': '<',
    '&gt;': '>',
    '&nbsp;': ' ',
}

# Partial entity names (missing leading &) — only safe/common ones
PARTIAL_ENTITY_NAMES = [
    'quot', 'lsquo', 'rsquo', 'ldquo', 'rdquo',
    'amp', 'ndash', 'mdash', 'hellip', 'apos',
]

# CJK Unicode ranges for detecting prose vs code
CJK_RE = re.compile(r'[一-鿿぀-ヿ＀-￯　-〿]')


def decode_entities(text: str) -> str:
    """Decode both full and partial HTML entities in a string.

    Uses (?<!&) lookbehind so we don't re-decode already-decoded & characters
    but DO handle entities glued to word chars like Directoryrsquo;
    """
    # Full entities first
    for entity, char in FULL_ENTITIES.items():
        text = text.replace(entity, char)
    # Partial entities: not preceded by & (prevents double-decoding &amp; → &amp; again)
    for name in PARTIAL_ENTITY_NAMES:
        char = FULL_ENTITIES.get(f'&{name};', '')
        if char:
            text = re.sub(r'(?<!&)' + re.escape(name) + r';', char, text)
    return text


def encode_yaml_double_quoted(value: str) -> str:
    """Encode a string as a YAML double-quoted scalar with proper escaping."""
    # Escape backslash first, then double-quote
    escaped = value.replace('\\', '\\\\').replace('"', '\\"')
    return f'"{escaped}"'


def parse_frontmatter(content: str):
    """Return (fm_lines, body, fm_end_line_idx) or None if no frontmatter."""
    lines = content.split('\n')
    if not lines or lines[0].rstrip() != '---':
        return None
    for i in range(1, len(lines)):
        if lines[i].rstrip() == '---':
            return lines[:i], lines[i:], i
    return None


def fix_frontmatter_entities(lines: list[str]) -> tuple[list[str], list[str]]:
    """Decode HTML entities in frontmatter title/description/slug, with proper YAML re-quoting."""
    changes = []
    new_lines = list(lines)
    for i, line in enumerate(new_lines):
        for field in ('title', 'description', 'slug'):
            prefix = f'{field}:'
            if not line.lower().startswith(prefix):
                continue
            rest = line[len(prefix):]
            stripped = rest.strip()

            if not stripped:
                break

            # Extract inner value based on quoting style
            if stripped.startswith('"'):
                # Double-quoted YAML scalar (including potentially-broken ones)
                if stripped.endswith('"') and len(stripped) >= 2:
                    inner = stripped[1:-1]
                    # Unescape any \" already in inner (for idempotency)
                    inner = inner.replace('\\"', '"')
                else:
                    inner = stripped.lstrip('"')
                decoded = decode_entities(inner)
                # Re-quote if entities were decoded OR if value has unescaped "
                has_unescaped_quote = '"' in inner.replace('\\"', '')
                if decoded == inner and not has_unescaped_quote:
                    break
                new_val = encode_yaml_double_quoted(decoded)
                new_lines[i] = f'{prefix} {new_val}'
                changes.append(f'frontmatter entity/quoting in {field}')

            elif stripped.startswith("'"):
                if stripped.endswith("'") and len(stripped) >= 2:
                    inner = stripped[1:-1].replace("''", "'")
                else:
                    inner = stripped.lstrip("'")
                decoded = decode_entities(inner)
                if decoded == inner:
                    break
                # Use double-quoted output since decoded value may contain '
                new_val = encode_yaml_double_quoted(decoded)
                new_lines[i] = f'{prefix} {new_val}'
                changes.append(f'frontmatter entity in {field}')

            else:
                # Unquoted value
                decoded = decode_entities(stripped)
                if decoded == stripped:
                    break
                new_lines[i] = f'{prefix} {decoded}'
                changes.append(f'frontmatter entity in {field}')

            break
    return new_lines, changes


def fix_empty_headers(lines: list[str]) -> tuple[list[str], list[str]]:
    """Merge empty headers (## + blank/tab text on next line) into a single header."""
    changes = []
    result = list(lines)
    i = 0
    while i < len(result):
        line = result[i]
        # Detect empty header: just # symbols, optional spaces/nbsp
        m = re.match(r'^(#{1,6})[\s\xa0]*$', line)
        if m:
            hashes = m.group(1)
            # Find next non-empty line
            j = i + 1
            while j < len(result) and not result[j].strip():
                j += 1

            if j < len(result) and j == i + 1:
                # Next line immediately follows — merge
                next_text = result[j].strip()
                if next_text:
                    result[i] = f'{hashes} {next_text}'
                    result[j] = ''
                    changes.append(f'merged empty header: {hashes} + {next_text[:40]!r}')
                    i = j + 1
                    continue
            else:
                # No content follows the empty header — remove it
                result[i] = ''
                changes.append(f'removed isolated empty header: {line!r}')
        i += 1
    return result, changes


def fix_frontmatter_closing_line(content: str) -> tuple[str, list[str]]:
    """Fix ---content on same line → ---\\ncontent."""
    changes = []
    # Pattern: a line starting with --- that has non-dash, non-whitespace content after it
    # This is the closing --- of frontmatter with content stuck to it
    new_content = re.sub(
        r'\n(---)((?![-\s\n])[^\n]+)',
        lambda m: f'\n{m.group(1)}\n\n{m.group(2)}',
        content
    )
    if new_content != content:
        changes.append('split ---content into separate lines')
    return new_content, changes


def fix_tab_indented_outside_fences(lines: list[str], fm_end: int) -> tuple[list[str], list[str]]:
    """Remove leading tabs from content outside code fences that starts with a tab.

    In Markdown, tab-indented lines are rendered as code blocks, which is wrong
    for prose text. We strip the tabs from prose (CJK-containing) lines and also
    from non-CJK lines (better to render as plain text than as wrongly-indented code).
    """
    changes = []
    result = list(lines)
    in_fence = False
    changed_count = 0

    for i in range(fm_end + 1, len(result)):
        line = result[i]

        # Track fence state
        if line.startswith('```'):
            in_fence = not in_fence
            continue

        if in_fence:
            continue

        # Strip leading tabs from non-fence tab-indented lines
        if line.startswith('\t'):
            new_line = re.sub(r'^\t+', '', line)
            if new_line != line:
                result[i] = new_line
                changed_count += 1

    if changed_count:
        changes.append(f'stripped tabs from {changed_count} lines outside code fences')
    return result, changes


def process_file(filepath: Path) -> dict:
    """Apply all fixes to a single blog post. Returns summary of changes."""
    try:
        content = filepath.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        return {'changed': False, 'error': 'binary/encoding error', 'changes': []}

    original = content
    all_changes = []

    # Fix 1 & 2: HTML entities in frontmatter
    parsed = parse_frontmatter(content)
    if parsed:
        fm_lines, rest_lines, fm_end_idx = parsed
        new_fm, changes = fix_frontmatter_entities(fm_lines[1:])  # skip opening ---
        if changes:
            all_changes.extend(changes)
            content = '---\n' + '\n'.join(new_fm) + '\n' + '\n'.join(rest_lines)

    # Fix 3: frontmatter closing --- followed by content on same line
    content, changes = fix_frontmatter_closing_line(content)
    all_changes.extend(changes)

    # Re-parse after potential fix 3
    parsed = parse_frontmatter(content)
    fm_end = parsed[2] if parsed else 0

    # Fix 4: empty headers
    lines = content.split('\n')
    lines, changes = fix_empty_headers(lines)
    all_changes.extend(changes)

    # Fix 5: tab-indented content outside code fences
    lines, changes = fix_tab_indented_outside_fences(lines, fm_end)
    all_changes.extend(changes)

    content = '\n'.join(lines)

    if content != original:
        filepath.write_text(content, encoding='utf-8')
        return {'changed': True, 'changes': all_changes}

    return {'changed': False, 'changes': []}


def main():
    posts = sorted(POSTS_DIR.glob('*/index.md'))
    print(f'Scanning {len(posts)} posts...\n')

    changed = []
    errors = []

    for filepath in posts:
        result = process_file(filepath)
        post_id = filepath.parent.name
        if result.get('error'):
            errors.append(f'{post_id}: {result["error"]}')
        elif result['changed']:
            changed.append((post_id, result['changes']))
            print(f'{post_id}:')
            for c in result['changes']:
                print(f'  - {c}')

    print(f'\n{"="*60}')
    print(f'Fixed {len(changed)} files out of {len(posts)} total.')
    if errors:
        print(f'Errors: {len(errors)}')
        for e in errors:
            print(f'  {e}')


if __name__ == '__main__':
    main()
