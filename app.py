from flask import Flask, render_template
app = Flask(__name__)
JOBS = [
  {
    "id": 1,
    "title": "Analyst",
    "location": "San Marcos, TX",
    "salary": "$ 1000"
  },
  {
    "id": 2,
    "title": "Data Scientist",
    "location": "San Antonio, TX",
    "salary": "$ 3000"
  },
  {
    "id": 3,
    "title": "FrontEnd Engineer",
    "location": "Austin, TX",
    "salary": "$ 10 000"
  },
  {
    "id": 4,
    "title": "FrontEnd Engineer",
    "location": "Austin, TX",
  }
]


@app.route("/")
def Jovian():
  return render_template('home.html', jobs = JOBS, company_name = "Nitty_girtty")

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  