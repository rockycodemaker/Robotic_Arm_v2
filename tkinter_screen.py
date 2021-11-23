from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from PIL import Image, ImageTk


class Screen(Tk):
    def __init__(self):
        super().__init__()
        self.title("Robot Arm")

        self.call('wm', 'iconphoto', self._w, PhotoImage(file='Smiley.png'))
        # self.iconbitmap("Smiley.ico")

        # Gets the requested values of the height and width.
        window_width = 800
        window_height = 800

        self.geometry(f"{window_width}x{window_height}")

        # Gets both half the screen width/height and window width/height
        position_right = int(self.winfo_screenwidth()/2 - window_width/2)
        position_down = int(self.winfo_screenheight()/2 - window_height/2)

        # Positions the window in the center of the page.
        self.geometry("+{}+{}".format(position_right, position_down))

        self.main_pane = PanedWindow(bd=4, orient=HORIZONTAL, relief=RAISED, bg="white")
        self.main_pane.pack(fill=BOTH, expand=True)

        self.window_left = PanedWindow(self.main_pane, relief=SUNKEN, orient=VERTICAL, bg="white")
        self.main_pane.add(self.window_left, stretch="always")

        # settings menu frame
        self.window_right = Frame(self.main_pane, width=200, relief=SUNKEN, bg="grey")
        self.main_pane.add(self.window_right, stretch="never")

        self.left_top = PanedWindow(self.main_pane, height=100, relief=SUNKEN, bg="white")
        self.window_left.add(self.left_top, stretch="always")

        self.left_bottom = Frame(self.window_left, height=100, relief=SUNKEN, bg="grey")
        self.window_left.add(self.left_bottom, stretch="never")

        self.console = scrolledtext.ScrolledText(self.left_bottom, bg="Black", fg="white", highlightcolor="white",
                                                 insertbackground="white", font=("Consolas", 12), height=10)
        self.console.pack(padx=10, pady=10, fill=BOTH, expand=True)
        self.console.configure(state="disabled")

        # notebook for settings
        self.notebook = ttk.Notebook(self.window_right)
        self.notebook.pack(padx=0, pady=0, anchor=N, fill=BOTH, expand=True)

        self.tab1 = Frame(self.notebook, bg="grey", padx=5, pady=10)
        self.tab2 = Frame(self.notebook, bg="grey", padx=5, pady=10)

        self.tab1.pack(fill=BOTH, expand=True)
        self.tab2.pack(fill=BOTH, expand=True)

        # add a notebook to right screen
        self.notebook.add(self.tab1, text="Settings")
        self.notebook.add(self.tab2, text="Keybinds")

        # button
        self.button1 = Button(self.left_top, text="Hello World!", command=self.cmd)
        self.button1.grid(row=0, column=0, padx=5, pady=5)

        # setting settings stuff
        self.label1 = Label(self.tab1, text="something", bg="white",
                            highlightbackground="black", highlightcolor="black")
        self.label1.grid(row=0, column=0, padx=3, sticky=E)

        self.label2 = Label(self.tab1, text="speed", bg="white",
                            highlightbackground="black", highlightcolor="black")
        self.label2.grid(row=1, column=0, padx=3, sticky=E)

        self.speed_entry = Entry(self.tab1, width=17)
        self.speed_entry.grid(row=0, column=1, sticky=W)

        self.w = Scale(self.tab1, orient=HORIZONTAL, showvalue=False, bd=False, bg="white",
                       highlightcolor="white", highlightbackground="white")
        self.w.grid(row=1, column=1, sticky=W)

        self.mainloop()

    # print to console
    def cmd(self, message="Hello World!"):
        self.console.configure(state=NORMAL)
        self.console.insert(END, message+"\n")
        self.console.see(END)
        self.console.configure(state=DISABLED)


class SplashScreen(Tk):
    def __init__(self):
        super().__init__()

        font = "Helvetica"

        # Gets the requested values of the height and width.
        window_width = 800
        window_height = 600

        self.geometry(f"{window_width}x{window_height}")

        # Gets both half the screen width/height and window width/height
        position_right = int(self.winfo_screenwidth()/2 - window_width/2)
        position_down = int(self.winfo_screenheight()/2 - window_height/2)

        # Positions the window in the center of the page.
        self.geometry("+{}+{}".format(position_right, position_down))

        self.title("splash screen")
        self.geometry(f'{window_width}x{window_height}')

        load = Image.open("kitty.jpg")
        self.bg = ImageTk.PhotoImage(load)

        my_canvas = Canvas(self, width=800, height=600, bd=0, highlightthickness=0)
        my_canvas.pack(fill=BOTH, expand=True)

        # Set image in canvas
        my_canvas.create_image(0, 0, image=self.bg, anchor="nw")

        self.main_label = Label(my_canvas, text="Robotic Arm v2", font=(font, 25), bg="white", width=18, height=2)
        self.main_label.pack(padx=5, pady=50)

        self.low_label = Label(my_canvas, text="By Jim Kerver", font=(font, 20), bg="white", width=20)
        self.low_label.pack(side=BOTTOM, pady=50)

        self.overrideredirect(True)

        self.after(3000, self.destroy)
        self.mainloop()


if __name__ == "__main__":

    splash_screen = SplashScreen()
    screen = Screen()
