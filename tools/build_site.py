#!/usr/bin/env python3
"""Build the recipe site from the Claude Project's files.

The Claude.ai Project ("Recipe Collection") is the source of truth. This site is a
read-only published view. Do not hand-edit the generated HTML; change the Project
file, then re-run this script.

Usage:
    python3 tools/build_site.py SRC_DIR OUT_DIR

SRC_DIR must contain:
    4_RECIPE_INDEX.md            (latest version of claude/4_RECIPE_INDEX, renamed)
    modules/Recipe_<Name>.md     (latest version of each modules/ recipe, date/version stripped)
"""
import datetime
import html
import re
import sys
from pathlib import Path

import markdown

SECTION_FOLDERS = {
    "Quick Weeknight": "dinner",
    "Standard Dinner": "dinner",
    "Full Flavor": "dinner",
    "Lunch": "lunch",
    "Breakfast": "breakfast",
    "Smoothies": "smoothies",
    "Desserts": "desserts",
    "Drinks": "drinks",
}
DINNER_SECTIONS = ["Quick Weeknight", "Standard Dinner", "Full Flavor"]

CSS = """
:root { --ink:#222; --muted:#666; --line:#e4e4e4; --accent:#b4441f; --link:#0b5cad; --soft:#faf7f4; }
* { box-sizing: border-box; }
body { font-family: -apple-system, "Segoe UI", Arial, sans-serif; margin: 0 auto; max-width: 900px;
       padding: 28px 18px 60px; line-height: 1.6; color: var(--ink); }
a { color: var(--link); text-decoration: none; }
a:hover { text-decoration: underline; }
h1 { margin: 0 0 6px; line-height: 1.25; }
h2 { border-bottom: 2px solid var(--line); padding-bottom: 6px; margin-top: 40px; }
h3 { margin-top: 28px; }
.subtitle, .crumbs, footer { color: var(--muted); }
.crumbs { font-size: .95em; margin: 0 0 14px; }
nav.toc { margin: 16px 0 0; display: flex; flex-wrap: wrap; gap: 6px 16px; }
.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 12px; margin-top: 14px; }
.card { display: block; border: 1px solid var(--line); border-radius: 10px; padding: 14px 16px;
        color: var(--ink); background: var(--soft); transition: box-shadow .15s, transform .15s; }
.card:hover { box-shadow: 0 2px 10px rgba(0,0,0,.09); transform: translateY(-1px); text-decoration: none; }
.card-title { font-weight: 600; color: var(--link); display: block; margin-bottom: 4px; }
.card-desc { font-size: .93em; color: #444; display: block; }
.tags { margin-top: 8px; display: flex; flex-wrap: wrap; gap: 6px; }
.tag { display: inline-block; background: #eee; border-radius: 4px; padding: 1px 8px; font-size: .8em; color: #444; }
.tag.warn { background: #fde8d8; color: #8a3410; }
.tag.cat { background: #e3eefb; color: #174a85; }
.empty { color: var(--muted); font-style: italic; }
dl.fields { display: grid; grid-template-columns: minmax(150px, 210px) 1fr; gap: 8px 18px; margin: 18px 0; }
dl.fields dt { font-weight: 600; color: #444; }
dl.fields dd { margin: 0; }
dl.fields dd ul { margin: 4px 0 0; padding-left: 20px; }
@media (max-width: 600px) { dl.fields { grid-template-columns: 1fr; gap: 2px; } dl.fields dd { margin-bottom: 10px; } }
table { width: 100%; border-collapse: collapse; margin: 16px 0; font-size: .93em; }
th, td { border: 1px solid #ddd; padding: 8px; text-align: left; vertical-align: top; }
th { background: #f4f4f4; }
.tablewrap { overflow-x: auto; }
ol li, ul li { margin-bottom: 4px; }
footer { margin-top: 50px; font-size: .85em; border-top: 1px solid var(--line); padding-top: 12px; }
"""


