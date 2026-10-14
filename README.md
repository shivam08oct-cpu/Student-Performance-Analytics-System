# Student Performance Analytics System

This project analyzes student marks and attendance using Python, NumPy, and Pandas. It calculates totals, averages, grades, pass/fail status, class statistics, subject averages, and top performers.

## Features

- A sample CSV dataset containing 20 student records
- Student-wise total marks, average marks, grades, and pass/fail status
- Overall class average, highest and lowest averages, and pass rate
- Subject-wise averages and the highest-performing subject
- Top three students and grade distribution

## Project Structure

| File | Purpose |
| --- | --- |
| `main.py` | Loads the dataset, processes it, and displays the analysis |
| `functions.py` | Reusable calculation and analysis functions |
| `app.py` | Flask web application |
| `templates/index.html` | Dashboard page |
| `static/` | Dashboard styling and student-table filters |
| `render.yaml` | Render deployment configuration |
| `students.csv` | Sample student dataset |
| `requirements.txt` | Python dependencies |
| `Project_Documentation.md` | Project objectives, implementation, and outcome |
| `.gitignore` | Excludes local and generated files from Git |

## Requirements

- Python 3.9 or later
- pip

## Run on Windows

Open PowerShell in the project folder and run:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Then open **http://127.0.0.1:5000** in your browser. The dashboard reads the included CSV and calculates its results when the page loads.

To run the original command-line report instead:

```powershell
python main.py
```

## Run on macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

Open **http://127.0.0.1:5000** in your browser. To run the command-line report instead, use `python main.py`.

## Grading Rules

- **A:** average marks of 85 or above
- **B:** average marks of 70 to less than 85
- **C:** average marks of 55 to less than 70
- **D:** average marks of 40 to less than 55
- **F:** average marks below 40
- **Pass:** average marks of at least 50 **and** attendance of at least 75%
- Otherwise, the student is marked **Fail**.

## Publish to GitHub

Push your latest local changes to the existing GitHub repository:

```powershell
git add .
git commit -m "Prepare dashboard for public deployment"
git push
```

## Deploy the Website Publicly

This project includes a Render Blueprint configuration in `render.yaml`.

1. Sign in to [Render](https://render.com/) and choose **New + → Blueprint**.
2. Connect your GitHub account if asked, and select `Student-Performance-Analytics-System`.
3. Review the service named `student-performance-analytics`, then click **Apply**.
4. Wait for the deploy to finish. Render will show the public `onrender.com` URL for your website.

The Blueprint runs the app using Gunicorn, checks that `/` is healthy, and uses Render's free web-service plan. Free services may sleep when inactive and take a short time to wake on the next visit.

To update the public site after making changes, push to GitHub:

```powershell
git add .
git commit -m "Update student analytics dashboard"
git push
```

## Technologies

- Python
- Pandas
- NumPy
- Flask

This is a data-analysis project; it does not require advanced machine learning.
