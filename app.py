from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id' : 1,
    'title' : "Co-Founder: Abhijeet Jadhav",
    'location' : "Bengaluru, India",
    'salary' : "Rs. 10,00,000"
  },
  {
    'id' : 2,
    'title' : "Frontend Developer",
    'location' : "Remote",
    
  },
  {
    'id' : 3,
    'title' : "Backend Developer",
    'location' : "San Francisco, USA",
    'salary' : "$150,000"
  }
]

@app.route('/')
def hello_world():
    return render_template('prac.html', jobs=JOBS)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post")
def post():
    return render_template("post.html")

@app.route("/job")
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__' :
  app.run(host='0.0.0.0', debug=True)