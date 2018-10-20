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
    return render_template("index.html")

@app.route('/1on')
def channel1low():
    GPIO.output(2, GPIO.LOW)
    return render_template("index.html")
    return redirect("index.html")


@app.route('/1off')
def channel1high():
    GPIO.output(2, GPIO.HIGH)
    return render_template("index.html")
    return redirect("index.html")

@app.route('/2on')
def channel2low():
    GPIO.output(3, GPIO.LOW)
    return render_template("index.html")
    return redirect("index.html")


@app.route('/2off')
def channel2high():
    GPIO.output(3, GPIO.HIGH)
    return render_template("index.html")
    return redirect("index.html")

@app.route('/3on')
def channel3low():
    GPIO.output(4, GPIO.LOW)
    return render_template("index.html")
    return redirect("index.html")


@app.route('/3off')
def channel3high():
    GPIO.output(4, GPIO.HIGH)
    return render_template("index.html")
    return redirect("index.html")

@app.route('/4on')
def channel4low():
    GPIO.output(17, GPIO.LOW)
    return render_template("index.html")
    return redirect("index.html")


@app.route('/4off')
def channel4high():
    GPIO.output(17, GPIO.HIGH)
    return render_template("index.html")
    return redirect("index.html")

@app.route('/5on')
def channel5low():
    GPIO.output(27, GPIO.LOW)
    return render_template("index.html")
    return redirect("index.html")


@app.route('/5off')
def channel5high():
    GPIO.output(27, GPIO.HIGH)
    return render_template("index.html")
    return redirect("index.html")

@app.route('/6on')
def channel6low():
    GPIO.output(22, GPIO.LOW)
    return render_template("index.html")
    return redirect("index.html")


@app.route('/6off')
def channel6high():
    GPIO.output(22, GPIO.HIGH)
    return render_template("index.html")
    return redirect("index.html")

@app.route('/7on')
def channel7low():
    GPIO.output(10, GPIO.LOW)
    return render_template("index.html")
    return redirect("index.html")


@app.route('/7off')
def channel7high():
    GPIO.output(10, GPIO.HIGH)
    return render_template("index.html")
    return redirect("index.html")

@app.route('/8on')
def channel8low():
    GPIO.output(9, GPIO.LOW)
    return render_template("index.html")
    return redirect("index.html")


@app.route('/8off')
def channel8high():
    GPIO.output(9, GPIO.HIGH)
    return render_template("index.html")
    return redirect("index.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


