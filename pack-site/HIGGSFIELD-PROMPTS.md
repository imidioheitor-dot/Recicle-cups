# Irish Comeback — Higgsfield Image Prompt Library
### Unit 01 · Rev 1.0 · Master visual specification

Every prompt below is written against one canonical machine. Read Section 0 first —
it is the source of truth that keeps all sixteen images consistent with each other.
Any prompt can be pasted into Higgsfield verbatim.

---

## 0. CANONICAL SPECIFICATION — the single source of truth

### 0.1 Overall envelope
```
Width      1180 mm
Height      720 mm  (bench surface at 900 mm when on legs)
Depth       620 mm
Dry mass    ~64 kg
Footprint   one standard lab bench
```

### 0.2 Materials and finish
| Element | Material | Finish / colour |
|---|---|---|
| Main frame, side panels | 6 mm laser-cut mild steel | Powder-coated **Notre Dame navy `#0C2340`**, satin |
| Hopper | 6 mm mild steel, folded | Same navy, interior raw mill steel |
| Heater bands, hazard marks, E-stop bezel | — | **Notre Dame gold `#C99700`** |
| Shredder blades, hex shaft | Hardened C45 tool steel | Raw ground steel, bright |
| Fasteners, pillow blocks | Zinc-plated steel | Silver-grey |
| Extrusion barrel | Aluminium | Anodised black |
| Cabling | Braided sleeve | Black with gold heat-shrink markers |
| Bench top | 18 mm plywood | Natural birch, clear-coated |

