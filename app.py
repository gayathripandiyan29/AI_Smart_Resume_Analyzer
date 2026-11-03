import streamlit as st
import pdfplumber
import pandas as pd
import re
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os

st.set_page_config(
    page_title="AI Smart Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)

st.image("logo.png", width=180)
st.markdown("""
<div style="
background: linear-gradient(90deg,#4CAF50,#2196F3);
padding:25px;
border-radius:15px;
text-align:center;
color:white;
box-shadow:0 4px 10px rgba(0,0,0,0.2);
">

<h1>🤖 AI SMART RESUME ANALYZER</h1>

<h4>AI-Powered Resume Analysis & Career Guidance</h4>

<p>
ATS Score • Tech Score • Career Prediction • AI Feedback • Learning Roadmap
</p>

</div>
""", unsafe_allow_html=True)

st.write("")
st.markdown("### 📂 Upload Your Resume")

uploaded_file = st.file_uploader(
    "",
    type=["pdf"],
    help="Upload your resume in PDF format"
)

if uploaded_file is not None:

    st.success("✅ Resume Uploaded Successfully!")

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text

    resume_text = text.lower()

    st.subheader("📄 Resume Preview")
    st.text_area("Resume Content", text, height=250)

    with st.sidebar:
        st.title("🤖 AI Smart Resume Analyzer")

        st.markdown("---")

        st.subheader("📋 Features")

        st.write("🎯 ATS Score")
        st.write("💻 Tech Score")
        st.write("🗣 Communication Score")
        st.write("📄 Resume Health Report")
        st.write("⭐ Resume Rating")
        st.write("🏆 Resume Grade")
        st.write("📈 Overall Status")
        st.write("📊 Resume Completeness")
        st.write("📉 Skill Gap Analysis")
        st.write("🛣 Learning Roadmap")
        st.write("🤖 AI Feedback")
        st.write("💼 Career Suggestion")
        st.write("💰 Salary Prediction")
        st.write("🎤 Interview Questions")
        st.write("📚 Course Recommendation")
        st.write("🚀 Project Recommendation")
        st.write("📥 Download Report")

        st.markdown("---")
        st.success("✨ AI Powered Resume Analysis")
        st.markdown("---")

        st.subheader("ℹ️ About")

        st.info("""
        🤖 AI Smart Resume Analyzer helps users analyze resumes using AI.

        ✅ ATS Score
        ✅ Tech Score
        ✅ Communication Score
        ✅ Career Suggestion
        ✅ Learning Roadmap
        ✅ Professional PDF Report
        """)
  # ---------------- Skills Database ----------------
    skills = pd.read_csv("skills.csv", header=None)

    skills_list = skills[0].tolist()

    matched_skills = []

    for skill in skills_list:

        if skill.lower() in resume_text:

            matched_skills.append(skill)

    st.subheader("✅ Matched Skills")

    if matched_skills:

        for skill in matched_skills:
            st.success(skill)
    else:

        st.error("No Skills Matched")
 # ---------------- ATS Score ----------------

    total_skills = len(skills_list)

    matched_count = len(matched_skills)

    ats_score = (matched_count / total_skills) * 100

    st.subheader("📊 ATS Score")

    st.progress(int(ats_score))

    st.write(f"### {ats_score:.2f}%")
 # ---------------- Missing Skills ----------------
    missing_skills = []

    for skill in skills_list:

        if skill not in matched_skills:

            missing_skills.append(skill)

    st.subheader("❌ Missing Skills")

    if missing_skills:

        for skill in missing_skills:

            st.warning(skill)
    else:

        st.success("No Missing Skills 🎉")
# ---------------- Tech Score ----------------
    tech_skills = [
        "Python", "SQL", "Machine Learning",
        "Deep Learning", "Pandas", "NumPy",
        "Java", "C", "C++", "HTML",
        "CSS", "JavaScript", "Git", "GitHub"
    ]
    matched_tech = 0

    for skill in tech_skills:
        if skill in matched_skills:
            matched_tech += 1

    tech_score = (matched_tech / len(tech_skills)) * 100
 # ---------------- Communication Score ----------------

    communication_words = [
        "communication",
        "leadership",
        "team",
        "presentation",
        "collaboration"
    ]

    comm_count = 0

    for word in communication_words:
        if word.lower() in resume_text:
            comm_count += 1

    communication_score = (comm_count / len(communication_words)) * 100

    # ---------------- Career Variable ----------------

    if "Machine Learning" in matched_skills and "Python" in matched_skills:
        career = "AI / ML Engineer"

    elif "Python" in matched_skills and "Data Analysis" in matched_skills:
        career = "Data Analyst"

    elif "SQL" in matched_skills and "Excel" in matched_skills:
        career = "Business Analyst"

    elif "Java" in matched_skills:
        career = "Java Developer"

    elif "HTML" in matched_skills and "CSS" in matched_skills:
        career = "Frontend Developer"

    else:
        career = "Keep Improving Your Skills"
 # ---------------- Dashboard&overall scre ----------------
    overall_score = (
                            ats_score +
                            tech_score +
                            communication_score
                    ) / 3

    col1, col2, col3,col4= st.columns(4)

    with col1:
        st.info("📊 ATS SCORE")
        st.metric("", f"{ats_score:.2f}%")
        st.progress(int(ats_score))

    with col2:
        st.info("💻 TECH SCORE")
        st.metric("", f"{tech_score:.2f}%")
        st.progress(int(tech_score))

    with col3:
        st.info("🗣 COMMUNICATION")
        st.metric("", f"{communication_score:.2f}%")
        st.progress(int(communication_score))
    with col4:
            st.info("⭐ OVERALL SCORE")
            st.metric("", f"{overall_score:.2f}%")
            st.progress(int(overall_score))
 # ---------------- AI Feedback ----------------

    st.subheader("🤖 AI Feedback")

    if overall_score >= 80:
        st.success("Excellent Resume! Your resume is ready for most technical roles.")
    elif overall_score >= 60:
        st.info("Good Resume. Add a few more skills and projects to improve.")
    else:
        st.warning("Your resume needs improvement. Focus on technical skills and projects.")
    # ---------------- Resume Strengths & Weaknesses ----------------
    st.subheader("💪 Resume Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.success("💪 Resume Strengths")

        if ats_score >= 80:
            st.write("✅ Strong technical skill profile")

        if len(matched_skills) >= 5:
            st.write("✅ Multiple relevant skills found")

        if communication_score >= 60:
            st.write("✅ Good communication keywords")

    with col2:
        st.error("⚠ Areas to Improve")

        if missing_skills:
            for skill in missing_skills:
                st.write(f"❌ {skill}")
        else:
            st.write("🎉 No missing skills found")
 #---------------- Resume Rating ----------------

    st.subheader("⭐ Resume Rating")

    if overall_score >= 90:
        rating = "⭐⭐⭐⭐⭐"
    elif overall_score >= 80:
        rating = "⭐⭐⭐⭐☆"
    elif overall_score >= 70:
        rating = "⭐⭐⭐☆☆"
    elif overall_score >= 60:
        rating = "⭐⭐☆☆☆"
    else:
        rating = "⭐☆☆☆☆"

    st.write(rating)
 # ---------------- Resume Grade ----------------

    st.subheader("🏆 Resume Grade")

    if overall_score >= 90:
        grade = "A+"
    elif overall_score >= 80:
        grade = "A"
    elif overall_score >= 70:
        grade = "B+"
    elif overall_score >= 60:
        grade = "B"
    elif overall_score >= 50:
        grade = "C"
    else:
        grade = "D"

    st.success(grade)
 # ---------------- Overall Status ----------------
    st.subheader("📈 Overall Status")

    if overall_score >= 85:
        st.success("🟢 EXCELLENT")
    elif overall_score >= 70:
        st.info("🟡 GOOD")
    elif overall_score >= 50:
        st.warning("🟠 AVERAGE")
    else:
        st.error("🔴 NEEDS IMPROVEMENT")
 # ---------------- Estimated Salary & career sugges ----------------
    st.subheader("🎯 Career Insights")

    col1, col2 = st.columns(2)

    with col1:
        st.success("🎯 Recommended Career")
        st.markdown(f"## {career}")

    with col2:

        if overall_score >= 90:
            salary = "₹10 LPA - ₹15 LPA"
        elif overall_score >= 75:
            salary = "₹7 LPA - ₹10 LPA"
        elif overall_score >= 60:
            salary = "₹5 LPA - ₹7 LPA"
        elif overall_score >= 40:
            salary = "₹3 LPA - ₹5 LPA"
        else:
            salary = "₹2 LPA - ₹3 LPA"

        st.info("💰 Estimated Salary")
        st.markdown(f"## {salary}")
# ---------------- Contact Details ----------------

    st.subheader("📞 Contact Details")

    email = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)

    phone = re.findall(r'\+?\d[\d\s-]{8,}\d', text)

    linkedin = re.findall(r'https?://(?:www\.)?linkedin\.com/\S+', text)

    github = re.findall(r'https?://(?:www\.)?github\.com/\S+', text)

    st.write("📧 Email :", email[0] if email else "Not Found")
    st.write("📱 Phone :", phone[0] if phone else "Not Found")
    st.write("💼 LinkedIn :", linkedin[0] if linkedin else "Not Found")
    st.write("💻 GitHub :", github[0] if github else "Not Found")

 # ---------------- Resume Completeness ----------------
    st.subheader("📋 Resume Completeness")

    sections = {
        "Education": ["education", "college", "university", "degree"],
        "Skills": ["skills"],
        "Projects": ["project"],
        "Experience": ["experience", "internship"],
        "Certifications": ["certificate", "certification"],
        "Email": ["@"],
        "Phone": ["phone", "mobile"]
    }

    completed = 0

    for section, keywords in sections.items():

        found = any(keyword.lower() in resume_text for keyword in keywords)

        if found:
            st.success(f"✅ {section}")
            completed += 1
        else:
            st.error(f"❌ {section}")

    completeness_score = (completed / len(sections)) * 100

    st.write(f"### Resume Completeness : {completeness_score:.2f}%")
    # ---------------- Course Map ----------------

    course_map = {
        "Power BI": "Microsoft Power BI",
        "SQL": "Advanced SQL",
        "Machine Learning": "Machine Learning with Scikit-Learn",
        "Git": "Git & GitHub",
        "AWS": "AWS Cloud Practitioner"
    }
    # ---------------- Project Map ----------------

    project_map = {
        "Power BI": "Sales Dashboard",
        "Machine Learning": "House Price Prediction",
        "SQL": "Student Database System",
        "Git": "GitHub Portfolio",
        "AWS": "Deploy Python Project on AWS"
    }

# ---------------- Course & prj Recommendations ----------------
    st.subheader("📚 Learning Resources")

    col1, col2 = st.columns(2)

    with col1:
        st.info("📚 Recommended Courses")

        found_course = False

        for skill in missing_skills:
            if skill in course_map:
                st.write(f"📘 {course_map[skill]}")
                found_course = True

        if not found_course:
            st.success("✅ No course recommendations. Great profile!")

    with col2:
        st.success("🚀 Recommended Projects")

        found_project = False

        for skill in missing_skills:
            if skill in project_map:
                st.write(f"🚀 {project_map[skill]}")
                found_project = True

        if not found_project:
            st.success("Build more advanced AI projects.")
 # ---------------------- Learning Roadmap ----------------------
    st.subheader("🎯 Learning Roadmap")

    roadmap = [
        "📘 Week 1 : Learn Advanced Python",
        "🗄️ Week 2 : Master SQL",
        "🐼 Week 3 : Practice Pandas & NumPy",
        "📊 Week 4 : Learn Power BI",
        "🤖 Week 5 : Study Machine Learning",
        "🚀 Week 6 : Build Real-Time Projects"
    ]

    for step in roadmap:
        st.success(step)
# ---------------------- AI Resume Summary ----------------------

    st.subheader("🤖 AI Resume Summary")

    summary = f"""
    Your resume demonstrates a strong foundation for Data Analytics and AI roles.

    📊 ATS Score            : {ats_score:.2f}%
    💻 Tech Score           : {tech_score:.2f}%
    🗣 Communication Score  : {communication_score:.2f}%

    Your strengths include the matched technical skills in your resume.
    To improve your profile further, focus on learning the missing skills,
    earning certifications, and building more real-world projects.
    """

    st.info(summary)

 # ---------------------- AI Interview Questions ----------------------

    st.subheader("🎤 AI Interview Questions")

    questions = [
        "Tell me about yourself.",
        "Explain the projects you have worked on.",
        "What is Machine Learning?",
        "Explain the difference between SQL JOIN and UNION.",
        "Why do you want this job?",
        "What are your strengths and weaknesses?",
        "Explain your final year project.",
        "How do you handle challenges in a team?",
        "Why should we hire you?",
        "Where do you see yourself in 5 years?"
    ]

    for q in questions:
        st.write("✅", q)

 # ---------------------- Resume Improvement Suggestions ----------------------

    st.subheader("💡 Resume Improvement Suggestions")

    if len(missing_skills) > 0:
        for skill in missing_skills:
            st.warning(f"Learn {skill}")

    st.success("✔ Add more real-time projects.")
    st.success("✔ Add certifications.")
    st.success("✔ Keep your GitHub updated.")
    st.success("✔ Customize your resume for each job.")
    import matplotlib.pyplot as plt

    st.subheader("📊 Performance Chart")

    labels = ["ATS", "Tech", "Communication"]
    scores = [ats_score, tech_score, communication_score]

    fig, ax = plt.subplots()

    ax.bar(labels, scores)

    ax.set_ylim(0, 100)

    ax.set_ylabel("Score")

    st.pyplot(fig)
    if overall_score >= 85:
        status = "EXCELLENT"
    elif overall_score >= 70:
        status = "GOOD"
    elif overall_score >= 50:
        status = "AVERAGE"
    else:
        status = "NEEDS IMPROVEMENT"
    st.subheader("📥 Download Report")

    report = f"""
    AI RESUME ANALYZER REPORT

    Career Suggestion : {career}

    ATS Score : {ats_score:.2f}%
    Tech Score : {tech_score:.2f}%
    Communication Score : {communication_score:.2f}%

    Resume Grade : {grade}
    Overall Status : {status}

    Matched Skills:
    {matched_skills}

    Missing Skills:
    {missing_skills}
    """
    # ---------------- Professional PDF Report ----------------

    from reportlab.platypus import (
        SimpleDocTemplate,
        Paragraph,
        Spacer,
        Table,
        TableStyle
    )

    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.enums import TA_CENTER
    from reportlab.lib.units import inch

    st.subheader("📄 Download Professional PDF Report")

    if st.button("📥 Generate Professional PDF"):
        pdf_file = "AI_Smart_Resume_Report.pdf"

        doc = SimpleDocTemplate(pdf_file)

        styles = getSampleStyleSheet()

        title_style = styles["Heading1"]
        title_style.alignment = TA_CENTER

        heading = styles["Heading2"]

        normal = styles["BodyText"]

        story = []

        # Title

        story.append(
            Paragraph(
                "🤖 AI SMART RESUME ANALYZER REPORT",
                title_style
            )
        )

        story.append(Spacer(1, 20))

        # Candidate Details

        story.append(
            Paragraph("👤 Candidate Details", heading)
        )

        candidate_table = [

            ["Email",
             email[0] if email else "Not Found"],

            ["Phone",
             phone[0] if phone else "Not Found"],

            ["LinkedIn",
             linkedin[0] if linkedin else "Not Found"],

            ["GitHub",
             github[0] if github else "Not Found"]

        ]

        table = Table(candidate_table, colWidths=[2 * inch, 4 * inch])

        table.setStyle(TableStyle([

            ("GRID", (0, 0), (-1, -1), 1, colors.black),

            ("BACKGROUND", (0, 0), (0, -1), colors.lightgrey),

            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),

            ("TOPPADDING", (0, 0), (-1, -1), 8)

        ]))

        story.append(table)

        story.append(Spacer(1, 20))
        # Resume Scores

        story.append(
            Paragraph("📊 Resume Scores", heading)
        )

        score_table = [

            ["ATS Score", f"{ats_score:.2f}%"],

            ["Tech Score", f"{tech_score:.2f}%"],

            ["Communication Score", f"{communication_score:.2f}%"],

            ["Resume Rating", rating],

            ["Resume Grade", grade],

            ["Overall Status", status]

        ]

        table = Table(score_table, colWidths=[3 * inch, 3 * inch])

        table.setStyle(TableStyle([

            ("GRID", (0, 0), (-1, -1), 1, colors.black),

            ("BACKGROUND", (0, 0), (0, -1), colors.lightblue),

            ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),

            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),

            ("TOPPADDING", (0, 0), (-1, -1), 8),

            ("ALIGN", (0, 0), (-1, -1), "CENTER")

        ]))

        story.append(table)

        story.append(Spacer(1, 20))
        # Strengths

        story.append(
            Paragraph("💪 Resume Strengths", heading)
        )

        for skill in matched_skills:
            story.append(
                Paragraph(f"✔ {skill}", normal)
            )

        story.append(Spacer(1, 15))

        # Missing Skills

        story.append(
            Paragraph("⚠ Missing Skills", heading)
        )

        if missing_skills:
            for skill in missing_skills:
                story.append(
                    Paragraph(f"• {skill}", normal)
                )
        else:
            story.append(
                Paragraph("No Missing Skills Found 🎉", normal)
            )

        story.append(Spacer(1, 15))

        # Career Suggestion

        story.append(
            Paragraph("🎯 Career Suggestion", heading)
        )

        story.append(
            Paragraph(career, normal)
        )

        story.append(Spacer(1, 20))
        # Learning Roadmap

        story.append(
            Paragraph("🛣 Learning Roadmap", heading)
        )

        roadmap_steps = [
            "Week 1 : Learn Advanced Python",
            "Week 2 : Master SQL",
            "Week 3 : Practice Pandas & NumPy",
            "Week 4 : Learn Power BI",
            "Week 5 : Study Machine Learning",
            "Week 6 : Build Real-Time Projects"
        ]

        for step in roadmap_steps:
            story.append(
                Paragraph(f"• {step}", normal)
            )

        story.append(Spacer(1, 15))

        # AI Feedback

        story.append(
            Paragraph("🤖 AI Feedback", heading)
        )

        if overall_score >= 80:
            feedback = "Excellent Resume! Your profile is suitable for most technical roles."
        elif overall_score >= 60:
            feedback = "Good Resume. Add more projects and technical skills."
        else:
            feedback = "Improve your technical skills, certifications, and projects."

        story.append(
            Paragraph(feedback, normal)
        )

        story.append(Spacer(1, 20))

        # Footer

        story.append(
            Paragraph(
                "<b>Generated by AI Smart Resume Analyzer</b>",
                heading
            )
        )

        doc.build(story)

        with open(pdf_file, "rb") as file:
            st.download_button(
                label="⬇ Download Professional PDF",
                data=file,
                file_name="AI_Smart_Resume_Report.pdf",
                mime="application/pdf"
            )
    st.markdown("---")
    st.success("🎉 Thank You For Using AI Resume Analyzer ❤️")
    st.markdown(
        """
        <div style="text-align:center; color:#666666; font-size:16px; line-height:1.8;">
            <b>© 2026 AI Smart Resume Analyzer</b><br>
            Version 1.0<br>
            Developed by <b>Gayathri Pandiyan</b><br>str
            Developed using Python • Streamlit • AI
        </div>
        """,
        unsafe_allow_html=True
    )
