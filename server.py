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
        return "Taurus - Bull <br>Element: Earth<br>Color: Green, Pink<br>Quality: Fixed<br>Day: Friday, Monday<br>Ruler: Venus<br>Greatest Overall Compatibility: Scorpio, Cancer<br>Lucky Numbers: 2, 6, 9, 12, 24<br>Dates: April 20 - May 20<br><br>Strengths: Reliable, patient, practical, devoted, responsible, stable<br>Weaknesses: Stubborn, possessive, uncompromising<br>Taurus likes: Gardening, cooking, music, romance, high quality clothes, working with hands<br>Taurus dislikes: Sudden changes, complications, insecurity of any kind, synthetic fabrics"
    elif (month == 5 and day > 20) or (month == 6 and day < 22):
        return "Gemini - Twins <br>Element: Air<br>Color: Light-Green, YellowQuality: Mutable<br>Day: Wednesday<brRuler: Mercury<br>Greatest Overall Compatibility: Sagittarius, Aquarius<br>Lucky Numbers: 5, 7, 14, 23<br>Dates: May 21 - June 20<br><br>Strengths: Gentle, affectionate, curious, adaptable, ability to learn quickly and exchange ideas<br>Weaknesses: Nervous, inconsistent, indecisive<br>Gemini likes: Music, books, magazines, chats with nearly anyone, short trips around the town<br>Gemini dislikes: Being alone, being confined, repetition and routine"
    elif (month == 6 and day > 21) or (month == 7 and day < 23):
        return "Cancer - Crab <br>Element: Water<br>Color: White<br>Quality: Cardinal<br>Day: Monday, Thursday<br>Ruler: Moon<br>Greatest Overall Compatibility: Capricorn, Taurus<br>Lucky Numbers: 2, 3, 15, 20<br>Dates: June 21 - July 22<br><br>Strengths: Tenacious, highly imaginative, loyal, emotional, sympathetic, persuasive<br>Weaknesses: Moody, pessimistic, suspicious, manipulative, insecure<br>Cancer likes: Art, home-based hobbies, relaxing near or in water, helping loved ones, a good meal with friends<br>Cancer dislikes: Strangers, any criticism of Mom, revealing of personal life"
    elif (month == 7 and day > 22) or (month == 8 and day < 23):
        return "Leo - Lion <br>Element: Fire<br>Color: Gold, Yellow, Orange<br>Quality: Fixed<br>Day: Sunday<br>Ruler: Sun<br>Greatest Overall Compatibility: Aquarius, Gemini<br>Lucky Numbers: 1, 3, 10, 19<br>Dates: July 23 - August 22<br><br>Strengths: Creative, passionate, generous, warm-hearted, cheerful, humorous<br>Weaknesses: Arrogant, stubborn, self-centered, lazy, inflexible<br>Leo likes: Theater, taking holidays, being admired, expensive things, bright colors, fun with friends<br>Leo dislikes: Being ignored, facing difficult reality, not being treated like a king or queen"
    elif (month == 8 and day > 22) or (month == 9 and day < 23):
        return "Virgo - Virgin <br>Element: Earth<br>Color: Grey, Beige, Pale-Yellow<br>Quality: Mutable<br>Day: Wednesday<br>Ruler: Mercury<br>Greatest Overall Compatibility: Pisces, Cancer<br>Lucky Numbers: 5, 14, 15, 23, 32<br>Dates: August 23 – September 22<br><br>Strengths: Loyal, analytical, kind, hardworking, practical<br>Weaknesses: Shyness, worry, overly critical of self and others, all work and no play<br>Virgo likes: Animals, healthy food, books, nature, cleanliness<br>Virgo dislikes: Rudeness, asking for help, taking center stage"
    elif (month == 9 and day > 22) or (month == 10 and day < 24):
        return "Libra - Balance <br>Element: AirColor: Pink, Green<br>Quality: Cardinal<br>Day: Friday<br>Ruler: Venus<br>Greatest Overall Compatibility: Aries, Sagittarius<br>Lucky Numbers: 4, 6, 13, 15, 24<br>Dates: September 23 - October 22<br<br>>Strengths: Cooperative,diplomatic, gracious, fair-minded, social<br>Weaknesses: Indecisive, avoids confrontations, will carry a grudge, self-pity<br>Libra likes: Harmony, gentleness, sharing with others, the outdoors<br>Libra dislikes: Violence, injustice, loudmouths, conformity"
    elif (month == 10 and day > 23) or (month == 11 and day < 22):
        return "Scorpiis - Scorpion <br>Element: Water<br>Color: Scarlet, Red, Rust<br>Quality: Fixed<br>Day: Tuesday<br>Ruler: Pluto, Mars<br>Greatest Overall Compatibility: Taurus, Cancer<br>Lucky Numbers: 8, 11, 18, 22<br>Dates: October 23 - November 21<br><br>Strengths: Resourceful, powerful, brave, passionate, a true friend<br>Weaknesses: Distrusting, jealous, manipulative, violent<br>Scorpio likes: Truth, facts, being right, talents, teasing, passion<br>Scorpio dislikes: Dishonesty, revealing secrets, superficiality, small talk"
    elif (month == 11 and day > 21) or (month == 12 and day < 22):
        return "Sagittarius - Archer <br>Element: Fire<br>Color: Blue<br>Quality: Mutable<br>Day: Thursday<br>Ruler: Jupiter<br>Greatest Overall Compatibility: Gemini, Aries<br>Lucky Numbers: 3, 7, 9, 12, 21<br>Dates: November 22 - December 21<br><br>Strengths: Generous, idealistic, great sense of humor<br>Weaknesses: Promises more than can deliver, very impatient, will say anything no matter how undiplomatic<br>Sagittarius likes: Freedom, travel, philosophy, being outdoors<br>Sagittarius dislikes: Clingy people, being constrained, off-the-wall theories, details"
    elif (month == 12 and day > 21) or (month == 1 and day < 20):
        return "Carpricornus - Goat <br>Element: Earth<br>Color: Brown, Black<br>Quality: Cardinal<br>Day: Saturday<br>Ruler: Saturn<br>Greatest Overall Compatibility: Taurus, Cancer<br>Lucky Numbers: 4, 8, 13, 22<br>Dates: December 22 - January 19<br><br>Strengths: Responsible, disciplined, self-control, good managers<br>Weaknesses: Know-it-all, unforgiving, condescending, expecting the worst<br>Capricorn likes: Family, tradition, music, understated status, quality craftsmanship<br>Capricorn dislikes: Almost everything at some point"
    elif (month == 1 and day > 19) or (month == 2 and day < 19):
        return "Aquarius - Water Bearer <br>Element: Air<br>Color: Light-Blue, Silver<br>Quality: Fixed<br>Day: Saturday<br>Ruler: Uranus, Saturn<br>Greatest Overall Compatibility: Leo, Sagittarius<br>Lucky Numbers: 4, 7, 11, 22, 29<br>Dates: January 20 - February 18<br><br>Strengths: Progressive, original, independent, humanitarian<br>Weaknesses: Runs from emotional expression, temperamental, uncompromising, aloof<br>Aquarius likes: Fun with friends, risky business, fighting for causes, intellectual conversations.<br>Aquarius dislikes: Limitations, broken promises, being lonely, dull or boring situations."
    elif (month == 2 and day > 18) or (month == 3 and day < 21):
        return "Pisces - Fish <br>Element: Water<br>Color: Mauve, Lilac, Purple, Violet, Sea green<br>Quality: Mutable<br>Day: Thursday<br>Ruler: Neptune, Jupiter<br>Greatest Overall Compatibility: Virgo, Taurus<br>Lucky Numbers: 3, 9, 12, 15, 18, 24<br>Dates: February 19 - March 20<br><br>Strengths: Compassionate, artistic, intuitive, gentle, wise, musical<br>Weaknesses: Fearful, overly trusting, sad, desire to escape reality, can be a victim or a martyr<br>Pisces likes: Being alone, love, sleeping, music, romance, swimming, spiritual themes<br>Pisces dislikes: Know-it-all, being criticized, the past coming back to haunt, cruelty of any kind"
    else:
        return "Wrong input. Try again. Format (__/__)"


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
    comment = "<br><br>The zodiac is a diagram used by astrologers to represent the positions of the planets and stars. <br>It is divided into twelve sections, each of which has its own name and symbol. <br>The zodiac is used to try to calculate the influence of the planets on people's lives."

    return {"sign" : sign, "comment" : comment}


app.run(port=5000, host="0.0.0.0")