import os
import random

class Student:
    def __init__(self, sno, name, class_sec, fav_sub, dob, marks):
        self.sno = sno
        self.name = name
        self.class_sec = class_sec
        self.fav_sub = fav_sub
        self.dob = dob
        self.marks = marks  
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
            <td data-value="{s.average}">{s.average}%</td>
            <td class="grade-{s.grade}">{s.grade}</td>
        </tr>
        """

    # Fully interactive HTML layout with searching and sorting arrays
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Live Student Search & Sort Dashboard</title>
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

        /* Search input elements bar */
        .search-container {{
            margin: 20px 0 10px 0;
            width: 100%;
        }}
        .search-box {{
            width: 100%;
            padding: 12px 16px;
            font-size: 15px;
            border: 2px solid #e2e8f0;
            border-radius: 8px;
            outline: none;
            box-sizing: border-box;
            transition: border-color 0.2s;
        }}
        .search-box:focus {{
            border-color: #2563eb;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
        }}
        th, td {{
            padding: 12px 16px;
            text-align: left;
            border-bottom: 1px solid #e2e8f0;
            font-size: 14px;
        }}
        th {{
            background-color: #f1f5f9;
            color: #475569;
            font-weight: 600;
            cursor: pointer; /* Indicates headers are clickable elements */
            user-select: none;
        }}
        th:hover {{
            background-color: #e2e8f0;
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
        <p>Interactive Client View: Live Search and Column Sorting enabled.</p>
        
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

        <!-- Real-time Filter Query Input Box -->
        <div class="search-container">
            <input type="text" id="searchInput" class="search-box" placeholder="🔍 Search for student names, classes, or subjects in real time...">
        </div>

        <table id="studentTable">
            <thead>
                <tr>
                    <th onclick="sortTable(0)">S.No. ↕</th>
                    <th onclick="sortTable(1)">Name ↕</th>
                    <th onclick="sortTable(2)">Class & Sec ↕</th>
                    <th onclick="sortTable(3)">Fav. Subject ↕</th>
                    <th onclick="sortTable(4)">D.O.B. ↕</th>
                    <th onclick="sortTable(5)">Avg Marks ↕</th>
                    <th onclick="sortTable(6)">Grade ↕</th>
                </tr>
            </thead>
            <tbody>
                {table_rows}
            </tbody>
        </table>
    </div>

    <!-- Frontend Interactive JavaScript Component -->
    <script>
        // 1. Live Filter/Search Functionality
        document.getElementById('searchInput').addEventListener('keyup', function() {{
            let filter = this.value.toLowerCase();
            let rows = document.querySelectorAll('#studentTable tbody tr');
            
            rows.forEach(row => {{
                let text = row.textContent.toLowerCase();
                // If query matches any text string inside the row elements, display it
                if (text.includes(filter)) {{
                    row.style.display = '';
                }} else {{
                    row.style.display = 'none';
                }}
            }});
        }});

        // 2. Interactive Column Sorting Algorithm
        let sortDirections = {{}};
        function sortTable(columnIndex) {{
            let table = document.getElementById('studentTable');
            let tbody = table.querySelector('tbody');
            let rows = Array.from(tbody.querySelectorAll('tr'));
            
            // Toggle directions between ascending/descending trackers
            let ascending = sortDirections[columnIndex] === undefined ? true : !sortDirections[columnIndex];
            sortDirections[columnIndex] = ascending;

            rows.sort((rowA, rowB) => {{
                let cellA = rowA.children[columnIndex];
                let cellB = rowB.children[columnIndex];

                // Extract custom values for precise floating math sorting, else fallback to text strings
                let valA = cellA.getAttribute('data-value') || cellA.textContent.trim();
                let valB = cellB.getAttribute('data-value') || cellB.textContent.trim();

                // Convert numbers for clean numerical values comparison
                if (!isNaN(valA) && !isNaN(valB)) {{
                    return ascending ? valA - valB : valB - valA;
                }}
                
                // Alphabetic comparison
                return ascending ? valA.localeCompare(valB) : valB.localeCompare(valA);
            }});

            // Append organized sorting arrays back into document grid node blocks
            rows.forEach(row => tbody.appendChild(row));
        }}
    </script>
</body>
</html>
"""

    with open(output_filename, "w", encoding="utf-8") as file:
        file.write(html_content)
    print(f"🚀 Success! Interactive sorting matrix built into '{output_filename}'")

if __name__ == "__main__":
    first_names = ["Aarav", "Diya", "Kabir", "Ananya", "Vivaan", "Isha", "Arjun", "Meera", "Rohan", "Sanya", "Rahul", "Neha", "Aditya", "Pooja", "Karan", "Riya"]
    last_names = ["Sharma", "Patel", "Singh", "Rao", "Das", "Joshi", "Mehta", "Kumar", "Verma", "Nair", "Gupta", "Reddy", "Choudhury", "Mishra"]
    subjects = ["Mathematics", "Science", "History", "English", "Computer Science", "Physics", "Chemistry"]
    sections = ["10-A", "10-B", "10-C"]

    student_database = []

    for i in range(1, 101):
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        class_sec = random.choice(sections)
        fav_sub = random.choice(subjects)
        
        day = str(random.randint(1, 28)).zfill(2)
        month = str(random.randint(1, 12)).zfill(2)
