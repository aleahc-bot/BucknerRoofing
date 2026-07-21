#!/usr/bin/env python3
"""Composes the 5 Buckner Roofing pages from shared partials."""
import pathlib

OUT = pathlib.Path(__file__).parent

PHONE_TXT = "(239) 922-8196"
PHONE_TEL = "+12399228196"
EMAIL = "nate@buckner-roofing.com"
ADDR = "7547 Captiva Blvd, Fort Myers, FL 33967"
MAPS = "https://maps.app.goo.gl/DTWB763Cg67UDxi96"
LIC = "CCC1334407"
# Buckner's real logo, inlined as base64 in index.css so it cannot 404 when the folder
# is moved or a file is missed. Two variants: the wordmark in their off-white (for dark
# bars) and recoloured to ink (for white bars). CSS shows whichever suits the background.
MARK = ('<span class="brand">'
        '<span class="brand__img brand__img--onlight" role="img" aria-label="Buckner Roofing"></span>'
        '<span class="brand__img brand__img--ondark" aria-hidden="true"></span>'
        '</span>')

NAVS = [
    ("index.html", "Home"),
    ("services.html", "Services"),
    ("projects.html", "Projects"),
    ("about.html", "About"),
    ("contact.html", "Contact"),
]


def head(title, desc, page):
    return f"""<!DOCTYPE html>
<!-- Design signed off: Crest layout, Classic Luxury type, Minimal Light, Spacious.
     These attributes are now FIXED. The Design Studio has been removed. -->
<html lang="en" data-layout="crest" data-type="luxury" data-theme="light" data-scale="spacious">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" type="image/png" href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAWEAAADUCAYAAABNj5KlAAAACXBIWXMAAAsTAAALEwEAmpwYAAAF1GlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgOS4xLWMwMDMgNzkuOTY5MGE4N2ZjLCAyMDI1LzAzLzA2LTIwOjUwOjE2ICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIgeG1sbnM6cGhvdG9zaG9wPSJodHRwOi8vbnMuYWRvYmUuY29tL3Bob3Rvc2hvcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RFdnQ9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZUV2ZW50IyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgMjYuMTEgKE1hY2ludG9zaCkiIHhtcDpDcmVhdGVEYXRlPSIyMDI2LTA3LTEzVDEyOjIxOjA5LTA0OjAwIiB4bXA6TW9kaWZ5RGF0ZT0iMjAyNi0wNy0xM1QxMjoyMzo1MC0wNDowMCIgeG1wOk1ldGFkYXRhRGF0ZT0iMjAyNi0wNy0xM1QxMjoyMzo1MC0wNDowMCIgZGM6Zm9ybWF0PSJpbWFnZS9wbmciIHBob3Rvc2hvcDpDb2xvck1vZGU9IjMiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6MzIyNjc2MTAtNTc0Ni00NjlhLWI0ODctOWM0MjM2ZjIxM2E3IiB4bXBNTTpEb2N1bWVu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">
<link rel="apple-touch-icon" href="data:image/png;base64,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">
<meta name="theme-color" content="#ff5307">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600;700&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="index.css">
<!-- DEV TOOL — delete this block and preview.html before client handoff -->
<a class="devbtn" href="preview.html" title="Open device preview" aria-label="Open device preview">
  <svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
    <rect x="2.5" y="4" width="13" height="10" rx="1.6"/>
    <path d="M6.5 17.5h5"/>
    <rect x="17" y="9" width="5" height="11" rx="1.4"/>
  </svg>
  <span>Preview</span>
</a>
<!-- /DEV TOOL -->
<script src="site.js" defer></script>
</head>
<body data-page="{page}">
"""


def nav(page):
    links = ""
    for href, label in NAVS:
        cur = ' aria-current="page"' if href == page else ""
        links += f'      <a href="{href}"{cur}>{label}</a>\n'
    return f"""<header class="nav nav--over">
  <div class="nav__in">
    <a class="nav__logo" href="index.html" aria-label="Buckner Roofing home">
      {MARK}
    </a>
    <nav class="nav__links" aria-label="Primary">
{links}    </nav>
    <a class="btn btn--primary nav__cta" href="contact.html"><span>Get a quote</span></a>
    <button class="nav__burger" id="burger" aria-label="Toggle menu"><i></i><i></i><i></i></button>
  </div>
</header>
"""


