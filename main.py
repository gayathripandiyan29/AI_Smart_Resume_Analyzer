
import pdfplumber
import pandas as pd
import re
#---------------pdf read--------------

pdf = pdfplumber.open("gayu resumeee.pdf")

text = ""

for page in pdf.pages:
    page_text = page.extract_text()
    if page_text:
        text += page_text

pdf.close()

print(text)

#----------------skills read--------------

skills = pd.read_csv("skills.csv", header=None)

print("\nSkills Database:\n")
print(skills)

#-----------resume skills match-------
resume_text = text.lower()

skills_list = skills[0].tolist()

matched_skills = []

for skill in skills_list:
    if skill.lower() in resume_text:
        matched_skills.append(skill)

print("\nMatched Skills:")
print(matched_skills)
#----------ATS SCORE----------
total_skills = len(skills_list)
matched_count = len(matched_skills)

ats_score = (matched_count / total_skills) * 100

print("\nATS Score:")
print(f"{ats_score:.2f}%")
#------------missing skills---------
missing_skills = []

for skill in skills_list:
    if skill not in matched_skills:
        missing_skills.append(skill)

print("\nMissing Skills:")
print(missing_skills)
#-----------career suggestion------
print("\nCareer Suggestion:")

if "Machine Learning" in matched_skills and "Python" in matched_skills:
    print("➡ AI/ML Engineer")

elif "Python" in matched_skills and "Data Analysis" in matched_skills:
    print("➡ Data Analyst")

elif "SQL" in matched_skills and "Excel" in matched_skills:
    print("➡ Business Analyst")

elif "Java" in matched_skills:
    print("➡ Java Developer")

elif "HTML" in matched_skills and "CSS" in matched_skills:
    print("➡ Frontend Developer")

else:
    print("➡ Keep improving your skills to explore more career opportunities.")
#----------------tech skills---------
tech_skills = [
    "Python", "SQL", "Machine Learning", "Deep Learning",
    "Pandas", "NumPy", "Java", "C", "C++",
    "HTML", "CSS", "JavaScript", "Git", "GitHub"
]

matched_tech = 0
#-------------communication------------
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

print("\nCommunication Score:")
print(f"{communication_score:.2f}%")

for skill in tech_skills:
    if skill in matched_skills:
        matched_tech += 1

tech_score = (matched_tech / len(tech_skills)) * 100

print("\nTech Score:")
print(f"{tech_score:.2f}%")
#------------resume analysis report--------
print("\n========== RESUME ANALYSIS REPORT ==========")

print("\nStrengths:")
if ats_score >= 70:
    print("✔ Excellent technical profile.")
elif ats_score >= 50:
    print("✔ Good technical profile. Improve a few more skills.")
else:
    print("✔ Keep learning more technical skills.")

print("\nWeaknesses:")
if len(missing_skills) > 0:
    print("Need to improve:", ", ".join(missing_skills))
else:
    print("No major missing skills.")

print("\nResume Summary:")
print(f"Matched Skills : {len(matched_skills)}")
print(f"Missing Skills : {len(missing_skills)}")
print(f"ATS Score      : {ats_score:.2f}%")
print(f"Tech Score     : {tech_score:.2f}%")
print(f"Communication Score : {communication_score:.2f}%")

print("\nInterview Tips:")
print("• Revise Python and SQL concepts.")
print("• Practice aptitude daily.")
print("• Improve communication skills.")
print("• Prepare project explanation.")
print("• Practice HR interview questions.")

print("\nRecommended Courses:")
if "Power BI" in missing_skills:
    print("• Learn Power BI")
if "SQL" in missing_skills:
    print("• Learn Advanced SQL")
if "Machine Learning" in missing_skills:
    print("• Learn Machine Learning")
if "Git" in missing_skills:
    print("• Learn Git & GitHub")
if len(missing_skills) == 0:
    print("• Great! Continue practicing projects.")

print("\n========== END OF REPORT ==========")
#------------resume rating------------
print("\nResume Rating:")

if ats_score >= 90:
    print("⭐⭐⭐⭐⭐ (10/10)")
elif ats_score >= 75:
    print("⭐⭐⭐⭐☆ (8/10)")
elif ats_score >= 60:
    print("⭐⭐⭐☆☆ (6/10)")
elif ats_score >= 40:
    print("⭐⭐☆☆☆ (4/10)")
else:
    print("⭐☆☆☆☆ (2/10)")
#------------improvement sugges--------
print("\nSuggestions to Improve Resume:")

if "Power BI" in missing_skills:
    print("• Add Power BI projects.")

if "GitHub" in missing_skills:
    print("• Upload projects to GitHub.")

if "Machine Learning" in missing_skills:
    print("• Add Machine Learning project.")

if "Communication" in missing_skills:
    print("• Mention communication skills.")

if ats_score >= 80:
    print("• Excellent Resume! Keep updating your projects.")
#---------------final rep--------
print("\n==============================")
print(" AI RESUME ANALYZER REPORT ")
print("==============================")

