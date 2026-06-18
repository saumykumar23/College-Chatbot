from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

faqs = {
    # Basic Info
    "about": "Brainware University is a UGC-recognized private university established in 2016 under The Brainware University Act, 2015. It is the largest private university in West Bengal with 19,000+ students and 36 years of academic excellence.",
    "address": "Barasat Campus: 398, Ramkrishnapur Road, Barasat, Near Jagadighata Market, Kolkata, West Bengal 700125. Salt Lake Campus: Y8, EP Block, Sector V, Bidhannagar, Kolkata 700091.",
    "contact": "📞 Admission: 70031 62601 | Academics: 33 6901 0507 | 📧 info@brainwareuniversity.ac.in | 🌐 www.brainwareuniversity.ac.in",
    "location": "Brainware University is located at Barasat, Kolkata, West Bengal. It also has a Salt Lake Campus in Sector V, Bidhannagar.",

    # Admission
    "admission": "Admissions are open for 2026-27! Steps: 1) Apply Online & take Brainware Entrance Test (BET) 2) Submit documents via email/WhatsApp 3) Pay fees via NEFT/IMPS/UPI 4) Fill Anti-Ragging form 5) Receive Admission Letter. Apply at: brainwareuniversity.ac.in/apply-now.php",
    "apply": "Apply online at brainwareuniversity.ac.in/apply-now.php. Early Bird Offer available — Up to ₹30,000 off on select courses for a limited period!",
    "eligibility": "Eligibility varies by program. Check at brainwareuniversity.ac.in/bwu-eligibility. Generally 60%+ in qualifying exam is required.",
    "document": "Required documents: Submit via email or WhatsApp to the Admission Cell after qualifying the entrance test.",

    # Fees & Scholarship
    "fees": "Course fees vary by program. Visit brainwareuniversity.ac.in/course-fees for details. Early Bird Offer: Up to ₹30,000 off available now!",
    "scholarship": "Multiple scholarships available: 1) Vidyalankar: 90-95% → 50% fee waiver, 95%+ → 100% fee waiver. 2) Merit Scholarship for 60%+ students. 3) Sports Scholarship: International medalists get 100% waiver. 4) Govt schemes: Swami Vivekananda, Aikyashree, Student Credit Card. Total ₹30 Cr+ scholarships awarded!",

    # Courses
    "course": "70+ programs offered across 9 schools: Engineering, Computational Sciences, Biotechnology, Medical & Allied Health, Agriculture, Management & Commerce, Law, Multimedia & Film Studies, Humanities & Social Sciences.",
    "engineering": "B.Tech programs: CSE, AI & ML, AI & Robotics, Cyber Security, Data Science & AI. M.Tech: CSE, Data Science, AI & ML, Robotics & Automation. Also PhD and Diploma programs available.",
    "bca": "BCA, BCA AI & ML, BSc Advanced Networking & Cyber Security available. Postgraduate: MCA, MSc ANCS, MSc Mathematics.",
    "mba": "MBA, MBA Hospital Management available. Also BBA, BBA Business Analytics, BBA Digital Marketing, BBA Hospital Management, B.Com.",
    "medical": "Programs: Medical Lab Science, BMRIT, Pharmacy, Nursing, Physiotherapy, Optometry, Nutrition & Dietetics, Critical Care Technology, and more.",
    "law": "Programs: LLB, BBA LLB, BA LLB, LLM. PhD in Law also available.",

    # Placement
    "placement": "98% placement record! 1,000+ global recruiters. Highest CTC: ₹36+ LPA. Average CTC: ₹4 LPA. 1,300+ selections in 2025. Top recruiters: Amazon, TCS, Cognizant, Wipro, EY, PwC, Apollo Hospitals, Swiggy.",
    "recruiter": "Top recruiters include Amazon, TCS, Cognizant, Wipro, EY, PwC, Apollo Hospitals, Swiggy, Infosys, Berger Paints, JUSPAY, Nomura Research Institute, Telaverge, The Blue Flame Labs and 1000+ more!",
    "internship": "Internship opportunities available. Visit brainwareuniversity.ac.in/internship for details.",
    "package": "Highest CTC: ₹36+ LPA. Average CTC: ₹4 LPA. Recent placements: B.Tech CSE at ₹12 LPA, CSE AIML at ₹11 LPA, TCS Prime at ₹9 LPA.",

    # Rankings & Recognition
    "ranking": "IIRF 2026: No.1 Liberal University in WB, No.1 Engineering College under Private University in WB, No.2 New Age Private University in WB. Also ranked among Top 100 Universities in India by Times Higher Education Impact Rankings.",
    "recognition": "Recognized by UGC, AIU, PCI (Pharmacy), INC (Nursing), BCI (Law), MSME, ACU, DSIR (SIRO), Cyber Safe Bengal, Department of Health & Family Welfare.",
    "award": "Times Group Awards: Best Institute in Engineering (Placement), Best Institute in MBA Education. Also received ABP Ananda Shiksha Samman and Zee 24 Ghanta Education Excellence award.",

    # Infrastructure
    "library": "Library facility available with digital access. Visit brainwareuniversity.ac.in/library-info for details.",
    "lab": "Advanced laboratories including AI labs, engineering labs, biotech labs, medical labs, and more with industry-grade equipment.",
    "hostel": "Hostel available for boys and girls. Rules at brainwareuniversity.ac.in/download/HostelRulesRegulations2024-25.pdf. Contact admission cell for fees.",
    "campus": "36-acre campus at Barasat with modern infrastructure, WiFi, canteen, sports facilities, clubs and more. Also Salt Lake Campus in Sector V.",
    "sports": "Sports and fitness facilities available on campus including Fit India Club activities.",

    # Clubs & Activities
    "club": "13+ student clubs: AI Club, Tech Club, Eco Club, Photo Club, Music Club, Fit India Club, Fashion Club, Dance Club, Cyber Club, Media Club, Cine Club, Art Club, Drama Club.",
    "event": "Regular events, fests, hackathons, and activities organized. Monthly newsletter, news & events at brainwareuniversity.ac.in/news-events.",
    "nss": "NSS (National Service Scheme) active at Brainware University. Visit brainwareuniversity.ac.in/nss for details.",

    # Research
    "research": "Strong R&D: 2165+ research papers, 962+ book chapters, 266+ books, 354+ patents, 51+ consultancy projects, 29+ government projects. Ranked DSIR-SIRO institution.",
    "phd": "PhD programs available in CSE, ECE, CS, Mathematics, Biotech, Law, Management, Commerce, Hospital Management, Pharmacy, English and more.",

    # International
    "international": "International collaborations with Livingstone College USA, Sejong University South Korea, Hanyang University South Korea, Kasama University College Zambia, and INTA.",

    # Contact & Support
    "helpline": "Student helpline available at brainwareuniversity.ac.in/helpline.php. Admission: 📞 70031 62601",
    "website": "Official website: www.brainwareuniversity.ac.in | Apply: brainwareuniversity.ac.in/apply-now.php | Exams: brainwareuniversity.ac.in/examresult.php",
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message'].lower()

    # Greetings
    greetings = ["hello", "hi", "hey", "namaste", "good morning", "good evening", "good afternoon"]
    if any(g in user_message for g in greetings):
        return jsonify({"reply": "👋 Hello! Welcome to Brainware University Chatbot! I can help you with admissions, courses, fees, placement, scholarships and more. How can I assist you today?"})

    # Thanks
    thanks = ["thank", "thanks", "thankyou", "great", "awesome", "perfect", "helpful"]
    if any(t in user_message for t in thanks):
        return jsonify({"reply": "😊 You're welcome! Feel free to ask anything else about Brainware University. We're here to help!"})

    # FAQ matching
    for keyword, answer in faqs.items():
        if keyword in user_message:
            return jsonify({"reply": answer})

    # Default
    return jsonify({"reply": "🤔 I don't have that specific information right now. Please contact us directly: 📞 70031 62601 | 📧 info@brainwareuniversity.ac.in | 🌐 www.brainwareuniversity.ac.in"})

if __name__ == '__main__':
    app.run(debug=True)