def hero(eyebrow, h1, sub, actions, inner=True, badge="Roof solutions, all in one", giant="Licensed CCC1334407"):
    cls = "hero hero--inner" if inner else "hero"
    return f"""<section class="{cls}">
  <div class="hero__frame">
    <div class="hero__media"></div>
    <div class="hero__scrim"></div>
    <span class="hero__ring" aria-hidden="true"></span>
    <span class="hero__giant" aria-hidden="true">{giant}</span>
    <div class="hero__in">
      <span class="hero__badge">{badge}</span>
      <ul class="hero__chips">
        <li>Licensed <b>CCC1334407</b></li>
        <li>Fort Myers, FL</li>
        <li>Free estimates</li>
      </ul>
      <span class="eyebrow">{eyebrow}</span>
      <h1>{h1}</h1>
      <p>{sub}</p>
      {actions}
    </div>
    <a class="hero__video" href="projects.html" aria-label="See the work">
      <span class="hero__video-k">See the work</span>
    </a>
  </div>
</section>

<section class="band">
  <div class="shell band__in">
    <span class="band__i"><svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12 12 4l9 8"/><path d="M6 11v8h12v-8"/></svg>Residential</span>
    <span class="band__i"><svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><path d="M4 13 12 5l8 8"/><path d="M14.5 8.5 9 20"/></svg>Repairs</span>
    <span class="band__i"><svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><path d="M3 20h18"/><path d="M5 20V9l7-4 7 4v11"/></svg>Light commercial</span>
    <span class="band__i"><svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3 4 6.5V12c0 4.6 3.4 7.8 8 9 4.6-1.2 8-4.4 8-9V6.5Z"/></svg>Maintenance</span>
    <span class="band__i"><svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3h9l3 3v15H6Z"/><path d="M9 9h6M9 13h6"/></svg>Free estimate</span>
    <span class="band__i"><svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>Same-day reply</span>
  </div>
</section>
"""



def pagehead(eyebrow, h1, sub, actions="", extra=""):
    """Inner pages get their own header. The nav sits on a solid bar above it,
       so no inner page reuses the homepage hero."""
    return f"""<header class="pagehead">
  <div class="shell pagehead__in">
    <div class="pagehead__lead">
      <span class="eyebrow">{eyebrow}</span>
      <h1>{h1}</h1>
    </div>
    <div class="pagehead__aside">
      <p class="lead">{sub}</p>
      {actions}
    </div>
  </div>
  {extra}
</header>
"""


STRIP = f"""<section class="strip">
  <div class="shell">
    <div class="strip__in">
      <div class="strip__cell">
        <span class="strip__k">State license</span>
        <span class="strip__v">CCC{LIC[3:]} &middot; Florida certified roofing contractor</span>
      </div>
      <a class="strip__cell strip__v" href="{MAPS}" target="_blank" rel="noopener">
        <span class="strip__k">Office</span>
        {ADDR}
      </a>
      <a class="strip__cell strip__v" href="mailto:{EMAIL}">
        <span class="strip__k">Email</span>
        {EMAIL}
      </a>
      <a class="strip__cell strip__v" href="tel:{PHONE_TEL}">
        <span class="strip__k">Call</span>
        {PHONE_TXT}
      </a>
    </div>
  </div>
</section>
"""

CTA = """<section class="section cta section--ink">
  <div class="shell cta__in">
    <div>
            <h2>Protect your home<br>with&nbsp;<em class="hl">confidence</em>.</h2>
      <p class="lead" style="margin-top:1.25rem;">Whether you need a simple repair or a full replacement, we will inspect your roof, explain your options, and help you make the right decision.</p>
    </div>
    <div class="cta__actions">
      <a class="btn btn--primary" href="contact.html"><span>Request a free inspection</span><span class="arrow">&rarr;</span></a>
      <a class="btn btn--light" href="tel:%s"><span>%s</span></a>
    </div>
  </div>
</section>
""" % (PHONE_TEL, PHONE_TXT)


