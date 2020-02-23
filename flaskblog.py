from flask import Flask, render_template
app = Flask(__name__)

# this is a flaskn project#
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/help")
def help():
    return render_template("help.html")


if __name__ == '__main__':
    app.run(debug=True)