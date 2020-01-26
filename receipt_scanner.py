import os
import requests
import json
import re
import time 
from datetime import date
from NewOCRTest import runOCRAlgo
from csvHandler import *

from flask import Flask, render_template, request, send_file
app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

IMG_FOLDER = os.path.join('images')
DATA_FOLDER = ""
app.config['UPLOAD_FOLDER'] = IMG_FOLDER
userDict = []
lengthOfData = 0
pleaseWorkForMe = ""

@app.route("/")
def index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'test.jpg')
    target =  os.path.join(APP_ROOT, "data")
    return render_template("upload.html", user_image = full_filename)

@app.route('/download/')
def downloadFile ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    return send_file("C:/Users/Sebastian/Documents/flask_blog/data/userData.csv", attachment_filename="userData.csv")

@app.route("/upload",methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, "images/")
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)
    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(target)

    userDict = loadDictFromCSV(os.path.join(APP_ROOT, "data"))
    lengthOfData = len(userDict['date'])
    finalString, fileName = runOCRAlgo(target, filename, lengthOfData)
    cost = float(finalString)
    today = date.today()
    timestamp = date.fromtimestamp(time.time())

    #print(cost)
    updateDict(userDict, [timestamp, cost, fileName + ".jpg"])

    saveDictToCSV(userDict, os.path.join(APP_ROOT, "data"))
    print(" Detected total: ", str(cost))
    lengthOfData = lengthOfData + 1
    print(today)
    print(timestamp)
    fileUploaded = "Latest File Uploaded:"
    total = round(getCost(userDict), 2)
    return render_template("upload.html", finalString="Cost: $" + str(finalString), today=" , Date of Purchase: " + str(today), fileUploaded=fileUploaded, total=total)


