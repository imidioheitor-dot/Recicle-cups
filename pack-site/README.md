# Irish Comeback — offline site pack

Unzip anywhere and open `presentation.html`. No build step, no server, no
network. Everything the page needs is in this folder.

## What is in here

    presentation.html            the site
    research.html                the research dossier
    irish-comeback-blueprint.zip BOM, die drawing, PID notes, log template
    assets/                      the five files the site actually loads
    assets/MANIFEST.json         what each asset is and why
    HIGGSFIELD-PROMPTS.md        the generation prompts, kept for the record
    fetch-assets.py              legacy fetcher, see "No CDN" below

## No CDN

Earlier builds pulled rendered PNGs of the machine and the products from a
CDN at first load. This build does not. Those renders were replaced by
geometry the page draws itself in WebGL, so the only binary assets left are
one video and four photographs, and all five ship inside this folder.

`fetch-assets.py` is kept because the manifest format is still useful if you
add remote assets of your own. Run against this manifest it will report every
entry as `bundled` and download nothing.

The one external request the page still makes is to Google Fonts. If it is
blocked, or you are offline, the page falls back to the system grotesk and
system monospace and the layout does not move.

## Swapping a render for a real photograph

Filenames are stable and descriptive. Drop a real photograph over
`assets/step-03-dry.jpg` and the site picks it up with no code change. Keep
the aspect ratio roughly as-is; the cards use `object-fit: cover`, so a
different ratio crops rather than distorts.

## Trademark

This is an independent student project. It is not affiliated with, endorsed
by, or sponsored by the University of Notre Dame. The University's registered
ND monogram, its wordmarks and its athletic marks are deliberately not
reproduced anywhere on the site or on any part the line produces.

Two supplied images did carry the registered monogram and were handled
before shipping:

* `step-03-dry.jpg` and `step-04-draw.jpg` were cropped to remove it.
* `step-05-print.jpg` could not be cropped — a print of the monogram was its
  entire subject — so it is no longer referenced. Process step 05 now shows a
  live WebGL build of MDL-02, the hex vessel, instead.
* `board-process.jpg` is the source board those crops came from. Every one of
  its five panels carries the monogram, so it is kept for reference only and
  is not referenced by the site.

Nothing was deleted; the originals are still in `assets/` if you want them.

## What the page renders itself

* Fig. 1, the problem section — 2,000 lit plates carrying three baked
  positions each (bottle wall, flake drift, wound spool), blended by scroll.
* The portal — a hexagonal shaft, one fullscreen fragment shader, 44 rings
  spaced exponentially so the recession is angularly even.
* MDL-01 to MDL-03 — procedural geometry, draggable. These are models. No
  part on this site has been manufactured yet, and the page says so.
* Process step 05 — the MDL-02 mesh under a rising clip plane.

All of it degrades: if WebGL is unavailable the canvases hide themselves and
the surrounding layout is unaffected.
