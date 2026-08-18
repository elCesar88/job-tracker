# JobTracker

This code creates a list of jobs that I have applied to, it helps me keep track of my job applications.

## Features

- Add new application
- Edit existing application
- Delete application
- List all my current applications and the status of each

## Tech stack

- **Backend:** Python, Flask
- **Database:** SQLite (raw SQL via `sqlite3`, no ORM)
- **Templating:** Jinja2
- **Styling:** hand-written CSS

## Screenshot

[you'll add this after — see note below]

## Running it locally

```bash
git clone https://github.com/elCesar88/job-tracker.git
cd job-tracker
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
flask --app app run --debug
```

## Live demo

[link goes here once deployed — next step]

## What I learned

- Flask routing, how to comunicate between my pages
- Parameterized SQL queries
- How to debug following the errors showd by the browser or the terminal
- Proper page styling