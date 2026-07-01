#!/usr/bin/env python3
"""
Erzeugt Präsentationsunterlagen für das Siemens-Mobility-Interview:
  1. input/marktdaten_weichenantriebe.xlsx  – Rohdaten (Backup/Dokumentation)
  2. output/Vortrag_Weichenantriebe.pptx    – 2-Folien-Präsentation mit eingebetteten Charts

Charts werden vollautomatisch per matplotlib generiert (kein Power BI erforderlich).

Aufruf: python3 scripts/build_presentation.py
"""

import io
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

ROOT  = Path(__file__).resolve().parent.parent
INPUT = ROOT / "input"
OUT   = ROOT / "output"
INPUT.mkdir(exist_ok=True)
OUT.mkdir(exist_ok=True)

# ---------------------------------------------------------------------------
# SIEMENS-FARBEN
# ---------------------------------------------------------------------------
PETROL    = RGBColor(0x00, 0x99, 0x99)   # #009999
DARKBLUE  = RGBColor(0x00, 0x30, 0x5E)   # #00305E
LIGHTGREY = RGBColor(0xF2, 0xF2, 0xF2)
MIDGREY   = RGBColor(0xA8, 0xA8, 0xA8)
WHITE     = RGBColor(0xFF, 0xFF, 0xFF)
BLACK     = RGBColor(0x1A, 0x1A, 0x1A)

C_PETROL   = "#009999"
C_DARKBLUE = "#00305E"
C_GREY     = "#A8A8A8"
C_LGREY    = "#F2F2F2"

# Hex für openpyxl (ohne #)
XL_PETROL  = "009999"
XL_DARKBLUE= "00305E"
XL_LGREY   = "F2F2F2"
XL_WHITE   = "FFFFFF"

# ---------------------------------------------------------------------------
# MARKTDATEN
# ---------------------------------------------------------------------------
TRENDS = [
    # (Name, Reifegrad 1-5, Relevanz 1-5, Marktpotenzial Mrd EUR)
    ("Condition Monitoring\n& Predictive Maintenance", 4, 5, 3.2),
    ("Digitale Stellwerks-\nintegration (EULYNX)",     3, 5, 2.8),
    ("Elektrifizierung &\nEnergieeffizienz",           4, 4, 1.9),
    ("Cybersecurity\n(NIS2 / IEC 62443)",              3, 4, 1.5),
    ("Remote Diagnostics\n& Cloud (Railigent X)",      4, 5, 2.4),
]

WETTBEWERBER_UMSATZ = {
    # Unternehmen: [Europa, Asien, Americas]  – Mrd. EUR, Schätzung 2024
    "Siemens Mobility":    [2.1, 0.9, 0.7],
    "Alstom":              [1.8, 0.7, 0.5],
    "Hitachi Rail":        [1.2, 1.0, 0.2],
    "Vossloh/Voestalpine": [0.6, 0.1, 0.1],
    "CRRC / CASCO":        [0.3, 1.5, 0.2],
}

MARKTANTEILE = [
    ("Siemens Mobility",    32),
    ("Alstom",              27),
    ("Hitachi Rail",        18),
    ("Vossloh/Voestalpine", 11),
    ("Hanning & Kahl",       6),
    ("Sonstige / CRRC",      6),
]


