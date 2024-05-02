from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv
import os
import datetime  
from site import USER_BASE, USER_SITE
import sqlite3
import json
current_date = datetime.date.today()
current_time = datetime.datetime.now().time()
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for


# Configure application
app = Flask(__name__)


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///students.db")

@app.route("/")
def home(): 
    return render_template("home.html") 

@app.route("/byname1", methods=["GET", "POST"])
def byname1(): 
    if request.method == "POST":
        name = request.form.get('name')
        student = db.execute("SELECT department, major, group_id, number, image FROM students WHERE name = ?", (name,))

        if student:
            department = student[0]["department"]
            major = student[0]["major"]
            group_id = student[0]["group_id"]
            number = student[0]["number"]
            image = student[0]["image"]
            return render_template("byname2.html", name=name, department=department, major=major, group_id=group_id, number=number, image=image)
        else:
            return render_template("byname2failure.html", name=name)
    else:
        return render_template("byname1.html")
@app.route("/byname2", methods=["GET", "POST"])
def byname2(): 
    if request.method == "POST":
        name = request.form.get('name')
        student = db.execute("SELECT department, major, group_id, number, image FROM students WHERE name = ?", (name,))

        if student:
            department = student[0]["department"]
            major = student[0]["major"]
            group_id = student[0]["group_id"]
            number = student[0]["number"]
            image = student[0]["image"]
            return render_template("byname2.html", name=name, department=department, major=major, group_id=group_id, number=number, image=image)
        else:
            return render_template("byname2failure.html", name=name)
    else:
        return render_template("byname1.html")

@app.route("/bycarac1", methods=["GET", "POST"])
def bycarac1(): 
    if request.method == "POST":
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        input_data = request.form.get('characteristics')
        data_array = input_data.split(',')
        
        if len(data_array) == 4:
            department = data_array[0].strip()
            major = data_array[1].strip()
            group_id = data_array[2].strip()
            number = data_array[3].strip()
            
            cursor.execute("SELECT name FROM students WHERE department = ? AND major = ? AND group_id = ? AND number = ?", (department, major, group_id, number))
            result = cursor.fetchone()
            
            if result:
                name = result[0]
                return render_template("bycarac2.html", name=name, department=department, major=major, group_id=group_id, number=number)
            else:
                return render_template("bycarac2failure.html")
        
        elif len(data_array) == 3:
            department = data_array[0].strip()
            major = data_array[1].strip()
            group_id = data_array[2].strip()
            
            cursor.execute("SELECT name FROM students WHERE department = ? AND major = ? AND group_id = ?", (department, major, group_id))
            result = cursor.fetchall()
            
            if result:
                names = [row[0] for row in result]
                return render_template("bycarac2.html", names=names, department=department, major=major, group_id=group_id)
            else:
                return render_template("bycarac2failure.html")
        
        elif len(data_array) == 2:
            department = data_array[0].strip()
            major = data_array[1].strip()
            
            cursor.execute("SELECT name FROM students WHERE department = ? AND major = ?", (department, major))
            result = cursor.fetchall()
            
            if result:
                names = [row[0] for row in result] 
                return render_template("bycarac2.html", names=names, department=department, major=major)
            else:
                return render_template("bycarac2failure.html")
        
        elif len(data_array) == 1:
            department = data_array[0].strip()
            
            cursor.execute("SELECT name FROM students WHERE department = ?", (department,))
            result = cursor.fetchall()
            
            if result:
                names = [row[0] for row in result]  # Extract names from the result
                return render_template("bycarac2.html", names=names, department=department)
            else:
                return render_template("bycarac2failure.html")
        
    else:
        return render_template("bycarac1.html")
 

@app.route("/bycarac2", methods=["GET", "POST"])
def bycarac2(): 
    if request.method == "POST":
        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()
        input_data = request.form.get('characteristics')
        data_array = input_data.split(',')
        
        if len(data_array) == 4:
            department = data_array[0].strip()
            major = data_array[1].strip()
            group_id = data_array[2].strip()
            number = data_array[3].strip()
            
            cursor.execute("SELECT name FROM students WHERE department = ? AND major = ? AND group_id = ? AND number = ?", (department, major, group_id, number))
            result = cursor.fetchone()
            
            if result:
                name = result[0]
                return render_template("bycarac2.html", name=name, department=department, major=major, group_id=group_id, number=number)
            else:
                return render_template("bycarac2failure.html")
        
        elif len(data_array) == 3:
            department = data_array[0].strip()
            major = data_array[1].strip()
            group_id = data_array[2].strip()
            
            cursor.execute("SELECT name FROM students WHERE department = ? AND major = ? AND group_id = ?", (department, major, group_id))
            result = cursor.fetchall()
            
            if result:
                names = [row[0] for row in result]
                return render_template("bycarac2.html", names=names, department=department, major=major, group_id=group_id)
            else:
                return render_template("bycarac2failure.html")
        
        elif len(data_array) == 2:
            department = data_array[0].strip()
            major = data_array[1].strip()
            
            cursor.execute("SELECT name FROM students WHERE department = ? AND major = ?", (department, major))
            result = cursor.fetchall()
            
            if result:
                names = [row[0] for row in result] 
                return render_template("bycarac2.html", names=names, department=department, major=major)
            else:
                return render_template("bycarac2failure.html")
        
        elif len(data_array) == 1:
            department = data_array[0].strip()
            
            cursor.execute("SELECT name FROM students WHERE department = ?", (department,))
            result = cursor.fetchall()
            
            if result:
                names = [row[0] for row in result]  # Extract names from the result
                return render_template("bycarac2.html", names=names, department=department)
            else:
                return render_template("bycarac2failure.html")
        
    else:
        return render_template("bycarac1.html")
    






