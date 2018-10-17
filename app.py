#!/usr/bin/python
import RPi.GPIO as GPIO
import time
from flask import Flask, redirect, render_template

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [2, 3, 4, 17, 27, 22, 10, 9]

# loop through pins and set mode and state to 'low'

GPIO.setwarnings(False)

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)
    
SleepTimeL = 1


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index3.html')

@app.route('/1aan')
def maak1high():
    GPIO.output(2, GPIO.LOW)
    return render_template('index3.html')
    return redirect("index3.html")


@app.route('/1uit')
def maak1low():
    GPIO.output(2, GPIO.HIGH)
    return render_template('index3.html')
    return redirect("index3.html")

@app.route('/2aan')
def maak2high():
    GPIO.output(3, GPIO.LOW)
    return render_template('index3.html')
    return redirect("index3.html")


@app.route('/2uit')
def maak2low():
    GPIO.output(3, GPIO.HIGH)
    return render_template('index3.html')
    return redirect("index3.html")

@app.route('/3aan')
def maak3high():
    GPIO.output(4, GPIO.LOW)
    return render_template('index3.html')
    return redirect("index3.html")


@app.route('/3uit')
def maak3low():
    GPIO.output(4, GPIO.HIGH)
    return render_template('index3.html')
    return redirect("index3.html")

@app.route('/4aan')
def maak4high():
    GPIO.output(17, GPIO.LOW)
    return render_template('index3.html')
    return redirect("index3.html")


@app.route('/4uit')
def maak4low():
    GPIO.output(17, GPIO.HIGH)
    return render_template('index3.html')
    return redirect("index3.html")

@app.route('/5aan')
def maak5high():
    GPIO.output(27, GPIO.LOW)
    return render_template('index3.html')
    return redirect("index3.html")


@app.route('/5uit')
def maak5low():
    GPIO.output(27, GPIO.HIGH)
    return render_template('index3.html')
    return redirect("index3.html")

@app.route('/6aan')
def maak6high():
    GPIO.output(22, GPIO.LOW)
    return render_template('index3.html')
    return redirect("index3.html")


@app.route('/6uit')
def maak6low():
    GPIO.output(22, GPIO.HIGH)
    return render_template('index3.html')
    return redirect("index3.html")

@app.route('/7aan')
def maak7high():
    GPIO.output(10, GPIO.LOW)
    return render_template('index3.html')
    return redirect("index3.html")


@app.route('/7uit')
def maak7low():
    GPIO.output(10, GPIO.HIGH)
    return render_template('index3.html')
    return redirect("index3.html")

@app.route('/8aan')
def maak8high():
    GPIO.output(9, GPIO.LOW)
    return render_template('index3.html')
    return redirect("index3.html")


@app.route('/8uit')
def maak8low():
    GPIO.output(9, GPIO.HIGH)
    return render_template('index3.html')
    return redirect("index3.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


