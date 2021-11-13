from tkinter import *
import arduino

root = Tk()
root.geometry("1200x800")

serial_com = arduino.SerialCom()


def my_click():
    hello = "Hello "+tkVar.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


def window_init():

    # create main panel
    mainPanedWindow = PanedWindow(bd=4, orient=HORIZONTAL, relief=RAISED, bg="white")
    mainPanedWindow.pack(fill=BOTH, expand=True)

    window_left = PanedWindow(mainPanedWindow, height=100, relief=SUNKEN, orient=VERTICAL, bg="white")
    window_right = PanedWindow(mainPanedWindow, width=200, relief=SUNKEN, bg="grey")
    mainPanedWindow.add(window_left, stretch="always")
    mainPanedWindow.add(window_right, stretch="never")

    left_top = PanedWindow(window_left, width=300, height=300, relief=SUNKEN, bg="white")
    left_bottom = PanedWindow(window_left, height=200, relief=SUNKEN, bg="black")
    window_left.add(left_top, stretch="always")
    window_left.add(left_bottom, stretch="never")


if __name__ == "__main__":
    window_init()

    root.mainloop()
