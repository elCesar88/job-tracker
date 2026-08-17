import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "application.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            role TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Applied',
            date_applied TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def add_application(company, role, status, date_applied):
    conn = get_connection()
    conn.execute(
        "INSERT INTO applications (company, role, status, date_applied) VALUES (?, ?, ?, ?)",
        (company, role, status, date_applied)
    )
    conn.commit()
    conn.close()


def get_all_applications():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM applications").fetchall()
    conn.close()
    return [dict(row) for row in rows]


0


def get_application(app_id):
    conn = get_connection()
    row = conn.execute(
        "SELECT * FROM applications WHERE id = ?", (app_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def update_application(app_id, company, role, status, date_applied):
    conn = get_connection()
    conn.execute(
        "UPDATE applications SET company = ?, role = ?, status = ?, date_applied = ? WHERE id = ? ",
        (company, role, status, date_applied, app_id)
    )
    conn.commit()
    conn.close()


def delete_application(app_id):
    conn = get_connection()
    conn.execute("DELETE FROM applications WHERE id = ? ", (app_id,))
    conn.commit()
    conn.close()