def foot():
    svc = "".join(f'<li><a href="services.html">{s}</a></li>' for s in [
        "Residential roofing", "Roof repairs", "Commercial roofing", "Maintenance plans", "Free inspection"])
    comp = "".join(f'<li><a href="{h}">{l}</a></li>' for h, l in NAVS[1:])
    return f"""<footer class="foot">
  <div class="shell">
    <div class="foot__top">
      <div>
        <div class="nav__logo foot__logo">{MARK}</div>
        <p class="foot__tag">A passion for keeping our customers dry inside and satisfied. Roofing Southwest Florida since the beginning.</p>
      </div>
      <div>
        <h4>Services</h4>
        <ul>{svc}</ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>{comp}
          <li><a href="tel:{PHONE_TEL}">{PHONE_TXT}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        </ul>
      </div>
    </div>
    <div class="foot__bot">
      <span>&copy; 2026 Buckner Roofing LLC</span>
      <span>License # {LIC}</span>
      <span>{ADDR}</span>
    </div>
  </div>
</footer>
"""


STUDIO = """</body>
</html>
"""


def page(filename, title, desc, body):
    html = head(title, desc, filename) + nav(filename) + body + foot() + STUDIO
    (OUT / filename).write_text(html, encoding="utf-8")
    print("wrote", filename)


# ---------------------------------------------------------------- services data
SERVICES = [
    ("Residential Roofing",
     "Whether you need a replacement or a roof for your new home, our experienced team delivers durable, weather-ready roofing with quality craftsmanship from start to finish.",
     '<path d="M3 12 12 4l9 8"/><path d="M6 11v8h12v-8"/><path d="M10 19v-5h4v5"/>'),
    ("Roof Repairs",
     "Not every roof needs replacing. We provide honest inspections and lasting repairs that solve the problem without selling you work you do not need.",
     '<path d="M4 13 12 5l8 8"/><path d="M14.5 8.5 9 20"/><path d="M6.5 15h5"/>'),
    ("Commercial Roofing",
     "Protect your business with dependable roofing solutions that minimize downtime and keep your property secure through Florida's toughest weather.",
     '<path d="M3 20h18"/><path d="M5 20V9l7-4 7 4v11"/><path d="M9 20v-5h6v5"/><path d="M9 11h.01M15 11h.01"/>'),
    ("Roof Maintenance Plans",
     "Routine inspections and preventative maintenance help extend your roof's life, reduce costly repairs, and keep small problems from becoming major ones.",
     '<path d="M12 3 4 6.5V12c0 4.6 3.4 7.8 8 9 4.6-1.2 8-4.4 8-9V6.5Z"/><path d="m9 12 2 2 4-4"/>'),
    ("Free Roof Inspection",
     "Get an honest assessment of your roof at no cost. No pressure, no gimmicks, just straightforward recommendations from experienced roofing professionals.",
     '<path d="M6 3h9l3 3v15H6Z"/><path d="M9 9h6M9 13h6M9 17h3"/>'),
]


def svc_cards():
    out = ['<div class="svc rv">']
    for _i, (name, copy, path) in enumerate(SERVICES):
        out.append(f"""  <article class="svc__card">
    <div class="svc__photo pic{_i+1}"></div>
    <svg class="svc__icon" viewBox="0 0 24 24" aria-hidden="true" stroke-linecap="round" stroke-linejoin="round">{path}</svg>
    <h3>{name}</h3>
    <p>{copy}</p>
    <a class="tlink" href="services.html">Learn more <span class="arrow">&rarr;</span></a>
  </article>""")
    out.append("""  <article class="svc__card svc__card--cta">
    <svg class="svc__icon" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="6"/><path d="m20 20-4.5-4.5"/><path d="M8.5 11h5M11 8.5v5"/></svg>
    <h3>Not sure what your roof needs?</h3>
    <p>Schedule a free roof inspection and we will evaluate your roof, explain your options, and recommend the right solution, without the sales pressure.</p>
    <a class="tlink" href="contact.html">Schedule your free inspection <span class="arrow">&rarr;</span></a>
  </article>""")
    out.append("</div>")
    return "\n".join(out)


