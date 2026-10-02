"""Buduje raport HTML (styl drkasiak.pl) z pliku Markdown.
Uzycie:  pip install markdown  &&  python narzedzia/build_html.py
"""
import re, markdown
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "raport" / "2026-09-25-mapa-procesow-dentalux-plan.md"
OUT = ROOT / "2026-09-25-mapa-procesow-dentalux-plan.html"

md = open(SRC, encoding="utf-8").read()
# Drop title + meta lines (rendered in hero instead)
md = re.sub(r"\A# .*?\n\n\*Data:.*?\n\*Źródła:.*?\n\n---\n", "", md, flags=re.S)
md = md.replace("- [ ] ", "- ☐ ")

conv = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists", "toc"],
                         extension_configs={"toc": {"toc_depth": "2"}})
body = conv.convert(md)

# Wrap tables for horizontal scroll on phones
body = re.sub(r"<table>", '<div class="tbl"><table>', body)
body = body.replace("</table>", "</table></div>")
# Remove horizontal rules between sections
body = body.replace("<hr />", "")
# Mono eyebrow numbers for h2 "N. Title"
def h2(m):
    idd, text = m.group(1), m.group(2)
    mm = re.match(r"(\d+)\.\s*(.*)", text)
    if mm:
        return f'<h2 id="{idd}"><span class="num">{int(mm.group(1)):02d}</span>{mm.group(2)}</h2>'
    return f'<h2 id="{idd}"><span class="num">&mdash;</span>{text}</h2>'
body = re.sub(r'<h2 id="([^"]+)">(.*?)</h2>', h2, body)
# Wrap each h2 section into <section>
parts = re.split(r'(?=<h2 )', body)
body = "".join(f'<section class="sec">{p}</section>' if p.startswith("<h2") else p for p in parts)
# Highlight TL;DR section
body = body.replace('<section class="sec"><h2 id="0-tldr', '<section class="sec tldr"><h2 id="0-tldr', 1)

toc_items = []
for tok in conv.toc_tokens:
    for t in [tok] + tok.get("children", []):
        if t["level"] == 2:
            name = re.sub(r"^\d+\.\s*", "", t["name"])
            toc_items.append(f'<li><a href="#{t["id"]}">{name}</a></li>')
toc = "\n".join(toc_items)

