import tkinter
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
import random

xAxis=[]
yAxis=[]


def RandomNumber():
    x=random.random()
    y=random.random()
    xAxis.append(x)
    yAxis.append(y)
i=0
while(i<10):
    RandomNumber()
    i=i+1



root = tkinter.Tk()
root.wm_title("Embedding in Tk")
RandomNumber()
fig = Figure(figsize=(5, 4), dpi=100)
fig.add_subplot(2,2,1).plot(xAxis,yAxis)

RandomNumber()
fig.add_subplot(2,2,3).plot(xAxis,yAxis )

RandomNumber()
fig.add_subplot(1,2,2).plot(xAxis, yAxis)

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


button = tkinter.Button(master=root, text="Quit", command=_quit)
button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manage