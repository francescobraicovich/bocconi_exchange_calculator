import tkinter as tk
from tkinter import ttk
import pandas as pd
import os

# Define the file path
file_path = '../../data/raw/courses.txt'

# Read the text file
courses_df = pd.read_csv(file_path, )
courses = list(courses_df)

print(courses)

class ExchangeScoreCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Exchange Score Calculator")

        self.course_label = ttk.Label(master, text="Select your course:")
        self.course_label.grid(row=0, column=0, padx=10, pady=10)

        self.course_var = tk.StringVar()
        self.course_dropdown = ttk.Combobox(master, textvariable=self.course_var)
        self.course_dropdown['values'] = courses  
        self.course_dropdown.grid(row=0, column=1, padx=10, pady=10)

        self.grade_labels = []
        self.grade_entries = []

        self.calculate_button = ttk.Button(master, text="Calculate Score", command=self.calculate_score)
        self.calculate_button.grid(row=2, columnspan=2, padx=10, pady=10)

    def calculate_score(self):
        # Add your score calculation logic here
        pass

def main():
    root = tk.Tk()
    app = ExchangeScoreCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()