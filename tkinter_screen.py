from tkinter import *
from tkinter import ttk
import arduino

root = Tk()
root.geometry("1200x800")

serial_com = arduino.SerialCom()


def my_click():
    hello = "Hello "+tkVar.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


def cmd():
    root.window_left.left_bottom.console.insert(INSERT, "Hi\n")


def window_init():

    # create main panel
    mainPanedWindow = PanedWindow(bd=4, orient=HORIZONTAL, relief=RAISED, bg="white")
    mainPanedWindow.pack(fill=BOTH, expand=True)

    # create left and right panel
    window_left = PanedWindow(mainPanedWindow, height=100, relief=SUNKEN, orient=VERTICAL, bg="white")
    window_right = PanedWindow(mainPanedWindow, width=200, relief=SUNKEN, bg="grey")
    mainPanedWindow.add(window_left, stretch="always")
    mainPanedWindow.add(window_right, stretch="never")

    # split left panel in top and down window
    left_top = PanedWindow(window_left, width=300, height=300, relief=SUNKEN, bg="grey")
    left_bottom = PanedWindow(window_left, height=200, relief=SUNKEN, bg="grey")
    window_left.add(left_top, stretch="always")
    window_left.add(left_bottom, stretch="never")

    # command line text widget
    console = Text(left_bottom, bg="Black", fg="white", highlightcolor="white",
                   insertbackground="white", font=("Consolas", 12), height=10)
    console.pack(padx=10, pady=10, fill=BOTH, expand=True)

    # add the notebook on the right window
    notebook = ttk.Notebook(window_right)
    notebook.pack(padx=0, pady=0, anchor=N, fill=BOTH, expand=True)

    tab1 = Frame(notebook, bg="grey", padx=5, pady=10)
    tab2 = Frame(notebook, bg="grey", padx=5, pady=10)

    tab1.pack(fill=BOTH, expand=True)
    tab2.pack(fill=BOTH, expand=True)

    # add a notebook to right screen
    notebook.add(tab1, text="Settings")
    notebook.add(tab2, text="Keybinds")

    # button
    button1 = Button(left_top, text="Hi", command=cmd)
    button1.grid(row=0, column=0)

    # settings stuff
    label1 = Label(tab1, text="something", bg="white", highlightbackground="black", highlightcolor="black")
    label1.grid(row=0, column=0, sticky=E+W)

    # settings stuff
    label2 = Label(tab1, text="speed", bg="white", highlightbackground="black", highlightcolor="black")
    label2.grid(row=1, column=0, sticky=E)

    speed_entry = Entry(tab1, width=17)
    speed_entry.grid(row=0, column=1, sticky=W)

    w = Scale(tab1, orient=HORIZONTAL, showvalue=False, bd=False, bg="white",
              highlightcolor="white", highlightbackground="white")
    w.grid(row=1, column=1, sticky=W)


if __name__ == "__main__":
    window_init()

    root.mainloop()
