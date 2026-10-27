import fitz
import os
import shutil

BASE_PDF = r"C:\Users\Suhani Srivastava\.gemini\antigravity\scratch\InfoHub\static\infohub_project_synopsis.pdf"
PIE_CHART = r"C:\Users\Suhani Srivastava\.gemini\antigravity\scratch\InfoHub\static\infohub_allocation_chart.png"
FLOWCHART = r"C:\Users\Suhani Srivastava\.gemini\antigravity\scratch\InfoHub\static\infohub_flowchart_vertical.png"
OUTPUT_PDF = r"C:\Users\Suhani Srivastava\.gemini\antigravity\scratch\InfoHub\static\infohub_project_synopsis.pdf"
BRAIN_PDF = r"C:\Users\Suhani Srivastava\.gemini\antigravity\brain\fd28118c-64ed-4da6-aae6-d71c60182d0a\infohub_project_synopsis.pdf"

def main():
    doc = fitz.open(BASE_PDF)
    print("Opened base PDF. Number of pages:", len(doc))

    # We want pages 1-8 untouched (page 1 already has the centered GNIOT logo).
    # We will build a new document:
    new_doc = fitz.open()
    for i in range(8):
        new_doc.insert_pdf(doc, from_page=i, to_page=i)
    
    # Now let's create Page 9:
    # Page 9 contains:
    # 4.1 Planned System Allocation
    # Bullets for 4.1
    # Pie chart
    # 4.2 Planned Technology Stack
    # Bullets for 4.2
    page9 = new_doc.new_page(width=595.28, height=841.89)
    
    # Fonts and styling
    # Heading style: 13pt bold, Liberation Sans / Helvetica
    # Body style: 11pt, line spacing
    margin_left = 62.7
    content_width = 470
    
    # 4.1 Header
    y = 70.0
    page9.insert_text(fitz.Point(margin_left, y + 13), "4.1 Planned System Allocation", fontname="helv", fontsize=13, fontfile=None)
    
    # 4.1 Bullets
    bullets_4_1 = [
        ("Admin Publishing Tools (40%):", " Notice Creation, Priority Tagging, Relational Field Mapping, and Lifecycle Expiry Scheduling."),
        ("User Discovery Tools (40%):", " Global Key-Phrase Queries, Sectional Feeds, Archive Access, and Verified Source Tagging."),
        ("Access Protocols (20%):", " Multi-Role Login Verification, Relational Integrity System Controls, and Granular Permission Enforcement.")
    ]
    
    y = 95.0
    for title, desc in bullets_4_1:
        # Bullet symbol
        page9.insert_text(fitz.Point(margin_left + 8, y + 10), "\u2022", fontname="helv", fontsize=11)
        # Bold title
        page9.insert_text(fitz.Point(margin_left + 20, y + 10), title, fontname="helv", fontsize=10.5)
        # Measure title width
        tl = fitz.get_text_length(title, fontname="helv", fontsize=10.5)
        # Description
        # We can write description with a small rect or text
        desc_rect = fitz.Rect(margin_left + 20 + tl, y, margin_left + content_width, y + 35)
        # If it fits on one/two lines:
        page9.insert_textbox(desc_rect, desc, fontname="helv", fontsize=10.5, lineheight=1.2)
        y += 32.0

    # Insert Pie Chart
    # Rect for pie chart: centered
    chart_w = 340
    chart_h = 190
    chart_x = (595.28 - chart_w) / 2
    chart_y = y + 5
    page9.insert_image(fitz.Rect(chart_x, chart_y, chart_x + chart_w, chart_y + chart_h), filename=PIE_CHART)
    
    # Pie chart caption
    caption_y = chart_y + chart_h + 12
    caption_text = "Figure 4.1: Planned System Resource & Feature Allocation Distribution"
    cap_w = fitz.get_text_length(caption_text, fontname="helv", fontsize=9.5)
    page9.insert_text(fitz.Point((595.28 - cap_w) / 2, caption_y), caption_text, fontname="helv", fontsize=9.5)
    
    # 4.2 Header
    y = caption_y + 24
    page9.insert_text(fitz.Point(margin_left, y + 13), "4.2 Planned Technology Stack", fontname="helv", fontsize=13)
    
    bullets_4_2 = [
        ("Frontend Presentational Layers:", " HTML5, CSS3 (Modern Responsive Flexbox & Grid), Vanilla JavaScript"),
        ("Application Framework:", " Python Flask (Lightweight WSGI Microframework, RESTful Endpoints & Jinja2 Templates)"),
        ("Relational Database:", " SQLite (Relational SQL Schema with Foreign Keys & ACID Transactional Integrity)"),
        ("Deployment & Server Environment:", " Gunicorn / WSGI Application Server, Cross-Platform Linux & Windows Compatibility")
    ]
    
    y = y + 22
    for title, desc in bullets_4_2:
        page9.insert_text(fitz.Point(margin_left + 8, y + 10), "\u2022", fontname="helv", fontsize=11)
        page9.insert_text(fitz.Point(margin_left + 20, y + 10), title, fontname="helv", fontsize=10)
        tl = fitz.get_text_length(title, fontname="helv", fontsize=10)
        desc_rect = fitz.Rect(margin_left + 20 + tl, y, margin_left + content_width, y + 30)
        page9.insert_textbox(desc_rect, desc, fontname="helv", fontsize=10, lineheight=1.15)
        y += 24.0
        
    # Brief pointer to next page
    pointer_text = "(The end-to-end architectural workflow and technology interaction is detailed in Figure 4.2 on the following page)"
    pt_w = fitz.get_text_length(pointer_text, fontname="helv", fontsize=9)
    page9.insert_text(fitz.Point((595.28 - pt_w) / 2, y + 10), pointer_text, fontname="helv", fontsize=9)
    
    # Page 9 number
    page9.insert_text(fitz.Point(533.0, 808.0), "9", fontname="helv", fontsize=10)
    
    # -------------------------------------------------------------
    # PAGE 10: DEDICATED FLOWCHART PAGE
    # -------------------------------------------------------------
    page10 = new_doc.new_page(width=595.28, height=841.89)
    
    # Header on Page 10
    flow_hdr = "4.2 Planned Technology Stack - System Architecture Flowchart"
    page10.insert_text(fitz.Point(margin_left, 65), flow_hdr, fontname="helv", fontsize=12)
    
    # Let's insert the vertical flowchart
    # Aspect ratio of vertical flowchart: 3334 x 5139 (w:h = 1 : 1.5414)
    # Target height: ~670 pt
    # Width = 670 / 1.5414 = 434.6 pt
    fc_h = 675
    fc_w = fc_h * (3334.0 / 5139.0)
    fc_x = (595.28 - fc_w) / 2
    fc_y = 80
    
    page10.insert_image(fitz.Rect(fc_x, fc_y, fc_x + fc_w, fc_y + fc_h), filename=FLOWCHART)
    
    # Caption below flowchart
    fc_caption = "Figure 4.2: InfoHub End-to-End System Architecture & Functional Flowchart"
    fc_cap_w = fitz.get_text_length(fc_caption, fontname="helv", fontsize=9.5)
    page10.insert_text(fitz.Point((595.28 - fc_cap_w) / 2, fc_y + fc_h + 14), fc_caption, fontname="helv", fontsize=9.5)
    
    # Page 10 number
    page10.insert_text(fitz.Point(533.0, 808.0), "10", fontname="helv", fontsize=10)
    
    # -------------------------------------------------------------
    # PAGE 11: REFERENCES PAGE
    # -------------------------------------------------------------
    page11 = new_doc.new_page(width=595.28, height=841.89)
    
    # 5. REFERENCES Header
    page11.insert_text(fitz.Point(margin_left, 75), "5. REFERENCES", fontname="helv", fontsize=14)
    
    refs = [
        'Pallets Projects, "Flask Documentation," official Flask documentation. [Online]. Available: https://flask.palletsprojects.com/. [Accessed: Oct. 2026].',
        'SQLite Development Team, "SQLite Documentation," SQLite official reference manual. [Online]. Available: https://www.sqlite.org/docs.html. [Accessed: Oct. 2026].',
        'Mozilla Developer Network (MDN), "HTML5 & CSS3 Web Technologies Guide," MDN Web Docs. [Online]. Available: https://developer.mozilla.org/. [Accessed: Oct. 2026].',
        'Python Software Foundation, "The Python Standard Library & WSGI Server Specifications (PEP 3333)." [Online]. Available: https://www.python.org/dev/peps/pep-3333/. [Accessed: Oct. 2026].',
        'R. Fielding et al., "Architectural Styles and the Design of Network-based Software Architectures," Doctoral dissertation, University of California, Irvine, 2000.'
    ]
    
    ref_y = 110.0
    for idx, ref_text in enumerate(refs, 1):
        # Number: "1."
        num_str = f"{idx}."
        page11.insert_text(fitz.Point(margin_left + 10, ref_y + 11), num_str, fontname="helv", fontsize=10)
        
        # Text box for reference
        ref_rect = fitz.Rect(margin_left + 28, ref_y, margin_left + content_width, ref_y + 50)
        page11.insert_textbox(ref_rect, ref_text, fontname="helv", fontsize=10, lineheight=1.25)
        ref_y += 50.0

    # Page 11 number
    page11.insert_text(fitz.Point(533.0, 808.0), "11", fontname="helv", fontsize=10)
    
    # Save output atomically
    temp_path = BASE_PDF + ".tmp"
    new_doc.save(temp_path)
    new_doc.close()
    doc.close()
    
    shutil.move(temp_path, OUTPUT_PDF)
    shutil.copyfile(OUTPUT_PDF, BRAIN_PDF)
    print("Successfully generated updated synopsis PDF with dedicated flowchart page!")

if __name__ == "__main__":
    main()
