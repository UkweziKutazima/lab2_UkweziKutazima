# Lab 2: ALU Transcript Generator


## What this does
This project has two parts. First, a Python script reads a CSV file with student grades and does the math to find their GPA and if they passed or failed. Second, a Bash script organizes the files by moving the old grade file to an archive folder so it's ready for new grades.


## The Files
  **grade-evaluator.py**: This is the Python code. It checks the grades and weights, calculates the GPA, and finds assignments to resubmit if the student failed.
  **grades.csv**: The file with the student's scores and weights.
  **organizer.sh**: The Bash script. It moves grades.csv into a folder called archive with a date on the name, makes a new empty grades.csv, and writes a note in a log file.
  **organizer.log**: A text file that keeps track of when files were archived.
## How to run it
Open your terminal in this folder.


**1. To run the Python code:**
bash
python3 grade-evaluator.py
