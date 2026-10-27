"""
=============================================================================
GNIOT Hub Platform - Ultra-Premium Glassmorphic Cyber-Theme Portal
=============================================================================
Zero-ERP Dynamic Crowdsourced Campus Notice Engine
Second-Year Engineering Mini-Project Evaluation Standard

Backend: Python Flask (runs strictly on port 5010)
Frontend: Bootstrap 5 + Custom Glassmorphic Cyber-CSS
Database: Local 'data.json' file (Atomic Zero-ERP Engine)
RBAC Security:
  - Student Profile: username='student' | password='password' (Read-Only)
  - Admin Profile:   username='admin'   | password='adminpassword' (Write/Delete)
=============================================================================
"""

import json
import os
import sys
import urllib.parse
from datetime import datetime
from functools import wraps
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
    abort
)

# Force UTF-8 reconfigure on Windows console
try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# ---------------------------------------------------------------------------
# App Initialization & Configuration
# ---------------------------------------------------------------------------
app = Flask(__name__)
app.secret_key = "gniot-hub-platform-cyber-2026-key"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE_PATH = os.path.join(BASE_DIR, "data.json")

# Serverless environment support (e.g. Vercel read-only filesystem)
if os.environ.get("VERCEL"):
    import shutil
    TMP_DATA_PATH = "/tmp/data.json"
    if not os.path.exists(TMP_DATA_PATH) and os.path.exists(DATA_FILE_PATH):
        try:
            shutil.copyfile(DATA_FILE_PATH, TMP_DATA_PATH)
        except Exception:
            pass
    if os.path.exists(TMP_DATA_PATH):
        DATA_FILE_PATH = TMP_DATA_PATH


