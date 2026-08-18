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

![screenshot](docs/screenshot.png)

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

(https://job-tracker-hjxm.onrender.com/)

## Deploying

Deployed on Render's free tier. Note: free instances spin down after 15
minutes of inactivity (the first request after that takes ~30-60s to wake
up), and the SQLite database resets on every redeploy since the free tier
doesn't have persistent disk. This deployment is for demoing the app —
the local version is what I actually use to track my own applications.

## What I learned

- Flask routing, how to communicate between my pages
- Parameterized SQL queries
- How to debug following the errors shown by the browser or the terminal
- Proper page styling