print(f"ATS Score              : {ats_score:.2f}%")
print(f"Tech Score             : {tech_score:.2f}%")
print(f"Communication Score    : {communication_score:.2f}%")

print(f"\nMatched Skills : {len(matched_skills)}")
print(f"Missing Skills : {len(missing_skills)}")

print("\nThank you for using AI Resume Analyzer ❤️")
#------------skill gap analyis----------
print("\n========== SKILL GAP ANALYSIS ==========")

print("\nCurrent Skills:")
for skill in matched_skills:
    print("✔", skill)

print("\nMissing Skills:")
for skill in missing_skills:
    print("✘", skill)
#---------learning roadmap------
print("\n========== LEARNING ROADMAP ==========")

roadmap = {
    "Power BI": "Week 1 - Learn Power BI Basics",
    "Tableau": "Week 2 - Learn Tableau",
    "AWS": "Week 3 - Learn AWS Cloud Basics",
    "Git": "Week 4 - Learn Git & GitHub",
    "GitHub": "Week 5 - Upload Projects to GitHub",
    "Machine Learning": "Week 6 - Practice ML Algorithms",
    "Deep Learning": "Week 7 - Learn Neural Networks",
    "Java": "Week 8 - Learn Java Basics"
}

found = False

for skill in missing_skills:
    if skill in roadmap:
        print("✔", roadmap[skill])
        found = True

if not found:
    print("Excellent! No learning roadmap needed.")
#------------ai feedback-------
print("\n========== AI RESUME FEEDBACK ==========")

if ats_score >= 80:
    print("✅ Excellent Resume!")
elif ats_score >= 60:
    print("👍 Good Resume. A few improvements can make it stronger.")
else:
    print("⚠ Your resume needs improvement.")

if len(missing_skills) > 0:
    print("\nSuggestions:")
    print("• Add the missing technical skills.")
    print("• Include more real-world projects.")
    print("• Add certifications if available.")
    print("• Keep your GitHub profile updated.")
else:
    print("\n Your resume looks strong"
             ". Keep updating it with new projects and achievements.")
#---------contact dtls----------------
print("\n========== CONTACT DETAILS ==========")

# Email
email = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)

if email:
    print("📧 Email :", email[0])
else:
    print("📧 Email : Not Found")

# Phone Number
phone = re.findall(r'\+?\d[\d\s-]{8,}\d', text)

if phone:
    print("📱 Phone :", phone[0])
else:
    print("📱 Phone : Not Found")
#-------------linked&github---------
# Linkedin
linkedin = re.findall(r'https?://(?:www\.)?linkedin\.com/\S+', text)

if linkedin:
    print("💼 LinkedIn :", linkedin[0])
else:
    print("💼 LinkedIn : Not Found")

# GitHub
github = re.findall(r'https?://(?:www\.)?github\.com/\S+', text)

if github:
    print("💻 GitHub :", github[0])
else:
    print("💻 GitHub : Not Found")
#--------salary prediction---------
print("\n========== ESTIMATED SALARY ==========")

if ats_score >= 90:
    salary = "₹10 LPA - ₹15 LPA"

elif ats_score >= 75:
    salary = "₹7 LPA - ₹10 LPA"

elif ats_score >= 60:
    salary = "₹5 LPA - ₹7 LPA"

elif ats_score >= 40:
    salary = "₹3 LPA - ₹5 LPA"

else:
    salary = "₹2 LPA - ₹3 LPA"

print("Estimated Salary :", salary)
#---------interview qs----------
print("\n========== AI INTERVIEW QUESTIONS ==========")

if "Python" in matched_skills:
    print("1. Explain Python OOP concepts.")

if "SQL" in matched_skills:
    print("2. What is the difference between JOIN and UNION?")

if "Machine Learning" in matched_skills:
    print("3. Explain the difference between Supervised and Unsupervised Learning.")

if "Pandas" in matched_skills:
    print("4. Why do we use Pandas? Explain DataFrame.")

if "NumPy" in matched_skills:
    print("5. What is the difference between NumPy and Pandas?")

if "HTML" in matched_skills:
    print("6. What is the difference between HTML and HTML5?")

if "CSS" in matched_skills:
    print("7. Explain Flexbox and Grid.")

if "GitHub" in matched_skills:
    print("8. Explain Git and GitHub workflow.")

print("9. Explain the projects you have worked on.")
print("10. Tell me about yourself.")
#---------course recom---------
print("\n========== COURSE RECOMMENDATIONS ==========")

course_recommendations = {
    "Python": "Python for Data Science",
    "SQL": "Advanced SQL",
    "Power BI": "Microsoft Power BI",
    "Tableau": "Tableau Desktop",
    "Machine Learning": "Machine Learning with Scikit-Learn",
    "Deep Learning": "Deep Learning using TensorFlow",
    "Git": "Git and GitHub",
    "GitHub": "GitHub for Developers",
    "AWS": "AWS Cloud Practitioner",
    "Excel": "Advanced Microsoft Excel",
    "Pandas": "Pandas for Data Analysis",
    "NumPy": "NumPy Essentials"
}

