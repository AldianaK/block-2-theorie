"""
Author: Aldiana Kucevic
Date 2-1-2023
Function: GUIs
"""

import tkinter
import tkinter.messagebox

# class EmptyGUI:
#
#     def __init__(self):
#         self.main_window = tkinter.Tk()
#         #create the main window
#
#         self.main_window.title("My first GUI")
#         # create title
#
#
#         self.label = tkinter.Label(self.main_window, text= "Hello world")
#         self.label.pack()
#         #label 1 ^
#         self.label2 = tkinter.Label(self.main_window, text="Bio-informatica 2023")
#         self.label2.pack()
#         # label 2 ^
#
#         tkinter.mainloop()
#         # enter the tkinter main loop
#
#         # deze heeft een titel
#
#
# my_gui = EmptyGUI()
#
#
# class Parameters_GUI:
#
#     def __init__(self):
#         self.main_window = tkinter.Tk()
#         self.top_frame = tkinter.Frame(self.main_window)
#         self.bottom_frame = tkinter.Frame(self.main_window)
#         self.label1 = tkinter.Label(self.top_frame, text="hello world", \
#                                     bg="red", relief="sunken")
#         self.label1.pack(side="top")
#         self.top_frame.pack()
#
#         self.label2 = tkinter.Label(self.bottom_frame, text="Bio-informatica 2023", \
#                                     relief="raised", bg="yellow", \
#                                     fg="blue")
#         self.label2.pack(side="top")
#         self.bottom_frame.pack()
#         tkinter.mainloop()
#
# gui_2 = Parameters_GUI()
#
# # ^ geeft meer details voor je widget aan de hand van parameters
# # dingen zoals kleurtjes en relief details zijn toegevoegd
#
# class Frames_GUI:
#
#     def __init__(self):
#
#         self.main_window = tkinter.Tk()
#         self.top_frame = tkinter.Frame(self.main_window)
#         self.bottom_frame = tkinter.Frame(self.main_window)
#         self.label1 = tkinter.Label(self.top_frame, text="Hello world")
#         self.label1.pack(side="top")
#         self.label2 = tkinter.Label(self.bottom_frame, text= "Bio-informatica 2023")
#         self.label2.pack(side="top")
#         self.top_frame.pack()
#         self.bottom_frame.pack()
#         tkinter.mainloop()
#
# frame_Gui = Frames_GUI()

# je kan een window organiseren door frames te creeren. deze frames bepalen de posities van je labels

"""
buttons: kijk hier nog naar terug!!!
"""

# class Buttons_GUI:
#
#     def __init__(self):
#
#         self.main_window =tkinter.Tk()
#
#         # create a button
#         # should appear on the face of the button
#         # do_something should be executed when user clicks the button
#         self.mybutton = tkinter.Button(self.main_window,
#                                        text="Click me!",
#                                        comand=self.do_something)
#         #creat a quit button and it will destroy when it's clicked
#         # aka the window will be closed
#         self.quit_button = tkinter.Button(self.main_window,
#                                           text="Quit",
#                                           command=self.main_window.destroy)
#
#         # pack the buttons
#         self.mybutton.pack()
#         self.quit_button.pack()
#
#         # enter the tkinter main loop
#         tkinter.mainloop()
#
#     def do_something(self):
#         tkinter.messagebox.showinfo("response",
#                                     "thanks for clicking")
# if __name__ == "__main__":
#     button = Buttons_GUI()

# volgens het boek maar dit geeft errors :(

"""
Input with entry widget
voorbeeld: kilo converter program
description: converts distances to kilometers
"""

class KiloConverterGUI:

    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.prompt_label = tkinter.Label(self.top_frame,
                                          text="Enter a distance in kilometers: ")
        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)

        self.prompt_label.pack(side="left")
        self.kilo_entry.pack(side="left")

        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text="convert",
                                          command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text="quit",
                                          command=self.main_window.destroy)

        self.calc_button.pack()
        self.quit_button.pack()

        tkinter.mainloop()

    def convert(self):

        kilo = float(self.kilo_entry.get())

        miles = kilo * 0.6214

        tkinter.messagebox.showinfo("results",
                                    str(kilo) +
                                    " kilometers is equal to " +
                                    str(miles) + "miles")

if __name__ == "__main__" :
    kilo_conv = KiloConverterGUI()

"""
Labels als output
aan de hand van vorige script
"""

class KiloConverterGUI:

    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window) #new
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.prompt_label = tkinter.Label(self.top_frame,
                                          text="Enter a distance in kilometers: ")
        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)

        self.prompt_label.pack(side="left")
        self.kilo_entry.pack(side="left")

        self.descr_label = tkinter.Label(self.mid_frame,
                                         text="converted to miles") #new
        self.value = tkinter.StringVar()

        self.miles_label = tkinter.Label(self.mid_frame,
                                         textvariable=self.value)

        self.descr_label.pack()
        self.miles_label.pack()

        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text="convert",
                                          command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text="quit",
                                          command=self.main_window.destroy)

        self.calc_button.pack()
        self.quit_button.pack()

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):

        kilo = float(self.kilo_entry.get())

        miles = kilo * 0.6214

        self.value.set(miles)

if __name__ == "__main__" :
    kilo_conv = KiloConverterGUI()


"""
Radiobox and check buttons
"""

class radiobox_check_GUI:

    def __init__(self):

        self.main_window = tkinter.Tk

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        self.rb1 = tkinter.Radiobutton(self.top_frame,
                                       text= "option 1",
                                       variable=self.radio_var,
                                       value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame,
                                       text= "option 2",
                                       variable=self.radio_var,
                                       value=1)
        self.rb3 = tkinter.Radiobutton(self.top_frame,
                                       text= "option 3",
                                       variable= self.radio_var,
                                       value=3)

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.ok_button = tkinter.Button(self.bottom_frame,
                                        text="ok",
                                        command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text= "quit",
                                          command=self.main_window.destroy)
        self.ok_button.pack()
        self.quit_button.pack()

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def show_choice(self):
        tkinter.messagebox.showinfo("selection", "you selected option: " +
                                    str(self.radio_var.get()))

if __name__ == "__main__":
    radioboxchecker = radiobox_check_GUI()

"""
checkbutton zie blz 688
"""