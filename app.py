from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': "Data Analyst",
        'location': "Delhi",
        'salary': "Rs 10,00,000"
    },
    {
        'id': 2,
        'title': "Data Scientist",
        'location': "Mumbai",
        'salary': "Rs 12,00,000"
    },
    {
        'id': 3,
        'title': "Web Developer Analyst",
        'location': "Hyderabad",
        'salary': "Rs 9,00,000"
    },
    {
        'id': 4,
        'title': "Frontend Engineer",
        'location': "Delhi",
        'salary': "Rs 12,00,000"
    }
]
@app.route("/")
def index():
    return render_template("home.html", jobs = JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)