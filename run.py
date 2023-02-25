import os
from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


# The page_title variabl is used to send the content to the actual
# frontend page on each of the sites, we have created a reference
# to this jinja template. 
@app.route("/about")
def about():
    data = []
    # python will open the file company RO and assing it to json_data
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
