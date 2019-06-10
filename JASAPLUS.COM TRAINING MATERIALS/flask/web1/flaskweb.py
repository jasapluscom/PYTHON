#!/usr/bin/env python3
'''
flaskweb.py

sample flask for python3 training
www.jasaplus.com
www.ringlayer.com
'''

from flask import Flask, render_template
app = Flask(__name__)

#register a decorator for uri : /
@app.route("/")
def Home():
    return render_template("home.html")

#register a decorator for uri : /about
@app.route("/about")
def About():
    return render_template("about.html")

#register a decorator for uri : /contact
@app.route("/contact")
def Contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(port=8888)