def page(title, body, depth):
    root = "../" * depth
    built = datetime.date.today().isoformat()
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)}</title>
<style>{CSS}</style>
</head>
<body>
{body}
<footer>Read-only view generated {built} from the Recipe Collection Claude Project. Changes are made in the Project, then the site is regenerated. &middot; <a href="{root}index.html">All recipes</a></footer>
</body>
</html>
"""


def slug_for(module_base):
    return re.sub(r"^Recipe_", "", module_base).lower()


def parse_index(text):
    """Return ordered list of (section, [entries]) from 4_RECIPE_INDEX."""
    sections, current = [], None
    item_re = re.compile(
        r"^\d+\.\s+\*\*(?P<title>.+?)\*\*\s+—\s+`modules/(?P<module>Recipe_[A-Za-z0-9_]+)`"
        r"(?:\s+—\s+(?P<desc>.*?))?\s*(?:\*\((?P<tags>[^)]*)\)\*)?\s*$"
    )
    for line in text.splitlines():
        if line.startswith("## "):
            current = (line[3:].strip(), [])
            sections.append(current)
            continue
        m = item_re.match(line.strip())
        if m and current is not None:
            desc = (m.group("desc") or "").strip()
            tags = [t.strip() for t in (m.group("tags") or "").split(",") if t.strip()]
            if "not yet cooked" in desc.lower():
                tags.append("not yet cooked")
            current[1].append({
                "title": m.group("title"),
                "module": m.group("module"),
                "desc": desc,
                "tags": tags,
                "section": current[0],
            })
    return sections


INLINE_MD = markdown.Markdown(extensions=[])


def inline(text):
    out = INLINE_MD.reset().convert(text)
    return re.sub(r"^<p>(.*)</p>$", r"\1", out, flags=re.S)


def link_recipes(html_text, links, depth):
    root = "../" * depth

    def sub(m):
        base = m.group(0)
        if base in links:
            title, href = links[base]
            return f'<a href="{root}{href}">{html.escape(title)}</a>'
        return base
    # Only replace outside of tags.
    parts = re.split(r"(<[^>]+>)", html_text)
    return "".join(p if p.startswith("<") else re.sub(r"Recipe_[A-Za-z0-9_]+", sub, p) for p in parts)


def tag_html(tags, category=None):
    out = []
    if category:
        out.append(f'<span class="tag cat">{html.escape(category)}</span>')
    for t in tags:
        cls = "tag warn" if t in ("upgrade candidate", "not yet cooked") else "tag"
        out.append(f'<span class="{cls}">{html.escape(t)}</span>')
    return f'<div class="tags">{"".join(out)}</div>' if out else ""


def normalize_body(md):
    """Make loose recipe markdown parse cleanly: blank lines between blocks, bold labels."""
    out, prev = [], "blank"
    for raw in md.splitlines():
        line = raw.rstrip()
        if not line.strip():
            kind = "blank"
        elif re.match(r"^\s*([-*]|\d+\.)\s", line):
            kind = "list"
        elif line.lstrip().startswith("|"):
            kind = "table"
        else:
            kind = "text"
        if kind == "list":
            indent = len(line) - len(line.lstrip())
            line = " " * (indent * 2) + line.lstrip()  # 2-space nesting -> 4-space
        if kind == "text":
            m = re.match(r"^\*\*(Full recipe detail \(from site\))\*\*$", line)
            if m:
                line, kind = "## Full Recipe", "heading"
            elif re.match(r"^\*\*[^*]+\*\*$", line):
                line, kind = "### " + line.strip("*"), "heading"
            else:
                line = re.sub(r"^([A-Z][A-Za-z0-9 ()&/'’-]{1,40}):(\s|$)", r"**\1:**\2", line)
        if prev != "blank" and (kind != prev or kind in ("text", "heading")):
            out.append("")
        out.append(line)
        prev = kind
    return "\n".join(out)


def parse_module(text):
    """Split a module into (title, [(label, value_md)], body_md)."""
    lines = text.splitlines()
    title = lines[0].lstrip("#").strip()
    fields, i = [], 1
    while i < len(lines) and not lines[i].strip():
        i += 1
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^- ([^:]+?):\s?(.*)$", line)
        if m:
            fields.append([m.group(1).strip(), m.group(2).strip(), []])
            i += 1
        elif line.startswith("  ") and fields and line.strip().startswith("-"):
            fields[-1][2].append(line[2:])
            i += 1
        else:
            break
    body = "\n".join(lines[i:]).strip()
    return title, fields, body


FIELD_LABELS = {
    "Sauce/gravy/marinade/seasoning notes": "Sauce & seasoning",
    "Success Rice guidance, if included": "Success Rice",
}


def render_fields(fields):
    rows = []
    for label, value, subs in fields:
        if value.strip().upper() == "N/A" and not subs:
            continue
        shown = FIELD_LABELS.get(label, label)
        val_html = inline(value) if value else ""
        if subs:
            sub_md = normalize_body("\n".join(subs))
            val_html += markdown.markdown(sub_md, extensions=["sane_lists"])
        rows.append(f"<dt>{html.escape(shown)}</dt><dd>{val_html}</dd>")
    return f'<dl class="fields">{"".join(rows)}</dl>'


def build(src, out):
    src, out = Path(src), Path(out)
    sections = parse_index((src / "4_RECIPE_INDEX.md").read_text())
    entries = [e for _, es in sections for e in es]

    links = {}
    for e in entries:
        folder = SECTION_FOLDERS[e["section"]]
        e["href"] = f"{folder}/{slug_for(e['module'])}.html"
        links[e["module"]] = (e["title"], e["href"])

    missing = [e["module"] for e in entries if not (src / "modules" / f"{e['module']}.md").exists()]
    unindexed = sorted(p.stem for p in (src / "modules").glob("Recipe_*.md") if p.stem not in links)
    if missing:
        sys.exit(f"Index references modules with no source file: {missing}")
    if unindexed:
        print(f"WARNING: recipe files not in the index (not published): {unindexed}")

    written = []
    for e in entries:
        title, fields, body = parse_module((src / "modules" / f"{e['module']}.md").read_text())
        body_html = markdown.markdown(normalize_body(body), extensions=["tables", "sane_lists"]) if body else ""
        body_html = body_html.replace("<table>", '<div class="tablewrap"><table>').replace("</table>", "</table></div>")
        folder = SECTION_FOLDERS[e["section"]]
        anchor = section_id(e["section"])
        content = f"""<p class="crumbs"><a href="../index.html">&larr; All recipes</a> &nbsp;|&nbsp; <a href="../index.html#{anchor}">{html.escape(e['section'])}</a></p>