# ---------------------------------------------------------------- HOME
home_body = hero(
    "Fort Myers &middot; Southwest Florida",
    "Protecting your home<br>from Florida's<br>toughest&nbsp;<em class=\"hl\">weather</em>.",
    "Licensed, insured, and dedicated to delivering a roof, and an experience, you can count on.",
    """<div class="hero__actions">
      <a class="btn btn--primary" href="contact.html"><span>Get a free inspection</span><span class="arrow">&rarr;</span></a>
      <a class="btn btn--light" href="projects.html"><span>View projects</span></a>
    </div>""",
    inner=False,
) + STRIP + f"""
<section class="section">
  <div class="shell">
    <div class="sec-head rv">
      <div>
        <span class="eyebrow">Our services</span>
                <h2>Roofing services built<br>for&nbsp;<em class="hl">Florida</em>.</h2>
      </div>
      <div class="sec-head__aside">
        <a class="btn btn--ghost" href="services.html"><span>All services</span><span class="arrow">&rarr;</span></a>
      </div>
    </div>
    {svc_cards()}
  </div>
</section>

<section class="section section--tint">
  <div class="shell">
    <div class="duo">
      <div class="rv">
        <span class="eyebrow">Why Buckner</span>
                <h2>The right recommendation.<br><em class="hl">Every&nbsp;time</em>.</h2>
        <p class="lead" style="margin-top:1.5rem;">We believe trust is earned through honesty. That is why we never recommend replacing a roof that can be repaired. Our goal is simple: give you the best solution for your home, not the biggest invoice.</p>
        <p style="margin-top:1rem;">From your first inspection to the final cleanup, you will receive dependable service, clear communication, and quality workmanship.</p>
        <div class="stats">
          <div><span class="stats__n">CCC{LIC[3:]}</span><span class="stats__l">Florida license</span></div>
          <div><span class="stats__n">Free</span><span class="stats__l">On-site estimate</span></div>
          <div><span class="stats__n">SWFL</span><span class="stats__l">Local, storm-tested</span></div>
        </div>
      </div>
      <div class="duo__media duo__media--feature rv">
        <span class="duo__badge">Licensed &amp; insured</span>
      </div>
    </div>
  </div>
</section>

<section class="section section--brand">
  <div class="shell">
    <div class="sec-head rv">
      <div>
        <span class="eyebrow">How it goes</span>
        <h2>A simple process.<br><em class="hl">Exceptional&nbsp;results</em>.</h2>
      </div>
      <div class="sec-head__aside"><p>Every project follows the same proven process: clear communication, honest recommendations, quality craftsmanship, and no surprises from start to finish.</p></div>
    </div>
    <div class="steps rv">
      <div class="step">
        <span class="step__n">01</span>
        <svg class="step__i" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2Z"/></svg>
        <h3>Schedule your inspection</h3>
        <p>Give us a call or request an estimate online. We will schedule a convenient time to inspect your roof and discuss any concerns you have.</p>
      </div>
      <div class="step">
        <span class="step__n">02</span>
        <svg class="step__i" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="6"/><path d="m20 20-4.5-4.5"/><path d="M8.5 11h5M11 8.5v5"/></svg>
        <h3>Comprehensive roof inspection</h3>
        <p>We inspect your entire roofing system, not just the problem area, to identify the root cause and recommend the best long-term solution.</p>
      </div>
      <div class="step">
        <span class="step__n">03</span>
        <svg class="step__i" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3h9l3 3v15H6Z"/><path d="M9 10h6M9 14h6M9 18h3"/></svg>
        <h3>Honest recommendations</h3>
        <p>You will receive a clear, detailed estimate outlining your options, timeline, and pricing, without pressure or hidden costs.</p>
      </div>
      <div class="step">
        <span class="step__n">04</span>
        <svg class="step__i" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12 12 4l9 8"/><path d="M6 11v8h12v-8"/><path d="m9.5 15.5 1.5 1.5 3.5-3.5"/></svg>
        <h3>Quality installation</h3>
        <p>Our experienced crew completes the work with precision, keeps the job site clean, and leaves your property protected and looking its best.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="shell">
    <div class="sec-head rv">
      <div>
        <span class="eyebrow">Testimonials</span>
                <h2>What our clients say<br>about us and our&nbsp;work.</h2>
      </div>
      <div class="sec-head__aside"><p>Placeholder slots. Drop in real reviews from Google or Facebook before launch.</p></div>
    </div>
    <div class="quotes__wrap rv">
      <button class="qnav qnav--prev" type="button" aria-label="Previous reviews">
        <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="m15 5-7 7 7 7"/></svg>
      </button>
      <button class="qnav qnav--next" type="button" aria-label="Next reviews">
        <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="m9 5 7 7-7 7"/></svg>
      </button>
      <div class="quotes" id="quotes">
        <figure class="quote">
          <span class="quote__mark">&ldquo;</span>
          <blockquote>Add a real customer review here.</blockquote>
          <p class="quote__hint">Pull the strongest two or three sentences from a verified Google or Facebook review and paste them in.</p>
          <figcaption><span class="quote__name">Customer name</span><br><span class="quote__loc">City, FL</span></figcaption>
        </figure>
        <figure class="quote">
          <span class="quote__mark">&ldquo;</span>
          <blockquote>Add a real customer review here.</blockquote>
          <p class="quote__hint">Reviews that name the specific problem and the specific outcome convert better than general praise.</p>
          <figcaption><span class="quote__name">Customer name</span><br><span class="quote__loc">City, FL</span></figcaption>
        </figure>
        <figure class="quote">
          <span class="quote__mark">&ldquo;</span>
          <blockquote>Add a real customer review here.</blockquote>
          <p class="quote__hint">Keep each one short. Three lines is plenty at this size.</p>
          <figcaption><span class="quote__name">Customer name</span><br><span class="quote__loc">City, FL</span></figcaption>
        </figure>
        <figure class="quote">
          <span class="quote__mark">&ldquo;</span>
          <blockquote>Add a real customer review here.</blockquote>
          <p class="quote__hint">A storm-damage or insurance-claim story is worth including if you have one.</p>
          <figcaption><span class="quote__name">Customer name</span><br><span class="quote__loc">City, FL</span></figcaption>
        </figure>
        <figure class="quote">
          <span class="quote__mark">&ldquo;</span>
          <blockquote>Add a real customer review here.</blockquote>
          <p class="quote__hint">One review mentioning cleanup and crew conduct rounds the set out nicely.</p>
          <figcaption><span class="quote__name">Customer name</span><br><span class="quote__loc">City, FL</span></figcaption>
        </figure>
      </div>
    </div>
  </div>
</section>

""" + CTA

