import os
# the request module is needed to handle the form data
# the flash module is used to display "flash" messages
from flask import Flask, render_template, request, flash
import json
# we only want to import the env, if there is and env.py file available
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
# we assign the secret key, created in the env.py file,
# to the app.secret_key var
app.secret_key = os.environ.get("SECRET_KEY")


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


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    # the first member in the arguments stands for the member.html and the
    # second member tands for the member var we have created in this method
    return render_template("member.html", member=member)


# We need to tell this view, that GET and POST methods will be alllowed
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # the name variable will be retreived from the name attribute
        # which we have set in the form elements on the contact.html
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
