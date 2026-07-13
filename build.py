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
LOGO = "https://cdn.prod.website-files.com/6345811585993ec91eadc2dc/63458a18016ddf7f2e5530dc_buckner%20roofing%20orange%20logo.png"

# The supplied logo PNG sets "BUCKNER ROOFING" in WHITE, so the brand name vanishes on
# every light background. The mark is redrawn here and the wordmark is set in live text,
# which inherits colour and therefore always reads. Swap in the real vector when you get
# a version with a dark or two-tone wordmark.
MARK = ('<span class="brand">'
        '<svg class="brand__mark" viewBox="0 0 46 30" aria-hidden="true">'
        '<path class="brand__roof" d="M23 1 45 16.5h-5.4V29H6.4V16.5H1Z"/>'
        '<text class="brand__br" x="23" y="25" text-anchor="middle">BR</text>'
        '</svg>'
        '<span class="brand__name">Buckner<span>Roofing</span></span>'
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
<html lang="en" data-layout="crest" data-type="contemporary" data-theme="light" data-scale="spacious">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{LOGO}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600;700&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="index.css">
<script src="studio.js" defer></script>
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
            <h2>Ready to know exactly where your roof stands?</h2>
      <p class="lead" style="margin-top:1.25rem;">The estimate is free and there is no obligation. We come out, we look at everything, and we tell you the truth about what you need.</p>
    </div>
    <div class="cta__actions">
      <a class="btn btn--primary" href="contact.html"><span>Get a free estimate</span><span class="arrow">&rarr;</span></a>
      <a class="btn btn--light" href="tel:%s"><span>%s</span></a>
    </div>
  </div>
</section>
""" % (PHONE_TEL, PHONE_TXT)


def foot():
    svc = "".join(f'<li><a href="services.html">{s}</a></li>' for s in [
        "Residential roofing", "Roof repairs", "Light commercial", "Maintenance agreements", "Free estimate"])
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


STUDIO = """<button class="studio-fab" id="studioFab" aria-label="Open Design Studio" aria-expanded="false" aria-controls="studio">
  <svg viewBox="0 0 24 24" aria-hidden="true">
    <circle cx="12" cy="12" r="9"/>
    <circle cx="12" cy="8" r="1.4" fill="currentColor" stroke="none"/>
    <circle cx="8.4" cy="11" r="1.4" fill="currentColor" stroke="none"/>
    <circle cx="9.6" cy="15.4" r="1.4" fill="currentColor" stroke="none"/>
    <path d="M15.5 11c1.6 0 2.5 1 2.5 2.4 0 2-1.8 3.6-4.2 3.6"/>
  </svg>
</button>

<div class="studio-veil" id="studioVeil"></div>

<aside class="studio" id="studio" aria-hidden="true" aria-label="Design Studio">
  <div class="studio__head">
    <div>
      <h3>Design Studio</h3>
      <p>Four layouts, four references. Mix with type, colour and spacing.</p>
    </div>
    <button class="studio__x" id="studioClose" aria-label="Close Design Studio">&times;</button>
  </div>

  <div class="studio__body">
    <div class="studio__grp">
      <span class="studio__lbl">Layout <b data-readout="layout"></b></span>
      <div class="seg">
        <button data-axis="layout" data-value="crest">
          <span class="wire wire--crest"></span>
          <span class="seg__t">Crest</span>
          <span class="seg__d">Sky gradient, centred, airy. Light weight type, soft shadows, pill buttons.</span>
        </button>
        <button data-axis="layout" data-value="split">
          <span class="wire wire--split"></span>
          <span class="seg__t">Editorial Split</span>
          <span class="seg__d">Rounded card on grey. White panel left, photo right, trust chips, showreel tile.</span>
        </button>
        <button data-axis="layout" data-value="fixbild">
          <span class="wire wire--fixbild"></span>
          <span class="seg__t">Bold Display</span>
          <span class="seg__d">Stark centred headline with orange words, dashed ring, black trust bar.</span>
        </button>
        <button data-axis="layout" data-value="roofguard">
          <span class="wire wire--roofguard"></span>
          <span class="seg__t">Warm Feature</span>
          <span class="seg__d">Full-bleed photo, oversized wordmark, cream base, large radius cards.</span>
        </button>
        <button data-axis="layout" data-value="ridge" style="grid-column:1/-1">
          <span class="wire wire--ridge"></span>
          <span class="seg__t">Ridge <em style="font-style:normal;color:var(--orange)">&middot; original</em></span>
          <span class="seg__d">Not from a reference. Ink panel butted against the photo, a vertical licence rail, cards that step down like courses on a roof plane, sections cut on a 4:12 pitch. Zero radius, hard edges.</span>
        </button>
      </div>
    </div>

    <div class="studio__grp">
      <span class="studio__lbl">Header + body type <b data-readout="type"></b></span>
      <div class="seg">
        <button data-axis="type" data-value="contemporary">
          <span class="seg__t">Contemporary</span>
          <span class="seg__d">Sora geometric sans + Inter</span>
        </button>
        <button data-axis="type" data-value="luxury">
          <span class="seg__t">Classic Luxury</span>
          <span class="seg__d">Playfair serif + Jost</span>
        </button>
      </div>
    </div>

    <div class="studio__grp">
      <span class="studio__lbl">Colour distribution <b data-readout="theme"></b></span>
      <div class="seg">
        <button data-axis="theme" data-value="light">
          <span class="seg__t">Minimal Light</span>
          <span class="seg__d">White and grey, orange as accent only</span>
          <span class="sw"><i style="background:#ffffff;box-shadow:inset 0 0 0 1px #ddd"></i><i style="background:#f5f5f6"></i><i style="background:#14161a"></i><i style="background:#f26a21"></i></span>
        </button>
        <button data-axis="theme" data-value="dark">
          <span class="seg__t">Bold Dark</span>
          <span class="seg__d">Charcoal base, stark white, orange CTAs</span>
          <span class="sw"><i style="background:#0e1013"></i><i style="background:#1d2126"></i><i style="background:#ffffff;box-shadow:inset 0 0 0 1px #ddd"></i><i style="background:#ff7a33"></i></span>
        </button>
      </div>
    </div>

    <div class="studio__grp">
      <span class="studio__lbl">Spacing + text scale <b data-readout="scale"></b></span>
      <div class="seg">
        <button data-axis="scale" data-value="spacious">
          <span class="seg__t">Default Spacious</span>
          <span class="seg__d">Large margins, airy sections</span>
        </button>
        <button data-axis="scale" data-value="compact">
          <span class="seg__t">Compact Editorial</span>
          <span class="seg__d">Tighter rhythm, denser page</span>
        </button>
      </div>
    </div>
  </div>

  <div class="studio__foot">
    <button class="studio__reset" id="studioReset">Reset</button>
    <span class="studio__stamp">32 combinations</span>
  </div>
</aside>
</body>
</html>
"""


def page(filename, title, desc, body):
    html = head(title, desc, filename) + nav(filename) + body + foot() + STUDIO
    (OUT / filename).write_text(html, encoding="utf-8")
    print("wrote", filename)


# ---------------------------------------------------------------- services data
SERVICES = [
    ("Residential Roofing",
     "Flat and peak roofs, gutters, skylights, sun tunnels. Whole-home roofing handled by one crew, start to finish.",
     '<path d="M3 12 12 4l9 8"/><path d="M6 11v8h12v-8"/><path d="M10 19v-5h4v5"/>'),
    ("Roof Repairs",
     "Sometimes you need a repair, not a whole new roof, even though plenty of companies will try to sell you one.",
     '<path d="M4 13 12 5l8 8"/><path d="M14.5 8.5 9 20"/><path d="M6.5 15h5"/>'),
    ("Light Commercial Roofing",
     "A damaged roof over your business is a damaged business. We keep the building sealed and the doors open.",
     '<path d="M3 20h18"/><path d="M5 20V9l7-4 7 4v11"/><path d="M9 20v-5h6v5"/><path d="M9 11h.01M15 11h.01"/>'),
    ("Roof Maintenance Agreements",
     "If you live in Southwest Florida you have lived through hurricane season. Call us out and we mark some of the price off. This is our home too.",
     '<path d="M12 3 4 6.5V12c0 4.6 3.4 7.8 8 9 4.6-1.2 8-4.4 8-9V6.5Z"/><path d="m9 12 2 2 4-4"/>'),
    ("Free Estimate",
     "Call us out and we will be there as soon as we can. No pressure, no obligation, no fine print.",
     '<path d="M6 3h9l3 3v15H6Z"/><path d="M9 9h6M9 13h6M9 17h3"/>'),
]


def svc_cards():
    out = ['<div class="svc rv">']
    for name, copy, path in SERVICES:
        out.append(f"""  <article class="svc__card">
    <svg class="svc__icon" viewBox="0 0 24 24" aria-hidden="true" stroke-linecap="round" stroke-linejoin="round">{path}</svg>
    <h3>{name}</h3>
    <p>{copy}</p>
    <a class="tlink" href="services.html">Learn more <span class="arrow">&rarr;</span></a>
  </article>""")
    out.append("""  <article class="svc__card svc__card--cta">
    <h3>Not sure which one you need?</h3>
    <p>That is what the free inspection is for. We come out, we look at the whole roof, and we tell you.</p>
    <a class="tlink" href="contact.html">Book the inspection <span class="arrow">&rarr;</span></a>
  </article>""")
    out.append("</div>")
    return "\n".join(out)


# ---------------------------------------------------------------- HOME
home_body = hero(
    "Fort Myers &middot; Southwest Florida",
    "Protective roofing at an <em class=\"hl\">honest</em> price.",
    "A passion for keeping our customers dry inside and satisfied. Licensed, insured, and built for the way Florida weather actually behaves.",
    """<div class="hero__actions">
      <a class="btn btn--primary" href="contact.html"><span>Get a free quote</span><span class="arrow">&rarr;</span></a>
      <a class="btn btn--light" href="projects.html"><span>View projects</span></a>
    </div>""",
    inner=False,
) + STRIP + f"""
<section class="section">
  <div class="shell">
    <div class="sec-head rv">
      <div>
        <span class="eyebrow">Our services</span>
                <h2>Knowledge in every sector.</h2>
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
                <h2>We would rather fix it than sell you something you do not need.</h2>
        <p class="lead" style="margin-top:1.5rem;">Plenty of roofers look at an ageing roof and see a replacement. We look at it and see a roof. Sometimes the answer really is a repair, and we will tell you so, even when the bigger invoice is sitting right there.</p>
        <p style="margin-top:1rem;">That is the whole business. Show up when we say we will, do the work properly, leave the property clean, and be straight with people about what their roof actually needs.</p>
        <div class="stats">
          <div><span class="stats__n">CCC{LIC[3:]}</span><span class="stats__l">Florida license</span></div>
          <div><span class="stats__n">Free</span><span class="stats__l">On-site estimate</span></div>
          <div><span class="stats__n">SWFL</span><span class="stats__l">Local, storm-tested</span></div>
        </div>
      </div>
      <div class="duo__media rv">
        <span class="duo__badge">Licensed &amp; insured</span>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="sec-head rv">
      <div>
        <span class="eyebrow">How it goes</span>
                <h2>Four steps, no surprises.</h2>
      </div>
      <div class="sec-head__aside"><p>Every job runs the same way, whether it is three shingles or three thousand square feet.</p></div>
    </div>
    <div class="steps rv">
      <div class="step"><span class="step__n">Step 01</span><h3>You call</h3><p>Tell us what you are seeing. A stain, a leak, a storm, or just a roof that has been up there a long time.</p></div>
      <div class="step"><span class="step__n">Step 02</span><h3>We inspect</h3><p>We come out and look at all of it, not just the spot you pointed at. Free, and with no obligation attached.</p></div>
      <div class="step"><span class="step__n">Step 03</span><h3>You get the honest version</h3><p>Repair or replace, what it costs, and how long it takes. In plain language, in writing.</p></div>
      <div class="step"><span class="step__n">Step 04</span><h3>We build it</h3><p>One crew, start to finish. We clean up after ourselves and we leave the property the way we found it.</p></div>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="shell">
    <div class="sec-head rv">
      <div>
        <span class="eyebrow">Testimonials</span>
                <h2>What our clients say about us and our work.</h2>
      </div>
      <div class="sec-head__aside"><p>Placeholder slots. Drop in real reviews from Google or Facebook before launch.</p></div>
    </div>
    <div class="quotes rv">
      <figure class="quote">
        <span class="quote__mark">&ldquo;</span>
        <blockquote>Add a real customer review here.</blockquote>
        <p>Pull the strongest two or three sentences from a verified Google or Facebook review and paste them in.</p>
        <figcaption><span class="quote__name">Customer name</span><br><span class="quote__loc">City, FL</span></figcaption>
      </figure>
      <figure class="quote">
        <span class="quote__mark">&ldquo;</span>
        <blockquote>Add a real customer review here.</blockquote>
        <p>Reviews that name the specific problem and the specific outcome convert better than general praise.</p>
        <figcaption><span class="quote__name">Customer name</span><br><span class="quote__loc">City, FL</span></figcaption>
      </figure>
      <figure class="quote">
        <span class="quote__mark">&ldquo;</span>
        <blockquote>Add a real customer review here.</blockquote>
        <p>Keep each one short. Three lines is plenty at this size.</p>
        <figcaption><span class="quote__name">Customer name</span><br><span class="quote__loc">City, FL</span></figcaption>
      </figure>
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
          <div class="acc__media"></div>
        </div>
      </details>"""

page("services.html", "Services | Buckner Roofing | Fort Myers, FL",
     "Residential roofing, roof repairs, light commercial roofing, maintenance agreements and free estimates across Southwest Florida.",
     pagehead("Services", 'Everything above the <em class="hl">ceiling</em>.',
              "Flat and peak. Repairs and replacements. Homes and light commercial. One licensed crew for the whole roof.",
              '<a class="btn btn--primary" href="contact.html"><span>Get a free quote</span><span class="arrow">&rarr;</span></a>',
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
    ("Residential", "residential", "Shingle re-roof"),
    ("Repair", "repair", "Storm leak repair"),
    ("Commercial", "commercial", "Flat roof recover"),
    ("Residential", "residential", "Tile roof replacement"),
    ("Repair", "repair", "Flashing and skylight"),
    ("Commercial", "commercial", "Light commercial re-roof"),
    ("Residential", "residential", "Metal roof install"),
    ("Repair", "repair", "Gutter and fascia"),
    ("Commercial", "commercial", "Warehouse roof"),
]
work_html = ""
for cat, key, title in WORK:
    work_html += f"""
      <article class="work" data-cat="{key}">
        <div class="work__meta">
          <span class="work__cat">{cat}</span>
          <span class="work__t">{title}</span>
        </div>
      </article>"""

featured = """
  <div class="shell">
    <div class="feature rv">
      <div class="feature__media"></div>
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
      <div class="portrait__media"><span class="duo__badge">Nathan Buckner &middot; Managing member</span></div>
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
      <div class="area"><span class="area__k">01</span><h3>Fort Myers</h3><p>Home base, and the bulk of the work.</p></div>
      <div class="area"><span class="area__k">02</span><h3>North Fort Myers</h3><p>Residential and light commercial.</p></div>
      <div class="area"><span class="area__k">03</span><h3>Cape Coral</h3><p>Repairs, replacements, maintenance.</p></div>
      <div class="area"><span class="area__k">04</span><h3>Lee &amp; Collier</h3><p>Call and we will tell you straight if you are in range.</p></div>
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
      <div class="quotebox__media">
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
        <span class="strip__k">Visit our office</span>
        <span class="strip__v">{ADDR}</span>
        <span class="tlink">Open in Maps <span class="arrow">&rarr;</span></span>
      </a>
      <a class="detail__cell" href="mailto:{EMAIL}">
        <span class="strip__k">Email us</span>
        <span class="strip__v">{EMAIL}</span>
        <span class="tlink">Write to Nate <span class="arrow">&rarr;</span></span>
      </a>
      <a class="detail__cell" href="tel:{PHONE_TEL}">
        <span class="strip__k">Call us</span>
        <span class="strip__v">{PHONE_TXT}</span>
        <span class="tlink">Same-day reply <span class="arrow">&rarr;</span></span>
      </a>
      <div class="detail__cell">
        <span class="strip__k">Licence</span>
        <span class="strip__v">{LIC}</span>
        <span class="tlink" style="color:var(--text-2)">Florida certified</span>
      </div>
    </div>
  </div>
</section>
""")

print("done")
