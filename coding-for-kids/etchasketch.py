import turtle
import serial
import math

ser = serial.Serial('/dev/cu.usbmodem14601', 9600, timeout=0.1) 

turtle.tracer(1, 0)
             
turtle.goto(0,0)
delta = 10
while True:
    data = ser.readline().decode().strip()
    if data:
        y, x, select = data.split(",")
        if not bool(int(select)):
            turtle.clear()
            turtle.goto(0,0)
        else:
            x = -(int(x) - 512) / 50
            y = -(int(y) - 512) / 50

            if math.fabs(x) <= 1:
                x = 0
            if math.fabs(y) <= 1:
                y = 0

            turtle.goto(turtle.xcor() + x, turtle.ycor() + y)
            #if x > 250:
            #    turtle.goto(turtle.xcor() + delta, turtle.ycor())
            #if x < -250:
            #    turtle.goto(turtle.xcor() - delta, turtle.ycor())
            #if y > 250:
            #    turtle.goto(turtle.xcor(), turtle.ycor() + delta)
            #if y < -250:
            #    turtle.goto(turtle.xcor(), turtle.ycor() - delta)