# ===========================================================================
# CHART 1 – Bubble Chart: Technologische Trends
# ===========================================================================
def make_bubble_chart() -> bytes:
    fig, ax = plt.subplots(figsize=(6.0, 4.2), dpi=150)
    fig.patch.set_facecolor("white")
    ax.set_facecolor(C_LGREY)

    for (name, x, y, size) in TRENDS:
        bubble_size = size * 800
        ax.scatter(x, y, s=bubble_size, color=C_PETROL, alpha=0.82,
                   edgecolors=C_DARKBLUE, linewidths=1.2, zorder=3)
        ax.annotate(name, (x, y),
                    textcoords="offset points", xytext=(0, -28),
                    ha="center", va="top", fontsize=7.5,
                    color=C_DARKBLUE, fontweight="bold",
                    multialignment="center")

    ax.set_xlim(1.5, 5.5)
    ax.set_ylim(2.8, 5.8)
    ax.set_xlabel("Technologischer Reifegrad  (1 = früh · 5 = etabliert)",
                  fontsize=8.5, color=C_DARKBLUE, labelpad=6)
    ax.set_ylabel("Strategische Relevanz für Siemens  (1–5)",
                  fontsize=8.5, color=C_DARKBLUE, labelpad=6)
    ax.set_title("Technologie-Radar – Weichenantriebe 2025",
                 fontsize=10, color=C_DARKBLUE, fontweight="bold", pad=8)

    ax.grid(True, color="white", linewidth=0.8, zorder=0)
    ax.tick_params(colors=C_DARKBLUE, labelsize=8)
    for spine in ax.spines.values():
        spine.set_edgecolor(C_GREY)

    legend_sizes = [1.0, 2.0, 3.2]
    legend_labels = ["1,0 Mrd. €", "2,0 Mrd. €", "3,2 Mrd. €"]
    handles = [
        mpatches.Circle((0, 0), radius=np.sqrt(s * 800) / 60,
                         color=C_PETROL, alpha=0.82,
                         label=l)
        for s, l in zip(legend_sizes, legend_labels)
    ]
    ax.legend(handles=handles, title="Marktpotenzial",
              title_fontsize=7, fontsize=7,
              loc="lower right", framealpha=0.85,
              edgecolor=C_GREY)

    plt.tight_layout(pad=0.6)
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight", dpi=150)
    plt.close(fig)
    buf.seek(0)
    return buf.read()


# ===========================================================================
# CHART 2 – Gruppiertes Balkendiagramm: Wettbewerber nach Region
# ===========================================================================
def make_bar_chart() -> bytes:
    regions   = ["Europa", "Asien", "Americas"]
    companies = list(WETTBEWERBER_UMSATZ.keys())
    n_comp    = len(companies)
    n_reg     = len(regions)

    # Siemens Petrol, Rest: abgestufte Grautöne
    palette = [C_PETROL, C_DARKBLUE, "#5B8DB8", C_GREY, "#CCCCCC"]

    x     = np.arange(n_reg)
    width = 0.14
    offsets = np.linspace(-(n_comp - 1) / 2, (n_comp - 1) / 2, n_comp) * width

    fig, ax = plt.subplots(figsize=(6.0, 4.2), dpi=150)
    fig.patch.set_facecolor("white")
    ax.set_facecolor(C_LGREY)

    for i, (company, values) in enumerate(WETTBEWERBER_UMSATZ.items()):
        bars = ax.bar(x + offsets[i], values, width=width * 0.9,
                      color=palette[i], label=company,
                      edgecolor="white", linewidth=0.5, zorder=3)
        # Werte über den Balken – nur Siemens
        if i == 0:
            for bar, val in zip(bars, values):
                ax.text(bar.get_x() + bar.get_width() / 2,
                        bar.get_height() + 0.04,
                        f"{val:.1f}", ha="center", va="bottom",
                        fontsize=7, color=C_DARKBLUE, fontweight="bold")

    ax.set_xticks(x)
    ax.set_xticklabels(regions, fontsize=9, color=C_DARKBLUE)
    ax.set_ylabel("Umsatz Signaling-Segment (Mrd. EUR, Schätzung 2024)",
                  fontsize=8, color=C_DARKBLUE, labelpad=6)
    ax.set_title("Wettbewerbsvergleich: Signaling-Umsatz nach Region",
                 fontsize=10, color=C_DARKBLUE, fontweight="bold", pad=8)
    ax.set_ylim(0, 2.7)

    ax.grid(True, axis="y", color="white", linewidth=0.8, zorder=0)
    ax.tick_params(colors=C_DARKBLUE, labelsize=8)
    for spine in ax.spines.values():
        spine.set_edgecolor(C_GREY)

    ax.legend(fontsize=7.5, loc="upper right",
              framealpha=0.9, edgecolor=C_GREY, ncol=1)

    plt.tight_layout(pad=0.6)
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight", dpi=150)
    plt.close(fig)
    buf.seek(0)
    return buf.read()


# ===========================================================================
# EXCEL – Rohdaten
# ===========================================================================
def _xl_header(ws, cols):
    for col, name in enumerate(cols, 1):
        c = ws.cell(1, col, name)
        c.font = Font(bold=True, color=XL_WHITE, name="Calibri")
        c.fill = PatternFill("solid", fgColor=XL_PETROL)
        c.alignment = Alignment(horizontal="center", wrap_text=True)
    ws.row_dimensions[1].height = 28

