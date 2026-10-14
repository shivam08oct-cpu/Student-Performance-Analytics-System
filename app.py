import os

from flask import Flask, render_template

from main import DATA_PATH, SUBJECT_COLUMNS, load_student_data, process_student_data
from functions import get_subject_averages, get_summary_metrics

app = Flask(__name__)


@app.route("/")
def dashboard():
    """Render the dashboard using the same CSV analysis as the command-line app."""
    student_data = process_student_data(load_student_data())
    summary = get_summary_metrics(student_data)
    subject_averages = get_subject_averages(student_data, SUBJECT_COLUMNS)
    best_subject = max(subject_averages, key=subject_averages.get)

    students = student_data.to_dict(orient="records")
    departments = sorted(student_data["Department"].unique().tolist())
    grade_counts = student_data["Grade"].value_counts().to_dict()
    grade_distribution = [
        {"grade": grade, "count": int(grade_counts.get(grade, 0))}
        for grade in ["A", "B", "C", "D", "F"]
    ]

    return render_template(
        "index.html",
        students=students,
        departments=departments,
        summary=summary,
        subject_averages=subject_averages,
        best_subject=best_subject,
        grade_distribution=grade_distribution,
        data_file=DATA_PATH.name,
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", "5000")),
        debug=False,
    )
