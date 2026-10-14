import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import textwrap

W, H = 17.0, 25.4
fig, ax = plt.subplots(figsize=(W, H), dpi=170)
ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")

C = dict(origin="#E3EEF9", chem="#FDEFD0", prop="#E5F4E3", cls="#EDE4F6", mod="#FCE4E4", use="#DDF1F1", tech="#F6F0DA", qmap="#F0F0F0")
EDGE = "#3A3A3A"


def box(x, y, w, h, text, fc, fs=11, bold=False, ec=EDGE, lw=1.4, align="center", wrap=None):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.18", fc=fc, ec=ec, lw=lw)
    ax.add_patch(p)
    if wrap:
        text = "\n".join(textwrap.fill(t, wrap) if t else "" for t in text.split("\n"))
    ha = "center" if align == "center" else "left"
    tx = x + w / 2 if align == "center" else x + 0.18
    ax.text(tx, y + h / 2, text, ha=ha, va="center", fontsize=fs, fontweight="bold" if bold else "normal", color="#111", linespacing=1.25)


def band(y, h, label, color):
    ax.add_patch(FancyBboxPatch((0.25, y), 16.5, h, boxstyle="round,pad=0.0,rounding_size=0.12", fc=color, ec="#999", lw=0.8, alpha=0.55))
    ax.text(0.45, y + h - 0.28, label, fontsize=12.5, fontweight="bold", color="#222", va="center")


def arrow(x1, y1, x2, y2, label=None, fs=9.5, rad=0.0):
    a = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=18, lw=1.8, color="#222", connectionstyle=f"arc3,rad={rad}")
    ax.add_patch(a)
    if label:
        ax.text((x1 + x2) / 2 + 0.1, (y1 + y2) / 2, label, fontsize=fs, ha="left", va="center", color="#222", style="italic")


# ---------- title
ax.text(W / 2, H - 0.4, "GLASS IONOMER CEMENT (GIC) - MASTER FLOWCHART", ha="center", fontsize=21, fontweight="bold", color="#1F3864")
ax.text(W / 2, H - 0.9, "Chemistry  ->  Properties  ->  Classification  ->  Modifications  ->  Clinical use  ->  Technique & failure   (Q-numbers = questions answered in this document)",
        ha="center", fontsize=10.5, color="#444")

# ---------- 1 ORIGIN
y1 = 20.0
band(y1, 4.0, "1  ORIGIN AND EVOLUTION    [Q1  Q6  Q8]", C["origin"])
box(1.2, y1 + 2.55, 5.6, 0.95, "SILICATE CEMENT\nfluoride release, translucent; but high solubility", "#FFFFFF", 10.2)
box(10.2, y1 + 2.55, 5.6, 0.95, "ZINC POLYCARBOXYLATE\nfirst inherent adhesion to tooth; but weak, soluble", "#FFFFFF", 10.2)
box(3.2, y1 + 1.25, 10.6, 0.95, "GLASS POLYALKENOATE CEMENT (ISO name) = GIC / ASPA   |   Wilson & Kent, 1970s (sources differ: 1969 to 1972)\nglass from silicate cement + polymeric acid from polycarboxylate", "#FFFFFF", 10.2)
arrow(4.0, y1 + 2.55, 6.0, y1 + 2.22)
arrow(13.0, y1 + 2.55, 11.0, y1 + 2.22)
box(0.6, y1 + 0.2, 15.8, 0.75, "1980s resin added -> RESIN-MODIFIED GIC   |   1990s finer glass + higher P/L -> HIGH-VISCOSITY GIC (ART)   |   2007 nano-filled RMGIC   |   today ion-releasing / alkasite resins (not true GIC)", "#FFFFFF", 8.9)
arrow(8.5, y1 + 1.25, 8.5, y1 + 0.97)

# ---------- 2 CHEMISTRY
y2 = 15.5
band(y2, 4.3, "2  COMPOSITION AND SETTING    [Q10  Q5  Q11]", C["chem"])
box(0.6, y2 + 1.95, 5.2, 1.5, "POWDER\nion-leachable fluoro-alumino-silicate glass\n(SiO2, Al2O3, CaF2 ...; 4-50 um)\nfluoride acts as flux", "#FFFFFF", 10)
box(0.6, y2 + 0.3, 5.2, 1.4, "LIQUID\n40-55% aqueous polyacrylic /\nitaconic (or maleic) copolymer\n+ tartaric acid 5-15%", "#FFFFFF", 10)
box(6.6, y2 + 2.45, 3.0, 1.0, "STAGE 1\nDISSOLUTION\nacid attacks glass", "#FFFFFF", 10)
box(10.0, y2 + 2.45, 3.1, 1.0, "STAGE 2\nGELATION\nCa/Sr then Al cross-links", "#FFFFFF", 10)
box(13.5, y2 + 2.45, 3.0, 1.0, "STAGE 3\nMATURATION\nhydration, weeks", "#FFFFFF", 10)
arrow(5.8, y2 + 2.7, 6.55, y2 + 2.95)
arrow(5.8, y2 + 1.0, 6.55, y2 + 2.7, rad=-0.15)
arrow(9.6, y2 + 2.95, 9.95, y2 + 2.95)
arrow(13.1, y2 + 2.95, 13.45, y2 + 2.95)
box(6.6, y2 + 0.3, 9.9, 1.95, "SET CEMENT: unreacted glass cores in a siliceous gel, inside a polysalt matrix\n(cross-linked polyacrylate; calcium/strontium early and fragile, aluminium later and insoluble)\nWATER BALANCE: ~24% water; early water uptake and early dehydration both damage the cement\nINITIAL HARD SET about 4-10 min; full properties over days to about a month",
    "#FFFFFF", 10, align="left")
