# Irish Comeback — Build Tutorial
### Unit 01 · Rev 1.0 · Bottle-to-filament line
University of Notre Dame · budget ceiling US$ 1,000

---

## 0. Read this first

This machine melts plastic and spins hardened steel. Two things will hurt you: the
**245 °C barrel** and the **shredder drum**. Neither is forgiving.

- Never open the shredder hopper while the motor has power. The E-stop cuts the
  primary side — wire it that way, not on the control side.
- Never process plastic you cannot identify. Unknown plastic may be PVC, which
  releases hydrogen chloride gas above ~180 °C. That gas corrodes the barrel and
  injures lungs.
- Run the barrel under extraction or beside an open window. Always.
- Keep a Class ABC extinguisher within arm's reach of the barrel.

If you are a student building this on campus, get your safety sign-off **before**
the motor turns under load, not after.

---

## 1. What the machine is

Two independent lines that share a bench, a dryer and a control box.

| Line | Input | Method | Output |
|---|---|---|---|
| **A** | PET #1 bottle bodies | Pultrusion — the bottle is cut into one continuous ribbon and *pulled* through a heated die | 1.75 mm filament |
| **B** | PP #5 caps, HDPE #2 | Shredding, then heat pressing | Flake, then pressed solids |

**Why two lines instead of one machine?** A commercial screw extruder (Filabot EX2)
lists at US$ 2,945 — roughly three times the entire budget. Pultrusion needs no
screw, no auger and no melt reservoir, which is exactly why it fits. Caps cannot go
through pultrusion (they are not a continuous sheet) and cannot be blended into PET
(they contaminate it), so they get their own, much cheaper, path.

---

## 2. Bill of materials

See `docs/BOM.csv`. Totals:

```
Line A — pultrusion      $342
Line B — shredder        $528
Shared                   $ 98
                        ------
Subtotal                 $968
Contingency              $ 32
Ceiling                $1,000
```

Order Line A first. If pultrusion does not work for you, you have spent $342
finding out — not $968.

---

## 3. Build sequence

### Step 1 — Frame and bench (≈4 h)

1. Laser-cut the 6 mm steel frame panels at the Innovation Lab from
   `drawings/frame-panels.svg`. Deburr every edge.
2. Bolt the frame square. Check diagonals — if they differ by more than 2 mm, the
   shredder shaft will bind later.
3. Mount the bench top. Leave the rear open for wiring access.

### Step 2 — Line B: shredder drum (≈6 h)

1. Slide blades and spacers alternately onto the 20 mm hex shaft. The stack must be
   **tight** — any axial play becomes a jam.
2. Fit the pillow-block bearings; the shaft must spin freely by hand with no rock.
3. Bolt the worm reducer to the shaft, then couple the 1.5 HP motor.
4. Fit the hopper. Confirm no hand can reach the blades through the throat.
   If it can, the throat is too wide — add a baffle.
5. **Wire the E-stop in series on the motor primary.** Test it with the drum empty,
   three times, before you ever load plastic.

> **Checkpoint:** with the hopper empty, the drum should spin at roughly 70 rpm and
> stop dead when the E-stop is struck.

### Step 3 — Shared: dryer (≈30 min)

Set the food dehydrator to 65 °C and verify with an independent thermometer. Cheap
dehydrators lie by up to 15 °C. If it overshoots past 70 °C the PET will soften and
fuse into a block.

### Step 4 — Line A: pultrusion head (≈8 h)

1. Assemble the ReCreator MK6 kit per its own documentation.
2. Mount the two heater bands on the barrel and seat the thermistor **between**
   them, not at one end.
3. Fit the 1.75 mm die at the barrel exit.
4. Wire board, PSU and hotend. Set the thermal runaway protection — do not skip it.
5. Mount the spooler so the filament path from die to spool is straight and short.

### Step 5 — Control box (≈3 h)

Board, display and E-stop into one enclosure. Label every switch. Anyone should be
able to shut the machine down without asking which button.

---

## 4. First run — Line A

1. **Wash** a bottle. Remove label and glue residue. Any adhesive left behind will
   carbonise in the die and plug it.
2. **Remove the cap and the tamper ring.** Both are PP. They go to Line B. This is
   the single most important habit in the entire process.
