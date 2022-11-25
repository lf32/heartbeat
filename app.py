#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import glob
import hashlib
import json
import os
import re
import time

from flask import Flask, render_template, request, jsonify, \
    send_from_directory, redirect, url_for, make_response, Response
from tools.stegnography import file_ripper
from werkzeug.utils import secure_filename
from forms import cForm, sForm


app = Flask(__name__)

app.config.update(dict(
  SECRET_KEY = os.urandom(32),
  WTF_CSRF_SECRET_KEY = os.urandom(32)
))

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = ["jpeg", "png", "bmp",
                      "gif", "tiff", "jpg", "jfif", "jpe", "tif"]


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
  form = cForm()
  output = None
  if request.method == "POST":
    if form.validate_on_submit():
      cracker = request.form["choices"]
      text = request.form["text"]
      print(type(text))
      print(type(cracker))
  
      if cracker == "b64e":
        output = tools.b64e(text)
      elif cracker == "b64d":
        output = tools.b64d(text)
      elif cracker == "hexe":
        output = tools.hexe(text)
      elif cracker == "hexd":
        output = tools.hexd(text)
      elif cracker == "r13e":
        output = tools.r13e(text)
      elif cracker == "r13d":
        output = tools.r13d(text)
      elif cracker == "urle":
        output = tools.urle(text)
      elif cracker == "urld":
        output = tools.urld(text)

      return render_template('c.html', result = {
        "text": text,
        "output": output,
        "form": cForm()
        })

  return render_template('c.html', result={
    "form": form
    })


@app.route("/s", methods=["GET", "POST"])
def s():
  form = sForm()
  if request.method == "POST":
    if form.validate_on_submit():
      if not request.files["file"]:
          return jsonify({"Error": "File not found."})
      else:
        file = request.files["file"]
        print(file)
        ext = str(os.path.splitext(file.filename)[1].lower().lstrip("."))
        if ext not in ALLOWED_EXTENSIONS:
            return jsonify({"Error": f"Invalid extension: {ext}"})
    
        # calculate input file hash
        file_name = secure_filename(file.filename)
        hash_file = str(hashlib.md5(file.read()).hexdigest())

        return render_template('s.html', result={
          "form": form,
          "output": {
            "file_name": file_name,
            "hash_file": hash_file
          }
          })
  return render_template('s.html', result={
    "form":form
    })


@app.route("/ctf", methods=["GET"])
def ctf():
  import requests
  import markdown

  url = "https://raw.githubusercontent.com/apsdehal/awesome-ctf/master/README.md"
  stat = requests.get(url)
  text = markdown.markdown(stat.text)
  return render_template("ctf.html", result={
    "text":text
    })

if __name__ == "__main__":
  app.run('0.0.0.0', port=5000, debug=True)
