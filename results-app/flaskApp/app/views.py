from app import app
from flask import render_template, redirect
from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()


UNAME = os.getenv("UNAME")
PASSWD = os.getenv("PASSWD")
mongohost = os.getenv("MONGO_SERVICE_SERVICE_HOST")


client = MongoClient(f'mongodb://{mongohost}', username=UNAME, password=PASSWD)
db = client['docker']


def db_stuff():
    try:
        col = db['percentages']
        vals = col.find().sort("_id", -1).limit(1)
        for val in vals:
            grades = val
        return grades
    except:
        return {'highest_grade': 'none', 'lowest_grade': 'none', 'avg_grade': 'none'}


@ app.route("/")
def index():
    return redirect("http://localhost:5000/")


@ app.route("/home")
def home():
    try:
        grades = db_stuff()
    except:
        grade = {'highest_grade': 'none', 'lowest_grade': 'none', 'avg_grade': 'none'}

    highest = str(grades['highest_grade'])
    lowest = str(grades['lowest_grade'])
    avg = str(grades['avg_grade'])
    
    return render_template("public/index.html", highest=highest, lowest=lowest, avg=avg)