page("index.html", "Buckner Roofing | Protective Roofing at an Honest Price | Fort Myers, FL",
     "Licensed Florida roofing contractor in Fort Myers. Residential roofing, roof repairs, light commercial roofing and maintenance agreements. Free estimates.",
     home_body)


# ---------------------------------------------------------------- SERVICES
# Structure: capability index. A jump-chip rail, then an accordion of the trade,
# then a spec table. No hero photo, no borrowed homepage furniture.
chips = "".join(
    f'<a class="chip" href="#{n.lower().split()[0]}">{n}</a>' for n, _, _ in SERVICES)

acc = ""
for i, (name, copy, path) in enumerate(SERVICES):
    acc += f"""
      <details class="acc" id="{name.lower().split()[0]}"{' open' if i == 0 else ''}>
        <summary>
          <span class="acc__n">{i+1:02d}</span>
          <svg class="svc__icon" viewBox="0 0 24 24" aria-hidden="true" stroke-linecap="round" stroke-linejoin="round">{path}</svg>
          <span class="acc__t">{name}</span>
          <span class="acc__x" aria-hidden="true"></span>
        </summary>
        <div class="acc__body">
          <p>{copy}</p>
          <div class="acc__media pic{i+1}"></div>
        </div>
      </details>"""

page("services.html", "Services | Buckner Roofing | Fort Myers, FL",
     "Residential roofing, roof repairs, light commercial roofing, maintenance agreements and free estimates across Southwest Florida.",
     pagehead("Services", 'Roofing services built for <em class="hl">Florida</em>.',
              "Replacements, repairs, commercial roofing and maintenance plans. One licensed crew, and an honest recommendation every time.",
              '<a class="btn btn--primary" href="contact.html"><span>Get a free inspection</span><span class="arrow">&rarr;</span></a>',
              extra=f'<div class="shell"><nav class="chiprail" aria-label="Jump to a service">{chips}</nav></div>')
     + f"""
<section class="section section--flush">
  <div class="shell">
    <div class="acclist">{acc}
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="shell">
    <div class="sec-head rv">
      <div>
        <span class="eyebrow">What is included</span>
        <h2>The same standard on every job.</h2>
      </div>
      <div class="sec-head__aside"><p>Whether it is three shingles or three thousand square feet.</p></div>
    </div>
    <div class="spec rv">
      <div class="spec__row"><span class="spec__k">Inspection</span><span class="spec__v">Full roof, not just the spot you pointed at</span><span class="spec__b">Free</span></div>
      <div class="spec__row"><span class="spec__k">Estimate</span><span class="spec__v">In writing, in plain language, no obligation</span><span class="spec__b">Free</span></div>
      <div class="spec__row"><span class="spec__k">Crew</span><span class="spec__v">One crew start to finish, no subcontractor churn</span><span class="spec__b">Included</span></div>
      <div class="spec__row"><span class="spec__k">Clean-up</span><span class="spec__v">Property left the way we found it</span><span class="spec__b">Included</span></div>
      <div class="spec__row"><span class="spec__k">Licence</span><span class="spec__v">Florida certified roofing contractor</span><span class="spec__b">{LIC}</span></div>
    </div>
  </div>
</section>
""" + CTA)


