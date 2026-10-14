import numpy as np


def calculate_total_marks(row, subject_columns):
    """Calculate the total marks scored by a student across all subjects."""
    total = 0.0
    for subject in subject_columns:
        total += float(row[subject])
    return total


def calculate_average_marks(total_marks, number_of_subjects):
    """Return the average mark for a student."""
    if number_of_subjects == 0:
        return 0.0
    return total_marks / number_of_subjects


def assign_grade(average_marks):
    """Assign a letter grade based on the average marks."""
    if average_marks >= 85:
        return "A"
    if average_marks >= 70:
        return "B"
    if average_marks >= 55:
        return "C"
    if average_marks >= 40:
        return "D"
    return "F"


def evaluate_student_status(average_marks, attendance):
    """Determine whether a student has passed the class requirements."""
    if average_marks >= 50 and attendance >= 75:
        return "Pass"
    return "Fail"


def get_subject_averages(student_data, subject_columns):
    """Calculate the mean marks for each subject using NumPy."""
    averages = {}
    for subject in subject_columns:
        values = np.array(student_data[subject].tolist(), dtype=float)
        averages[subject] = round(float(np.mean(values)), 2)
    return averages


def get_summary_metrics(student_data):
    """Return core metrics like class average, highest, lowest, and pass rate."""
    total_students = len(student_data)
    overall_average = round(float(np.mean(student_data["Average Marks"])), 2)
    highest_average = round(float(student_data["Average Marks"].max()), 2)
    lowest_average = round(float(student_data["Average Marks"].min()), 2)
    pass_count = int((student_data["Pass/Fail"] == "Pass").sum())
    fail_count = total_students - pass_count
    pass_rate = round((pass_count / total_students) * 100, 2) if total_students else 0.0

    return {
        "total_students": total_students,
        "overall_average": overall_average,
        "highest_average": highest_average,
        "lowest_average": lowest_average,
        "pass_count": pass_count,
        "fail_count": fail_count,
        "pass_rate": pass_rate,
    }
