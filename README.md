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
python main.py
```

If PowerShell blocks virtual environment activation, install and run without activating it:

```powershell
python -m pip install -r requirements.txt
python main.py
```

## Run on macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

## Grading Rules

- **A:** average marks of 85 or above
- **B:** average marks of 70 to less than 85
- **C:** average marks of 55 to less than 70
- **D:** average marks of 40 to less than 55
- **F:** average marks below 40
- **Pass:** average marks of at least 50 **and** attendance of at least 75%
- Otherwise, the student is marked **Fail**.

## Publish to GitHub

1. Create a new, empty repository on GitHub. Do not initialize it with a README or other files.
2. In PowerShell, from this project folder, connect the local repository and push:

```powershell
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git add .
git commit -m "Add student performance analytics project"
git push -u origin main
```

Replace `YOUR-USERNAME` and `YOUR-REPOSITORY` with your GitHub details. GitHub may ask you to authenticate when you push.

## Technologies

- Python
- Pandas
- NumPy

This is a data-analysis project; it does not require advanced machine learning.
