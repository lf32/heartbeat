from flask import Flask
from flask import render_template
from flask import request
from flask import url_for

from tools import b64e
from tools import b64d
from tools import r13e
from tools import r13d
from tools import urle
from tools import urld

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
    output = None
    cracker = str(request.form["crypto"])
    text = request.form["text_input"]

    if cracker == "b64e":
      output = b64e(text)
    elif cracker == "b64d":
      output = b64d(text)
    elif cracker == "r13e":
      output = r13e(text)
    elif cracker == "r13d":
      output = r13d(text)
    elif cracker == "urle":
      output = urle(text)
    elif cracker == "urld":
      output = urld(text)

    if output:
      return render_template('c.html', result = {
        "text": text,
        "output": output
        })

  return render_template('c.html')


@app.route("/s", methods=["GET", "POST"])
def s():
  if request.method == "POST":
    print(request)
  return render_template('s.html')


if __name__ == "__main__":
  app.run(debug=False)