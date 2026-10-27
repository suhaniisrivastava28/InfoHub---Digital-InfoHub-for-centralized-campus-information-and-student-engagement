import pymupdf
import os
import shutil

pdf_path = r"C:\Users\Suhani Srivastava\.gemini\antigravity\scratch\InfoHub\static\infohub_project_synopsis.pdf"
flowchart_path = r"C:\Users\Suhani Srivastava\.gemini\antigravity\scratch\InfoHub\static\infohub_flowchart_vertical.png"
temp_pdf = r"C:\Users\Suhani Srivastava\.gemini\antigravity\scratch\InfoHub\static\temp_synopsis.pdf"
brain_pdf = r"C:\Users\Suhani Srivastava\.gemini\antigravity\brain\fd28118c-64ed-4da6-aae6-d71c60182d0a\infohub_project_synopsis.pdf"

doc = pymupdf.open(pdf_path)
print("Initial page count:", len(doc))

PAGE_W = 595.28
PAGE_H = 841.89

# If document has 9 pages:
# Page 9 (index 8):
page9 = doc[8]

# 1. Redact Section 5 References from Page 9 (from y=498 down to y=795)
# This leaves 4.1 (Allocation + Pie chart) and 4.2 (Planned Technology Stack + 4 bullets) intact!
page9.add_redact_annot(pymupdf.Rect(50, 498, 550, 795), fill=(1, 1, 1))
page9.apply_redactions()

# Add an elegant cross-reference note below 4.2 on Page 9
note_text = "(The comprehensive end-to-end architecture and technology stack workflow is illustrated in Figure 4.2 on the following page)"
font_regular = "helv"
font_bold = "hebo"
color = (0.25, 0.28, 0.32)
note_len = pymupdf.get_text_length(note_text, fontname=font_regular, fontsize=9.5)
page9.insert_text(pymupdf.Point((PAGE_W - note_len) / 2, 515), note_text, fontname=font_regular, fontsize=9.5, color=color)

# 2. Create Page 10: Dedicated Flowchart Page (after 4.2 and before 5 References)
page10 = doc.new_page(pno=-1, width=PAGE_W, height=PAGE_H)

# Header on Page 10
p10_title = "4.2 Planned Technology Stack - System Architecture Matrix"
page10.insert_text(pymupdf.Point(62.7, 58), p10_title, fontname=font_bold, fontsize=12, color=(0.13, 0.15, 0.16))

# Flowchart placement on Page 10
# Aspect ratio of vertical flowchart: 3334 x 5139 (w:h = 1 : 1.5414)
# Target height: ~690 pt (from y=72 to y=762)
fc_h = 690.0
fc_w = fc_h * (3334.0 / 5139.0)  # ~447.6 pt
fc_x = (PAGE_W - fc_w) / 2
fc_y = 70.0

# Add a subtle, sleek border around the flowchart container
border_rect = pymupdf.Rect(fc_x - 1, fc_y - 1, fc_x + fc_w + 1, fc_y + fc_h + 1)
shape = page10.new_shape()
shape.draw_rect(border_rect)
shape.finish(color=(0.85, 0.88, 0.92), width=0.8)
shape.commit()

page10.insert_image(pymupdf.Rect(fc_x, fc_y, fc_x + fc_w, fc_y + fc_h), filename=flowchart_path)

# Figure caption below flowchart
fc_caption = "Figure 4.2: InfoHub End-to-End System Architecture & Functional Flowchart"
fc_cap_w = pymupdf.get_text_length(fc_caption, fontname=font_bold, fontsize=9.5)
page10.insert_text(pymupdf.Point((PAGE_W - fc_cap_w) / 2, fc_y + fc_h + 16), fc_caption, fontname=font_bold, fontsize=9.5, color=(0.15, 0.18, 0.22))

# Page 10 footer page number
page10.insert_text(pymupdf.Point(533.0, 808.0), "10", fontname=font_regular, fontsize=10, color=(0.13, 0.15, 0.16))

# 3. Create Page 11: Section 5 REFERENCES Page
page11 = doc.new_page(pno=-1, width=PAGE_W, height=PAGE_H)

# Section 5 Header
page11.insert_text(pymupdf.Point(62.7, 75), "5. REFERENCES", fontname=font_bold, fontsize=14, color=(0.13, 0.15, 0.16))

# Separator line
shape = page11.new_shape()
shape.draw_line(pymupdf.Point(62.7, 83), pymupdf.Point(532.6, 83))
shape.finish(color=(0.82, 0.85, 0.88), width=0.75)
shape.commit()

refs = [
    ('1. ', 'Pallets Projects, "Flask Documentation," official Flask documentation. [Online]. Available: flask.palletsprojects.com'),
    ('2. ', 'SQLite Consortium, "SQLite Documentation," official SQLite documentation. [Online]. Available: sqlite.org/docs.html'),
    ('3. ', 'GitHub, "GitHub Documentation," official GitHub documentation. [Online]. Available: docs.github.com'),
    ('4. ', 'Bootstrap, "Bootstrap Documentation," official Bootstrap documentation. [Online]. Available: getbootstrap.com/docs')
]

ref_y = 110.0
for num, ref_text in refs:
    full_text = f"{num}{ref_text}"
    rect = pymupdf.Rect(79.35, ref_y - 9, 532.6, ref_y + 35)
    page11.insert_textbox(rect, full_text, fontname=font_regular, fontsize=11, color=(0.13, 0.15, 0.16), lineheight=1.2)
    ref_y += 38.0

# Page 11 footer page number
page11.insert_text(pymupdf.Point(533.0, 808.0), "11", fontname=font_regular, fontsize=10, color=(0.13, 0.15, 0.16))

# Save PDF
doc.save(temp_pdf)
doc.close()

shutil.move(temp_pdf, pdf_path)
shutil.copyfile(pdf_path, brain_pdf)
print(f"Successfully generated 11-page synopsis PDF at {pdf_path}")

# Render previews for verification
doc_verify = pymupdf.open(pdf_path)
print("Verified page count:", len(doc_verify))

# Render page 9
p9_pix = doc_verify[8].get_pixmap(dpi=150)
p9_pix.save(r"C:\Users\Suhani Srivastava\.gemini\antigravity\scratch\InfoHub\static\synopsis_page9_preview.png")

# Render page 10
p10_pix = doc_verify[9].get_pixmap(dpi=150)
p10_pix.save(r"C:\Users\Suhani Srivastava\.gemini\antigravity\scratch\InfoHub\static\synopsis_page10_preview.png")

# Render page 11
p11_pix = doc_verify[10].get_pixmap(dpi=150)
p11_pix.save(r"C:\Users\Suhani Srivastava\.gemini\antigravity\scratch\InfoHub\static\synopsis_page11_preview.png")

doc_verify.close()
print("Saved previews for pages 9, 10, and 11.")