html = f"""<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Mapa procesów Dentalux</title>
<meta name="description" content="Plan krok po kroku mapowania procesów w Centrum Stomatologii Dentalux">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700;800&family=Chivo+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root {{
  --red: #B1161C; --red-ink: #FFF8F7; --navy: #001D39;
  --bg: #F7F8FA; --surface: #FFFFFF; --surface-2: #EDF0F4;
  --line: #CFD5DB; --text: #001D39; --muted: #4A5A6B; --link: #374FD4;
  --red-soft: rgba(177,22,28,.07);
}}
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
    --red: #E0474D; --red-ink: #FFF8F7; --navy: #E6ECF2;
    --bg: #07131F; --surface: #0D1D2E; --surface-2: #13273B;
    --line: #26394D; --text: #E6ECF2; --muted: #9AABBC; --link: #8FA0FF;
    --red-soft: rgba(224,71,77,.10);
  }}
}}
:root[data-theme="dark"] {{
  --red: #E0474D; --red-ink: #FFF8F7; --navy: #E6ECF2;
  --bg: #07131F; --surface: #0D1D2E; --surface-2: #13273B;
  --line: #26394D; --text: #E6ECF2; --muted: #9AABBC; --link: #8FA0FF;
  --red-soft: rgba(224,71,77,.10);
}}
* {{ box-sizing: border-box; }}
html {{ scroll-behavior: smooth; -webkit-text-size-adjust: 100%; }}
body {{ margin: 0; background: var(--bg); color: var(--text);
  font: 400 16px/1.65 Archivo, system-ui, sans-serif; }}
a {{ color: var(--link); text-underline-offset: 3px; }}
.topbar {{ position: sticky; top: 0; z-index: 10; background: color-mix(in srgb, var(--bg) 88%, transparent);
  backdrop-filter: blur(8px); border-bottom: 1px solid var(--line); }}
.topbar .in {{ max-width: 1240px; margin: 0 auto; padding: 14px 24px; display: flex; align-items: center; justify-content: space-between; gap: 16px; }}
.brand {{ display: flex; align-items: baseline; gap: 10px; font-weight: 700; letter-spacing: -.01em; color: var(--text); text-decoration: none; }}
.brand .dr {{ color: var(--red); }}
.brand small {{ font: 400 12px 'Chivo Mono', monospace; color: var(--muted); letter-spacing: .04em; }}
.btn {{ display: inline-block; background: var(--red); color: var(--red-ink); padding: 10px 18px; border-radius: 2px;
  font-weight: 600; font-size: 14px; text-decoration: none; box-shadow: 0 6px 16px rgba(177,22,28,.22); white-space: nowrap; }}
.btn.sec {{ background: var(--surface-2); color: var(--text); border: 1px solid var(--line); box-shadow: none; }}
.hero {{ max-width: 1240px; margin: 0 auto; padding: 72px 24px 48px; }}
.eyebrow {{ font: 500 12px/1 'Chivo Mono', monospace; letter-spacing: .14em; text-transform: uppercase; color: var(--red); }}
.hero h1 {{ font-size: clamp(38px, 6vw, 66px); line-height: 1.02; letter-spacing: -.03em; font-weight: 800; margin: 18px 0 20px; max-width: 15ch; text-wrap: balance; }}
.hero h1 em {{ font-style: normal; color: var(--red); }}
.hero p.lead {{ font-size: 19px; color: var(--muted); max-width: 62ch; margin: 0 0 28px; }}
.meta {{ display: flex; flex-wrap: wrap; gap: 10px 28px; font: 400 13px 'Chivo Mono', monospace; color: var(--muted);
  border-top: 1px solid var(--line); padding-top: 18px; }}
.meta b {{ color: var(--text); font-weight: 500; }}
.layout {{ max-width: 1240px; margin: 0 auto; padding: 0 24px 96px; display: grid; grid-template-columns: 260px minmax(0,1fr); gap: 56px; }}
nav.toc {{ position: sticky; top: 76px; align-self: start; max-height: calc(100vh - 96px); overflow: auto; }}
nav.toc h4 {{ font: 500 11px 'Chivo Mono', monospace; letter-spacing: .14em; text-transform: uppercase; color: var(--muted); margin: 0 0 12px; }}
nav.toc ol {{ list-style: none; margin: 0; padding: 0; counter-reset: t -1; }}
nav.toc li {{ counter-increment: t; }}
nav.toc a {{ display: grid; grid-template-columns: 28px 1fr; padding: 6px 0; font-size: 14px; line-height: 1.35; color: var(--muted);
  text-decoration: none; border-left: 2px solid transparent; padding-left: 10px; }}
nav.toc a::before {{ content: counter(t, decimal-leading-zero); font: 400 11px/1.9 'Chivo Mono', monospace; color: var(--line); }}
nav.toc a:hover, nav.toc a.on {{ color: var(--text); border-left-color: var(--red); }}
nav.toc a.on::before {{ color: var(--red); }}
main {{ min-width: 0; }}
.sec {{ background: var(--surface); border: 1px solid var(--line); border-radius: 4px; padding: 40px 44px; margin-bottom: 24px; }}
.sec.tldr {{ border-top: 4px solid var(--red); }}
h2 {{ font-size: clamp(26px, 3.2vw, 38px); line-height: 1.12; letter-spacing: -.02em; font-weight: 800; margin: 0 0 24px; scroll-margin-top: 90px; text-wrap: balance; }}
h2 .num {{ display: block; font: 500 13px 'Chivo Mono', monospace; color: var(--red); letter-spacing: .1em; margin-bottom: 10px; }}
h3 {{ font-size: 20px; font-weight: 700; letter-spacing: -.01em; margin: 36px 0 12px; padding-top: 20px; border-top: 1px dashed var(--line); }}
h2 + h3 {{ border-top: 0; padding-top: 0; margin-top: 8px; }}
p, li {{ max-width: 78ch; }}
ul, ol {{ padding-left: 22px; }}
li {{ margin: 6px 0; }}
li::marker {{ color: var(--red); font-weight: 600; }}
strong {{ font-weight: 700; }}
em {{ color: var(--muted); }}
code {{ font: 400 .88em 'Chivo Mono', monospace; background: var(--surface-2); padding: 1px 5px; border-radius: 2px; }}
pre {{ background: var(--navy); color: #E6ECF2; padding: 22px; border-radius: 4px; overflow-x: auto; font: 400 12.5px/1.55 'Chivo Mono', monospace; }}
:root[data-theme="dark"] pre {{ background: #03101C; }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) pre {{ background: #03101C; }} }}
pre code {{ background: none; padding: 0; color: inherit; font-size: inherit; }}
blockquote {{ margin: 20px 0; padding: 14px 18px; background: var(--red-soft); border-left: 3px solid var(--red); border-radius: 2px; }}
blockquote p {{ margin: 0; }}
.tbl {{ overflow-x: auto; margin: 18px 0 8px; border: 1px solid var(--line); border-radius: 4px; }}
table {{ border-collapse: collapse; width: 100%; font-size: 14.5px; line-height: 1.5; }}
th {{ text-align: left; background: var(--surface-2); font: 500 11.5px 'Chivo Mono', monospace; letter-spacing: .06em; text-transform: uppercase;
  color: var(--muted); padding: 11px 14px; border-bottom: 1px solid var(--line); white-space: nowrap; }}
td {{ padding: 11px 14px; border-bottom: 1px solid var(--line); vertical-align: top; }}
tr:last-child td {{ border-bottom: 0; }}
tbody tr:hover td {{ background: var(--red-soft); }}
td:first-child {{ font-weight: 600; }}
footer {{ border-top: 1px solid var(--line); }}
footer .in {{ max-width: 1240px; margin: 0 auto; padding: 28px 24px; display: flex; flex-wrap: wrap; justify-content: space-between; gap: 12px;
  font: 400 12px 'Chivo Mono', monospace; color: var(--muted); }}
.theme {{ background: none; border: 1px solid var(--line); color: var(--text); border-radius: 2px; padding: 8px 10px; cursor: pointer; font: 400 12px 'Chivo Mono', monospace; }}
@media (max-width: 980px) {{
  .layout {{ grid-template-columns: minmax(0,1fr); gap: 0; }}
  nav.toc {{ display: none; }}
}}
@media (max-width: 640px) {{
  .topbar .in, .hero, .layout, footer .in {{ padding-left: 16px; padding-right: 16px; }}
  .hero {{ padding-top: 44px; }}
  .brand small, .topbar .btn {{ display: none; }}
  .meta {{ flex-direction: column; gap: 6px; }}
  .sec {{ padding: 26px 18px; }}
  .hero p.lead {{ font-size: 17px; }}
}}
@media print {{
  .topbar, nav.toc, .theme {{ display: none; }}
  .layout {{ display: block; }}
  .sec {{ break-inside: avoid-page; border: 0; padding: 0 0 20px; }}
  body {{ background: #fff; }}
}}
</style>
</head>
<body>
<header class="topbar"><div class="in">
  <a class="brand" href="https://drkasiak.pl/"><span><span class="dr">dr</span> Marcin Kasiak</span><small>ENDODONCJA · WARSZAWA</small></a>
  <div style="display:flex;gap:10px;align-items:center">
    <button class="theme" id="themeBtn" type="button" aria-label="Przełącz motyw">◐ Motyw</button>
    <a class="btn" href="#11-harmonogram-wersja-przy-pracy-czesci-etatu">Harmonogram</a>
  </div>
</div></header>

<div class="hero">
  <div class="eyebrow">Raport · Centrum Stomatologii Dentalux</div>
  <h1>Mapa procesów <em>Dentalux</em>: plan krok po kroku</h1>
  <p class="lead">Jak przygotować, przeprowadzić i utrzymać mapę procesów w dwóch klinikach Dentalux: narzędzia, kolejność prac, powiązania między procesami, obowiązki prawne i pułapki, których nikt nie opisuje w podręcznikach.</p>
  <div class="meta">
    <span>Data <b>25.09.2026</b></span>
    <span>Dla <b>dr n. med. Marcin Kasiak</b></span>
    <span>Czas realizacji <b>~10 tygodni</b></span>
    <span>Źródła <b>NHS · IHI · PMC · dentalux.pl</b></span>
  </div>
</div>

<div class="layout">
  <nav class="toc" aria-label="Spis treści"><h4>Spis treści</h4><ol>
{toc}
  </ol></nav>
  <main>
{body}
  </main>
</div>

<footer><div class="in">
  <span>dr n. med. Marcin Kasiak · Racławicka 131, Warszawa</span>
  <span>Przygotowano z Claude Code · 2026-09-25</span>
</div></footer>

<script>
(function(){{
  var root = document.documentElement, key = 'dx-theme';
  try {{ var s = localStorage.getItem(key); if (s) root.setAttribute('data-theme', s); }} catch(e) {{}}
  document.getElementById('themeBtn').addEventListener('click', function(){{
    var cur = root.getAttribute('data-theme') ||
      (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    var next = cur === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try {{ localStorage.setItem(key, next); }} catch(e) {{}}
  }});
  var links = [].slice.call(document.querySelectorAll('nav.toc a'));
  var map = {{}}; links.forEach(function(a){{ map[a.getAttribute('href').slice(1)] = a; }});
  if ('IntersectionObserver' in window) {{
    var io = new IntersectionObserver(function(es){{
      es.forEach(function(e){{ if (e.isIntersecting) {{
        links.forEach(function(l){{ l.classList.remove('on'); }});
        var a = map[e.target.id]; if (a) a.classList.add('on');
      }} }});
    }}, {{ rootMargin: '-20% 0px -70% 0px' }});
    document.querySelectorAll('h2[id]').forEach(function(h){{ io.observe(h); }});
  }}
}})();
</script>
</body>
</html>
"""
open(OUT, "w", encoding="utf-8").write(html)
print("ok", len(html), len(toc_items))
