#!/usr/bin/env python3
"""Convert the answer Markdown dialect used in this project to a styled .docx.
Usage: md2docx.py out.docx in1.md [in2.md ...]
Dialect: # ## ### #### headings; paragraphs; '- ' bullets; '1. ' numbers; pipe tables;
'> ' callouts; ![caption](path.png) images; a line '<<<PAGEBREAK>>>'; **bold**, *italic*.
Evidence tags [SRC] [LIT] [RECALL] and confidence tags [Certain] [Likely] [Guessing] are colour-coded.
"""
import re, sys, os
from docx import Document
from docx.shared import Pt, RGBColor, Cm, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

TAGS = {
    "[CITE]": RGBColor(0x1B, 0x7A, 0x3D),
    "[LIT]": RGBColor(0x1F, 0x4E, 0xA8),
    "[RECALL]": RGBColor(0xC2, 0x6A, 0x00),
    "[Certain]": RGBColor(0x55, 0x55, 0x55),
    "[Likely]": RGBColor(0x55, 0x55, 0x55),
    "[Guessing]": RGBColor(0xB0, 0x2A, 0x2A),
}
TAG_RE = re.compile(r"(\([A-Z][^()]*?\b(?:(?:19|20)\d{2}[a-z]?|undated)\*?(?:; [^()]*?\b(?:(?:19|20)\d{2}[a-z]?|undated)\*?)*\)|\[RECALL\]|\[Certain\]|\[Likely\]|\[Guessing\])")
INLINE_RE = re.compile(r"(\*\*[^*]+\*\*|\*[^*\s][^*]*\*)")


def shade(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hexcolor)
    tcPr.append(shd)


def add_runs(par, text, base_bold=False, size=None, color=None):
    for chunk in INLINE_RE.split(text):
        if not chunk:
            continue
        bold, ital = base_bold, False
        if chunk.startswith("**") and chunk.endswith("**") and len(chunk) > 4:
            chunk, bold = chunk[2:-2], True
        elif chunk.startswith("*") and chunk.endswith("*") and len(chunk) > 2:
            chunk, ital = chunk[1:-1], True
        for piece in TAG_RE.split(chunk):
            if not piece:
                continue
            r = par.add_run(piece)
            r.bold = bold
            r.italic = ital
            if size:
                r.font.size = Pt(size)
            tagkey = "[CITE]" if (piece.startswith("(") and piece.endswith(")")) else piece
            if tagkey in TAGS:
                r.font.color.rgb = TAGS[tagkey]
                if tagkey == "[CITE]":
                    r.font.size = Pt((size or 11) - 0.5)
                else:
                    r.bold = True
                    r.font.size = Pt((size or 11) - 1.5)
            elif color:
                r.font.color.rgb = color


def set_cell_text(cell, text, bold=False, size=9.5):
    cell.text = ""
    par = cell.paragraphs[0]
    par.paragraph_format.space_after = Pt(1)
    add_runs(par, text.replace("<br>", "\n"), base_bold=bold, size=size)


def add_table(doc, rows):
    n = max(len(r) for r in rows)
    rows = [r + [""] * (n - len(r)) for r in rows]
    t = doc.add_table(rows=len(rows), cols=n)
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, r in enumerate(rows):
        for j, c in enumerate(r):
            set_cell_text(t.cell(i, j), c, bold=(i == 0))
            if i == 0:
                shade(t.cell(i, j), "D9E2F3")
    doc.add_paragraph().paragraph_format.space_after = Pt(2)


def add_page_number(section):
    p = section.footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run()
    for kind, txt in (("begin", None), (None, "PAGE"), ("end", None)):
        if kind:
            el = OxmlElement("w:fldChar")
            el.set(qn("w:fldCharType"), kind)
        else:
            el = OxmlElement("w:instrText")
            el.set(qn("xml:space"), "preserve")
            el.text = txt
        r._r.append(el)
    r.font.size = Pt(9)