def _xl_border(ws, max_row, max_col):
    thin = Side(style="thin", color="CCCCCC")
    for row in ws.iter_rows(min_row=1, max_row=max_row, max_col=max_col):
        for cell in row:
            cell.border = Border(left=thin, right=thin, top=thin, bottom=thin)
            if cell.row > 1:
                cell.alignment = Alignment(horizontal="center")

def build_excel():
    wb = openpyxl.Workbook()

    ws1 = wb.active
    ws1.title = "Technologische Trends"
    _xl_header(ws1, ["Trend", "Reifegrad (1–5)", "Relevanz Siemens (1–5)",
                      "Marktpotenzial (Mrd. EUR)"])
    ws1.column_dimensions["A"].width = 36
    for col in ["B", "C", "D"]:
        ws1.column_dimensions[col].width = 22
    for i, (name, r, rel, pot) in enumerate(TRENDS, 2):
        ws1.cell(i, 1, name.replace("\n", " ")).alignment = Alignment(wrap_text=True)
        ws1.cell(i, 2, r); ws1.cell(i, 3, rel); ws1.cell(i, 4, pot)
        if i % 2 == 0:
            for col in range(1, 5):
                ws1.cell(i, col).fill = PatternFill("solid", fgColor=XL_LGREY)
    _xl_border(ws1, len(TRENDS) + 1, 4)

    ws2 = wb.create_sheet("Wettbewerb – Umsatz nach Region")
    _xl_header(ws2, ["Unternehmen", "Region", "Umsatz Signaling (Mrd. EUR)"])
    ws2.column_dimensions["A"].width = 26
    ws2.column_dimensions["B"].width = 14
    ws2.column_dimensions["C"].width = 28
    row = 2
    for firma, values in WETTBEWERBER_UMSATZ.items():
        for region, val in zip(["Europa", "Asien", "Americas"], values):
            ws2.cell(row, 1, firma); ws2.cell(row, 2, region); ws2.cell(row, 3, val)
            if row % 2 == 0:
                for col in range(1, 4):
                    ws2.cell(row, col).fill = PatternFill("solid", fgColor=XL_LGREY)
            row += 1
    _xl_border(ws2, row - 1, 3)

    ws3 = wb.create_sheet("Marktanteile Europa")
    _xl_header(ws3, ["Unternehmen", "Marktanteil % (Schätzung Europa)"])
    ws3.column_dimensions["A"].width = 28
    ws3.column_dimensions["B"].width = 30
    for i, (firma, anteil) in enumerate(MARKTANTEILE, 2):
        ws3.cell(i, 1, firma); ws3.cell(i, 2, anteil)
        if i % 2 == 0:
            for col in range(1, 3):
                ws3.cell(i, col).fill = PatternFill("solid", fgColor=XL_LGREY)
    _xl_border(ws3, len(MARKTANTEILE) + 1, 2)

    path = INPUT / "marktdaten_weichenantriebe.xlsx"
    wb.save(path)
    return path


# ===========================================================================
# POWERPOINT-HELFER
# ===========================================================================
SLIDE_W = Inches(13.33)
SLIDE_H = Inches(7.5)
MARGIN  = Inches(0.45)
HEADER_H = Inches(1.35)
FOOTER_H = Inches(0.40)
CONTENT_TOP = HEADER_H + Inches(0.08)
CONTENT_H   = SLIDE_H - HEADER_H - FOOTER_H - Inches(0.1)


def _rect(slide, left, top, width, height, fill, line=None):
    from pptx.util import Emu
    sh = slide.shapes.add_shape(1, left, top, width, height)
    sh.fill.solid()
    sh.fill.fore_color.rgb = fill
    if line:
        sh.line.color.rgb = line
    else:
        sh.line.fill.background()
    return sh


def _text(slide, text, left, top, width, height,
          size=14, bold=False, italic=False,
          color=None, align=PP_ALIGN.LEFT, wrap=True):
    if color is None:
        color = BLACK
    tb = slide.shapes.add_textbox(left, top, width, height)
    tf = tb.text_frame
    tf.word_wrap = wrap
    p = tf.paragraphs[0]
    p.alignment = align
    r = p.add_run()
    r.text = text
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.italic = italic
    r.font.color.rgb = color
    r.font.name = "Calibri"
    return tb


