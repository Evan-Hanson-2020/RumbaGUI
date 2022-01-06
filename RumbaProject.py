
import tkinter as tk
import numpy as np
import serial as sr
import time

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import socket
import rumbaMapping as RM


port = 288
# Change to whatever IP/Port your device is running from
ip = "192.168.1.1"
try:
    socketBase = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket Created")
except socket.error as err:
    print("Socket Failed because %s" % (err))


def connectionInit():
    socketBase.connect(('127.0.0.1', 22))
    print("Socket has made connection with Rumba... At Port %s and Ip %s" % (port, ip))
    print(socketBase.recv(1024).decode())


def uart_moveBack():
    socketBase.send('s'.encode())
    check = socketBase.recv(20)
    check = check.decode().split(',')
    if(check[0] == 'f'):
        RM.moveBackward(25);
    else:
        RM.moveBackward(int(check[1]))


def uart_moveForward():
    socketBase.send('w'.encode())
    check = socketBase.recv(20)
    check = check.decode().split(',')
    if (check[0] == 'f'):
        RM.moveForward(25)
    elif (check[0] == 'l'):
        RM.Rumba.pen(pencolor="black", pensize=2, speed=1)
        RM.moveForward(int(check[1]))
        RM.Rumba.hideturtle()
        RM.rotateClockWise()
        RM.Rumba.pen(pencolor="red", pensize=2, speed=1)
        RM.moveForward(10)
        RM.moveBackward(20)
        RM.moveForward(10)
        RM.rotateCounterClockWise()
        RM.Rumba.showturtle()
    elif(check[0] == 'bm'):
        RM.moveForward(int(check[1]))
        RM.Rumba.pen(pencolor="purple", fillcolor="orange", pensize=1, speed=15)
        RM.Rumba.hideturtle()
        RM.Rumba.rt(90)
        RM.Rumba.begin_fill()
        RM.Rumba.circle(11)
        RM.Rumba.end_fill()
        RM.Rumba.lt(90)
        RM.Rumba.showturtle()
    elif(check[0] == 'bl'):
        RM.moveForward(int(check[1]))
        RM.Rumba.pen(pencolor="purple", fillcolor="orange", pensize=1, speed=15)
        RM.Rumba.hideturtle()
        RM.Rumba.begin_fill()
        RM.Rumba.circle(11)
        RM.Rumba.end_fill()
        RM.Rumba.showturtle()
    elif(check[0] == 'br'):
        RM.moveForward(int(check[1]))
        RM.Rumba.pen(pencolor="purple", fillcolor="orange", pensize=1, speed=15)
        RM.Rumba.hideturtle()
        RM.Rumba.rt(180)
        RM.Rumba.begin_fill()
        RM.Rumba.circle(11)
        RM.Rumba.end_fill()
        RM.Rumba.lt(180)
        RM.Rumba.backward(10)
        RM.Rumba.showturtle()



def uart_rotateClockWise():
    socketBase.send('a'.encode())
    RM.rotateClockWise()

def uart_rotateCounterClockwise():
    socketBase.send('d'.encode())
    RM.rotateCounterClockWise()

def uart_ScanArea():
    x = 0
    RM.Rumba.hideturtle()
    socketBase.send('m'.encode())
    check = socketBase.recv(1024)
    check = check.decode().split(';')


    if(check[0] != 'n'):
        while check[x] != 'n':
            location = check[x].split(',')
            print(location)
            RM.Rumba.penup()
            RM.Rumba.lt(int(location[0]))
            RM.Rumba.forward(int(location[1]))
            RM.Rumba.pendown()
            if(int(location[2])<13):
                RM.Rumba.pen(pencolor="blue", fillcolor="blue", pensize=1, speed=8)
                circle = 1.75
            elif(int(location[2])>=13 and int(location[2])<20):
                circle = 8.83
                RM.Rumba.pen(pencolor="black", fillcolor="black", pensize=1, speed=8) #TODO: Include function adding to bar graph
            else:
                RM.Rumba.pen(pencolor="red", fillcolor="red", pensize=1, speed=8)
                circle = 0
            RM.Rumba.begin_fill()
            RM.Rumba.circle(circle)
            RM.Rumba.end_fill()
            RM.Rumba.penup()
            RM.Rumba.backward(int(location[1]))
            RM.Rumba.rt(int(location[0]))
            x += 1
    RM.Rumba.showturtle()
    RM.Rumba.pendown()

# Press the green button in the gutter to run the script.
def main():
    connectionInit()

