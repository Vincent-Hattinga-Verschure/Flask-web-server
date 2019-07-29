from flask import Flask
import RPi.GPIO as GPIO
import time
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [2, 3, 4, 17, 27, 22, 10, 9, 18, 23, 24, 25, 12, 16, 20, 21]

# loop through pins and set mode and state to 'low'

GPIO.setwarnings(False)

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

 
app = Flask(__name__)
 
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return redirect('/index')
 
@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


@app.route('/index')
def index():
    return render_template("index.html")


#Kanaal 1
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


#Kanaal 2
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


#Kanaal 3
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


#Kanaal 4
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


#Kanaal 5
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


#Kanaal 6
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


#Kanaal 7
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


#Kanaal 8
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


#Kanaal 9
@app.route('/9on')
def channel9low():
   GPIO.output(18, GPIO.LOW)
   return render_template("index.html")
   return redirect("index.html")

@app.route('/9off')
def channel9high():
	 GPIO.output(18, GPIO.HIGH)
	 return render_template("index.html")
	 return redirect("index.html")




#Kanaal 10
@app.route('/10on')
def channel10low():
   GPIO.output(23, GPIO.LOW)
   return render_template("index.html")
   return redirect("index.html")

@app.route('/10ff')
def channel10high():
	 GPIO.output(23, GPIO.HIGH)
	 return render_template("index.html")
	 return redirect("index.html")



#Kanaal 11
@app.route('/11on')
def channel11low():
   GPIO.output(24, GPIO.LOW)
   return render_template("index.html")
   return redirect("index.html")

@app.route('/11off')
def channel11high():
	 GPIO.output(24, GPIO.HIGH)
	 return render_template("index.html")
	 return redirect("index.html")






#Kanaal 12
@app.route('/12on')
def channel12low():
   GPIO.output(25, GPIO.LOW)
   return render_template("index.html")
   return redirect("index.html")

@app.route('/12off')
def channel12high():
	 GPIO.output(25, GPIO.HIGH)
	 return render_template("index.html")
	 return redirect("index.html")




#Kanaal 13
@app.route('/13on')
def channel13low():
   GPIO.output(12, GPIO.LOW)
   return render_template("index.html")
   return redirect("index.html")

@app.route('/13off')
def channel13high():
	 GPIO.output(12, GPIO.HIGH)
	 return render_template("index.html")
	 return redirect("index.html")




#Kanaal 14
@app.route('/14on')
def channel14low():
   GPIO.output(16, GPIO.LOW)
   return render_template("index.html")
   return redirect("index.html")

@app.route('/14off')
def channel14high():
	 GPIO.output(16, GPIO.HIGH)
	 return render_template("index.html")
	 return redirect("index.html")



#Kanaal 15
@app.route('/15on')
def channel15low():
   GPIO.output(20, GPIO.LOW)
   return render_template("index.html")
   return redirect("index.html")

@app.route('/15off')
def channel15high():
	 GPIO.output(20, GPIO.HIGH)
	 return render_template("index.html")
	 return redirect("index.html")



#Kanaal 16
@app.route('/16on')
def channel16low():
   GPIO.output(21, GPIO.LOW)
   return render_template("index.html")
   return redirect("index.html")

@app.route('/16off')
def channel16high():
	 GPIO.output(21, GPIO.HIGH)
	 return render_template("index.html")
	 return redirect("index.html")




 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)