3. **Dry** the bottle: 4 hours at 65 °C. Non-negotiable.
4. **Cut** the bottle into one continuous ribbon with the jig. Set the jig to the
   width your die expects — for a 1.75 mm output that is typically 7–9 mm; find your
   exact figure by test.
5. **Heat** the barrel to 245 °C. Wait for it to stabilise, not just to arrive.
6. **Thread** the ribbon and start the spooler at low speed.
7. **Tune:** measure the output with calipers.
   - Filament too **thick** → increase pull speed
   - Filament too **thin** → decrease pull speed
   - Filament **bubbling or spitting** → your PET is still wet. Stop. Dry it again.

Target: **1.75 ± 0.05 mm**, sampled at ten points along the spool.

---

## 5. First run — Line B

1. Collect caps and rings. Wash and air-dry — these do not need the dehydrator, they
   are not hygroscopic like PET.
2. Feed the shredder slowly. Overfeeding stalls the drum and can burn out the motor.
3. Collect flake, then heat-press into moulds at roughly 170–180 °C for PP.
4. Cool under pressure. Releasing pressure while hot causes warping.

---

## 6. Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Filament snaps in your fingers | Moisture — hydrolysis in the melt | Dry 4 h at 65 °C; store with desiccant |
| Filament bubbles leaving the die | Same, worse | Stop, dry, restart |
| Diameter drifts along the spool | Pull speed varying, or ribbon width varying | Re-check jig; tension-compensate spooler |
| Brittle even when dry | PP contamination from a cap | Discard batch; tighten intake separation |
| Die plugs | Label adhesive or dirt | Wash bottles properly; purge the die |
| Shredder stalls | Overfeeding, or blade stack has play | Feed slower; re-tighten the stack |
| Printed part warps off the bed | Wrong polymer for the geometry | HDPE warps — press it instead of printing it |

---

## 7. Printing with recycled filament

Notre Dame's **Stratasys F120 and F370** at the Innovation Lab are closed-material
systems: they read a chip on the cartridge and refuse anything else. They will not
print this filament — do not waste a slot trying.

Use an **open-material** machine. The Architecture Library Makerspace runs a
Prusa-family workflow through PrusaSlicer and will accept it. Submit files at least
two weeks before a deadline, and note that Architecture coursework has priority.

Starting profile for recycled PET:

```
Nozzle          240–250 °C
Bed              70–80 °C
First layer      0.25 mm
Layer height     0.20 mm
Speed            35–45 mm/s   (slower than virgin PETG)
Cooling          40–60 %
Retraction       tune per spool — recycled varies more than virgin
```

Expect roughly **10–20 % lower layer adhesion** than virgin PETG. Design around it:
thicker walls, generous fillets, no thin cantilevers.

---

## 8. NFC tagging

Every product has a printed recess sized for a 25 mm NTAG215 disc.

1. Pause the print two layers above the recess floor.
2. Drop the tag in, flat, chip side down.
3. Resume. The tag is sealed permanently inside the part.
4. Encode with any NFC writer app. 504 bytes of NDEF is plenty for a URL.

Three payloads in use:

- **Focus block** → a URL that triggers a focus/shortcut routine on the phone
- **Material passport** → a URL to that specific object's record
- **Shop tag** → a direct product link

Lock the tag read-only once written if it will leave your control.

---

## 9. Maintenance

| Interval | Task |
|---|---|
| Every run | Purge the die; wipe the barrel exit |
| Weekly | Check blade stack torque; inspect belts |
| Monthly | Re-verify dehydrator temperature against an independent probe |
| Monthly | Test the E-stop under load |
| Per spool | Ten-point diameter sample before release |

---

## 10. Drawings in this pack

- `drawings/assembly-elevation.svg` — dimensioned side elevation, scale 1:8
- `drawings/frame-panels.svg` — flat panels for laser cutting, 6 mm steel
- `drawings/process-flow.svg` — material flow, both lines
- `docs/BOM.csv` — full bill of materials with vendors

---

*Irish Comeback — a student circular-manufacturing initiative at the University of
Notre Dame. Not affiliated with or endorsed by the University. Build at your own
risk; follow your institution's shop safety rules.*