recommended = False

for skill in missing_skills:
    if skill in course_recommendations:
        print(f"📘 {skill} → {course_recommendations[skill]}")
        recommended = True

if not recommended:
    print("Great! No course recommendations. Your resume already contains the required skills.")
#---------------prj recom-------------
print("\n========== PROJECT RECOMMENDATIONS ==========")

project_recommendations = {
    "Power BI": "Build a Sales Dashboard using Power BI",
    "Machine Learning": "Build a House Price Prediction System",
    "Deep Learning": "Build a Face Mask Detection System",
    "SQL": "Build a Student Database Management System",
    "Python": "Build a Library Management System",
    "GitHub": "Create a Professional GitHub Portfolio",
    "AWS": "Deploy a Python Project on AWS",
    "Pandas": "Build a Data Analysis Project",
    "NumPy": "Build a Data Visualization Project"
}

found = False

for skill in missing_skills:
    if skill in project_recommendations:
        print(f"🚀 {project_recommendations[skill]}")
        found = True

if not found:
    print(" Excellent! Try building advanced AI projects.")
#----------------dash boards-----------
def progress_bar(score):
    filled = int(score / 10)
    empty = 10 - filled
    return "█" * filled + "░" * empty
print("\n========== AI RESUME DASHBOARD ==========")

print(f"ATS Score             : {progress_bar(ats_score)} {ats_score:.2f}%")
print(f"Tech Score            : {progress_bar(tech_score)} {tech_score:.2f}%")
print(f"Communication Score   : {progress_bar(communication_score)} {communication_score:.2f}%")
#----------overall resume sts-------------
print("\n========== OVERALL RESUME STATUS ==========")

overall_score = (
    ats_score +
    tech_score +
    communication_score
) / 3

print(f"Overall Score : {overall_score:.2f}%")

if overall_score >= 85:
    print("🟢 Status : EXCELLENT")
elif overall_score >= 70:
    print("🟡 Status : GOOD")
elif overall_score >= 50:
    print("🟠 Status : AVERAGE")
else:
    print("🔴 Status : NEEDS IMPROVEMENT")
#----------------resume complteness-----------
print("\n========== RESUME COMPLETENESS ==========")

sections = {
    "Education": ["education", "college", "university", "b.sc", "b.tech", "degree"],
    "Skills": ["skills"],
    "Projects": ["project"],
    "Experience": ["experience", "internship"],
    "Certifications": ["certificate", "certification"],
    "Email": ["@"],
    "Phone": ["mobile", "phone"]
}

completed = 0

for section, keywords in sections.items():
    found = False

    for keyword in keywords:
        if keyword.lower() in resume_text.lower():
            found = True
            break

    if found:
        print(f"✅ {section}")
        completed += 1
    else:
        print(f"❌ {section}")

completeness_score = (completed / len(sections)) * 100

print(f"\nResume Completeness Score : {completeness_score:.2f}%")
#------------overall sts----------
print("\n")
print("╔══════════════════════════════════════════════╗")
print("║           AI RESUME ANALYSIS REPORT           ║")
print("╚══════════════════════════════════════════════╝")
career="data analyst"
print(f"🎯 Career Suggestion   : {career}")

print(f"📊 ATS Score           : {progress_bar(ats_score)} {ats_score:.2f}%")
print(f"💻 Tech Score          : {progress_bar(tech_score)} {tech_score:.2f}%")
print(f"🗣 Communication       : {progress_bar(communication_score)} {communication_score:.2f}%")
print(f"📄 Resume analysis       : {progress_bar(overall_score)} {overall_score:.2f}%")

# Hiring Probability
if overall_score >= 80:
    hiring = "🟢 HIGH"
elif overall_score >= 60:
    hiring = "🟡 MEDIUM"
else:
    hiring = "🔴 LOW"

print(f"💼 Hiring Probability  : {hiring}")

# Skill Level
if overall_score >= 85:
    level = "🟣 EXPERT"
elif overall_score >= 70:
    level = "🔵 ADVANCED"
elif overall_score >= 50:
    level = "🟡 INTERMEDIATE"
else:
    level = "🟢 BEGINNER"

print(f"🚀 Skill Level         : {level}")

# Resume Rating
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

print(f"⭐ Resume Rating       : {rating}")

# Resume Grade
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

print(f"🏆 Resume Grade        : {grade}")

# Overall Status
if overall_score >= 85:
    status = "🟢 EXCELLENT"
elif overall_score >= 70:
    status = "🟡 GOOD"
elif overall_score >= 50:
    status = "🟠 AVERAGE"
else:
    status = "🔴 NEEDS IMPROVEMENT"

print(f"📈 Overall Status      : {status}")

print("\n🎓 Next Recommendation")

for skill in missing_skills:
    print(f"✔ Learn {skill}")

print("\n══════════════════════════════════════════════")
print("      Thank You For Using")
print("   AI Smart Resume Analyzer")
print("══════════════════════════════════════════════")