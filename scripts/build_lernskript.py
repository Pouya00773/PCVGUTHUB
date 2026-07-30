#!/usr/bin/env python3
"""
Erzeugt aus den Markdown-Quellen in lernskript/ die Word-Dokumente:

- output/Lernskript_Automation.docx    (Skript + Aufgabentypen)
- output/Spickzettel_Automation.docx   (nur die Formelsammlung, zweispaltig)

Der Markdown-Dialekt ist bewusst klein gehalten: Überschriften (#, ##, ###),
Absätze, Aufzählungen (-), nummerierte Listen (1.), Tabellen (|), Merksätze (>),
Codeblöcke (```) und Trennlinien (---). Inline wird **fett** ausgewertet, sowie
`Code` als nichtproportionale Schrift.

Aufruf:  python3 scripts/build_lernskript.py
"""
import re
from pathlib import Path

from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

from docx_common import (
    set_base_style,
    heading,
    subheading,
    add_page_numbers,
    callout,
    AKZENT,
)

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "lernskript"
OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)

MONO = "Consolas"


# ---------------------------------------------------------------------------
# MARKDOWN -> BLOCKLISTE
# ---------------------------------------------------------------------------
def parse(md):
    """Zerlegt Markdown in eine Liste von (typ, nutzlast)-Tupeln."""
    blocks = []
    lines = md.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        # Codeblock
        if stripped.startswith("```"):
            code = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code.append(lines[i])
                i += 1
            i += 1
            blocks.append(("code", "\n".join(code)))
            continue

        # Trennlinie
        if re.fullmatch(r"-{3,}", stripped):
            blocks.append(("rule", None))
            i += 1
            continue

        # Überschriften
        m = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if m:
            blocks.append((f"h{len(m.group(1))}", m.group(2).strip()))
            i += 1
            continue

        # Tabelle: mindestens Kopfzeile + Trennzeile
        if stripped.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(lines[i].strip())
                i += 1
            blocks.append(("table", _parse_table(rows)))
            continue

        # Merksatz / Zitat
        if stripped.startswith(">"):
            quote = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip().lstrip(">").strip())
                i += 1
            blocks.append(("quote", " ".join(q for q in quote if q)))
            continue

        # Aufzählung
        if re.match(r"^[-*]\s+", stripped):
            items, i = _collect_list(lines, i, r"^[-*]\s+")
            blocks.append(("ul", items))
            continue

        # nummerierte Liste
        if re.match(r"^\d+\.\s+", stripped):
            items, i = _collect_list(lines, i, r"^\d+\.\s+")
            blocks.append(("ol", items))
            continue

        # Absatz: bis Leerzeile oder Beginn eines anderen Blocks
        para = []
        while i < len(lines):
            s = lines[i].strip()
            if not s or s.startswith(("|", ">", "#", "```")) or re.fullmatch(r"-{3,}", s):
                break
            if re.match(r"^[-*]\s+", s) or re.match(r"^\d+\.\s+", s):
                break
            para.append(s)
            i += 1
        blocks.append(("p", " ".join(para)))
    return blocks


def _collect_list(lines, i, pattern):
    """Sammelt Listeneinträge inklusive eingerückter Fortsetzungszeilen."""
    items = []
    while i < len(lines):
        s = lines[i].strip()
        if re.match(pattern, s):
            items.append(re.sub(pattern, "", s))
            i += 1
        elif s and lines[i].startswith((" ", "\t")) and items:
            items[-1] += " " + s
            i += 1
        else:
            break
    return items, i


def _parse_table(rows):
    """Wandelt Markdown-Tabellenzeilen in eine Zellenmatrix; Trennzeile entfällt."""
    out = []
    for r in rows:
        cells = [c.strip() for c in r.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
            continue
        out.append(cells)
    if not out:
        return out
    width = max(len(r) for r in out)
    return [r + [""] * (width - len(r)) for r in out]


# ---------------------------------------------------------------------------
# INLINE-FORMATIERUNG
# ---------------------------------------------------------------------------
INLINE = re.compile(r"(\*\*.+?\*\*|`[^`]+`)")


def write_inline(paragraph, text, size=None):
    """Schreibt Text mit **fett** und `Code` in einen Absatz."""
    for part in INLINE.split(text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            run = paragraph.add_run(part[2:-2])
            run.bold = True
        elif part.startswith("`") and part.endswith("`"):
            run = paragraph.add_run(part[1:-1])
            run.font.name = MONO
        else:
            run = paragraph.add_run(part)
        if size:
            run.font.size = Pt(size)
    return paragraph


# ---------------------------------------------------------------------------
# BLOCKLISTE -> DOCX
# ---------------------------------------------------------------------------
def render(doc, blocks, base_size=11, skip_h1=True):
    for kind, payload in blocks:
        if kind == "h1":
            if skip_h1:
                continue
            heading(doc, payload)
        elif kind == "h2":
            doc.add_page_break()
            heading(doc, payload)
        elif kind == "h3":
            subheading(doc, payload, size=base_size)
        elif kind == "h4":
            subheading(doc, payload, size=base_size - 1)
        elif kind == "p":
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(4)
            write_inline(p, payload, size=base_size)
        elif kind == "quote":
            p = callout(doc, "")
            write_inline(p, payload, size=base_size)
        elif kind == "ul":
            for item in payload:
                p = doc.add_paragraph(style="List Bullet")
                p.paragraph_format.space_after = Pt(1)
                write_inline(p, item, size=base_size)
        elif kind == "ol":
            for item in payload:
                p = doc.add_paragraph(style="List Number")
                p.paragraph_format.space_after = Pt(1)
                write_inline(p, item, size=base_size)
        elif kind == "table":
            add_table(doc, payload, size=base_size - 1)
        elif kind == "code":
            add_code(doc, payload, size=base_size - 1)
        elif kind == "rule":
            pass


def add_table(doc, rows, size=10):
    if not rows:
        return
    table = doc.add_table(rows=len(rows), cols=len(rows[0]))
    table.style = "Table Grid"
    table.autofit = True
    for ri, row in enumerate(rows):
        for ci, cell_text in enumerate(row):
            cell = table.cell(ri, ci)
            cell.text = ""
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            write_inline(p, cell_text, size=size)
            if ri == 0:
                for run in p.runs:
                    run.bold = True
                shd = OxmlElement("w:shd")
                shd.set(qn("w:val"), "clear")
                shd.set(qn("w:fill"), "EEF2F7")
                cell._tc.get_or_add_tcPr().append(shd)
    # Tabellen nicht über den Seitenumbruch zerreißen
    for row in table.rows:
        trPr = row._tr.get_or_add_trPr()
        cant = OxmlElement("w:cantSplit")
        trPr.append(cant)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)


def add_code(doc, code, size=10):
    for line in code.split("\n"):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.left_indent = Cm(0.5)
        run = p.add_run(line if line else " ")
        run.font.name = MONO
        run.font.size = Pt(size)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)