# ---------------------------------------------------------------- PROJECTS
# Structure: the work leads. A featured slab, then the filterable grid.
# No page header photo, because the gallery IS the photo.
WORK = [
    ("Residential", "residential", "Tile roof replacement", "w1"),
    ("Repair", "repair", "Storm damage repair", "w2"),
    ("Commercial", "commercial", "Light commercial re-roof", "w3"),
    ("Residential", "residential", "Metal roof install", "w4"),
    ("Repair", "repair", "Shingle and flashing repair", "w5"),
    ("Commercial", "commercial", "Commercial tear-off", "w6"),
    ("Residential", "residential", "Tile roof, full replacement", "w7"),
    ("Repair", "repair", "Hurricane damage rebuild", "w8"),
    ("Residential", "residential", "New construction roof", "w9"),
    ("Residential", "residential", "Tile roof, crew install", "w10"),
    ("Residential", "residential", "Shingle tear-off and replace", "w11"),
    ("Repair", "repair", "Wind damage, shingle loss", "w12"),
    ("Repair", "repair", "Tile strip and re-batten", "w13"),
    ("Residential", "residential", "Suburban shingle repair", "w14"),
    ("Repair", "repair", "Asphalt shingle repair", "w15"),
    ("Commercial", "commercial", "Flat roof tear-out", "w16"),
    ("Residential", "residential", "New shingle application", "w17"),
    ("Repair", "repair", "Hurricane Ian tarp and rebuild", "w18"),
]
work_html = ""
for cat, key, title, pic in WORK:
    work_html += f"""
      <article class="work {pic}" data-cat="{key}">
        <div class="work__meta">
          <span class="work__cat">{cat}</span>
          <span class="work__t">{title}</span>
        </div>
      </article>"""

featured = """
  <div class="shell">
    <div class="feature rv">
      <div class="feature__media picband"></div>
      <div class="feature__card">
        <span class="work__cat">Featured</span>
        <h3>Add your strongest job here.</h3>
        <p>One project, told properly. What was wrong, what you did, what it looks like now. This slab is the single most persuasive thing on the site, so give it the best photograph you own.</p>
        <a class="tlink" href="contact.html">Start your project <span class="arrow">&rarr;</span></a>
      </div>
    </div>
  </div>
"""

page("projects.html", "Projects | Buckner Roofing | Fort Myers, FL",
     "Recent roofing work across Fort Myers and Southwest Florida. Residential, repair and light commercial roofing projects.",
     pagehead("Projects", 'The work speaks <em class="hl">first</em>.',
              "Residential, repair and light commercial roofing across Southwest Florida. Filter by the kind of job you have.",
              extra=featured)
     + f"""
<section class="section">
  <div class="shell">
    <div class="filters rv">
      <button data-filter="all" class="is-on">All work</button>
      <button data-filter="residential">Residential</button>
      <button data-filter="repair">Repairs</button>
      <button data-filter="commercial">Light commercial</button>
    </div>
    <div class="grid-work rv">{work_html}
    </div>
    <p class="note rv" style="margin-top:2rem;">Image slots are ready. Drop real job photos into <code>images/</code> and set the background on each tile.</p>
  </div>
</section>
""" + CTA)


