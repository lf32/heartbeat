from flask import Flask
from flask import render_template
from flask import request
from flask import url_for

app = Flask(__name__)

@app.route("/", methods=["GET"])
def greet():
  return render_template('index.html')


@app.route("/r", methods=["GET", "POST"])
def r():
  if request.method == "POST":
    print(request)

  return render_template('r.html')


@app.route("/c", methods=["GET", "POST"])
def c():
  if request.method == "POST":
      cracker = request.form["crypto"]
      text = request.form["text_input"]

  return render_template('c.html')


@app.route("/s", methods=["GET", "POST"])
def s():
  if request.method == "POST":
    print(request)
  return render_template('s.html')


if __name__ == "__main__":
  app.run(debug=False)