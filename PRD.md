# Product Requirements Document (PRD)

## Project Title
**InfoHub — Digital InfoHub for Centralized Campus Information and Student Engagement**

---

## 1. Executive Summary
**InfoHub** is an ultra-premium, centralized digital notice board and student engagement web platform designed specifically for Greater Noida Institute of Technology (GNIOT). The platform replaces chaotic physical bulletin boards, fragmented WhatsApp class groups, and clunky legacy ERP interfaces with a real-time, interactive, glassmorphic campus portal. 

InfoHub empowers students to instantly view categorized notices, track official academic calendars, engage with events through dynamic registration links, and bookmark critical circulars, while giving administrators and department heads a secure, streamlined interface for broadcasting verifiable campus communications.

---

## 2. Problem Statement
1. **Notice Fragmentation & Noise**: Important announcements (exam dates, fee submission deadlines, campus placements, hackathons) are scattered across WhatsApp channels, unofficial Telegram groups, and physical departmental notice boards.
2. **Missing Time-Sensitive Deadlines**: Students frequently miss registration deadlines or examination form submission cutoffs due to lack of real-time visibility and clear visual prioritization.
3. **Information Asymmetry**: Juniors, new semester entrants, and transfer students struggle to find unified academic calendars, semester-wise notices, and official college circulars.
4. **Poor Student User Experience**: Traditional university ERP systems are cumbersome, slow, mobile-unfriendly, and fail to engage modern digital-native students.

---

## 3. Product Vision & Goals
* **Single Source of Truth**: Centralize 100% of campus notices, official posters, circulars, and academic calendars under one unified portal.
* **Streamlined Student Access**: Fast, friction-free login with persistent authentication ("Remember Me"), semester-level personalization, and instant zero-friction registration for new students.
* **Categorized Intelligence**: 8 distinct campus channels (Scholarships, Events, Holidays, Seminars, SIP Tracker, Orientation, Hackathons, Placements).
* **Role-Based Governance**: Strict segregation between administrative notice broadcast authorities and student read/engagement access.
* **Modern Aesthetic**: Glassmorphic, dark/light responsive cyber-academic visual architecture adhering to university design standards.

---

## 4. User Personas

### Persona A: Regular Student (Aarav, 3rd Year B.Tech CSE)
* **Needs**: Needs to check upcoming mid-term exam dates, register for technical hackathons (e.g., SHE INNOVATES 2.0, SIH 2026), and download the official academic calendar.
* **Pain Points**: Overwhelmed by spam in informal WhatsApp groups; fears missing critical AKTU / GNIOT exam schedules.
* **InfoHub Solution**: 1-click Quick Login with saved semester profile, filtered examination track, visual countdowns, and direct registration links.

### Persona B: New / First-Year Student (Riya, 1st Year B.Tech)
* **Needs**: Quickly onboard to the university portal, find induction details, syllabus schedules, club orientations, and contact points.
* **Pain Points**: Does not have college ERP credentials immediately upon joining; feels isolated from campus activities.
* **InfoHub Solution**: Self-service student registration tab with semester selector and instant access to campus life tracks.

### Persona C: Department Head / Admin (Dr. Sharma, Head of Academics)
* **Needs**: Publish verified circulars with deadline dates, category tags, urgency badges (High/Medium/Low), and poster attachments.
* **Pain Points**: Physical notice boards get defaced; circulating PDFs manually via staff is unreliable.
* **InfoHub Solution**: Protected administrative dashboard with instant notice creation, edit, and deletion capabilities.

---

## 5. Functional Requirements & Feature Matrix

| Feature ID | Feature Name | Description | Priority |
| :--- | :--- | :--- | :--- |
| **FR-01** | **Campus Themed Authentication** | Full-bleed edge-to-edge campus background, compact glassmorphic login card, light/dark mode compatibility. | P0 (Must Have) |
| **FR-02** | **Semester Selection** | Dropdown selection (1st through 8th Semester) captured during login and registration, displayed across dashboard badges. | P0 (Must Have) |
| **FR-03** | **Remember Me & Quick Login** | Persistent client-side session caching with 1-click instant login banner and profile forget button. | P0 (Must Have) |
| **FR-04** | **New Student Registration** | Dedicated self-registration tab validating Student ID, Full Name, Password, and Semester with instant credential enrollment. | P0 (Must Have) |
| **FR-05** | **8 Campus Notice Tracks** | Dedicated channels: Scholarships, Events, Holidays, Seminars, SIP Tracker, Orientation, Hackathons, Placements. | P0 (Must Have) |
| **FR-06** | **Search & Real-time Filter** | Interactive client-side live keyword search, urgency filter (Urgent/Normal), and category pill filters. | P0 (Must Have) |
| **FR-07** | **Interactive Academic Calendar** | Embedded PDF viewer for official GNIOT Academic Calendar Session 2026-27 (Odd Sem), multi-page image viewports, and timeline milestones. | P0 (Must Have) |
| **FR-08** | **Role-Based Access Control (RBAC)**| Protected session routing: Student (`student`/`password`), Admin (`admin`/`adminpassword`). Only Admin can post/delete notices. | P0 (Must Have) |
| **FR-09** | **Notice Detail & Poster Viewer** | Dedicated notice view with high-res poster displays (IDS Workshop, SHE INNOVATES, Blood Donation, SIH), actionable registration URLs, and social share links. | P1 (High) |
| **FR-10** | **Analytics & Engagement Metrics** | Metric cards displaying Total Published Notices, Active Categories, Upcoming Deadlines, and User Engagement counts. | P1 (High) |

---

## 6. Non-Functional Requirements (NFRs)
1. **Performance**: Page load under 1.2s; instant client-side filtering without page reloads.
2. **Responsiveness**: Fluid layout across all devices (Mobile 320px+, Tablet 768px+, Desktop 1080p+).
3. **Reliability & Availability**: 99.9% uptime powered by serverless infrastructure on Vercel.
4. **Security**: Session-based encryption (`Flask.secret_key`), CSRF mitigation, sanitized form input, and strict route-level decorators (`@login_required`, `@admin_required`).
5. **Portability**: Self-contained JSON atomic datastore eliminating database server overhead for zero-maintenance campus deployments.

---

## 7. Release Milestones & Roadmap
* **v1.0 (Current MVP)**: Complete glassmorphic web portal, 8 notice categories, semester-aware authentication, GNIOT Odd Semester 2026-27 Academic Calendar integration, Vercel serverless deployment.
* **v2.0 (Planned)**: Push notifications via WebSockets / Firebase Cloud Messaging, student club application forms, automated Telegram bot notification bridge.
* **v3.0 (Future)**: AKTU Result integration API and AI-powered notice summarizer and exam reminder bot.
