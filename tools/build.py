#!/usr/bin/env python3
"""Regenerate the ready-to-host HTML. Python 3 standard library only."""
from pathlib import Path
import json
from html import escape
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / 'content.json').read_text(encoding='utf-8'))
PROJECTS = DATA['projects']
FAVICON = 'data:image/svg+xml,' + quote('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><rect width="48" height="48" rx="24" fill="#234fe7"/><text x="24" y="30" font-family="Arial,sans-serif" font-weight="700" font-size="20" text-anchor="middle" fill="white">SC</text></svg>')

def esc(s):
    return escape(str(s), quote=True)

def head(title, desc, prefix=''):
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(desc)}"><meta name="theme-color" content="#234fe7">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:type" content="website">
<link rel="icon" type="image/svg+xml" href="{FAVICON}"><link rel="stylesheet" href="{prefix}assets/styles.css"></head><body>
<a href="#main" class="skip">Skip to content</a>'''

def header(prefix=''):
    home = prefix + 'index.html'
    return f'''<div class="wrap"><header class="site-header"><a class="wordmark" href="{home}" aria-label="Siya Chhibber, home"><span class="monogram" aria-hidden="true">SC</span>Siya Chhibber</a><nav class="site-nav" aria-label="Main navigation"><a href="{home}#work">Work</a><a href="{home}#about">About</a></nav></header></div>'''

def footer(prefix=''):
    return f'''<div class="wrap"><footer class="footer"><span>© 2026 Siya Chhibber</span><span>Code, circuits, stories &amp; yarn.</span><a href="#top">Back to top ↑</a></footer></div></body></html>'''

def artwork(p, prefix='', detail=False):
    kind = p['id']
    if kind in ('kina', 'crochet'):
        image = p['hero_image'] if detail else p['card_image']
        return f'<div class="card-art card-{kind}"><img src="{prefix}assets/{image}" alt="{esc(p["image_alt"])}" width="1600" height="900" loading="{"eager" if kind == "kina" else "lazy"}"></div>'
    if kind == 'pill-sleeve':
        dots = '<i></i>' * 8
        return f'''<div class="card-art card-pill"><div><p class="eyebrow">Pill adherence sleeve</p><div class="pill-title">A small signal.<br>A little less guessing.</div><div class="pill-state"><span>No bottle cycles yet</span><span class="leds red" aria-hidden="true">{dots}</span></div><div class="pill-state"><span>Two cycles counted</span><span class="leds green" aria-hidden="true">{dots}</span></div><div class="pill-state"><span>Bottle is out</span><span class="leds blue" aria-hidden="true">{dots}</span></div></div><span class="art-caption">LED state diagram</span></div>'''
    if kind == 'dropledger':
        return '''<div class="card-art card-drop"><div><p class="eyebrow">DropLedger</p><div class="art-type">Less typing.<br>More keeping track.</div><div class="app-ledger"><strong>Properties</strong><div class="ledger-row"><span>Uncategorized<small>Receipt needs a property</small></span><span class="ledger-review">Review</span></div><div class="ledger-row"><span>Oak Street<small>Home maintenance</small></span><span>$84.50</span></div></div></div><span class="art-caption">Interface concept · sample data</span></div>'''
    if kind == 'books':
        return '''<div class="card-art card-books"><div><p class="eyebrow">Written &amp; illustrated by Siya Chhibber</p><div class="book-titles">A Day of Discovery<br>at Chabot<div class="second">Sally’s Rockets</div></div><p style="margin-top:22px;font-size:.85rem">From a story to a museum shelf.</p></div></div>'''
    if kind == 'nasa':
        return '''<div class="card-art card-nasa"><div><p class="eyebrow">NASA Ames Research Center</p><div class="art-type" style="margin-top:18px">What happens<br>before takeoff?</div><div class="flow-line"><span>Travel data</span><b aria-hidden="true">→</b><span>Ground scenarios</span><b aria-hidden="true">→</b><span>Simulation</span></div><p style="color:#bac7e8;font-size:.85rem;margin-top:23px">Research in drone safety &amp; urban air mobility</p></div></div>'''
    return '''<div class="card-art card-journalism"><div><p class="eyebrow">Journalism · April–July 2026</p><div class="journal-type">Four stories.<br>One complicated<br>crisis.</div><div class="journal-rule"></div><p style="font-size:.85rem;margin-top:14px">Research. Interview. Question. Rewrite.</p></div></div>'''

def card(p, n):
    return f'''<a class="project-card" href="projects/{p['id']}.html">{artwork(p)}<div class="card-info"><div><span class="card-number">{n:02d} / {esc(p['category'])}</span><h3>{esc(p['title'])}</h3><p>{esc(p['card_description'])}</p></div><span class="card-arrow" aria-hidden="true">↗</span></div></a>'''

def render_home():
    cards = ''.join(card(p, i + 1) for i, p in enumerate(PROJECTS))
    experiences = ''.join(f'<article><p class="eyebrow">{esc(e["label"])}</p><h3>{esc(e["title"])}</h3><p>{esc(e["text"])}</p></article>' for e in DATA['experiences'])
    return head('Siya Chhibber — Projects, stories & things I make', DATA['description']) + header() + f'''
