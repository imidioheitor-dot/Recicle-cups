# Irish Comeback — site package

Not self-contained by design: the HTML loads its media from `./assets/`, so you can
open any image, swap it, recrop it or replace it with a real photograph later.

```
presentation.html            the product site — open this first
research.html                the sourced feasibility dossier
HIGGSFIELD-PROMPTS.md        every prompt used, plus the canonical machine spec
irish-comeback-blueprint.zip the build pack (drawings, BOM, tutorial)
assets/MANIFEST.json         the 24 media files and where they come from
fetch-assets.py              downloads them into ./assets
fetch-assets.sh              same thing, for a shell
```

## Start here

```bash
python3 fetch-assets.py      # ~24 files into ./assets
```

Then open `presentation.html` in a browser. That's it — no server, no build step.

**You can skip the download entirely.** Every `<img>` carries an `onerror` fallback and
every `<video>` a `data-fallback`, both pointing at the original CDN URL. Open the HTML
straight out of the zip with an internet connection and it renders exactly the same.
Running the fetcher just makes it work offline and lets you edit the files.

## Swapping in your own photographs

Filenames are stable and descriptive, so replacing a render with a real photo is a
drop-in. Keep the name, keep the aspect ratio.

| File | Where it appears |
|---|---|
| `bp-01-elevation.png` … `bp-05-panels.png` | Machine section, the drawing set |
| `machine-assembled.png` | Built section, hero shot + process backdrop |
| `machine-knolling.png` | Built section, the disassembled inventory |
| `machine-front.png` | Built section + the Dry process step |
| `machine-die.png` | Built section + the Draw process step |
| `machine-hopper.png` | Built section + the Separate process step |
| `machine-lab-night.png` | Built section + Collect step + Problem backdrop |
| `product-organizer.png` … `product-filament.png` | The six product cards (cutouts with alpha) |
| `product-family.png` | Banner above the product grid |
| `handle-tap.png` / `block-focus.png` | The Tag section pair |
| `spool-macro.png` | Built section + the Print process step |
| `board-process.jpg` | Process section backdrop — the full five-step board |
| `step-01-collect.jpg` … `step-05-print.jpg` | behind each of the five process steps |
| `bg-machine.mp4` / `bg-products.mp4` / `bg-tag.mp4` | Silent background video on three sections |

The six `product-*.png` files are **transparent PNGs** — they were generated on a white
plate and background-removed, so they sit on the dark page with no visible box. If you
replace one, cut it out too or it will show a rectangle.

The six `.jpg` files are **already in the zip** — they came from the process board
you supplied, sliced along its own gutters. `fetch-assets.py` skips them (they are
marked `bundled` in the manifest); everything else it downloads.

## A note on the media

These are AI-generated renders and drawings, not photographs of a machine that exists.
The blueprint sheets are illustrative — the dimensioned, hand-drawn SVGs inside
`irish-comeback-blueprint.zip` are the ones to build from.

## Trademark

The visual language is Notre Dame's palette and architecture — navy, gold, the domed
silhouette, collegiate gothic arches. The registered **ND monogram and University
wordmarks are deliberately not reproduced.** Using those on anything public, especially
anything with a price on it, needs licensing from the University.
