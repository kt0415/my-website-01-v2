from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job, add_application_to_db

app = Flask(__name__)


@app.route("/")
def hello():
  JOBS = load_jobs_from_db()
  return render_template('home.html', jobs=JOBS)

@app.route("/features")
def features():
    return render_template('features.html')

@app.route("/courses")
def pricing():
    return render_template('pricing.html')

@app.route("/api/jobs")
def list_jobs():
  JOBS = load_jobs_from_db()
  return jsonify(JOBS)


@app.route("/job/<id>")
def show_job(id):
  job = load_job(id)
  if not job:
    return "Not Found", 404
  return render_template('jobpage.html', job=job)


@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  data = request.form
  job = load_job(id)

  add_application_to_db(id, data)
  return render_template('application_submitted.html',
                         application=data,
                         job=job)


if (__name__) == "__main__":
  app.run(host='0.0.0.0', debug=True)
