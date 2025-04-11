!pip install fpdf
import csv
from fpdf import FPDF

# Sample Data File (data.csv)
csv_data = """Name,Marks
Alice,85
Bob,90
Charlie,78
David,92
Emma,88"""

# ... (rest of your code)
import csv
from fpdf import FPDF

# Sample Data File (data.csv)
csv_data = """Name,Marks
Alice,85
Bob,90
Charlie,78
David,92
Emma,88"""

# Save sample data to a file
with open("data.csv", "w") as file:
    file.write(csv_data)

# Function to read and analyze data
def analyze_data(file_path):
    total_marks = 0
    num_students = 0
    data = []

    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            name, marks = row
            marks = int(marks)
            data.append((name, marks))
            total_marks += marks
            num_students += 1

    avg_marks = total_marks / num_students if num_students else 0
    return data, total_marks, avg_marks

# Function to generate PDF report
def generate_pdf(data, total_marks, avg_marks):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=16)

    pdf.cell(200, 10, "Student Marks Report", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", size=12)
    pdf.cell(40, 10, "Name", 1)
    pdf.cell(40, 10, "Marks", 1)
    pdf.ln()

    for name, marks in data:
        pdf.cell(40, 10, name, 1)
        pdf.cell(40, 10, str(marks), 1)
        pdf.ln()

    pdf.ln(10)
    pdf.cell(40, 10, f"Total Marks: {total_marks}")
    pdf.ln()
    pdf.cell(40, 10, f"Average Marks: {avg_marks:.2f}")

    pdf.output("report.pdf")
    print("PDF Report Generated: report.pdf")

!pip install fpdf # Install the fpdf library

import csv
from fpdf import FPDF

# Sample Data File (data.csv)
csv_data = """Name,Marks
Alice,85
Bob,90
Charlie,78
David,92
Emma,88"""

# Save sample data to a file
with open("data.csv", "w") as file:
    file.write(csv_data)

# Function to read and analyze data
def analyze_data(file_path):
    total_marks = 0
    num_students = 0
    data = []

    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            name, marks = row
            marks = int(marks)
            data.append((name, marks))
            total_marks += marks
            num_students += 1

    avg_marks = total_marks / num_students if num_students else 0
    return data, total_marks, avg_marks

# Function to generate PDF report
def generate_pdf(data, total_marks, avg_marks):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=16)

    pdf.cell(200, 10, "Student Marks Report", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", size=12)
    pdf.cell(40, 10, "Name", 1)
    pdf.cell(40, 10, "Marks", 1)
    pdf.ln()

    for name, marks in data:
        pdf.cell(40, 10, name, 1)
        pdf.cell(40, 10, str(marks), 1)
        pdf.ln()

    pdf.ln(10)
    pdf.cell(40, 10, f"Total Marks: {total_marks}")
    pdf.ln()
    pdf.cell(40, 10, f"Average Marks: {avg_marks:.2f}")

    pdf.output("report.pdf")
    print("PDF Report Generated: report.pdf")

# Run the script
data, total_marks, avg_marks = analyze_data("data.csv")
generate_pdf(data, total_marks, avg_marks)
import os
print(os.getcwd())

from google.colab import files
files.download("report.pdf")
