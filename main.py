
print("=" * 50)
print("       AI LIVE COACHING COPILOT")
print("=" * 50)

print("\nWelcome to the Student Rescue Center!")

student_name = "Sophia"
subject = "Mathematics"
mastery = 42
target = 80

gap = target - mastery

print("\nSTUDENT INFORMATION")
print("-" * 30)
print("Student Name:", student_name)
print("Subject:", subject)
print("Current Mastery:", str(mastery) + "%")
print("Target Mastery:", str(target) + "%")
print("Mastery Gap:", str(gap) + "%")

print("\nCOACHING ALERT")

if mastery < 40:
    print("URGENT: Student needs immediate coaching.")
elif mastery < 60:
    print("HIGH PRIORITY: Student needs targeted support.")
elif mastery < 80:
    print("MONITOR: Student needs additional practice.")
else:
    print("TARGET ACHIEVED: Student is performing well.")

print("\nCoaching Copilot is ready!")


print("\n" + "=" * 50)
print("       LIVE COACHING SESSION")
print("=" * 50)

student_response = input(
    "\nCoach: Sophia, are you comfortable with fractions? (yes/no): "
)

if student_response.lower() == "yes":
    print("Coach: Excellent! Let's try a challenging question.")
else:
    print("Coach: No problem! Let's learn together.")
    print("Coach: I'll explain fractions using simple examples.")
    print("Coach: Let's practice one question at a time.")

print("\nCoaching session initialized!")


print("\n" + "=" * 50)
print("       FRACTION KNOWLEDGE CHECK")
print("=" * 50)

answer = input("\nCoach: What is 1/2 + 1/4? ")

if answer.strip() == "3/4":
    print("\nCoach: Excellent work, Sophia!")
    print("Diagnosis: Correct understanding.")
else:
    print("\nCoach: Let's work through this together.")
    print("Diagnosis: Possible fraction misconception.")
    print("Intervention: Provide visual fraction examples.")
    print("Next Step: Give Sophia targeted practice questions.")


print("\n" + "=" * 50)
print("       PERSONALIZED INTERVENTION ENGINE")
print("=" * 50)

if mastery < 40:
    print("Intervention Level: URGENT")
    print("1. Schedule an immediate coaching session.")
    print("2. Explain concepts using visual examples.")
    print("3. Provide foundational practice questions.")

elif mastery < 60:
    print("Intervention Level: HIGH")
    print("1. Schedule targeted coaching.")
    print("2. Identify specific misconceptions.")
    print("3. Provide personalized assignments.")

elif mastery < 80:
    print("Intervention Level: MODERATE")
    print("1. Provide additional practice.")
    print("2. Monitor weekly progress.")
    print("3. Address remaining learning gaps.")

else:
    print("Intervention Level: ACHIEVED")
    print("1. Maintain current learning progress.")
    print("2. Introduce advanced challenges.")
    
print("\nPersonalized intervention generated!")


print("\n" + "=" * 50)
print("       STUDENT COACHING SESSION REPORT")
print("=" * 50)

print("Student:", student_name)
print("Subject:", subject)
print("Mastery:", str(mastery) + "%")
print("Target:", str(target) + "%")
print("Learning Gap:", str(gap) + " percentage points")

print("\nSESSION SUMMARY")
print("Student participated in a fraction knowledge check.")
print("Fraction understanding was assessed.")

print("\nRECOMMENDED ACTIONS")
print("- Targeted fraction practice")
print("- Visual learning examples")
print("- Follow-up coaching session")
print("- Monitor student progress")

print("\nSESSION STATUS: COMPLETED")
print("=" * 50)


report = f"""
========================================
       AI LIVE COACHING COPILOT
========================================

STUDENT COACHING REPORT

Student: {student_name}
Subject: {subject}

Current Mastery: {mastery}%
Target Mastery: {target}%
Mastery Gap: {gap} percentage points

PRIORITY: HIGH

RECOMMENDED INTERVENTIONS:
1. Targeted coaching sessions.
2. Visual fraction examples.
3. Personalized practice assignments.
4. Monitor student progress.

STATUS: Coaching report generated.
========================================
"""

with open("coaching_report.txt", "w") as file:
    file.write(report)

print("\nCoaching report saved successfully!")
print("File: coaching_report.txt")


print("\n" + "=" * 50)
print("       MULTI-STUDENT RESCUE CENTER")
print("=" * 50)

students = [
    {"name": "Sophia", "mastery": 42},
    {"name": "Noah", "mastery": 58},
    {"name": "Maya", "mastery": 75},
    {"name": "Alex", "mastery": 88}
]

for student in students:

    mastery_score = student["mastery"]

    if mastery_score < 40:
        priority = "URGENT"
    elif mastery_score < 60:
        priority = "HIGH"
    elif mastery_score < 80:
        priority = "MODERATE"
    else:
        priority = "TARGET ACHIEVED"

    print("\nStudent:", student["name"])
    print("Mastery:", str(mastery_score) + "%")
    print("Priority:", priority)

print("\nMulti-student analysis completed!")


