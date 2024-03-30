import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os
import numpy as np
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(script_dir, "../calculator"))
from calculate_gpa import calculate_gpa
from calculate_score import calculate_score



class ExchangeScoreCalculator:
    def __init__(self, master, courses, course_data):
        self.master = master
        self.master.title("Exchange Score Calculator")

        self.course_data = course_data

        self.course_label = ttk.Label(master, text="Select your course:")
        self.course_label.grid(row=0, column=0, padx=10, pady=10)

        self.course_var = tk.StringVar()
        self.course_dropdown = ttk.Combobox(master, textvariable=self.course_var)
        self.course_dropdown['values'] = courses
        self.course_dropdown.grid(row=0, column=1, padx=10, pady=10)
        self.course_dropdown.bind("<<ComboboxSelected>>", self.on_course_select)

        self.frame = ttk.Frame(master)
        self.frame.grid(row=1, column=0, columnspan=2)

        self.grade_labels = []
        self.grade_entries = []

        self.calculate_button = ttk.Button(master, text="Calculate Score", command=self.calculate_score)
        self.calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def on_course_select(self, event):
        selected_course = self.course_var.get()
        self.course_data_subset = self.course_data[self.course_data['Course'] == selected_course]
        self.create_grade_fields()

    def create_grade_fields(self):
        # Remove existing labels and entries
        for label, entry in zip(self.grade_labels, self.grade_entries):
            label.grid_forget()
            entry.grid_forget()

        self.grade_labels.clear()
        self.grade_entries.clear()

        # Create labels and entries for each exam in course_data
        exams = list(self.course_data_subset['Exam'])
        seminars = np.array(self.course_data_subset['seminar'])

        for i, (exam, seminar) in enumerate(zip(exams, seminars)):
            label = ttk.Label(self.frame, text=f"{exam}")
            label.grid(row=i, column=0, padx=10, pady=5)

            # If it's a seminar, create a dropdown menu for pass/no-pass
            if seminar == 1:
                pass_var = tk.StringVar()
                pass_dropdown = ttk.Combobox(self.frame, textvariable=pass_var, values=["Pass", "No-pass"])
                pass_dropdown.grid(row=i, column=1, padx=10, pady=5)
                pass_dropdown.current(0)  # Set default value to "Pass"
                self.grade_entries.append(pass_dropdown)
            else:
                entry = tk.Entry(self.frame)
                entry.grid(row=i, column=1, padx=10, pady=5)
                self.grade_entries.append(entry)

        self.grade_labels.append(label)

    def calculate_score(self):
        all_grades = []  # List to store all grades
        
        for entry in self.grade_entries:
            # For seminar exams, convert "Pass" to 30 and "No-pass" to 0
            if isinstance(entry, ttk.Combobox):
                grade = 30 if entry.get() == "Pass" else 0
            else:
                grade = entry.get()
                if not grade.isdigit():
                    messagebox.showerror("Error", "Grades must be integers.")
                    return
                grade = int(grade)

                if (grade != 0 and (grade < 18 or grade > 31)):
                    print(grade != 0)
                    print(grade < 18 or grade > 31 )

                    messagebox.showerror("Error", f"Grades must be either 0 or an integer between 18 and 31. {grade} doesn't satisfy the requirement.")
                    return
            
            all_grades.append(grade)

        grades = np.array(all_grades)
        
        # Check if all grades have been inserted
        if len(all_grades) != len(self.grade_entries):
            messagebox.showerror("Error", "Please insert grades for all exams.")
            return



def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    courses_path = '../../data/raw/courses.txt'

    # Construct the relative path to the file
    total_courses_path = os.path.join(script_dir, courses_path)

    with open(total_courses_path, 'r') as file:
        # Read lines and strip newline characters
        lines = [line.strip() for line in file]

    # Now 'lines' contains each element from the text file as a separate string
    # Convert it into a list
    courses = list(lines)
    courses = sorted(courses)

    course_data_path = '../../data/processed/processed_course_data.csv'
    total_course_data_path = os.path.join(script_dir, course_data_path)
    course_data = pd.read_csv(total_course_data_path)

    root = tk.Tk()
    app = ExchangeScoreCalculator(root, courses, course_data)
    root.mainloop()

if __name__ == "__main__":
    main()