<main id="main" class="wrap"><div id="top"></div><section class="hero motion-in" aria-labelledby="hero-title"><div><p class="eyebrow">Design · Engineering · Storytelling</p><h1 id="hero-title">Curiosity,<br><em>made tangible.</em></h1></div><div class="hero-note"><p>{esc(DATA['intro'])}</p><a class="text-link" href="#work">Explore my work <span aria-hidden="true">↓</span></a></div></section>
<section id="work" aria-labelledby="work-title"><div class="section-heading"><h2 id="work-title">Selected work</h2><span>Ideas, iterations, and things I’ve made</span></div><div class="project-grid">{cards}</div></section>
<section id="about" class="about" aria-labelledby="about-title"><div><p class="eyebrow">A little about me</p><h2 id="about-title">There’s usually more than one way to make something.</h2></div><div class="about-copy">{''.join('<p>'+esc(p)+'</p>' for p in DATA['about'])}</div></section><section class="experience" aria-label="Beyond the projects">{experiences}</section></main>''' + footer()

def render_project(p, next_p):
    prefix = '../'
    facts = ''.join(f'<div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>' for k,v in p['facts'])
    sections = ''
    for s in p['sections']:
        sections += f'<section class="detail-section"><h2>{esc(s["title"])}</h2>'
        sections += ''.join(f'<p>{esc(t)}</p>' for t in s.get('paragraphs', []))
        if s.get('bullets'):
            sections += '<ul>' + ''.join(f'<li>{esc(t)}</li>' for t in s['bullets']) + '</ul>'
        sections += '</section>'
    media = ''
    for m in p.get('media', []):
        if m['type'] == 'image':
            element = f'<img src="../assets/{esc(m["src"])}" alt="{esc(m["alt"])}" loading="lazy">'
        else:
            element = f'<video controls playsinline preload="none" poster="../assets/{esc(m["poster"])}" aria-label="{esc(m["alt"])}"><source src="../assets/{esc(m["src"])}" type="video/mp4">Your browser cannot play this video. <a href="../assets/{esc(m["src"])}">Download the video</a>.</video>'
        media += f'<figure class="media-block">{element}<figcaption>{esc(m["caption"])}</figcaption></figure>'
    links = ''
    for l in p.get('links', []):
        href = l['href'] if l['href'].startswith('https://') else '../' + l['href']
        external = ' target="_blank" rel="noopener noreferrer"' if l['href'].startswith('https://') else ''
        links += f'<a class="button-link" href="{esc(href)}"{external}>{esc(l["label"])} <span aria-hidden="true">↗</span></a>'
    if links:
        links = '<div class="project-links">' + links + '</div>'
    callout = f'<aside class="callout"><p>{esc(p["note"])}</p></aside>' if p.get('note') else ''
    return head(p['title'] + ' — Siya Chhibber', p['description'], prefix) + header(prefix) + f'''
<main id="main" class="wrap"><div id="top"></div><section class="detail-intro"><a href="../index.html#work" class="back-link">← All projects</a><div class="detail-top"><div><p class="eyebrow">{esc(p['category'])}</p><h1>{esc(p['title'])}</h1><p class="detail-deck">{esc(p['description'])}</p></div><dl class="project-facts">{facts}</dl></div></section><div class="detail-visual">{artwork(p, prefix, True)}</div><div class="detail-body">{sections}{callout}{media}{links}</div><nav class="next-project" aria-label="Project navigation"><div><span>Keep exploring</span><a href="{next_p['id']}.html">{esc(next_p['title'])} →</a></div><a class="text-link" href="../index.html#work">All work</a></nav></main>''' + footer(prefix)

(ROOT / 'projects').mkdir(exist_ok=True)
(ROOT / 'index.html').write_text(render_home(), encoding='utf-8')
for i,p in enumerate(PROJECTS):
    (ROOT/'projects'/f'{p["id"]}.html').write_text(render_project(p, PROJECTS[(i+1)%len(PROJECTS)]), encoding='utf-8')
print(f'Generated index.html and {len(PROJECTS)} project pages.')