print("\n" + "=" * 50)
print("       STUDENT RESCUE PRIORITY QUEUE")
print("=" * 50)

TARGET = 80

# Sort students from lowest mastery to highest
ranked_students = sorted(
    students,
    key=lambda student: student["mastery"]
)

print("\nCOACHING PRIORITY RANKING\n")

for rank, student in enumerate(ranked_students, start=1):

    mastery_score = student["mastery"]
    gap = max(0, TARGET - mastery_score)

    print(f"Priority Rank: {rank}")
    print("Student:", student["name"])
    print("Current Mastery:", str(mastery_score) + "%")
    print("Gap to Target:", str(gap) + " percentage points")

    if mastery_score < 40:
        print("Action: Immediate intervention")
    elif mastery_score < 60:
        print("Action: Targeted coaching")
    elif mastery_score < 80:
        print("Action: Additional practice")
    else:
        print("Action: Advanced learning challenges")

    print("-" * 35)

print("\nStudent risk ranking completed!")


print("\n" + "=" * 55)
print("       AUTOMATIC INTERVENTION ASSIGNMENT ENGINE")
print("=" * 55)

for student in students:

    score = student["mastery"]

    print("\nStudent:", student["name"])
    print("Mastery:", str(score) + "%")

    if score < 40:
        print("Intervention: URGENT SUPPORT")
        print("1. Individual coaching sessions")
        print("2. Foundational concept explanations")
        print("3. Daily progress monitoring")

    elif score < 60:
        print("Intervention: TARGETED SUPPORT")
        print("1. Identify learning misconceptions")
        print("2. Personalized practice assignments")
        print("3. Additional coaching sessions")

    elif score < 80:
        print("Intervention: SKILL IMPROVEMENT")
        print("1. Topic-specific practice")
        print("2. Weekly progress assessments")
        print("3. Address remaining learning gaps")

    else:
        print("Intervention: ADVANCED LEARNING")
        print("1. Advanced problem-solving")
        print("2. Enrichment assignments")
        print("3. Maintain mastery")

    print("-" * 40)

print("\nAll intervention plans generated!")


print("\n" + "=" * 55)
print("       STUDENT INTERVENTION TRACKER")
print("=" * 55)

for student in students:

    previous_score = student["mastery"]

    print("\nStudent:", student["name"])
    print("Previous Mastery:", str(previous_score) + "%")

    while True:
        try:
            new_score = float(input("Enter reassessment mastery (%): "))

            if 0 <= new_score <= 100:
                break

            print("Please enter a score between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    progress = new_score - previous_score

    print("New Mastery:", str(new_score) + "%")
    print("Progress:", str(progress) + " percentage points")

    if progress > 0:
        print("Status: IMPROVING")
        print("Action: Continue the intervention.")

    elif progress == 0:
        print("Status: NO CHANGE")
        print("Action: Review the coaching strategy.")

    else:
        print("Status: DECLINING")
        print("Action: Reassess misconceptions and intervention.")

    student["mastery"] = new_score

    print("-" * 40)

print("\nIntervention tracking completed!")

print("\n" + "=" * 55)
print("       ACADEMIC PERFORMANCE SUMMARY")
print("=" * 55)

total_students = len(students)

if total_students > 0:

    scores = [student["mastery"] for student in students]

    average_mastery = sum(scores) / total_students
    highest = max(students, key=lambda s: s["mastery"])
    lowest = min(students, key=lambda s: s["mastery"])

    needing_support = [
        student for student in students
        if student["mastery"] < 80
    ]

    achieved_target = [
        student for student in students
        if student["mastery"] >= 80
    ]

    print("Total Students:", total_students)
    print("Average Mastery:", round(average_mastery, 2), "%")

    print(
        "Highest Mastery:",
        highest["name"],
        "-", highest["mastery"], "%"
    )

    print(
        "Lowest Mastery:",
        lowest["name"],
        "-", lowest["mastery"], "%"
    )

    print("Students Needing Support:", len(needing_support))
    print("Students Achieving Target:", len(achieved_target))

    print("\nSTUDENT STATUS")

    for student in students:
        if student["mastery"] >= 80:
            status = "TARGET ACHIEVED"
        else:
            status = "NEEDS SUPPORT"

        print(student["name"], "-", student["mastery"], "% -", status)

else:
    print("No student records available.")

print("\nAcademic summary generated successfully!")

import csv
import os
from datetime import datetime

print("\n" + "=" * 55)
print("       COACHING SESSION HISTORY")
print("=" * 55)

file_name = "session_history.csv"

file_exists = os.path.exists(file_name)

with open(file_name, "a", newline="") as file:

    writer = csv.writer(file)

    if not file_exists:
        writer.writerow([
            "Session Date",
            "Student Name",
            "Mastery",
            "Target",
            "Mastery Gap",
            "Status"
        ])

    for student in students:

        score = student["mastery"]
        gap = max(0, 80 - score)

        if score < 40:
            status = "URGENT SUPPORT"
        elif score < 60:
            status = "HIGH PRIORITY"
        elif score < 80:
            status = "NEEDS MONITORING"
        else:
            status = "TARGET ACHIEVED"

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M"),
            student["name"],
            score,
            80,
            gap,
            status
        ])

