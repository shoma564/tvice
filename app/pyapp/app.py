from flask import Flask, render_template, request
import PIL.Image, PIL.ImageDraw, PIL.ImageFont


app = Flask(__name__)


@app.route('/')
def index():
    global name
    return render_template("index.html", name = name)



@app.route('/name', methods=["POST"])
def name():
    global name

    return render_template("name.html", name = name)

@app.route('/menu')
def menu():
    return render_template("menu.html", player = player)

@app.route('/room')
def room():
    return "roomdaze"

@app.route('/show')
def show():
    message = "hello world"
    return render_template("form.html", message = message)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
