import turtle
import serial

ser = serial.Serial('/dev/cu.usbmodem14601', 9600, timeout=0.1) 

turtle.tracer(1, 0)

for i in range(10000):
    turtle.forward(i)
    data = ser.readline().decode().strip()
    if data:
        if data == "1":
            #break
            turtle.forward(50)
        if data == "-1":
            turtle.write("noob 1234", font=('Arial', 19, 'normal'))
    turtle.left(89)
turtle.exitonclick()