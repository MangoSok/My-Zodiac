from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin


app = Flask(__name__)

CORS(app)

def find_zodiac(date):
    if not (len(date) == 5):
        return "Wrong input. Try again."
        
    month = int(date[0:2])
    day = int(date[3:5])
        
    if (month == 3 and day > 20) or (month == 4 and day < 20):
        f = open("data/aries.txt", "r")
        text = f.read()
        f.close()
        return text
    elif (month == 4 and day > 19) or (month == 5 and day < 21):
        f = open("data/taurus.txt","r")
        text = f.read()
        f.close()
        return text
    elif (month == 5 and day > 20) or (month == 6 and day < 22):
        f = open("data/gemini.txt","r")
        text = f.read()
        f.close()
        return text
    elif (month == 6 and day > 21) or (month == 7 and day < 23):
        f = open("data/cancer.txt","r")
        text = f.read()
        f.close()
        return text
    elif (month == 7 and day > 22) or (month == 8 and day < 23):
        f = open("data/leo.txt","r")
        text = f.read()
        f.close()
        return text
    elif (month == 8 and day > 22) or (month == 9 and day < 23):
        f = open("data/virgo.txt","r")
        text = f.read()
        f.close()
        return text
    elif (month == 9 and day > 22) or (month == 10 and day < 24):
        f = open("data/libra.txt","r")
        text = f.read()
        f.close()
        return text
    elif (month == 10 and day > 23) or (month == 11 and day < 22):
        f = open("data/scorpio.txt","r")
        text = f.read()
        f.close()
        return text
    elif (month == 11 and day > 21) or (month == 12 and day < 22):
        f = open("data/sagittar.txt","r")
        text = f.read()
        f.close()
        return text
    elif (month == 12 and day > 21) or (month == 1 and day < 20):
        f = open("data/capricorn.txt","r")
        text = f.read()
        f.close()
        return text
    elif (month == 1 and day > 19) or (month == 2 and day < 19):
        f = open("data/aquarius.txt","r")
        text = f.read()
        f.close()
        return text
    elif (month == 2 and day > 18) or (month == 3 and day < 21):
        f = open("data/pisces.txt","r")
        text = f.read()
        f.close()
        return text
    else:
        return "Wrong input. Try again."


@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/a")
def say_bye():
    return "<h1>Good Night!</h1>"


@app.route("/data")
def data():
    info = {"name" : "Tom", "age" : 10}

    return info


@app.route("/zodiac")
def zodiac_sign():
    date = request.args.get("date")
    sign = find_zodiac(date)
    f = open("data/comment.txt","r")
    text = f.read()
    f.close()
    comment = text

    return {"sign" : sign, "comment" : comment}


app.run(port=5000, host="0.0.0.0")