# ---------------------------------------------------------------------------
# Database File Operations
# ---------------------------------------------------------------------------
def load_database():
    """Reads categories and notices dynamically from local 'data.json'."""
    if not os.path.exists(DATA_FILE_PATH):
        return {"categories": [], "notices": []}
    try:
        with open(DATA_FILE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception:
        # Fallback to base file if temp copy had an issue
        orig_path = os.path.join(BASE_DIR, "data.json")
        if os.path.exists(orig_path):
            with open(orig_path, "r", encoding="utf-8") as file:
                return json.load(file)
        return {"categories": [], "notices": []}


def save_database(data):
    """Writes updated notices atomically to local 'data.json'."""
    try:
        with open(DATA_FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Warning: Database write could not complete: {e}", file=sys.stderr)


# ---------------------------------------------------------------------------
# Role-Based Access Control (RBAC) Guards
# ---------------------------------------------------------------------------
def login_required(f):
    """Requires active authentication as either Student or Admin."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("logged_in"):
            flash("Authorization Required: Please authenticate with GNIOT Hub credentials.", "warning")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function


def admin_required(f):
    """Guards administrative actions (notice creation & record deletion)."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("logged_in"):
            flash("Please sign in first.", "warning")
            return redirect(url_for("login"))
        if session.get("role") != "admin":
            flash("Access Restricted: Full administrative privileges are required for this action.", "danger")
            return redirect(url_for("dashboard"))
        return f(*args, **kwargs)
    return decorated_function


@app.context_processor
def inject_global_data():
    """Supplies global categories and active RBAC mode to all templates."""
    db = load_database()
    return {
        "global_categories": db.get("categories", []),
        "current_user": session.get("username"),
        "current_role": session.get("role", "guest"),
        "is_admin": session.get("role") == "admin"
    }


# ---------------------------------------------------------------------------
# LEVEL 1: Entrance Portal Landing ('login.html')
# ---------------------------------------------------------------------------
@app.route("/", methods=["GET"])
def index():
    if session.get("logged_in"):
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    LEVEL 1: Entrance Portal Landing
    Supports dynamic registered students as well as default credentials.
    """
    if request.method == "POST":
        username = request.form.get("username", "").strip().lower()
        password = request.form.get("password", "").strip()
        semester = request.form.get("semester", "").strip()

        db = load_database()
        users = db.get("users", [])

        # 1. Check against registered users in database
        matched_user = next((u for u in users if u.get("username", "").lower() == username and u.get("password") == password), None)

        if matched_user:
            session["logged_in"] = True
            session["username"] = matched_user["username"]
            session["role"] = matched_user.get("role", "student")
            session["full_name"] = matched_user.get("full_name", matched_user["username"])
            session["department"] = matched_user.get("department", "Student Scholar")
            session["semester"] = semester or matched_user.get("semester", "8th Semester")
            role_title = "Administrator" if matched_user.get("role") == "admin" else "Student"
            flash(f"Welcome back, {session['full_name']}! ({session['semester']} • {role_title} session activated)", "success")
            return redirect(url_for("dashboard"))

        # 2. Built-in fallback accounts
        elif username == "admin" and password == "adminpassword":
            session["logged_in"] = True
            session["username"] = "admin"
            session["role"] = "admin"
            session["full_name"] = "Faculty Administrator"
            session["department"] = "Central Administrative Tower"
            session["semester"] = semester or "Faculty / Academic Office"
            flash("Administrator session activated. Full write and delete permissions granted.", "success")
            return redirect(url_for("dashboard"))
        elif username == "student" and (password == "password" or password == "student123"):
            session["logged_in"] = True
            session["username"] = "student"
            session["role"] = "student"
            session["full_name"] = "Student Scholar"
            session["department"] = "B.Tech Engineering"
            session["semester"] = semester or "8th Semester"
            flash(f"Student session activated ({session['semester']}). University portal feed enabled.", "info")
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid credentials! Incorrect username or password for GNIOT Hub.", "danger")

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    New Student Self-Registration Portal.
    Allows new students to set up their custom login and password.
    """
    if request.method == "GET":
        return redirect(url_for("login"))
    full_name = request.form.get("reg_fullname", "").strip()
    username = request.form.get("reg_username", "").strip().lower()
    password = request.form.get("reg_password", "").strip()
    department = request.form.get("reg_department", "B.Tech CSE").strip()
    semester = request.form.get("reg_semester", "1st Semester").strip()

    if not username or not password:
        flash("Registration Failed: Username/Roll Number and Password are required.", "danger")
        return redirect(url_for("login"))

    db = load_database()
    users = db.get("users", [])

    # Check if username already exists
    if any(u.get("username", "").lower() == username for u in users) or username in ["admin", "student"]:
        flash(f"Student ID / Username '{username}' is already registered! Please sign in using your password.", "warning")
        return redirect(url_for("login"))

    # Register new student
    new_user = {
        "username": username,
        "password": password,
        "role": "student",
        "full_name": full_name or username.title(),
        "department": department,
        "semester": semester
    }
    users.append(new_user)
    db["users"] = users
    save_database(db)

    # Immediately activate session for the new student
    session["logged_in"] = True
    session["username"] = username
    session["role"] = "student"
    session["full_name"] = new_user["full_name"]
    session["department"] = department
    session["semester"] = semester

    flash(f"🎉 Registration Successful! Welcome to GNIOT Hub, {new_user['full_name']} ({semester}).", "success")
    return redirect(url_for("dashboard"))


@app.route("/logout")
def logout():
    session.clear()
    flash("Session terminated safely. Mode disconnected.", "secondary")
    return redirect(url_for("login"))


# ---------------------------------------------------------------------------
# LEVEL 2: Premium GNIOT Console Dashboard ('dashboard.html')
# ---------------------------------------------------------------------------
@app.route("/dashboard")
@login_required
def dashboard():
    """
    LEVEL 2: Premium GNIOT Console Dashboard
    - Sketched Navigation Bar: '🏫 GNIOT Hub Platform Console'
    - Engineering Constraints Status Box (4 distinct border-mapped badge cards):
        '🗺️ Campus Nav: ✅ Yes', '🤖 AI Agent: ❌ No',
        '🔒 ERP Access: ❌ Restricted', '🔄 Update Mode: 👥 Crowdsourced'
    - Visual Channel Grid Matrix: 8 core academic option cards:
        Scholarships, Events, Holidays, Seminars, SIP Tracker,
        Orientation, Hackathons, Placements
    - Document Workspace Anchor for 'academic_calendar.pdf'
    - RBAC Content Injector Form (Visible ONLY for Admin)
    """
    db = load_database()
    categories = db.get("categories", [])
    notices = db.get("notices", [])

    category_counts = {}
    for cat in categories:
        category_counts[cat["id"]] = sum(1 for n in notices if n.get("category") == cat["id"])

    engineering_constraints = [
        {"icon": "🗺️", "title": "Campus Nav", "status": "✅ Yes", "border_class": "border-neon-cyan"},
        {"icon": "🤖", "title": "AI Agent", "status": "❌ No", "border_class": "border-neon-secondary"},
        {"icon": "🔒", "title": "ERP Access", "status": "❌ Restricted", "border_class": "border-neon-rose"},
        {"icon": "🔄", "title": "Update Mode", "status": "👥 Crowdsourced", "border_class": "border-neon-emerald"}
    ]

    return render_template(
        "dashboard.html",
        categories=categories,
        category_counts=category_counts,
        engineering_constraints=engineering_constraints
    )


# ---------------------------------------------------------------------------
# RBAC Write Action: Content Injector Notice Creation
# ---------------------------------------------------------------------------
@app.route("/admin/create-notice", methods=["POST"])
@admin_required
def create_notice():
    """
    Administrative Content Injector Terminal.
    Injects data live into 'data.json'.
    """
    db = load_database()
    notices = db.get("notices", [])

    category = request.form.get("category", "scholarships").strip()
    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    eligibility = request.form.get("eligibility", "").strip()
    starting_date = request.form.get("starting_date", "").strip()
    ending_date = request.form.get("ending_date", "").strip()
    reward_amount = request.form.get("reward_amount", "").strip()
    concerned_authorities = request.form.get("concerned_authorities", "").strip()
    if not concerned_authorities:
        concerned_authorities = "Contact Registrar Office, Dean, or relevant HOD Section (Central Admin Tower Desk)"

    verification_level = request.form.get("verification_level", "official").strip()
    submission_type = request.form.get("submission_type", "Online Track").strip()
    official_url = request.form.get("official_url", "https://gniot.edu.in").strip()

    # Dynamic Verification Label
    verification_labels = {
        "official": "🟢 Officially Authorized (Faculty / Dean / HOD)",
        "crowdsourced": "🟡 Crowdsourced (Contributed by CR / Student Council)",
        "unconfirmed": "🔴 Unconfirmed Public Entry (Verification Pending)"
    }
    verification_label = verification_labels.get(verification_level, "🟢 Officially Authorized (Faculty / Dean / HOD)")

    raw_docs = request.form.get("required_documents", "").strip()
    if raw_docs:
        docs_list = [d.strip() for d in raw_docs.replace("\r\n", "\n").split("\n") if d.strip()]
    else:
        docs_list = ["GNIOT Student ID Card", "Bonafide Certificate"]

    prefix_map = {
        "scholarships": "SCH", "events": "EVT", "holidays": "HOL",
        "seminars": "SEM", "sip-tracker": "SIP", "orientation": "ORI",
        "hackathons": "HAK", "placements": "PLC"
    }
    pfx = prefix_map.get(category, "NOT")
    year = datetime.now().year
    count_in_cat = sum(1 for n in notices if n.get("category") == category) + 1
    new_id = f"{pfx}-{year}-{count_in_cat:02d}"

    new_notice = {
        "id": new_id,
        "category": category,
        "title": title or "Untitled Notice",
        "description": description or "Notice details pending official upload.",
        "eligibility": eligibility or "Open to all enrolled students.",
        "starting_date": starting_date or datetime.now().strftime("%Y-%m-%d"),
        "ending_date": ending_date or datetime.now().strftime("%Y-%m-%d"),
        "reward_amount": reward_amount,
        "concerned_authorities": concerned_authorities,
        "verification_level": verification_level,
        "verification_label": verification_label,
        "submission_type": submission_type,
        "required_documents": docs_list,
        "official_url": official_url
    }

    notices.insert(0, new_notice)
    db["notices"] = notices
    save_database(db)

    flash(f"Notice '{new_id}' committed live into 'data.json'!", "success")
    return redirect(url_for("category_view", category_id=category))


# ---------------------------------------------------------------------------
# RBAC Delete Action: Notice Record Deletion
# ---------------------------------------------------------------------------
@app.route("/admin/delete-notice/<notice_id>", methods=["POST"])
@admin_required
def delete_notice(notice_id):
    """
    Administrative Delete Record Endpoint.
    Securely strips matching notice ID from the local JSON array file live.
    """
    db = load_database()
    notices = db.get("notices", [])

    target_notice = next((n for n in notices if n.get("id") == notice_id), None)
    if not target_notice:
        flash("Target record not found or already stripped.", "warning")
        return redirect(url_for("dashboard"))

    category_id = target_notice.get("category", "scholarships")
    updated_notices = [n for n in notices if n.get("id") != notice_id]
    db["notices"] = updated_notices
    save_database(db)

    flash(f"Record '{notice_id}' permanently stripped from data.json.", "danger")
    return redirect(url_for("category_view", category_id=category_id))


# ---------------------------------------------------------------------------
# LEVEL 3: Category Listings Feed ('category.html')
# ---------------------------------------------------------------------------
@app.route("/category/<category_id>")
@login_required
def category_view(category_id):
    """
    LEVEL 3: Category Listings Feed
    - Filtered dynamically for chosen track
    - Fast JavaScript string parsing live search
    - Dynamic Color Dot Verification Embed:
        🟢 Green Dot: Faculty / Dean / HOD authorized
        🟡 Yellow Dot: Crowdsourced CR / Student club
        🔴 Red Dot: Unconfirmed / Public entry
    - RBAC: 'Delete Record' button rendered ONLY for Admin
    """
    db = load_database()
    categories = db.get("categories", [])
    category_map = {c["id"]: c for c in categories}

    if category_id not in category_map:
        abort(404)

    current_category = category_map[category_id]
    filtered_notices = [n for n in db.get("notices", []) if n.get("category") == category_id]

    return render_template(
        "category.html",
        category=current_category,
        notices=filtered_notices
    )


# ---------------------------------------------------------------------------
# LEVEL 4: Deep Detailed Specification View ('detail.html')
# ---------------------------------------------------------------------------
@app.route("/notice/<notice_id>")
@login_required
def detail_view(notice_id):
    """
    LEVEL 4: Deep Detailed Specification View
    - Title, Description, Qualification Terms, Dates, Dynamic Package Value
    - Mapped Resolved Doubt Component:
        '📍 Concerned Authorities / Doubt Clearance Desk'
        ('Contact Registrar Office, Dean, or relevant HOD Section')
    - Dropdown Documents Checklist (dynamic soft green translucent glow)
    - Compact Action Row: '🌐 Forms Link Portal', '📅 Add Google Calendar', '💬 WhatsApp Share'
    """
    db = load_database()
    notices = db.get("notices", [])
    categories = db.get("categories", [])
    category_map = {c["id"]: c for c in categories}

    notice = next((n for n in notices if n.get("id") == notice_id), None)
    if not notice:
        abort(404)

    category = category_map.get(notice.get("category"), {
        "id": notice.get("category"),
        "name": notice.get("category", "General").capitalize(),
        "icon": "📌"
    })

    # Google Calendar Template URL Builder (Auto-populates deadline)
    def format_cal_date(date_str):
        try:
            dt = datetime.strptime(date_str, "%Y-%m-%d")
            return dt.strftime("%Y%m%d")
        except Exception:
            return "20261030"

    start_cal = format_cal_date(notice.get("starting_date", ""))
    end_cal = format_cal_date(notice.get("ending_date", ""))

    cal_params = {
        "action": "TEMPLATE",
        "text": f"[GNIOT Hub] {notice.get('title')}",
        "details": f"{notice.get('description')}\n\nAuthorities: {notice.get('concerned_authorities')}\nEligibility: {notice.get('eligibility')}",
        "location": notice.get("concerned_authorities", "GNIOT Campus, Greater Noida"),
        "dates": f"{start_cal}/{end_cal}"
    }
    google_calendar_url = f"https://calendar.google.com/calendar/render?{urllib.parse.urlencode(cal_params)}"

    # WhatsApp Click-to-Chat Share URL Builder
    live_notice_url = f"{request.host_url}notice/{notice.get('id')}"
    whatsapp_text = (
        f"📢 *GNIOT InfoHub Notification*\n\n"
        f"📌 *{notice.get('title')}*\n"
        f"🗓️ *Deadline:* {notice.get('ending_date')}\n"
        f"🏛️ *Authority Desk:* {notice.get('concerned_authorities')}\n"
        f"🛡️ *Status:* {notice.get('verification_label', 'Verified')}\n"
        f"🔗 *Notice Link:* {live_notice_url}"
    )
    whatsapp_url = f"https://api.whatsapp.com/send?text={urllib.parse.quote(whatsapp_text)}"

    # Determine if package value scale should be shown (Financial tracks)
    is_financial_track = (
        notice.get("category") in ["scholarships", "sip-tracker", "hackathons"]
        or bool(notice.get("reward_amount"))
    )

    return render_template(
        "detail.html",
        notice=notice,
        category=category,
        google_calendar_url=google_calendar_url,
        whatsapp_url=whatsapp_url,
        is_financial_track=is_financial_track
    )


# ---------------------------------------------------------------------------
# Error Handlers
# ---------------------------------------------------------------------------
@app.errorhandler(404)
def page_not_found(e):
    return render_template(
        "base.html",
        error_title="404 - Channel or Notice Not Found",
        error_message="The requested track or notice ID does not exist in local data.json."
    ), 404


@app.errorhandler(500)
def server_error(e):
    return render_template(
        "base.html",
        error_title="500 - Internal Server Error",
        error_message="An unexpected system condition occurred. Please retry or return to dashboard."
    ), 500


# ---------------------------------------------------------------------------
# Application Server Launch (Strictly Port 5010)
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("==========================================================")
    print(" [GNIOT Hub Platform] Ultra-Premium Console Active")
    print(" Running strictly on: http://127.0.0.1:5010")
    print(" Student Mode: username='student' | password='password'")
    print(" Admin Mode:   username='admin'   | password='adminpassword'")
    print("==========================================================")
    app.run(debug=True, port=5010)
