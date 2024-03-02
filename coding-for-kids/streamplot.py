import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial
from collections import deque
from matplotlib import style


ser = serial.Serial('/dev/cu.usbmodem14601', 9600, timeout=0.1)
print(dir(ser))

style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

c = 0
fifo = deque()
def animate(i):
    global c
    global fifo

    data = None
    while not data:
        data = ser.readline().decode().strip()
        ser.flush()
    fifo.append(int(data))
    
    xs = []
    ys = []
    for element in fifo:
        xs.append(c)
        ys.append(element)
        c = c + 1
    ax1.clear()
    ax1.plot(xs, ys)

    if len(fifo) > 10:
        fifo.popleft()
    

ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()