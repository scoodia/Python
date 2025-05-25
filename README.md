# Job Hunting Assistant

This project provides a simple Python package that helps users find relevant job
postings, optimise their resumes and prepare for interviews. It is a minimal
example and uses only the Python standard library so it can run without
additional dependencies.

## Features

- **User Profile Ingestion** – load resume text and preferences.
- **Job Posting Matching** – match resumes to job descriptions using keyword
  overlap.
- **Resume Optimisation** – suggest keywords to include in a resume.
- **Interview Preparation** – generate sample technical and behavioural
  questions.

The entry point `main.py` demonstrates a basic command line interface. Run it
with the path to a text resume:

```bash
python main.py path/to/resume.txt
```

Example job postings are stored in `jobhunt/data/jobs.json`.