def _multiline_bullets(slide, items, left, top, width, height,
                        title_size=13, body_size=10.5):
    tb = slide.shapes.add_textbox(left, top, width, height)
    tf = tb.text_frame
    tf.word_wrap = True
    first = True
    for (title, sub) in items:
        if first:
            p = tf.paragraphs[0]
            first = False
        else:
            p = tf.add_paragraph()
        p.space_before = Pt(5)
        r = p.add_run()
        r.text = f"▸  {title}"
        r.font.size = Pt(title_size)
        r.font.bold = True
        r.font.color.rgb = DARKBLUE
        r.font.name = "Calibri"

        p2 = tf.add_paragraph()
        p2.space_before = Pt(0)
        r2 = p2.add_run()
        r2.text = f"    {sub}"
        r2.font.size = Pt(body_size)
        r2.font.color.rgb = BLACK
        r2.font.name = "Calibri"
    return tb


def _header(slide, title, subtitle=""):
    _rect(slide, 0, 0, SLIDE_W, HEADER_H, PETROL)
    _text(slide, title,
          MARGIN, Inches(0.10), SLIDE_W - MARGIN * 2, Inches(0.65),
          size=22, bold=True, color=WHITE)
    if subtitle:
        _text(slide, subtitle,
              MARGIN, Inches(0.70), SLIDE_W - MARGIN * 2, Inches(0.58),
              size=13, italic=False, color=WHITE)


def _footer(slide, source):
    _rect(slide, 0, SLIDE_H - FOOTER_H, SLIDE_W, FOOTER_H, DARKBLUE)
    _text(slide, source,
          MARGIN, SLIDE_H - FOOTER_H + Inches(0.04),
          SLIDE_W - MARGIN * 2, FOOTER_H - Inches(0.06),
          size=8, color=WHITE)


def _implication(slide, text):
    impl_top = CONTENT_TOP + CONTENT_H - Inches(0.42)
    _rect(slide, MARGIN, impl_top,
          SLIDE_W - MARGIN * 2, Inches(0.38), DARKBLUE)
    _text(slide, text,
          MARGIN + Inches(0.12), impl_top + Inches(0.04),
          SLIDE_W - MARGIN * 2 - Inches(0.24), Inches(0.32),
          size=9.5, bold=True, color=WHITE)


def _embed_png(slide, png_bytes, left, top, width, height):
    buf = io.BytesIO(png_bytes)
    slide.shapes.add_picture(buf, left, top, width, height)


# ===========================================================================
# POWERPOINT AUFBAUEN
# ===========================================================================
CHART_W  = Inches(6.1)
CHART_H  = Inches(4.55)
DIVIDER  = MARGIN + CHART_W + Inches(0.12)
RIGHT_L  = DIVIDER + Inches(0.12)
RIGHT_W  = SLIDE_W - RIGHT_L - MARGIN

SOURCE_1 = (
    "Quellen: Siemens Mobility GB 2024 | Europe's Rail JU Roadmap 2025 | "
    "BMDV Deutschlandtakt | Eigene Schätzung"
)
SOURCE_2 = (
    "Quellen: Siemens Mobility GB 2024 | Alstom AR 2024 | Hitachi Rail AR 2024 | "
    "Mordor Intelligence Rail Signaling Market 2024 | Eigene Schätzung"
)

IMPL_1 = (
    "Implikation für Siemens:  Differenzierung nicht über Hardware-Preis, "
    "sondern über digitale Plattform (Railigent X) und EULYNX-Systemkompetenz."
)
IMPL_2 = (
    "Implikation für Siemens:  Premium-Positionierung + Software/Service-Anteil erhöhen – "
    "Wachstumshebel in Europa durch Deutschlandtakt & TEN-T-Investitionen nutzen."
)

TRENDS_BULLETS = [
    ("Condition Monitoring & Predictive Maintenance",
     "IoT-Sensoren + KI-Analyse → Wartungskosten –20–30 %"),
    ("Digitale Stellwerksintegration (EULYNX)",
     "EU-Norm ersetzt analoge Relaistechnik → offene Schnittstellen Pflicht"),
    ("Elektrifizierung & Energieeffizienz",
     "Ablösung hydraulischer Antriebe; Rückspeisung beim Schaltvorgang"),
    ("Cybersecurity  (NIS2 / IEC 62443)",
     "Security-by-Design in Firmware und Feldbusse verpflichtend"),
    ("Remote Diagnostics & Cloud  (Railigent X)",
     "Fernüberwachung → Vor-Ort-Einsätze signifikant reduziert"),
]