def title_page(doc, titel, untertitel, zeilen):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(90)
    run = p.add_run(titel)
    run.bold = True
    run.font.size = Pt(26)
    run.font.color.rgb = AKZENT

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(untertitel)
    run.font.size = Pt(13)

    for zeile in zeilen:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(zeile)
        run.font.size = Pt(10)
        run.font.color.rgb = RGBColor(0x55, 0x55, 0x55)


def set_columns(doc, count):
    """Setzt den letzten Abschnitt auf mehrere Spalten."""
    sectPr = doc.sections[-1]._sectPr
    cols = sectPr.xpath("./w:cols")
    cols = cols[0] if cols else OxmlElement("w:cols")
    cols.set(qn("w:num"), str(count))
    cols.set(qn("w:space"), "360")
    if not sectPr.xpath("./w:cols"):
        sectPr.append(cols)


def slice_section(blocks, ueberschrift):
    """Schneidet den Abschnitt ab einer h2-Überschrift bis zur nächsten h2 heraus."""
    out, aktiv = [], False
    for kind, payload in blocks:
        if kind == "h2":
            if aktiv:
                break
            aktiv = payload.strip().lower() == ueberschrift.lower()
            continue
        if aktiv:
            out.append((kind, payload))
    return out


# ---------------------------------------------------------------------------
# DOKUMENTE
# ---------------------------------------------------------------------------
def build_lernskript(skript_blocks, aufgaben_blocks):
    doc = Document()
    set_base_style(doc)
    for s in doc.sections:
        s.top_margin = s.bottom_margin = Cm(2.0)
        s.left_margin = s.right_margin = Cm(2.2)

    title_page(
        doc,
        "Grundlagen der Automation",
        "Lernskript zur Klausurvorbereitung",
        [
            "",
            "HTW Berlin · Studiengang Wirtschaftsingenieurwesen",
            "nach der Vorlesung von Prof. Patrick Fabian, SS 2026",
            "",
            "Kapitel 2 bis 7 · Handouts H2 bis H12 · Übungen 1 bis 7",
        ],
    )

    render(doc, skript_blocks, base_size=11)

    doc.add_page_break()
    heading(doc, "Klausur-Aufgabentypen")
    render(doc, aufgaben_blocks, base_size=11)

    add_page_numbers(doc, prefix="Grundlagen der Automation")
    pfad = OUT / "Lernskript_Automation.docx"
    doc.save(pfad)
    return pfad


def build_spickzettel(skript_blocks):
    formeln = slice_section(skript_blocks, "Formelsammlung")
    if not formeln:
        raise SystemExit("Abschnitt 'Formelsammlung' nicht gefunden.")

    doc = Document()
    set_base_style(doc, size=9)
    for s in doc.sections:
        s.top_margin = s.bottom_margin = Cm(1.2)
        s.left_margin = s.right_margin = Cm(1.2)

    heading(doc, "Spickzettel — Grundlagen der Automation", size=13)
    p = doc.add_paragraph()
    run = p.add_run(
        "Verdichtete Formelsammlung. Fundstellen und Herleitungen stehen im "
        "Lernskript."
    )
    run.font.size = Pt(8)
    run.italic = True

    set_columns(doc, 2)
    render(doc, formeln, base_size=9)

    add_page_numbers(doc)
    pfad = OUT / "Spickzettel_Automation.docx"
    doc.save(pfad)
    return pfad


def main():
    skript_blocks = parse((SRC / "lernskript_at.md").read_text(encoding="utf-8"))
    aufgaben_blocks = parse((SRC / "aufgabentypen.md").read_text(encoding="utf-8"))

    a = build_lernskript(skript_blocks, aufgaben_blocks)
    b = build_spickzettel(skript_blocks)
    for pfad in (a, b):
        print(f"geschrieben: {pfad.relative_to(ROOT)}  ({pfad.stat().st_size/1024:.0f} KB)")


if __name__ == "__main__":
    main()