# ---------------------------------------------------------------- ABOUT
# Structure: a portrait slab with an offset colour block behind it, a ledger of
# what the company holds to, and a service-area map rail. No hero photo.
page("about.html", "About | Buckner Roofing | Fort Myers, FL",
     "Buckner Roofing is a licensed Florida roofing contractor based in Fort Myers, led by Nathan Buckner. License CCC1334407.",
     pagehead("About us", 'This is our <em class="hl">home</em> too.',
              "Buckner Roofing is a licensed Florida roofing contractor working out of Fort Myers, led by Nathan Buckner.",
              '<a class="btn btn--primary" href="contact.html"><span>Talk to us</span><span class="arrow">&rarr;</span></a>')
     + f"""
<section class="section section--flush">
  <div class="shell">
    <div class="portrait rv">
      <div class="portrait__block" aria-hidden="true"></div>
      <div class="portrait__media picabout"><span class="duo__badge">Nathan Buckner &middot; Managing member</span></div>
      <div class="portrait__copy">
        <span class="eyebrow">Who we are</span>
        <h2>A passion for keeping our customers dry inside and satisfied.</h2>
        <p class="lead" style="margin-top:1.25rem;">That line is not marketing. It is the actual job. A roof either keeps the water out or it does not, and everything else we do is in service of that one outcome.</p>
        <p style="margin-top:1rem;">We are based in Fort Myers and we work across Southwest Florida. We hold Florida roofing licence {LIC}. We live under the same weather you do, which is a reasonable reason to trust the advice we give about it.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="shell">
    <div class="ledger rv">
      <div class="ledger__head">
        <span class="eyebrow">What we hold to</span>
        <h2>Three things, non-negotiable.</h2>
        <p>Everything else is detail.</p>
      </div>
      <div class="ledger__rows">
        <div class="ledger__row">
          <span class="ledger__n">01</span>
          <div><h3>Tell people the truth about their roof</h3><p>Including when the truth is that they do not need to spend money with us yet.</p></div>
        </div>
        <div class="ledger__row">
          <span class="ledger__n">02</span>
          <div><h3>Respect the property</h3><p>Your yard, your driveway, your landscaping. We work around them and we clean up after ourselves.</p></div>
        </div>
        <div class="ledger__row">
          <span class="ledger__n">03</span>
          <div><h3>Answer the phone</h3><p>Responsiveness is most of what separates a good contractor from a bad one, and it costs nothing.</p></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="sec-head rv">
      <div>
        <span class="eyebrow">Where we work</span>
        <h2>Southwest Florida, roof by roof.</h2>
      </div>
      <div class="sec-head__aside">
        <a class="btn btn--ghost" href="contact.html"><span>Check your address</span><span class="arrow">&rarr;</span></a>
      </div>
    </div>
    <div class="arearail rv">
      <div class="area"><span class="area__k">01</span><svg class="step__i" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s7-5.2 7-11a7 7 0 1 0-14 0c0 5.8 7 11 7 11Z"/><circle cx="12" cy="10" r="2.5"/></svg><h3>Fort Myers</h3><p>Home base, and the bulk of the work.</p></div>
      <div class="area"><span class="area__k">02</span><svg class="step__i" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M3 20h18"/><path d="M5 20V9l7-4 7 4v11"/><path d="M9 20v-5h6v5"/></svg><h3>North Fort Myers</h3><p>Residential and light commercial.</p></div>
      <div class="area"><span class="area__k">03</span><svg class="step__i" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3 4 6.5V12c0 4.6 3.4 7.8 8 9 4.6-1.2 8-4.4 8-9V6.5Z"/><path d="m9 12 2 2 4-4"/></svg><h3>Cape Coral</h3><p>Repairs, replacements, maintenance.</p></div>
      <div class="area"><span class="area__k">04</span><svg class="step__i" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M3.5 12h17M12 3a15 15 0 0 1 0 18M12 3a15 15 0 0 0 0 18"/></svg><h3>Lee &amp; Collier</h3><p>Call and we will tell you straight if you are in range.</p></div>
    </div>
  </div>
</section>
""" + CTA)


