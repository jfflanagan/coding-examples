import turtle
import serial
import math

ser = serial.Serial('/dev/cu.usbmodem14601', 9600, timeout=0.1) 

turtle.tracer(1, 0)
             
turtle.goto(0,0)
delta = 30
while True:
    data = ser.readline().decode().strip()
    if data:
        x = 0
        y = 0
        if data == "POWER":
            turtle.clear()
            turtle.goto(0,0)
        else:
            if data == "UP":
                y = delta
            if data == "DOWN":
                y = -delta
            if data == "RIGHT":
                x = delta
            if data == "LEFT":
                x = -delta

            turtle.goto(turtle.xcor() + x, turtle.ycor() + y)

