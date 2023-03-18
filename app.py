from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'salary': 'Rs. 10,00,000',
  'location': 'Bangalore, India'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'salary': 'Rs. 15,00,000',
  'location': 'Delhi, India'
}, {
  'id': 3,
  'title': 'Frontend Intern',
  'stipend': 'Rs. 20000/month',
  'location': 'Remote'
}, {
  'id': 4,
  'title': 'Software Developer',
  'salary': '220000 AUD',
  'location': 'Canberra, Australia'
}]


@app.route("/")
def hello():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if (__name__) == "__main__":
  app.run(host='0.0.0.0', debug=True)
