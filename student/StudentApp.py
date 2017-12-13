from flask import Flask, redirect, render_template, request, url_for
import time #time and date related functions
import re

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def Stud():
	if request.method == "GET":
		return render_template("StudentEntry.html")

	if request.method == "POST":
		marks = request.form.getlist('marks[]')
		marks = list(map(int, marks))

		credits = request.form.getlist('credits[]')
		credits = list(map(int, credits))

		op = []
		numOfSubjects = len(marks) #or subjects; or pass it via POST
		gradePointSum = 0
		for i in range(numOfSubjects):
			item = []
			item.append("Subject"+str(i+1))
			item.append(marks[i])
			credit = credits[i]
			item.append(credit)
			grade = getGrade(marks[i])
			points = getPoints(grade)
			item.append(grade)
			item.append(points)
			gradePointSum = gradePointSum + (credit * points)
			op.append(item)
		sgpa = gradePointSum*1.0/sum(credits)
		return render_template("serversidesuccess.html", data=op, name = request.form.get('name'), usn = request.form.get('usn'), dob = request.form.get('dob'), sgpa = sgpa)

def getGrade(marks):
	if(marks >= 0 and marks < 40):
		return "F"
	elif(marks >= 40 and marks < 50):
		return "D"
	elif(marks >= 50 and marks < 60):
		return "C"
	elif(marks >= 60 and marks < 75):
		return "B"
	elif(marks >= 75 and marks < 90):
		return "A"
	elif(marks >= 90 and marks < 100):
		return "S"

def getPoints(grade):
	if(grade == "S"):
		return 10
	elif(grade == "A"):
		return 9
	elif(grade == "B"):
		return 8
	elif(grade == "C"):
		return 7
	elif(grade == "D"):
		return 6
	elif(grade == "F"):
		return 0

if __name__ == '__main__':
	app.run()