WETTBEWERB_BULLETS = [
    ("Siemens Mobility",
     "EULYNX-Leader, Railigent X, globales Servicenetz"),
    ("Alstom  (+Bombardier)",
     "Breites Signaling-Portfolio, CBTC-Stärke in Metropolen"),
    ("Hitachi Rail  (ehem. Ansaldo STS)",
     "Systemintegration, solide Europa & Asien Präsenz"),
    ("Vossloh / Hanning & Kahl",
     "Nischenspezialisten – hohe Qualität, begrenztes Portfolio"),
    ("CRRC / CASCO",
     "Preiswettbewerb, aggressiver Export nach Osteuropa & Afrika"),
]


def build_pptx(chart1_png: bytes, chart2_png: bytes) -> Path:
    prs = Presentation()
    prs.slide_width  = SLIDE_W
    prs.slide_height = SLIDE_H
    blank = prs.slide_layouts[6]

    # ---- FOLIE 1 ----
    s1 = prs.slides.add_slide(blank)
    _rect(s1, 0, 0, SLIDE_W, SLIDE_H, WHITE)
    _header(s1,
            "Technologische Trends – Weichenantriebe",
            "Digitalisierung und Predictive Maintenance definieren die nächste Generation")

    # Chart links einbetten
    _embed_png(s1, chart1_png,
               MARGIN, CONTENT_TOP, CHART_W, CHART_H)

    # Trennlinie
    _rect(s1, DIVIDER, CONTENT_TOP, Inches(0.03),
          CONTENT_H - Inches(0.45), MIDGREY)

    # Bullets rechts
    _text(s1, "Fünf Schlüsseltrends",
          RIGHT_L, CONTENT_TOP, RIGHT_W, Inches(0.36),
          size=13, bold=True, color=DARKBLUE)

    _multiline_bullets(s1, TRENDS_BULLETS,
                       RIGHT_L, CONTENT_TOP + Inches(0.40),
                       RIGHT_W, CHART_H - Inches(0.45))

    _implication(s1, IMPL_1)
    _footer(s1, SOURCE_1)

    # ---- FOLIE 2 ----
    s2 = prs.slides.add_slide(blank)
    _rect(s2, 0, 0, SLIDE_W, SLIDE_H, WHITE)
    _header(s2,
            "Wettbewerbssituation – Weichenantriebe",
            "Konsolidierter Markt, 3–4 globale Platzhirsche – Differenzierung über Digitalisierung")

    _embed_png(s2, chart2_png,
               MARGIN, CONTENT_TOP, CHART_W, CHART_H)

    _rect(s2, DIVIDER, CONTENT_TOP, Inches(0.03),
          CONTENT_H - Inches(0.45), MIDGREY)

    _text(s2, "Key Competitors",
          RIGHT_L, CONTENT_TOP, RIGHT_W, Inches(0.36),
          size=13, bold=True, color=DARKBLUE)

    _multiline_bullets(s2, WETTBEWERB_BULLETS,
                       RIGHT_L, CONTENT_TOP + Inches(0.40),
                       RIGHT_W, CHART_H - Inches(0.45))

    _implication(s2, IMPL_2)
    _footer(s2, SOURCE_2)

    path = OUT / "Vortrag_Weichenantriebe.pptx"
    prs.save(path)
    return path


# ===========================================================================
if __name__ == "__main__":
    print("Erzeuge Charts …")
    png1 = make_bubble_chart()
    png2 = make_bar_chart()
    print(f"  Bubble Chart: {len(png1):,} Bytes")
    print(f"  Bar Chart:    {len(png2):,} Bytes")

    print("Erzeuge Excel-Rohdaten …")
    xl = build_excel()
    print(f"  {xl}")

    print("Erzeuge PowerPoint …")
    pptx_path = build_pptx(png1, png2)
    print(f"  {pptx_path}")

    print("\nFertig! Dateien:")
    print(f"  {xl}")
    print(f"  {pptx_path}")
    print("\nNächste Schritte:")
    print("  1. PPTX herunterladen und in PowerPoint öffnen")
    print("  2. Schrift prüfen: Calibri ist voreingestellt")
    print("     (Optional: Siemens Sans von fonts.siemens.com ersetzen)")
    print("  3. Vortrag laut üben – Ziel: unter 7 Minuten")
