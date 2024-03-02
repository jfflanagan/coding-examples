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

c = 1
fifo = deque()
def animate(i):
    global c
    global fifo

    temperature, humidity = (0.0, 0.0)
    data = None
    while not data:
        data = ser.readline().decode().strip()
        try:
            temperature, humidity = data.split(",")
            temperature = float(temperature) * 1.8 + 32
            humidity = float(humidity)
        except:
            pass
        ser.flush()
    fifo.append((temperature, humidity))
    
    xs = []
    temps = []
    humids = []
    idx = c - len(fifo)
    for element in fifo:
        temperature, humidity = element
        xs.append(idx)
        temps.append(temperature)
        humids.append(humidity)
        idx += 1
    ax1.clear()
    
    ax1.plot(xs, temps, label="Temperature (F)")
    ax1.plot(xs, humids, label="Humidity (%)")
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Temp (F) / Humidity (%)")
    ax1.legend(loc='lower left')

    c = c + 1
    if len(fifo) > 50:
        fifo.popleft()
    

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()