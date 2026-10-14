# Project Documentation

## Objective
The Student Performance Analytics System is designed to analyze student records and provide a clear understanding of academic performance. It helps identify high achievers, weak areas, and overall class performance trends.

## Dataset
The project uses a CSV dataset containing student details such as:

- Student ID
- Name
- Department
- Subject marks (Mathematics, Physics, Chemistry, Biology, English)
- Attendance

## Implementation Details

### 1. Loading Data
The dataset is loaded using the Pandas library.

### 2. Data Processing
The following tasks are completed for each student:

- Total mark calculation
- Average mark calculation
- Grade assignment
- Pass/fail evaluation

### 3. Use of NumPy and Pandas
- Pandas is used to read and manage the dataset and create a DataFrame.
- NumPy is used for numerical calculations like mean values.

### 4. Reusable Functions
Functions were created to keep the code organized and reusable. These functions include:

- total marks calculation
- average calculation
- grade assignment
- pass/fail evaluation
- subject-wise average analysis
- summary metrics

### 5. Output and Analysis
The system generates results such as:

- overall average
- highest and lowest average marks
- pass percentage
- subject-wise averages and the best-performing subject
- top-performing students
- grade distribution

## Grading and Pass/Fail Rules

Grades are assigned from each student's average across five subjects:

- A: 85 or above
- B: 70 to less than 85
- C: 55 to less than 70
- D: 40 to less than 55
- F: below 40

A student passes when their average is at least 50 and attendance is at least 75%. Students who do not meet both conditions fail.

## Final Outcome
This project is useful for teachers and academic coordinators because it converts raw marks into meaningful insights. The final output is easy to understand and can be expanded further for future reporting and dashboards.

## Conclusion
The project demonstrates practical usage of Python data analysis with NumPy and Pandas while following the assignment requirements.