<h1>{html.escape(title)}</h1>
{tag_html(e['tags'], e['section'])}
{render_fields(fields)}
{body_html}"""
        content = link_recipes(content, links, 1)
        dest = out / e["href"]
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(page(title, content, 1))
        written.append(e["href"])

    # Home page
    toc, blocks = [], []
    dinner_done = False
    for name, es in sections:
        sid = section_id(name)
        if name in DINNER_SECTIONS and not dinner_done:
            blocks.append('<h2 id="dinner">Dinner</h2>')
            toc.append('<a href="#dinner">Dinner</a>')
            dinner_done = True
        heading = "h3" if name in DINNER_SECTIONS else "h2"
        if name not in DINNER_SECTIONS:
            toc.append(f'<a href="#{sid}">{html.escape(name)}</a>')
        cards = []
        for e in es:
            desc = inline(e["desc"]) if e["desc"] else ""
            desc = re.sub(r"\s*<strong>not yet cooked</strong>\.?", "", desc).rstrip("; ")
            cards.append(
                f'<a class="card" href="{e["href"]}"><span class="card-title">{html.escape(e["title"])}</span>'
                f'<span class="card-desc">{desc}</span>{tag_html([t for t in e["tags"] if t != "site import"])}</a>'
            )
        grid = f'<div class="grid">{"".join(cards)}</div>' if cards else '<p class="empty">None saved yet.</p>'
        blocks.append(f'<{heading} id="{sid}">{html.escape(name)}</{heading}>\n{grid}')
    home = f"""<h1>Our Recipes</h1>
<p class="subtitle">{len(entries)} saved recipes &mdash; Southern/Cajun-leaning dinners, plus breakfast, lunch, smoothies, desserts, and drinks.</p>
<nav class="toc">{"".join(toc)}</nav>
{chr(10).join(blocks)}"""
    (out / "index.html").write_text(page("Our Recipes", home, 0))
    written.append("index.html")
    return written


def section_id(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    for f in build(sys.argv[1], sys.argv[2]):
        print(f)
