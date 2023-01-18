# https://www.twilio.com/docs/usage/tutorials/how-to-set-up-your-python-and-flask-development-environment
# from flask import Flask
# app = Flask(__name__)
#
# @app.route("/")
# def hello():
#   return "Hello World!"
#
# if __name__ == "__main__":
#   app.run()
#


# https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
  # return "Hello, World!"
  context = {
      'message': 'Helloooo',
      'message2': 'Hello again',
  }
  return render_template("home.html", **context)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/salvador")
def salvador():
  return "Hello, Salvador"


if __name__ == "__main__":
  app.run(debug=True)


# https://www.codecademy.com/learn/learn-flask/modules/flask-templates-and-forms/cheatsheet
# https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3/
