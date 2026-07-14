# Buckner Roofing — modernized multi-page site

Static. No build step to deploy. Drag the folder to Netlify or Vercel.

## Files
- index.html, services.html, projects.html, about.html, contact.html
- index.css — the whole design system, one file
- studio.js — Design Studio, sticky nav, mobile menu, scroll reveal, gallery filter
- build.py — regenerates the 5 pages from shared partials. Edit nav/footer/CTA HERE,
  not in the .html files, or the pages will drift apart.
- images/ — see images/README.md

## The logo
Buckner's own artwork, **inlined as base64 in index.css**. It has no file dependency and
cannot 404 when the folder is moved or a file is missed in a copy.

Their file sets the "BUCKNER ROOFING" wordmark in off-white (#f5f4ef), which disappears on
any light background. So two variants are embedded, identical except for that wordmark:

| Variant | Wordmark | Shown on |
|---|---|---|
| on-dark | off-white (their original) | charcoal bars, photo heroes, footer |
| on-light | recoloured to ink | white and cream bars |

The orange mark is untouched in both. CSS cross-fades between them based on what is behind
the bar. Verified legible in all 40 nav/footer x layout x theme combinations.

The source PNGs are still in `images/` for reference, but the SITE DOES NOT READ THEM.
To change the logo, regenerate the base64 (see the BRAND LOCKUP block in index.css).

## Brand colour
#FF5307, sampled directly from the pixels of their logo file. ONE place to change it:

    index.css → :root → --orange: #ff5307;

Everything else (buttons, accent words, icons, focus rings, the FAB) derives from it.
The dark theme lifts it to #ff6a2b for contrast on charcoal.

## Design Studio
Floating orange circle, bottom right. Four axes on `<html>`:

    data-layout : crest | split | fixbild | roofguard | ridge
    data-type   : contemporary | luxury
    data-theme  : light | dark
    data-scale  : spacious | compact

40 combinations. The choice persists across pages via localStorage.

### The five layouts
Each one restructures the WHOLE page, not just the hero: services, the feature block,
process, gallery, testimonials and the CTA band all change shape.

| Preset | From | Hero | Services | Feature block | Process | Testimonials | CTA |
|---|---|---|---|---|---|---|---|
| **Crest** | ref 1 | Sky gradient, centred, photo masked into the base | 3x2, centred, icon in a soft disc, no borders | Stacked and centred, photo as a 21:9 plate below the copy | Four beats strung on one hairline, numbers in circles | Borderless, floating, centred | Quiet tinted band, centred |
| **Editorial Split** | ref 2 | Rounded white card on grey, photo right, trust chips, showreel tile | Collapses to editorial rows | Side by side, tall 4:5 portrait | Ruled rows | Two wide slabs with an orange left rule | Ink band, actions right-aligned |
| **Bold Display** | ref 3 | Stark centred display type, dashed ring, black trust bar | Bento: one tall black card, full-width orange banner closes it | Photo left with a play cue, stats become a ruled checklist | Alternating black and white blocks | Black cards, orange top rule | Full black band, oversized |
| **Warm Feature** | ref 4 | Full-bleed photo, oversized ROOFING wordmark, cream base | Bento: wide lead card, orange call-now banner | Copy left, square photo right, stats become pill chips | Soft cards, number as a corner chip | Soft cards with an avatar disc | Inset orange gradient card |
| **Ridge** | **original** | Ink panel butted against the photo, vertical licence rail | Two columns that STEP DOWN like courses on a roof plane | Photo hard left, copy indented off a rule | Oversized numerals on ruled rows | No cards, columns divided by rules | Cut on a 4:12 pitch |

**Ridge** is the one that is not a recreation. It is built off the ridge line rather than
off web fashion: zero radius, hard edges, the licence number set vertically down the left
edge as a rail, service cards offset so they step like shingle courses, and the CTA band
clipped on a 4:12 roof pitch so the section join reads as a roofline. Pitch it as the
"nobody else in SWFL has this" option.

The layout axis is independent of the other three, so Warm Feature can run dark and
compact with serif headers if the client wants it.

## Locking in the final look
Once they pick, set their combo as the default in build.py (`data-layout="..."` in
`head()`, and DEFAULTS in studio.js), then delete the FAB, veil and `<aside class="studio">`
blocks from build.py and rebuild.

## Before launch
1. **Photography.** The hero now uses Buckner's own CDN photo, with a drawn roofline scene
   layered underneath as a fallback. Self-host it before launch rather than hotlinking
   Webflow. See images/README.md.
2. **Reviews.** The three testimonial slots on index.html are marked placeholders. The old
   site shipped the Webflow template lorem ipsum under fake names. Do not repeat that.
3. **Form.** Currently intercepts submit and shows a note. Point it at GHL, Formspree, or Netlify Forms.
4. **Phone number.** The live site displays (239) 922-8196 but its own tel: link points at
   (239) 980-2837. One of them is wrong. I used the displayed one.

## Page architecture
Only the HOME page uses the big hero. Every inner page has its own structure, so the nav
is solid from the first pixel on all four of them and no page borrows another's furniture.

| Page | Structure |
|---|---|
| **Home** | Full hero (shape set by the layout axis) + services + feature block + process + testimonials + CTA |
| **Services** | Page header + jump-chip rail + accordion of the trade (`<details>`, native, no JS) + spec table |
| **Projects** | Page header + featured slab with an overlapping caption card + filterable grid |
| **About** | Page header + portrait slab on an offset colour block + numbered ledger + service-area rail |
| **Contact** | Page header + the form in a raised card overlapping a photo panel + detail cells. No CTA band, because the whole page IS the call to action. |

These structures are page-level. The layout axis still restyles them (radius, type,
colour, whether heads centre or run asymmetric), so Services in Ridge and Services in
Crest look like different sites — but Services never looks like Home.

## Secondary CTA buttons
`.btn--light` is white text on a white border. It works on a dark photo and is INVISIBLE on
a light one. Bold Display and Editorial Split both put the hero copy on a light panel, so
the "View projects" button was rendering white-on-white — which also made the CTA pair look
off-centre, because only one of the two buttons was actually visible.

Those two layouts, and every inner-page header, now flip `.btn--light` to a dark outline.
If you add a hero with a light background, do the same or the secondary CTA will disappear.

## The orange band
The process section on Home runs `.section--brand` — full-bleed orange, white text,
glass step cards, icons. It sits between two neutral sections so it reads as one
deliberate beat rather than decoration.

**Do not set it to #ff5307.** White on the brand orange is only 3.2:1, which fails AA for
body copy. The band runs on #cc3c00 (4.71:1) and all its text is SOLID white — alpha
transparency on white text cost 0.7 of a contrast point and pushed it back under. Hierarchy
in the band comes from size and weight, not opacity.

To move the band to another section, add `section--brand` to that `<section>` in build.py.
The colour rules already override every layout's step styling.

## Mobile
Sized from measurements at 390px, not from clamps. Warm Feature was padding 176px above
the fold and every page header 128px; both are cut roughly in half. Hero CTAs go full
width and stack, stacked heroes drop their desktop `min-height`, the Split showreel tile
and the Bold Display ring are hidden, and overlapping cards pull their negative margins
back. Verified across 8 widths x 5 layouts x 5 pages: no horizontal overflow anywhere.

Known trap, now fixed: `backdrop-filter` on the stuck nav makes it a containing block for
`position: fixed` children, which clipped the off-canvas menu to the 58px bar instead of the
viewport. Inner pages are always stuck, so the menu links leaked over the page content there.
The mobile block drops the filter and goes opaque. Do not put backdrop-filter back.

The mobile block is deliberately the LAST thing in index.css. It has to win over the
layout rules above it. Do not append new layout CSS below it.

## Nav contrast
The nav is transparent over the hero, so its colour is set PER LAYOUT, not globally:

- **Inner pages have no hero**, so the nav is pinned solid from the first pixel. Contrast
  is never in question there.
- On HOME: **Crest** is the only layout with dark sky behind the nav, so it runs white text
  and a knocked-out white logo.
- **Editorial Split, Bold Display and Warm Feature** all pad the hero down, which means the
  nav actually floats over a LIGHT page background. They run dark text and the original
  orange logo.
- Dark theme flips the last three back to white.

If you add a fifth layout, set its `.nav--over` colour deliberately or it will inherit
white text and vanish on a light page.