### 0.3 Component register — names, positions, prices
**LINE A — Pultrusion (PET #1) · $342**
| # | Component | Spec | Position | Price |
|---|---|---|---|---|
| A1 | ReCreator 3D MK6 pultrusion kit | Open-source | Centre-right of frame | $189 |
| A2 | Bottle cutter jig | 4-blade adjustable, 7–9 mm ribbon | Left of barrel, bench-mounted | $18 |
| A3 | E3D V6 hotend, 24 V | Brass die, 1.75 mm bore | Barrel exit | $24 |
| A4 | NEMA 17 stepper + A4988 driver | 1.8° | Under spooler | $22 |
| A5 | BTT/MKS 32-bit board + LCD | — | Control fascia | $35 |
| A6 | Power supply | 24 V 10 A | Rear left, caged | $28 |
| A7 | PTFE tubing + nozzle set | 1.75 mm | Along barrel | $14 |
| A8 | Spooler and guide | Printed PETG, navy | Far right | $12 |

**LINE B — Shredder (PP #5 / HDPE #2) · $528**
| # | Component | Spec | Position | Price |
|---|---|---|---|---|
| B1 | Blade set | 12 hardened blades + spacers | Inside drum, left | $110 |
| B2 | Hex drive shaft | 20 mm across flats, C45 | Through drum | $24 |
| B3 | Pillow-block bearings ×4 | 20 mm bore | Both sides of drum | $26 |
| B4 | Worm gear reducer | 60:1, cast iron | Below drum | $145 |
| B5 | Motor | 1.5 HP, 110 V, surplus | Lower left | $120 |
| B6 | Frame + hopper | 6 mm steel, laser cut | Structure | $45 |
| B7 | Switchgear, E-stop, wiring | IEC rated | Control fascia | $58 |

**SHARED · $98**
| # | Component | Spec | Position | Price |
|---|---|---|---|---|
| S1 | Food dehydrator | Adjustable to 65 °C, 5 trays | Upper centre shelf | $45 |
| S2 | NTAG215 NFC tags ×100 | 25 mm disc, 504-byte NDEF | Parts drawer | $18 |
| S3 | PPE set | Gloves, goggles, respirator, ABC extinguisher | Wall hook | $35 |

```
Line A   $342
Line B   $528
Shared   $ 98
------------
Total    $968      Contingency $32      Ceiling $1,000
```

### 0.4 Left-to-right layout (this ordering must never change)
```
[ MOTOR + REDUCER ] → [ SHREDDER DRUM + HOPPER ] → [ DEHYDRATOR ]
    → [ CUTTER JIG ] → [ PULTRUSION BARREL + 2 HEATER BANDS ] → [ DIE ] → [ SPOOLER ]
                              [ CONTROL FASCIA + E-STOP ] below barrel
```

### 0.5 Operating values that appear as callouts
```
Shredder drum      70 rpm, ~500 N·m
Dehydrator         65 °C, 4 h
Barrel zone 1      238 °C
Barrel zone 2      245 °C
Die                1.75 mm ± 0.05
Spooler            closed-loop pull, tension compensated
Mains              110 V, 15 A
```

---

## 1. SHARED STYLE BLOCKS

Paste the matching block at the end of any prompt.

### 1.1 BLUEPRINT STYLE BLOCK
> Rendered as a technical engineering blueprint: deep navy `#0A1626` background with a
> faint 24-pixel grid, all linework in pale cyan-blue `#7FA9DC` at consistent 1.4 px
> weight, hidden edges as dashed lines, centrelines as long-dash-dot. Dimension lines
> and part callouts in metallic gold `#E8B923` with precise arrowheads and extension
> lines. Annotation text in a clean condensed monospace, uppercase, small and legible.
> Title block in the lower right corner. Orthographic projection, absolutely flat, no
> perspective, no shading, no gradients, no photographic lighting. Drafting precision,
> CAD-plot aesthetic, crisp vector-like edges.

### 1.2 PHOTOREAL STYLE BLOCK
> Photorealistic product photography on a matte charcoal surface in a dark workshop.
> Single large softbox from the upper right as key, cool blue fill from the left, warm
> gold rim light tracing the top edges. Deep controlled shadows, faint volumetric haze,
> shallow depth of field. Shot on a full-frame camera, 50 mm lens at f/4 for the wide
> views and 100 mm macro at f/2.8 for details. Colour-graded cool with warm highlights.
> Real machined-metal microdetail: brushed grain, faint scratches, fingerprint smudges
> on powder coat, visible weld seams, hex bolt heads. Commercial catalogue quality.

### 1.3 UNIVERSAL NEGATIVES
> No cartoon styling, no CGI plastic look, no floating parts without support, no
> distorted or nonsensical text, no watermarks, no human faces, no brand logos of
> real companies, no lens flare, no oversaturation.

---

## 2. BLUEPRINT PROMPTS (5)

### B1 — Master assembly elevation
> Technical engineering blueprint, front elevation of a bench-top plastic recycling
> machine labelled "IRISH COMEBACK — UNIT 01". The machine is a rectangular welded
> steel frame 1180 mm wide by 720 mm tall, drawn in orthographic front view.
> From left to right the drawing shows: a cylindrical electric motor with a cast worm
> gear reducer bolted above it in the lower left; a large circular shredder drum of
> 116 mm radius containing twelve radial blade slots around a 20 mm hexagonal centre
> shaft, with a trapezoidal hopper funnelling into it from above; a rectangular
> five-tray dehydrator cabinet in the upper centre; a long horizontal extrusion barrel
> spanning the centre-right with two vertical heater bands drawn as gold rectangles at
> one third and two thirds along it; a conical die at the barrel exit; and a large
> circular filament spooler at the far right with a dashed filament path curving from
> die to spool. A rectangular control box with an LCD window, two indicator lamps and
> one round E-stop button sits below the barrel.
> Overall dimension lines run along the bottom reading "1180" and up the right side
> reading "720", both in gold with arrowheads. Numbered gold circular balloons 1
> through 5 point to the shredder drum, dehydrator, barrel, spooler and motor.
> Small uppercase labels read: HOPPER, SHREDDER DRUM 12 BLADES, DEHYDRATOR 65C,
> PULTRUSION BARREL 245C, SPOOLER, MOTOR 1.5HP, CONTROL + E-STOP.
> Title block lower right reads "SIDE ELEVATION · SCALE 1:8 · REV 1.0 · BUDGET $968".
>
> [BLUEPRINT STYLE BLOCK] [UNIVERSAL NEGATIVES]

### B2 — Exploded axonometric, fully disassembled
> Technical engineering blueprint, exploded axonometric view of the same bench-top
> plastic recycling machine, every component separated along vertical and diagonal
> explosion axes with thin gold dashed leader lines connecting each part back to its
> assembled position.
> Components floating in the explosion, each with a gold balloon number and a small
> label: six flat steel frame panels fanned outward; the trapezoidal hopper lifted
> above; twelve individual circular shredder blades separated like a deck of cards
> along a horizontal hexagonal shaft with spacer rings between them; four pillow-block
> bearings; a cast worm gear reducer; a cylindrical motor; the five-tray dehydrator
> cabinet with trays pulled out and stacked; a horizontal barrel split from its two
> gold heater bands and its brass conical die; a stepper motor; a spool hub with its
> guide arm; a control board with an LCD and a round E-stop; a coiled wiring loom.
> A parts list table sits along the right edge with rows reading:
> "B1 BLADE SET x12 $110 / B2 HEX SHAFT 20MM $24 / B3 BEARINGS x4 $26 /
> B4 REDUCER 60:1 $145 / B5 MOTOR 1.5HP $120 / B6 FRAME 6MM $45 /
> A1 PULTRUSION KIT $189 / A3 HOTEND V6 $24 / S1 DEHYDRATOR $45 / TOTAL $968".
> Isometric projection at 30 degrees, everything drawn in flat linework.
>
> [BLUEPRINT STYLE BLOCK] [UNIVERSAL NEGATIVES]

### B3 — Shredder drum, section detail
> Technical engineering blueprint, large-scale cutaway section detail of a plastic
> shredder drum, drawn at scale 2:1. The section reveals twelve hardened steel cutting
> blades stacked alternately with spacer rings on a 20 mm hexagonal drive shaft, the
> hexagonal profile clearly visible in the centre of each blade. Cut material is shown
> with 45-degree gold hatching. Blade teeth are drawn as hooked profiles engaging small
> irregular plastic cap fragments falling from a hopper throat above.
> Two pillow-block bearings bracket the shaft at each end, with a splined coupling on
> the right connecting to a worm gear reducer shown partially.
> Gold dimension callouts read: "BLADE OD 96", "SHAFT AF 20", "BLADE t 6",
> "SPACER t 4", "STACK L 132", "12 OFF". Annotation notes read
> "70 RPM · 500 N·M · HARDENED C45" and "FEED: PP #5 CAPS · HDPE #2 ONLY — NEVER PET".
> A detail bubble in the upper right shows a single blade tooth profile enlarged 8:1.
>
> [BLUEPRINT STYLE BLOCK] [UNIVERSAL NEGATIVES]

### B4 — Pultrusion head, thermal cutaway
> Technical engineering blueprint, longitudinal cutaway section through a filament
> pultrusion head, scale 2:1. A continuous flat plastic ribbon 8 mm wide enters from
> the left, passes through a tapered convergence zone, and exits on the right as round
> filament through a brass die. Cut metal shown with fine gold hatching.
> Two heater bands are drawn as gold blocks clamped around the aluminium barrel with a
> thermistor probe drawn between them on a thin lead. A thermal gradient is annotated
> along the barrel with gold tick marks reading "ZONE 1 238C", "ZONE 2 245C",
> "DIE 1.75 ±0.05".
> To the right, a pair of driven pinch rollers pull the filament, with a gold arrow
> labelled "PULL — NOT PUSH" and a note reading "NO SCREW · NO MELT RESERVOIR ·
> THIS IS WHY IT FITS THE BUDGET".
> Dimension lines give "BARREL L 284", "BARREL OD 42", "DIE BORE 1.75",
> "RIBBON W 7-9". Lower left note reads "PET #1 ONLY · DRY 4H AT 65C BEFORE RUN".
>
> [BLUEPRINT STYLE BLOCK] [UNIVERSAL NEGATIVES]

### B5 — Frame panels, laser-cut nesting sheet
> Technical engineering blueprint, flat pattern nesting layout for laser cutting,
> showing five steel panels arranged efficiently on a single rectangular sheet.
> Panel A: a 300 by 200 rectangle with four corner bolt holes and a large 84 mm
> diameter central bore, marked "x2". Panel B: a 220 by 200 rectangle with a rounded
> rectangular cable port. Panel C: a hopper throat development, a rectangle with a
> trapezoidal fold-out flap and dashed bend lines. Panel D: a 380 by 120 bench top with
> two dashed rectangles marked as motor and reducer footprints. Panel E: a control
> fascia with a rectangular LCD window and two round button holes.
> All cut contours drawn in bright gold as the cut path; dashed pale blue lines mark
> bend and reference lines only. Each panel carries a small label beneath it giving its
> letter, name, quantity and size.
> A note along the bottom reads "MATERIAL 6MM MILD STEEL · SHEET AREA 0.42 M2 ·
> LASER CUT AT ND INNOVATION LAB · MATERIAL COST $45 · DEBURR ALL EDGES".
>
> [BLUEPRINT STYLE BLOCK] [UNIVERSAL NEGATIVES]

---

## 3. PHOTOREALISTIC MACHINE PROMPTS (6)

### P1 — Hero three-quarter, assembled
> A complete bench-top plastic recycling machine photographed in three-quarter view
> from slightly above, 1180 mm wide and 720 mm tall. Its welded frame is 6 mm steel
> powder-coated deep navy blue `#0C2340` with a satin finish showing faint fingerprints.
> On the left sits a cylindrical grey electric motor coupled to a cast-iron worm gear
> reducer, feeding a large drum housing above it with a folded navy steel hopper.
> In the centre a stainless five-tray dehydrator cabinet glows faintly amber through
> its door. To the right a horizontal black anodised aluminium extrusion barrel carries
> two brass-gold heater bands with a thermistor lead taped between them; a thin strand
> of glossy navy-blue filament emerges from the brass die at its end and winds onto a
> large 3D-printed navy spool at the far right. Below the barrel, a small control box
> shows a lit LCD and a single mushroom-shaped gold-bezelled emergency stop button.
> Black braided cable looms run along the frame secured with gold heat-shrink markers.
> Zinc-plated hex bolts, visible weld seams, a birch plywood bench top.
>
> [PHOTOREAL STYLE BLOCK] [UNIVERSAL NEGATIVES]

### P2 — Front elevation, assembled, studio
> The same navy bench-top plastic recycling machine photographed dead-on in strict
> front elevation, perfectly symmetrical to the camera, filling the frame edge to edge
> against a near-black seamless background. Every subsystem is readable in silhouette:
> motor and reducer far left, circular shredder drum housing with trapezoidal hopper
> above it, dehydrator cabinet centre, long horizontal barrel with two gold heater
> bands, brass die, and the circular spool at far right wound with navy filament.
> The control box below the barrel shows a glowing cyan LCD and a gold emergency stop.
> Lighting is a single broad overhead softbox with two narrow gold strip lights raking
> the sides, producing a clean product-catalogue separation from the background.
>
> [PHOTOREAL STYLE BLOCK] [UNIVERSAL NEGATIVES]

### P3 — Fully disassembled, knolling top-down
> Top-down flat-lay knolling photograph of the same machine completely disassembled,
> every component laid out on matte charcoal in neat parallel rows with even spacing,
> perfectly square to the frame.
> Visible: six navy powder-coated steel panels; a folded navy hopper; twelve bright
> hardened steel circular shredder blades fanned in a row with small spacer rings
> between them; a 20 mm hexagonal steel shaft; four zinc pillow-block bearings; a
> cast-iron worm gear reducer; a grey electric motor; a stainless dehydrator with its
> five trays stacked beside it; a black anodised barrel with two brass heater bands and
> a brass conical die placed alongside; a small stepper motor; a 3D-printed navy spool
> hub; a green control board with an LCD; a gold-bezelled emergency stop button; a
> coiled black wiring loom; a small tray of 25 mm white NFC discs; safety goggles and
> gloves in one corner.
> Every part is crisply lit and separated, nothing overlapping — the visual inventory
> of a $968 build.
>
> [PHOTOREAL STYLE BLOCK] [UNIVERSAL NEGATIVES]

### P4 — Pultrusion head running, macro
> Extreme macro photograph of a filament pultrusion head in operation. A black anodised
> aluminium barrel with a brass-gold heater band fills the left of the frame, its
> surface radiating visible heat shimmer. From a polished brass conical die at the
> centre, a single continuous strand of glossy deep-navy recycled plastic filament
> emerges, still faintly translucent and hot, catching a warm gold specular highlight
> along its length before curving off to the right toward a spool.
> A thin thermistor lead and a braided black cable run out of frame. A small digital
> readout glows in the dark background reading "245". Dust motes float in the beam.
> 100 mm macro lens at f/2.8, focus precisely on the die exit, background dissolved.
>
> [PHOTOREAL STYLE BLOCK] [UNIVERSAL NEGATIVES]

### P5 — Shredder hopper and flake, macro
> Macro photograph looking down into the open trapezoidal navy steel hopper of a
> plastic shredder. Below the throat, twelve bright hardened steel blades on a
> hexagonal shaft are partly visible in shadow, their hooked teeth catching a hard
> raking highlight. Falling and resting on the blades are dozens of small irregular
> shredded plastic cap fragments in mixed navy blue, white and gold, each 5 to 12 mm
> across with sharp fractured edges and a slight satin sheen.
> A gold hazard stripe is painted along the hopper rim. Fine plastic dust clings to the
> steel. Cool overhead light with a warm gold kicker from the right.
>
> [PHOTOREAL STYLE BLOCK] [UNIVERSAL NEGATIVES]

### P6 — In context, student lab at night
> Wide environmental photograph of the navy bench-top plastic recycling machine
> installed on a birch plywood workbench in a university engineering lab at night.
> Behind it, out of focus, are pegboard walls with hand tools, blue plastic crates
> overflowing with clear empty water bottles, and a 3D printer glowing faintly.
> The machine is the only sharply lit object, its gold heater bands and gold emergency
> stop button glowing warm against cool blue ambient light from unseen windows.
> A finished navy spool of filament sits on the bench beside a scattering of clear
> bottle ribbons and a digital caliper. Nobody is present.
> 35 mm lens at f/2.8, cinematic, atmospheric, faint haze.
>
> [PHOTOREAL STYLE BLOCK] [UNIVERSAL NEGATIVES]

---

## 4. PRODUCT PROMPTS (5)

### Q1 — "The Handle", the social keychain, hero macro
> Macro product photograph of a small 3D-printed keychain tag lying on matte black
> slate. The tag is a rounded-corner rectangle roughly 55 by 32 by 4 mm, printed in
> deep navy blue recycled plastic with crisp visible horizontal FDM layer lines across
> every face and a subtle satin finish.
> On its face, a circular recess 25 mm across holds a flush metallic-gold disc with a
> fine engraved concentric ring pattern radiating from the centre, reading as a contact
> point rather than a symbol. A small hole at one end carries a brushed steel split
> ring and a short navy woven lanyard loop.
> A modern smartphone rests at the top edge of the frame, tilted, its screen a soft
> cool glow just out of focus.
> 100 mm macro at f/2.8 focused on the gold disc, gold rim light along the tag edge,
> deep shadow beneath. No text or lettering anywhere on the tag.
>
> [PHOTOREAL STYLE BLOCK] [UNIVERSAL NEGATIVES]

### Q2 — "The Handle" in use, tap moment
> Close photograph of a hand holding a smartphone a few centimetres above a small navy
> 3D-printed keychain tag with a gold circular contact disc, captured at the instant of
> a contactless tap. Faint concentric rings of warm gold light ripple outward from the
> gold disc toward the phone, suggesting a wireless read.
> The phone screen is bright but its content is abstract and out of focus. The keychain
> rests on a dark oak café table beside a set of keys and a navy filament offcut.
> Shot from a low three-quarter angle, 50 mm at f/2.0, warm practical light from the
> right, cool ambient from behind. Skin tones natural, hand in soft focus.
>
> [PHOTOREAL STYLE BLOCK] [UNIVERSAL NEGATIVES]

### Q3 — Product family
> Product photograph of five 3D-printed objects made from recycled plastic, arranged in
> a shallow arc on matte charcoal.
> From left: a hexagonal faceted desk organiser 150 mm tall holding pens, with a thin
> metallic-gold ring band around its collar; a ribbed cylindrical tumbler 170 mm tall
> with vertical flutes and a gold lip ring; a small flat navy keychain tag with a gold
> circular contact disc; a solid rectangular block 130 by 52 by 90 mm with a recessed
> gold circular target on its top face; and a square open shelf module 160 mm across
> with a small gold connector node at one corner.
> All are printed in deep navy blue with clearly visible fine horizontal layer lines,
> matte satin finish, softly rounded edges. The gold elements are the only warm colour.
> Wide 50 mm lens at f/5.6 so all five stay sharp, single soft key from upper right,
> gold rim tracing every top edge.
>
> [PHOTOREAL STYLE BLOCK] [UNIVERSAL NEGATIVES]

### Q4 — The Comeback Block, focus mode
> Photograph of a smartphone lying face-down on top of a solid navy 3D-printed block
> roughly the size of a hardback book, 130 by 52 by 90 mm, with crisp visible print
> layer lines and a recessed gold circular contact target visible at the block's edge.
> The block sits on a wooden dorm desk beside a closed laptop, an open notebook and a
> pen. The room is dark; the only light is a warm desk lamp from the upper left and a
> faint cool glow escaping from beneath the phone.
> The composition reads as deliberate — a phone put away on purpose.
> 35 mm at f/2.0, shallow focus on the block edge, cinematic and calm.
>
> [PHOTOREAL STYLE BLOCK] [UNIVERSAL NEGATIVES]

### Q5 — Recycled filament spool
> Macro photograph of a 3D-printed navy spool wound with roughly 800 grams of deep-navy
> recycled PET filament, 1.75 mm diameter, the coils neatly parallel and catching a
> long gold specular highlight across the wind.
> The spool rests on matte charcoal. In the soft background, out of focus, lie a few
> long clear spiral ribbons cut from plastic bottles and a digital caliper open at
> 1.75. A faint dusting of plastic particles on the surface.
> 100 mm macro at f/3.2, focus on the filament coils, cool key with warm gold rim.
>
> [PHOTOREAL STYLE BLOCK] [UNIVERSAL NEGATIVES]

---

## 4B. ISOLATED PRODUCT RENDERS — transparent background (6)

These are the images actually used on the product cards. Each is generated on a pure
white seamless background and then passed through Higgsfield's `remove_background`
tool, which returns a real PNG with an alpha channel — so the object sits on the dark
site with no visible box.

### 4B.0 Shared cutout tail — append to every prompt in this group
> The object is centred, complete and fully visible with generous empty margin on all
> sides, floating with no cast shadow, on a pure flat solid white seamless background
> with absolutely no gradient, no props, no surface and no horizon line. Soft even
> three-point studio lighting with a gentle warm gold rim light along the top edges.
> Photorealistic product render, sharp focus throughout, crisp clean silhouette edges
> suitable for cutout, commercial catalogue quality. No text, no lettering, no numbers,
> no logos.

**Why white and not black:** the cutout matte is cleaner against white for a navy
object, and alpha removes the background entirely afterwards, so the plate colour
never reaches the page.

**Notre Dame theming without trademark risk:** the motifs are described generically —
a *classical domed university building silhouette with a slender spire*, *collegiate
gothic arches*, a *four-leaf clover* — moulded as low relief in the same navy plastic.
This reads unmistakably as Notre Dame without reproducing any protected mark.

### R1 — The Dome Organizer
> Studio product render of a hexagonal desk organizer, 150 mm tall, 3D printed in deep
> navy blue recycled PET plastic with crisp visible fine horizontal FDM layer lines
> across all six flat facets and a matte satin finish. A polished metallic gold band
> encircles the collar near the top rim. On the front facet there is a subtle low
> raised relief of a classical domed university building silhouette topped by a slender
> spire, moulded in the same navy plastic and catching a soft highlight. The organizer
> holds three pens and a small pair of scissors. [SHARED CUTOUT TAIL]

### R2 — Ribbed Tumbler
> Studio product render of a ribbed cylindrical drinking tumbler, 170 mm tall, 3D
> printed in deep navy blue recycled PET plastic with crisp visible fine horizontal FDM
> layer lines and vertical fluted ribs running the full height, matte satin finish. A
> polished metallic gold ring forms the lip at the top. Near the base, a narrow band of
> subtle raised collegiate gothic arch motifs is moulded into the navy plastic.
> [SHARED CUTOUT TAIL]

### R3 — The Handle (the Instagram keychain)
> Studio product render of a small flat keychain tag, a rounded-corner rectangle
> roughly 55 by 32 by 4 mm, 3D printed in deep navy blue recycled plastic with crisp
> visible fine horizontal FDM layer lines and a matte satin finish. Set flush into its
> face is a circular metallic gold contact disc 25 mm across with a fine engraved
> concentric ring pattern radiating from the centre. A brushed stainless steel split
> ring passes through a hole at one end. A subtle raised relief of a small four-leaf
> clover is moulded into the navy plastic in one corner. [SHARED CUTOUT TAIL]

### R4 — The Comeback Block
> Studio product render of a solid rectangular block 130 by 52 by 90 mm, 3D printed in
> deep navy blue recycled PET plastic with crisp visible fine horizontal FDM layer lines
> on every face and a matte satin finish, edges softly chamfered. Recessed into the
> centre of the top face is a circular metallic gold contact target 54 mm across with a
> fine engraved concentric ring pattern. Along one long side, a shallow raised relief
> band of collegiate gothic arches is moulded into the navy plastic. [SHARED CUTOUT TAIL]

### R5 — Stack Shelf Module
> Studio product render of a square open shelf module, 160 mm across, 3D printed in deep
> navy blue recycled plastic with crisp visible fine horizontal FDM layer lines and a
> matte satin finish. It is a hollow square frame with thick flat rails, softly
> chamfered edges, and a small polished metallic gold cylindrical connector node seated
> at one top corner where modules interlock. A subtle raised relief of collegiate gothic
> arches runs along the inner face of the top rail. Shown at a slight three-quarter
> angle so the depth of the frame reads clearly. [SHARED CUTOUT TAIL]

### R6 — Comeback Filament
> Studio product render of a 3D printed filament spool wound with deep navy blue
> recycled PET filament at 1.75 mm diameter. The spool has two flat circular navy
> flanges with visible fine FDM layer lines and a polished metallic gold hub ring at the
> centre bore. Between the flanges the filament is wound in neat parallel coils, glossy,
> catching a long soft specular highlight across the wind. A short loose end of filament
> curls out from the top. Shown at a slight three-quarter angle. [SHARED CUTOUT TAIL]

### Post-processing
```
1. generate_image   nano_banana_pro · 1:1 · 2k · white plate
2. remove_background  media_type: image, media_id: <the generation job_id>
3. the returned PNG carries real alpha — drop it straight onto the dark page
```

---

## 5. Generation settings used

```
Model        nano_banana_pro   (best text and diagram fidelity)
Resolution   2k
Aspect       16:9  for machine and blueprints
             4:3   for product macros
             1:1   for knolling
Cost         2 credits per image
```

## 6. Consistency rules when regenerating

1. Never change the left-to-right subsystem order from Section 0.4.
2. Navy `#0C2340` is the only body colour; gold `#C99700` only ever appears on heater
   bands, the E-stop bezel, hazard stripes, NFC contact discs and dimension lines.
3. The barrel always has exactly **two** heater bands.
4. The shredder always has exactly **twelve** blades.
5. Filament is always **1.75 mm** and always navy.
6. No real company logos. No human faces. No invented lettering on products.
7. Prices, when shown, must match Section 0.3 and total `$968`.