def build(out, files):
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
    sec.left_margin = sec.right_margin = Cm(2.0)
    sec.top_margin = sec.bottom_margin = Cm(2.0)
    add_page_number(sec)
    st = doc.styles["Normal"]
    st.font.name = "Calibri"
    st.font.size = Pt(11)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
    st.paragraph_format.space_after = Pt(4)
    colors = {1: "1F3864", 2: "2F5496", 3: "2E74B5", 4: "404040"}
    sizes = {1: 20, 2: 15, 3: 12.5, 4: 11.5}
    for lvl in (1, 2, 3, 4):
        h = doc.styles[f"Heading {lvl}"]
        h.font.name = "Calibri"
        h.font.size = Pt(sizes[lvl])
        h.font.bold = True
        h.font.color.rgb = RGBColor.from_string(colors[lvl])
        h.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
        h.paragraph_format.space_before = Pt(12 if lvl > 1 else 16)
        h.paragraph_format.space_after = Pt(4)
        h.paragraph_format.keep_with_next = True

    for fi, path in enumerate(files):
        lines = open(path, encoding="utf-8").read().split("\n")
        i = 0
        while i < len(lines):
            ln = lines[i].rstrip()
            if not ln.strip():
                i += 1
                continue
            if ln.strip() == "<<<PAGEBREAK>>>":
                doc.add_page_break()
                i += 1
                continue
            m = re.match(r"^(#{1,4})\s+(.*)$", ln)
            if m:
                lvl = len(m.group(1))
                h = doc.add_heading(level=lvl)
                add_runs(h, m.group(2))
                i += 1
                continue
            m = re.match(r"^!\[(.*?)\]\((.*?)\)\s*$", ln)
            if m:
                cap, img = m.groups()
                p = doc.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                if os.path.exists(img):
                    p.add_run().add_picture(img, width=Cm(17))
                if cap:
                    c = doc.add_paragraph()
                    c.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    add_runs(c, cap, size=9, color=RGBColor(0x55, 0x55, 0x55))
                i += 1
                continue
            if ln.lstrip().startswith("|"):
                rows = []
                while i < len(lines) and lines[i].lstrip().startswith("|"):
                    cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                    if not all(re.fullmatch(r":?-{2,}:?", c) or c == "" for c in cells) or not any(cells):
                        rows.append(cells)
                    elif not all(re.fullmatch(r":?-+:?", c) for c in cells if c):
                        rows.append(cells)
                    i += 1
                add_table(doc, rows)
                continue
            if ln.startswith("> "):
                buf = []
                while i < len(lines) and lines[i].startswith("> "):
                    buf.append(lines[i][2:])
                    i += 1
                t = doc.add_table(rows=1, cols=1)
                t.style = "Table Grid"
                cell = t.cell(0, 0)
                shade(cell, "FFF4CE")
                cell.text = ""
                for k, b in enumerate(buf):
                    p = cell.paragraphs[0] if k == 0 else cell.add_paragraph()
                    p.paragraph_format.space_after = Pt(2)
                    add_runs(p, b, size=10.5)
                doc.add_paragraph().paragraph_format.space_after = Pt(2)
                continue
            m = re.match(r"^(\s*)[-*]\s+(.*)$", ln)
            if m:
                p = doc.add_paragraph(style="List Bullet" if len(m.group(1)) < 2 else "List Bullet 2")
                p.paragraph_format.space_after = Pt(2)
                add_runs(p, m.group(2))
                i += 1
                continue
            m = re.match(r"^\s*(\d+)[.)]\s+(.*)$", ln)
            if m:
                p = doc.add_paragraph(style="List Number")
                p.paragraph_format.space_after = Pt(2)
                add_runs(p, m.group(2))
                i += 1
                continue
            p = doc.add_paragraph()
            add_runs(p, ln)
            i += 1
        if fi < len(files) - 1:
            doc.add_page_break()
    doc.save(out)
    print("saved", out)


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2:])