print("Coaching session history saved!")
print("File:", file_name)
print("Students recorded:", len(students))

import csv
import os

print("\n" + "=" * 55)
print("       STUDENT PROGRESS TREND DETECTOR")
print("=" * 55)

file_name = "session_history.csv"

if not os.path.exists(file_name):
    print("No session history found.")
    print("Run the session history tracker first.")

else:
    history = {}

    with open(file_name, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            name = row["Student Name"]
            score = float(row["Mastery"])

            if name not in history:
                history[name] = []

            history[name].append(score)

    for name, scores in history.items():

        print("\nStudent:", name)

        if len(scores) < 2:
            print("Not enough sessions to identify a trend.")
            continue

        previous = scores[-2]
        current = scores[-1]
        change = current - previous

        print("Previous Mastery:", previous, "%")
        print("Current Mastery:", current, "%")
        print("Change:", change, "percentage points")

        if change > 0:
            print("Trend: IMPROVING")
            print("Action: Continue the intervention.")

        elif change < 0:
            print("Trend: DECLINING")
            print("Action: Review misconceptions and coaching.")

        else:
            print("Trend: NO CHANGE")
            print("Action: Adjust the teaching strategy.")

print("\nProgress trend analysis completed!")

import csv
import os

print("\n" + "=" * 55)
print("       STUDENT EARLY WARNING SYSTEM")
print("=" * 55)

file_name = "session_history.csv"

if not os.path.exists(file_name):
    print("Session history not found.")

else:
    history = {}

    with open(file_name, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            name = row["Student Name"]
            score = float(row["Mastery"])

            if name not in history:
                history[name] = []

            history[name].append(score)

    alerts_found = 0

    for name, scores in history.items():

        if len(scores) < 2:
            continue

        previous = scores[-2]
        current = scores[-1]

        if current < previous:
            alerts_found += 1

            print("\nRISK ALERT!")
            print("Student:", name)
            print("Previous Mastery:", previous, "%")
            print("Current Mastery:", current, "%")
            print("Decline:", round(previous - current, 2), "points")
            print("Recommended Action: Immediate coaching review.")

    if alerts_found == 0:
        print("No declining students detected.")

    print("\nTotal Risk Alerts:", alerts_found)

print("\nEarly warning analysis completed!")


print("\n" + "=" * 55)
print("       ADVANCED MISCONCEPTION DIAGNOSIS")
print("=" * 55)

print("\nCoach: Let's solve a fraction problem!")

print("Question: What is 1/2 + 1/4?")

answer = input("Student answer: ").strip()

print("\n--- DIAGNOSIS REPORT ---")

if answer == "3/4":
    print("Result: CORRECT")
    print("Diagnosis: Correct understanding of fraction addition.")
    print("Recommendation: Introduce a slightly harder problem.")

elif answer == "2/6":
    print("Result: INCORRECT")
    print("Misconception: Adding numerators and denominators directly.")
    print("Recommendation: Teach equivalent fractions using visual models.")

elif answer == "2/4":
    print("Result: INCORRECT")
    print("Possible misconception: Incorrect numerator calculation.")
    print("Recommendation: Review equivalent fractions and common denominators.")

elif answer == "3/6":
    print("Result: INCORRECT")
    print("Possible misconception: Incorrect fraction conversion.")
    print("Recommendation: Practice converting fractions to equivalent forms.")

else:
    print("Result: INCORRECT")
    print("Diagnosis: Unknown error pattern.")
    print("Recommendation: Ask the student to explain their steps.")

print("\nDiagnosis completed!")



print("\n" + "=" * 55)
print("       ADAPTIVE PRACTICE GENERATOR")
print("=" * 55)

print("\nStudent: Sophia")

while True:
    try:
        mastery = float(input("Enter student's current mastery (%): "))

        if 0 <= mastery <= 100:
            break

        print("Enter a score between 0 and 100.")

    except ValueError:
        print("Please enter a valid number.")

if mastery < 40:
    print("\nDifficulty: BEGINNER")
    print("Question: What is half of 8?")
    correct_answer = "4"

elif mastery < 60:
    print("\nDifficulty: INTERMEDIATE")
    print("Question: What is 1/2 + 1/4?")
    correct_answer = "3/4"

elif mastery < 80:
    print("\nDifficulty: ADVANCED")
    print("Question: What is 3/4 + 2/3?")
    correct_answer = "17/12"

else:
    print("\nDifficulty: CHALLENGE")
    print("Question: What is 25% of 240?")
    correct_answer = "60"

student_answer = input("\nStudent answer: ").strip()

if student_answer == correct_answer:
    print("\nResult: CORRECT!")
    print("Recommendation: Increase question difficulty.")
else:
    print("\nResult: INCORRECT.")
    print("Correct answer:", correct_answer)
    print("Recommendation: Provide a worked example and targeted practice.")

print("\nAdaptive practice session completed!")