# ---------------------------------------------------------------- CONTACT
# Structure: the form is the page. It sits in a raised card overlapping a photo
# panel, with the office details as a rail beneath. No hero, no CTA band at the
# bottom, because the whole page IS the call to action.
page("contact.html", "Contact | Buckner Roofing | Fort Myers, FL",
     f"Get a free roofing estimate. Call {PHONE_TXT}, email {EMAIL}, or visit our Fort Myers office.",
     pagehead("Contact", 'Get in <em class="hl">touch</em> today.',
              "Free estimate, no obligation. Tell us what is going on up there and we will come and look at it.",
              f'<a class="btn btn--ghost" href="tel:{PHONE_TEL}"><span>Call {PHONE_TXT}</span></a>')
     + f"""
<section class="section section--flush">
  <div class="shell">
    <div class="quotebox rv">
      <div class="quotebox__media piccontact">
        <div class="quotebox__stat">
          <span class="stats__n">Free</span>
          <span class="stats__l">On-site estimate, no obligation</span>
        </div>
      </div>
      <div class="quotebox__card">
        <span class="eyebrow">Request a quote</span>
        <h2>Tell us about your roof.</h2>
        <form id="quoteForm" style="margin-top:2rem;">
          <div class="row2">
            <div class="field"><label for="fn">First name</label><input id="fn" name="fn" type="text" required></div>
            <div class="field"><label for="ln">Last name</label><input id="ln" name="ln" type="text" required></div>
          </div>
          <div class="row2">
            <div class="field"><label for="em">Email</label><input id="em" name="em" type="email" required></div>
            <div class="field"><label for="ph">Phone</label><input id="ph" name="ph" type="tel" required></div>
          </div>
          <div class="field">
            <label for="sv">What do you need</label>
            <select id="sv" name="sv">
              <option>Residential roofing</option>
              <option>Roof repair</option>
              <option>Light commercial roofing</option>
              <option>Roof maintenance agreement</option>
              <option>Not sure, I need an inspection</option>
            </select>
          </div>
          <div class="field"><label for="ms">What is going on</label><textarea id="ms" name="ms" placeholder="Leak in the back bedroom after the last storm..."></textarea></div>
          <button class="btn btn--primary" type="submit"><span>Send request</span><span class="arrow">&rarr;</span></button>
          <p class="note" id="formNote">We reply fast. Usually the same day.</p>
        </form>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="detail rv">
      <a class="detail__cell" href="{MAPS}" target="_blank" rel="noopener">
        <svg class="step__i" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s7-5.2 7-11a7 7 0 1 0-14 0c0 5.8 7 11 7 11Z"/><circle cx="12" cy="10" r="2.5"/></svg><span class="strip__k">Visit our office</span>
        <span class="strip__v">{ADDR}</span>
        <span class="tlink">Open in Maps <span class="arrow">&rarr;</span></span>
      </a>
      <a class="detail__cell" href="mailto:{EMAIL}">
        <svg class="step__i" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3.5 6.5 8.5 6 8.5-6"/></svg><span class="strip__k">Email us</span>
        <span class="strip__v">{EMAIL}</span>
        <span class="tlink">Write to Nate <span class="arrow">&rarr;</span></span>
      </a>
      <a class="detail__cell" href="tel:{PHONE_TEL}">
        <svg class="step__i" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2Z"/></svg><span class="strip__k">Call us</span>
        <span class="strip__v">{PHONE_TXT}</span>
        <span class="tlink">Same-day reply <span class="arrow">&rarr;</span></span>
      </a>
      <div class="detail__cell">
        <svg class="step__i" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3 4 6.5V12c0 4.6 3.4 7.8 8 9 4.6-1.2 8-4.4 8-9V6.5Z"/><path d="m9 12 2 2 4-4"/></svg><span class="strip__k">Licence</span>
        <span class="strip__v">{LIC}</span>
        <span class="tlink" style="color:var(--text-2)">Florida certified</span>
      </div>
    </div>
  </div>
</section>
""")

print("done")
