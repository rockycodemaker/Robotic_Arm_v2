import tkinter
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

        self.notebook = Notebook(self, self.window_right)
        self.notebook.pack(padx=0, pady=0, anchor=N, fill=BOTH, expand=True)

        self.mainloop()

    # print to console
    def cmd(self, message="Hello World!"):
        self.console.configure(state=NORMAL)
        self.console.insert(END, message+"\n")
        self.console.see(END)
        self.console.configure(state=DISABLED)


class Notebook(ttk.Notebook):
    def __init__(self, root, master):
        # notebook for settings
        ttk.Notebook.__init__(self, master)

        root.tab1 = SettingsTab(root, self)
        root.tab2 = KeybindsTab(root, self)
        # root.tab1 = Frame(self, bg="grey", padx=5, pady=10)
        # root.tab2 = Frame(self, bg="grey", padx=5, pady=10)

        root.tab1.pack(fill=BOTH, expand=True)
        root.tab2.pack(fill=BOTH, expand=True)

        self.add(root.tab1, text="Settings")
        self.add(root.tab2, text="Keybinds")

        # self.speed_entry = Entry(self.tab1, width=17)
        # self.speed_entry.grid(row=0, column=1, sticky=W)
        #
        # self.w = Scale(self.tab1, orient=HORIZONTAL, showvalue=False, bd=False, bg="white",
        #                highlightcolor="white", highlightbackground="white")
        # self.w.grid(row=1, column=1, sticky=W)


class SettingsTab(tkinter.Frame):
    def __init__(self, root, master):
        tkinter.Frame.__init__(self, bg="grey", padx=5, pady=10)

        # settings labels
        root.label1 = SettingsLabel(root, self, "Com port")
        root.label1.grid(row=0, column=0, padx=3, sticky=E)

        root.label2 = SettingsLabel(root, self, "speed")
        root.label2.grid(row=1, column=0, padx=3, sticky=E)


class KeybindsTab(tkinter.Frame):
    def __init__(self, root, master):
        tkinter.Frame.__init__(self, bg="grey", padx=5, pady=10)

        # settings labels
        root.label1 = SettingsLabel(root, self, "upwards")
        root.label1.grid(row=0, column=0, padx=3, sticky=E)

        root.label2 = SettingsLabel(root, self, "downwards")
        root.label2.grid(row=1, column=0, padx=3, sticky=E)


class SettingsLabel(tkinter.Label):
    def __init__(self, root, master, text):
        tkinter.Label.__init__(self, master, text=text, bg="white", relief="solid", borderwidth=0.5, width=10, anchor=E)


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
