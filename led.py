from flask import Flask, render_template , request
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)


GPIO.output(13, GPIO.HIGH)
GPIO.output(3, GPIO.LOW)
time.sleep(1)
GPIO.output(3, GPIO.HIGH)
GPIO.output(5, GPIO.LOW)
time.sleep(1)
GPIO.output(5, GPIO.HIGH)
time.sleep(0.1)
GPIO.output(5, GPIO.LOW)
GPIO.output(3, GPIO.LOW)
GPIO.output(13, GPIO.LOW)

time.sleep(1)
GPIO.output(5, GPIO.HIGH)
GPIO.output(3, GPIO.HIGH)
GPIO.output(13, GPIO.HIGH)
GPIO.output(11, GPIO.LOW)

app = Flask(__name__)
a = 'checked'
@app.route('/',methods=['GET','POST'])
def index():
    if request.method =='POST':
        GPIO.output(5, GPIO.LOW)
        time.sleep(0.001)
        GPIO.output(5, GPIO.HIGH)
        a = request.form["on2"]
        b = request.form["radio"]
        if b == 'one':
            if a == 'on':
                GPIO.output(11, GPIO.HIGH)
                return render_template('led.html',i = 'ON',a = 'checked')
            else:
                GPIO.output(11, GPIO.LOW)
                return render_template('led.html',i = 'OFF',a = 'checked')
        if b == 'two':
            if a == 'on':
                GPIO.output(13, GPIO.LOW)
                return render_template('led.html',j = 'ON',b = 'checked')
            else:
                GPIO.output(13, GPIO.HIGH)
                return render_template('led.html',j = 'OFF',b = 'checked')
        else:
            return render_template('led.html',w = 'please choose the botton!')

    else:
        GPIO.output(3, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(3, GPIO.HIGH)
    return render_template('led.html')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)
