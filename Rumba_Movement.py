
import turtle
import tkinter as tk
import main as RM
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from turtle import Screen, Turtle
import matplotlib.pyplot as plt
def moveForward(dist):
    Rumba.forward(dist)


def moveBackward(dist):
    Rumba.backward(dist)


def rotateClockWise():
    Rumba.right(90)


def rotateCounterClockWise():
    Rumba.left(90)


def commandCenterInit():
    window = tk.Tk()
    window.title("Rumba View")
    window.config(background='grey')
    window.geometry("900x900")

    # ---------Create Plot Object----------#
    fig = Figure()
    axis = fig.add_subplot(111)
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().place(x=10, y=10, width=800, height=800)
    canvas.draw()

    fish = [0, 0, 1, 1, 2, 3, 4, 5]
    garbage = [0, 0, 2, 3, 3, 3, 4]
    scanTime = [0, 1, 2, 3, 4, 5, 6, 7]

  #  plt.plot(scanTime, fish)
   # plt.plot(scanTime, garbage)
   # plt.title('Garbage To Fish')
   # plt.xlabel('Time')
   # plt.ylabel('Amount')
   # plt.show()

    # -------Button-------#
    window.update();
    moveForward = tk.Button(window, text="W", font=('calibri', 15), command=lambda: RM.uart_moveForward())
    moveForward.place(x=30, y=0)

    window.update()
    moveForward = tk.Button(window, text="A", font=('calibri', 15), command=lambda: RM.uart_rotateCounterClockwise())
    moveForward.place(x=5, y=40)

    window.update()
    moveForward = tk.Button(window, text="D", font=('calibri', 15), command=lambda: RM.uart_rotateClockWise())
    moveForward.place(x=50, y=40)

    window.update()
    moveBackward = tk.Button(window, text="S", font=('calibri', 15), command=lambda: RM.uart_moveBack())
    moveBackward.place(x=30, y=40)

    window.update();
    scan = tk.Button(window, text="W", font=('calibri', 15), command=lambda: RM.uart_ScanArea())
    scan.place(x=30, y=80)


    window.mainloop()





RM.main()
screen = Screen()
screen.setup(555.555,1000)
screen.setworldcoordinates(-10,-10,555.555,1000)

Rumba = turtle.Turtle()

commandCenterInit()
turtle.done()