from pathlib import Path

import pandas as pd

from functions import (
    assign_grade,
    calculate_average_marks,
    calculate_total_marks,
    evaluate_student_status,
    get_subject_averages,
    get_summary_metrics,
)

DATA_PATH = Path(__file__).resolve().parent / "students.csv"
SUBJECT_COLUMNS = ["Mathematics", "Physics", "Chemistry", "Biology", "English"]


def load_student_data():
    """Read the CSV dataset and convert required columns to numeric values."""
    data = pd.read_csv(DATA_PATH)
    for subject in SUBJECT_COLUMNS:
        data[subject] = pd.to_numeric(data[subject], errors="coerce")
    data["Attendance"] = pd.to_numeric(data["Attendance"], errors="coerce")
    return data


def process_student_data(student_data):
    """Compute totals, averages, grades, and pass/fail results for each student."""
    for index, row in student_data.iterrows():
        total_marks = calculate_total_marks(row, SUBJECT_COLUMNS)
        average_marks = calculate_average_marks(total_marks, len(SUBJECT_COLUMNS))
        student_data.at[index, "Total Marks"] = round(total_marks, 2)
        student_data.at[index, "Average Marks"] = round(average_marks, 2)
        student_data.at[index, "Grade"] = assign_grade(average_marks)
        student_data.at[index, "Pass/Fail"] = evaluate_student_status(average_marks, row["Attendance"])
    return student_data


def display_summary(student_data):
    """Display a readable summary of the dataset and key insights."""
    print("=" * 70)
    print("STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 70)
    print("\nStudent dataset preview:\n")
    print(student_data.head(10).to_string(index=False))

    summary = get_summary_metrics(student_data)
    print("\nPerformance Summary:")
    print(f"Total Students: {summary['total_students']}")
    print(f"Overall Class Average: {summary['overall_average']}")
    print(f"Highest Average Marks: {summary['highest_average']}")
    print(f"Lowest Average Marks: {summary['lowest_average']}")
    print(f"Pass Count: {summary['pass_count']}")
    print(f"Fail Count: {summary['fail_count']}")
    print(f"Pass Rate: {summary['pass_rate']}%")

    subject_averages = get_subject_averages(student_data, SUBJECT_COLUMNS)
    print("\nSubject-wise Performance:")
    for subject, value in subject_averages.items():
        print(f"{subject}: {value}")
    best_subject = max(subject_averages, key=subject_averages.get)
    print(f"Best-performing subject: {best_subject} ({subject_averages[best_subject]})")

    top_students = student_data.sort_values(by="Average Marks", ascending=False).head(3)
    print("\nTop-performing students:")
    print(top_students[["Student ID", "Name", "Department", "Average Marks", "Grade"]].to_string(index=False))

    print("\nGrade Distribution:")
    for grade, count in student_data["Grade"].value_counts().sort_index().items():
        print(f"Grade {grade}: {count}")

    print("\nPass/Fail Distribution:")
    passed = student_data[student_data["Pass/Fail"] == "Pass"].shape[0]
    failed = student_data[student_data["Pass/Fail"] == "Fail"].shape[0]
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")

    print("\nFinal performance analysis complete.")


def main():
    """Run the analytics pipeline."""
    student_data = load_student_data()
    student_data = process_student_data(student_data)
    display_summary(student_data)


if __name__ == "__main__":
    main()
