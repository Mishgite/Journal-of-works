from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


def get_jobs_from_db():
    conn = sqlite3.connect('db/mars_explorer.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jobs")
    jobs = cursor.fetchall()
    conn.close()
    return jobs


@app.route('/')
def display_jobs():
    jobs = get_jobs_from_db()
    return render_template('jobs.html', jobs=jobs)

if __name__ == '__main__':
    app.run(debug=True)
