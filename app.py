from flask import Flask, render_template, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'jobs'

mysql = MySQL(app)


@app.route("/")
def index():
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, title, location, salary FROM job_info")
    jobs = cur.fetchall()
    cur.close()

    
    jobs_list = [{'id': job[0], 'title': job[1], 'location': job[2], 'salary': job[3]} for job in jobs]

    return render_template("home.html", jobs=jobs_list)

@app.route("/api/jobs")
def list_jobs():
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, title, location, salary FROM job_info")
    jobs = cur.fetchall()
    cur.close()

    
    jobs_list = [{'id': job[0], 'title': job[1], 'location': job[2], 'salary': job[3]} for job in jobs]

    return jsonify(jobs_list)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