arrow(8.1, y2 + 2.45, 8.1, y2 + 2.28)

# ---------- 3 PROPERTIES
y3 = 11.5
band(y3, 3.75, "3  KEY PROPERTIES    [Q4  Q16  Q8]", C["prop"])
bw = 3.8
for i, (t, s) in enumerate([
    ("ADHESION", "ion exchange with enamel/dentine\n10% polyacrylic acid, 10 s\n(never acid-etch the tooth)\nfailure is cohesive in the cement"),
    ("FLUORIDE", "high release first weeks, then low\nsteady level for years\nreservoir: can be recharged\n(clinical benefit: debated)"),
    ("BIOCOMPATIBILITY", "fresh pH about 1 buffered by dentine\nmild, resolving pulp response\nplaque resistant; high gingival\ntolerance"),
    ("LIMITS", "brittle, low tensile strength\nnot for marginal ridge / incisal\ncorner / heavy load alone\nneeds moisture control"),
]):
    x = 0.6 + i * (bw + 0.2)
    box(x, y3 + 0.35, bw, 2.55, f"{t}\n\n{s}", "#FFFFFF", 10, bold=False)

# ---------- 4 CLASSIFICATION
y4 = 8.1
band(y4, 3.15, "4  CLASSIFICATION (Wilson & McLean 1988; Mount)    [Q5  Q7]", C["cls"])
cls = [("TYPE I\nLUTING", "crowns, bridges,\northodontic bands\nP/L about 1.5:1"),
       ("TYPE II.1\nAESTHETIC\nRESTORATIVE", "auto-cure or dual-cure\nanterior / Class V\nP/L 2.8-6.8:1"),
       ("TYPE II.2\nREINFORCED\nRESTORATIVE", "metal-modified (cermet,\nalloy admix) or high\nstrength; P/L 3-4:1"),
       ("TYPE III\nLINING / BASE", "lining P/L 1.5:1\nbase / dentine substitute\nP/L 3:1 or more")]
for i, (t, s) in enumerate(cls):
    x = 0.6 + i * (bw + 0.2)
    box(x, y4 + 0.3, bw, 2.15, f"{t}\n{s}", "#FFFFFF", 9.8)

# ---------- 5 MODIFICATIONS
y5 = 4.7
band(y5, 3.15, "5  MODIFICATIONS AND NEWER MATERIALS    [Q3  Q8  Q11  Q13  P-series]", C["mod"])
mods = [("RESIN-MODIFIED\n(light / dual / tri-cure)", "15-25% resin (HEMA)\nstill sets in the dark"),
        ("HIGH-VISCOSITY\n(ART, packable)", "finer glass, higher P/L\nsingle-surface cavities"),
        ("METAL-REINFORCED", "silver cermet, alloy admix\nabrasion resistance"),
        ("NANO-IONOMER", "nano-filled RMGIC (2007)\nbetter polish / optics"),
        ("NOT TRUE GIC", "compomer, giomer,\nalkasite (resin-based)")]
mw = 3.15
for i, (t, s) in enumerate(mods):
    x = 0.6 + i * (mw + 0.09)
    box(x, y5 + 0.3, mw, 2.15, f"{t}\n\n{s}", "#FFFFFF", 9.3)

# ---------- 6 CLINICAL USE + 7 TECHNIQUE
y6 = 1.45
band(y6, 3.0, "6  CLINICAL USE  ->  7  TECHNIQUE AND FAILURE    [Q2  Q7  Q9  Q12  Q14  Q15]", C["use"])
box(0.6, y6 + 0.3, 7.8, 1.95,
    "USES\nluting  |  Class III, V, root caries  |  primary teeth\nliner / base  |  SANDWICH (bi-layered) with composite\nsealant  |  ART / minimal intervention  |  limited core",
    "#FFFFFF", 9.8)
box(8.8, y6 + 0.3, 7.6, 1.95,
    "TECHNIQUE: isolate -> condition 10 s -> capsule mix -> place under matrix\n-> seal at once (unfilled resin / varnish) -> finish at 24 h or later\nFAILURE: early water or dehydration | low-powder mix | overload\n-> ditching, cracks, bulk fracture",
    "#FFFFFF", 9.8)

ax.text(W / 2, 0.62, "Q1 past, present, future | Q2 role in restorative dentistry | Q3 recent advances | Q4 adhesion | Q5 classification and composition | Q6 history 1971-2006\nQ7 uses and bi-layered | Q8 developments and biocompatibility | Q9 MID | Q10 setting reaction | Q11 light-cured, RMGIC, tri-cure | Q12 GIC restorations\nQ13 alkasite | Q14 sandwich | Q15 cavosurface | Q16 fluoride release | P-series = predicted questions", ha="center", va="center", fontsize=9, color="#333", linespacing=1.5)

# vertical flow arrows between bands
for yy in (y1, y2, y3, y4, y5):
    pass
for ya, yb in ((y1, y2 + 4.3), (y2, y3 + 3.75), (y3, y4 + 3.15), (y4, y5 + 3.15), (y5, y6 + 3.0)):
    arrow(W / 2, ya - 0.01, W / 2, yb + 0.01)

fig.savefig("/Users/niranjan/.claude/answer_tools/gic_flowchart.png", bbox_inches="tight", pad_inches=0.15)
print("ok")
