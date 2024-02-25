from flask import Flask, render_template

app = Flask(__name__)

jobs = [
    {
        'id': 1,
        'job_description': 'Deployment of residential modules 1 and 2 for the crew',
        'team_leader_surname': 'Scott',
        'team_leader_name': 'Ridley',
        'work_size_hours': 15,
        'collaborators': [2, 3],
        'is_finished': False
    },
]


@app.route('/')
def display_jobs():
    return render_template('jobs.html', jobs=jobs)


if __name__ == '__main__':
    app.run(debug=True)
