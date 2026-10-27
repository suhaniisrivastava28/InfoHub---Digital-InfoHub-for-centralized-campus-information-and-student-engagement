import json

db_path = r"C:\Users\Suhani Srivastava\.gemini\antigravity\scratch\InfoHub\data.json"
with open(db_path, "r", encoding="utf-8") as f:
    db = json.load(f)

# Ensure no duplicate IDs if re-run
existing_ids = {n["id"] for n in db.get("notices", [])}

new_notices = [
    {
        "id": "SEM-2026-03",
        "category": "seminars",
        "title": "IDS & CareerXel – Emerging Technology Workshop Series 2026",
        "description": "Comprehensive online emerging technology workshop series focusing on Artificial Intelligence (AI), Cybersecurity, Blockchain Technology, Product Management, and Industry & Career Guidance. Learn directly from industry experts, gain practical insights, develop future-ready skills, and earn a Blockchain-Verified Certificate.",
        "eligibility": "Open to all enrolled students across all branches and academic years. Free registration.",
        "starting_date": "2026-10-26",
        "ending_date": "2026-10-30",
        "reward_amount": "Free Registration + Blockchain-Verified Certificate",
        "concerned_authorities": "IDS & CareerXel Industry Partnership Desk / GNIOT Training & Placement Cell",
        "verification_level": "official",
        "verification_label": "🟢 Officially Authorized (Faculty / Dean / HOD)",
        "submission_type": "Online Track",
        "official_url": "https://careerxel.com",
        "required_documents": [
            "GNIOT Student ID Card",
            "Registered Email for Online Portal Access"
        ],
        "timing": "4:00 PM – 6:00 PM IST (Monday to Friday)",
        "venue": "Online Virtual Classroom"
    },
    {
        "id": "HAK-2026-02",
        "category": "hackathons",
        "title": "SHE INNOVATES 2.0 - IDEATHON (She Ideates | She Presents | She Wins)",
        "description": "Inter-College Idea Competition organized exclusively for female students by WISE Society of Greater Noida Institute of Technology. Teams of 1 to 2 members present original and innovative solutions with a max 8-slide PPT covering Problem, Solution, Technology & Outcome (5 min presentation + 2 min Q&A). Organized under the leadership of Prof. (Dr.) Dhiraj Gupta (Director), Prof. (Dr.) Seema Arora (President-WISE, HOD EE), and Dr. Monika Dixit (Vice President-WISE).",
        "eligibility": "Exclusively for Female Students from Any College / Branch / Year. Teams of 1 to 2 members.",
        "starting_date": "2026-09-10",
        "ending_date": "2026-09-18",
        "reward_amount": "Prizes for Winners + Official Certificates for All Participants",
        "concerned_authorities": "Team WISE, GNIOT (Innovation Centre & Department of Electrical Engineering)",
        "verification_level": "official",
        "verification_label": "🟢 Officially Authorized (Faculty / Dean / HOD)",
        "submission_type": "Physical Track",
        "official_url": "https://forms.gle/1wALrvDQaQyizBW2A",
        "poster_image": "she_innovates_poster.png",
        "required_documents": [
            "College Student ID Card (Female Students Only)",
            "Max 8 Slides PPT (Problem, Solution, Technology, Outcome)",
            "Google Form Registration Confirmation"
        ],
        "timing": "23rd September 2026, 9:00 AM Onwards",
        "venue": "Innovation Centre, GNIOT"
    },
    {
        "id": "EVT-2026-02",
        "category": "events",
        "title": "Blood Donation Camp 2026 - Social Club GNIOT & Rotary Club",
        "description": "Life-saving blood donation camp organized by The Social Club of GNIOT in association with Rotary Club. Staff, faculty members, and students from B.Tech 132 and all campus departments are encouraged to register and step forward. Donors will be provided official attendance in lieu of their presence in the camp. 'Your Blood Can Be Someone's Lifeline — Be a Hero, Donate Today!'",
        "eligibility": "Open to all staff, faculty members, and students (B.Tech 132 & all branches). Donors must be 18+ and medically eligible.",
        "starting_date": "2026-09-12",
        "ending_date": "2026-09-22",
        "reward_amount": "Donor Honor Certificate, Refreshments & Official Attendance Waiver",
        "concerned_authorities": "The Social Club of GNIOT & Rotary Club Liaison Desk (GIPS Seminar Wing)",
        "verification_level": "official",
        "verification_label": "🟢 Officially Authorized (Faculty / Dean / HOD)",
        "submission_type": "Physical Track",
        "official_url": "https://docs.google.com/forms/d/e/1FAIpQLSe6ZcSS64K2-mk5Hd1RaavlkY94-eT5f4o3jaCnS-vZ6N-hmA/viewform?usp=publish-editor",
        "poster_image": "blood_donation_poster.png",
        "required_documents": [
            "GNIOT Student / Staff ID Card",
            "Aadhaar / Government Photo ID",
            "Camp Registration Form"
        ],
        "timing": "22nd September 2026 (Tuesday), 10:00 AM to 3:30 PM",
        "venue": "Seminar Hall, GIPS"
    },
    {
        "id": "SIP-2026-02",
        "category": "sip-tracker",
        "title": "Industrial Visit at Microsoft India - Sovereign Capital Sector 16A Noida",
        "description": "The Department of Computer Science & Engineering, in collaboration with GNIOT CSE Tech Club, is pleased to announce an exclusive industrial visit to Microsoft India. Experience the professional corporate environment of a global technology leader, gain direct industry exposure, and understand enterprise cloud & software architectures.",
        "eligibility": "Exclusively for 2nd & 3rd Year CSE Students. Strictly limited to 50 participants (selection based on registration details).",
        "starting_date": "2026-07-28",
        "ending_date": "2026-08-06",
        "reward_amount": "Corporate Industry Exposure & Official Visit Participation Certificate",
        "concerned_authorities": "Department of Computer Science & Engineering & GNIOT CSE Tech Club",
        "verification_level": "official",
        "verification_label": "🟢 Officially Authorized (Faculty / Dean / HOD)",
        "submission_type": "Physical Track",
        "official_url": "https://forms.gle/VaqXcrJ5tMG77xAC9",
        "required_documents": [
            "CSE Student ID Card (2nd or 3rd Year)",
            "Parental Consent Letter",
            "Departmental Bonafide Clearance"
        ],
        "timing": "8th August 2026 (Saturday) | Visit: 10:00 AM – 12:00 PM | Reporting: 9:00 AM at Campus",
        "venue": "Microsoft Sovereign Capital Sector 16A, Noida (College Bus Facility Provided)"
    },
    {
        "id": "HAK-2026-03",
        "category": "hackathons",
        "title": "SIH 2026 – Internal Smart India Hackathon at GNIOT (Think. Build. Innovate. Compete.)",
        "description": "Internal qualification hackathon for Smart India Hackathon (SIH 2026) organized by the Department of Computer Science & Engineering & GNIOT-CSE Tech Club. Participating teams showcase innovative technical prototypes, embedded engineering, and software architectures to secure official institutional nomination for the national Smart India Hackathon.",
        "eligibility": "All participating B.Tech / CSE teams registered for Smart India Hackathon 2026. Teams of 6 members including at least one female teammate.",
        "starting_date": "2026-08-25",
        "ending_date": "2026-09-12",
        "reward_amount": "Official GNIOT Nomination for National SIH 2026 + Institutional Grants",
        "concerned_authorities": "Department of Computer Science & Engineering & GNIOT-CSE Tech Club",
        "verification_level": "official",
        "verification_label": "🟢 Officially Authorized (Faculty / Dean / HOD)",
        "submission_type": "Physical Track",
        "official_url": "https://gniotgroup.edu.in",
        "poster_image": "sih_2026_poster.png",
        "required_documents": [
            "SIH 2026 Idea Presentation PPT",
            "Team Member GNIOT ID Cards",
            "Working Prototype / GitHub Repository"
        ],
        "timing": "12th September 2026, 10:00 AM Onwards",
        "venue": "Department of CSE, GNIOT"
    }
]

# Insert items that are not already present
for n in reversed(new_notices):
    if n["id"] not in existing_ids:
        db["notices"].insert(0, n)

with open(db_path, "w", encoding="utf-8") as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print(f"Successfully processed notices! Total notices now: {len(db['notices'])}")
