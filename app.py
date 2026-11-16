import os

class Student:
    def __init__(self, sno, name, class_sec, fav_sub, dob, marks):
        self.sno = sno
        self.name = name
        self.class_sec = class_sec
        self.fav_sub = fav_sub
        self.dob = dob
        self.marks = marks # A list of 3 test scores out of 100
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
    # Generate the table rows dynamically using a loop
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

    # The HTML boilerplate with embedded CSS styling
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Automated Student Dashboard</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 40px;
            background-color: #f8fafc;
            color: #1e293b;
        }}
        .container {{
            max-width: 800px;
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
        /* Color coding for grades */
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
    print(f" Success! HTML dashboard generated as '{output_filename}'")

if __name__ == "__main__":
    # Sample Student Database (5 columns + performance metrics data)
    student_database = [
        Student(1, "Aarav Sharma", "10-A", "Mathematics", "12-04-2011", [95, 88, 92]),
        Student(2, "Diya Patel", "10-B", "Science", "23-08-2011", [78, 85, 80]),
        Student(3, "Kabir Singh", "10-A", "History", "05-01-2012", [62, 70, 65]),
        Student(4, "Ananya Rao", "10-C", "English", "19-11-2011", [88, 91, 94]),
        Student(5, "Vivaan Das", "10-B", "Computer Science", "30-06-2011", [98, 95, 100]),
    ]

    generate_html_report(student_database)
