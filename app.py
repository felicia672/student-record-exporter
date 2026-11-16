import os
import random

class Student:
    def __init__(self, sno, name, class_sec, fav_sub, dob, marks):
        self.sno = sno
        self.name = name
        self.class_sec = class_sec
        self.fav_sub = fav_sub
        self.dob = dob
        self.marks = marks  # A list of test scores
        self.average = self.calculate_average()
        self.grade = self.calculate_grade()

    def calculate_average(self):
        if not self.marks:
            return 0
        return round(sum(self.marks) / len(self.marks), 2)

    def calculate_grade(self):
        if self.average >= 90: return "A"
        elif self.average >= 80: return "B"
        elif self.average >= 70: return "C"
        elif self.average >= 60: return "D"
        else: return "F"

def generate_html_report(students, output_filename="index.html"):
    total_students = len(students)
    if total_students == 0:
        print("⚠ No student records to export.")
        return

    # --- DASHBOARD ANALYTICS COMPUTATION ---
    class_average = round(sum(s.average for s in students) / total_students, 2)
    
    highest_scorer = students[0]
    for s in students:
        if s.average > highest_scorer.average:
            highest_scorer = s
            
    passing_count = sum(1 for s in students if s.grade != "F")

    # Generate the table rows dynamically for all 100 students
    table_rows = ""
    for s in students:
        table_rows += f"""
        <tr>
            <td>{s.sno}</td>
            <td>{s.name}</td>
            <td>{s.class_sec}</td>
            <td>{s.fav_sub}</td>
            <td>{s.dob}</td>
            <td>{s.average}%</td>
            <td class="grade-{s.grade}">{s.grade}</td>
        </tr>
        """

    # The HTML boilerplate with embedded CSS styling + KPI Cards
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Academic Analytics Dashboard</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 40px;
            background-color: #f8fafc;
            color: #1e293b;
        }}
        .container {{
            max-width: 950px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
        }}
        h1 {{
            margin-top: 0;
            color: #0f172a;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 10px;
        }}
        .analytics-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 25px 0;
        }}
        .card {{
            background: #f1f5f9;
            padding: 20px;
            border-radius: 8px;
            border-left: 5px solid #64748b;
        }}
        .card.accent-green {{ border-left-color: #16a34a; }}
        .card.accent-blue {{ border-left-color: #2563eb; }}
        .card.accent-purple {{ border-left-color: #7c3aed; }}
        
        .card-title {{
            font-size: 13px;
            text-transform: uppercase;
            color: #64748b;
            font-weight: 600;
            margin-bottom: 5px;
        }}
        .card-value {{
            font-size: 22px;
            font-weight: bold;
            color: #0f172a;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}
        th, td {{
            padding: 10px 16px;
            text-align: left;
            border-bottom: 1px solid #e2e8f0;
            font-size: 14px;
        }}
        th {{
            background-color: #f1f5f9;
            color: #475569;
            font-weight: 600;
            position: sticky;
            top: 0; /* Keeps headers visible when scrolling large data arrays */
        }}
        tr:hover {{
            background-color: #f8fafc;
        }}
        .grade-A {{ color: #16a34a; font-weight: bold; }}
        .grade-B {{ color: #2563eb; font-weight: bold; }}
        .grade-C {{ color: #d97706; font-weight: bold; }}
        .grade-D {{ color: #ea580c; font-weight: bold; }}
        .grade-F {{ color: #dc2626; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Academic Performance Dashboard</h1>
        <p>Big Data Simulation: 100 Student Records.</p>
        
        <div class="analytics-grid">
            <div class="card accent-blue">
                <div class="card-title">Class Average</div>
                <div class="card-value">{class_average}%</div>
            </div>
            <div class="card accent-purple">
                <div class="card-title">Top Performer</div>
                <div class="card-value">{highest_scorer.name} ({highest_scorer.average}%)</div>
            </div>
            <div class="card accent-green">
                <div class="card-title">Passing Roster</div>
                <div class="card-value">{passing_count} / {total_students} Students</div>
            </div>
        </div>

        <table>
            <thead>
                <tr>
                    <th>S.No.</th>
                    <th>Name</th>
                    <th>Class & Sec</th>
                    <th>Fav. Subject</th>
                    <th>D.O.B.</th>
                    <th>Avg Marks</th>
                    <th>Grade</th>
                </tr>
            </thead>
            <tbody>
                {table_rows}
            </tbody>
        </table>
    </div>
</body>
</html>
"""

    with open(output_filename, "w", encoding="utf-8") as file:
        file.write(html_content)
    print(f"🚀 Success! Simulated {total_students} records inside '{output_filename}'")

if __name__ == "__main__":
    # Seed lists for random data compilation
    first_names = ["Aarav", "Diya", "Kabir", "Ananya", "Vivaan", "Isha", "Arjun", "Meera", "Rohan", "Sanya", "Rahul", "Neha", "Aditya", "Pooja", "Karan", "Riya"]
    last_names = ["Sharma", "Patel", "Singh", "Rao", "Das", "Joshi", "Mehta", "Kumar", "Verma", "Nair", "Gupta", "Reddy", "Choudhury", "Mishra"]
    subjects = ["Mathematics", "Science", "History", "English", "Computer Science", "Physics", "Chemistry"]
    sections = ["10-A", "10-B", "10-C"]

    student_database = []

    # Dynamic generation loop to build exactly 100 student records
    for i in range(1, 101):
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        class_sec = random.choice(sections)
        fav_sub = random.choice(subjects)
        
        # Make a mock date of birth
        day = str(random.randint(1, 28)).zfill(2)
        month = str(random.randint(1, 12)).zfill(2)
        dob = f"{day}-{month}-2011"
        
        # Generate 3 mock scores skewed towards passing grades
        marks = [random.randint(55, 100) for _ in range(3)]
        
        student = Student(i, name, class_sec, fav_sub, dob, marks)
        student_database.append(student)

    generate_html_report(student_database)
