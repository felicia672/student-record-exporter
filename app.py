import os

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

    # Generate the table rows dynamically
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

    # The HTML boilerplate with embedded CSS styling + new KPI Cards
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
            max-width: 900px;
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
            padding: 12px 16px;
            text-align: left;
            border-bottom: 1px solid #e2e8f0;
        }}
        th {{
            background-color: #f1f5f9;
            color: #475569;
            font-weight: 600;
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
        <p>Generated automatically via Python Backend script.</p>
        
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
    print(f"\n✨ Success! Dashboard compiled locally as '{output_filename}'\n")

if __name__ == "__main__":
    student_database = []
    serial_counter = 1

    print("=========================================")
    print("      STUDENT DASHBOARD GENERATOR        ")
    print("=========================================")
    
    while True:
        print(f"\nEntering details for Student #{serial_counter}:")
        
        name = input("Enter Name (or type 'exit' to finish): ").strip()
        if name.lower() == 'exit':
            break
            
        class_sec = input("Enter Class & Section (e.g., 10-A): ").strip()
        fav_sub = input("Enter Favorite Subject: ").strip()
        dob = input("Enter Date of Birth (DD-MM-YYYY): ").strip()
        
        # Collect marks loop
        marks = []
        print("Enter 3 test scores out of 100:")
        for i in range(1, 4):
            while True:
                try:
                    score = float(input(f"  Test {i} Score: "))
                    if 0 <= score <= 100:
                        marks.append(score)
                        break
                    else:
                        print("  ❌ Score must be between 0 and 100.")
                except ValueError:
                    print("  ❌ Invalid input. Please enter a valid number.")

        # Create student object and add to data array
        new_student = Student(serial_counter, name, class_sec, fav_sub, dob, marks)
        student_database.append(new_student)
        
        print(f"✅ Added {name} successfully! (Average: {new_student.average}%, Grade: {new_student.grade})")
        serial_counter += 1

    # If the user added students before exiting, generate the report
    if student_database:
        generate_html_report(student_database)
    else:
        print("\n👋 Exited application without creating any records.")
