# InfoHub — Digital InfoHub for Centralized Campus Information and Student Engagement

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Flask 3.0](https://img.shields.io/badge/Flask-3.0-green.svg)](https://flask.palletsprojects.com/)
[![Bootstrap 5](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)](https://getbootstrap.com/)
[![Deployed on Vercel](https://img.shields.io/badge/Deployed%20with-Vercel-black.svg)](https://vercel.com)

**InfoHub** is an ultra-premium, centralized digital notice board and student engagement web platform designed for **Greater Noida Institute of Technology (GNIOT)**. The platform replaces fragmented WhatsApp circulars and physical bulletin boards with an atomic, glassmorphic campus portal.

---

## 📑 Core Documentation
* 📋 **[Product Requirements Document (PRD)](PRD.md)**: Vision, personas, functional requirements, and roadmap.
* 🛠️ **[Technical Requirements Document (TRD)](TRD.md)**: Architecture, data schema, security, routes, and serverless specs.

---

## ✨ Key Features
1. **Glassmorphic Cyber-Academic Design**: Full-bleed campus background, compact glass card, responsive dark/light mode.
2. **Academic Semester Tracking**: Capture & persist semester (1st through 8th Semester) during login/registration.
3. **Remember Me & Quick Sign-In**: Persistent local storage credentials for instant 1-click login with profile forget option.
4. **New Student Self-Registration**: Instant enrollment into `data.json["users"]` for new admissions.
5. **8 Core Academic Tracks**: Academic Notices, Examination Cell, Placement & Training, Events & Fests, Sports & Fitness, Clubs & Societies, Research & Innovation, Hostels & Transport.
6. **Official GNIOT Academic Calendar Session 2026-27 (Odd Sem)**: Embedded PDF viewer, high-res preview sheets, and timeline cutoffs.
7. **Role-Based Access Control (RBAC)**: Student (read-only) and Admin (notice authoring & deletion) profiles.

---

## 🚀 Quick Start (Local Run)

```bash
# Clone the repository
git clone https://github.com/suhaniisrivastava28/InfoHub---Digital-InfoHub-for-centralized-campus-information-and-student-engagement.git
cd InfoHub---Digital-InfoHub-for-centralized-campus-information-and-student-engagement

# Install dependencies
pip install -r requirements.txt

# Run the server
python app.py
```
Open **`http://127.0.0.1:5010`** in your browser.

### Default Credentials:
- **Student Profile**: `student` / `password`
- **Admin Profile**: `admin` / `adminpassword`

---

## 🌐 Cloud Deployment (Vercel)
Configured for zero-config serverless deployment via `vercel.json` and `@vercel/python`:
```bash
npm install -g vercel
vercel --prod
```
