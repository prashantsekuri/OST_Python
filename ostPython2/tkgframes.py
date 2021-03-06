#!/usr/bin/env python3
#
#
#             tkgframes.py
#         (Uses "grid" manager)
#
#      for OST Lesson 8: GUILayout
#
#      by David S Jackson on 2/18/15
#
#          Instructor:  Pat Barton
#
"""
Write a GUI-based program to build a window layout as shown
below (not copied into this program).  When the frame is
resized, the buttons should stay the same height and expand
sideways.  Frame 1 and 2 should always be the same height
and width as each other, and Frame 3 should be half as wide
again as they are (ie, 150% width, as shown below).  
Labeling each Frame is optional/good exercise.

"""
from tkinter import *

root = Tk()
root.title("Hi Pat!")
ALL = N+S+E+W
wt = 8

frame1 = Frame(root)

# 3 rows x 5 columns...
for r in range(3):
    root.rowconfigure(r, weight=wt)
    frame1.rowconfigure(r, weight=wt)
    for c in range(5):
        root.columnconfigure(c, weight=wt)
        frame1.columnconfigure(c, weight=wt)


# Here are the labels...
# With grid(), there's really only 1 frame...
label_1 = Label(frame1, text="Frame 1")
label_1.config(bg="green", height=10, width=10)
label_2 = Label(frame1, text="Frame 2")
label_2.config(bg="yellow", height=10, width=10)
label_3 = Label(frame1, text="Frame 3")
label_3.config(bg="blue", height=20, width=15)

# Add 5 buttons
button_1 = Button(frame1, text="Button 1")
button_2 = Button(frame1, text="Button 2")
button_3 = Button(frame1, text="Button 3")
button_4 = Button(frame1, text="Button 4")
button_5 = Button(frame1, text="Button 5")

# Labels all should resize in both X & Y axis
label_1.grid(row=0, column=0, columnspan=2, rowspan=1, sticky=ALL)
label_2.grid(row=1, column=0, columnspan=2, rowspan=1, sticky=ALL)
label_3.grid(row=0, column=2, columnspan=3, rowspan=2, sticky=ALL)

# Buttons should expand only in horizontal axis
button_1.grid(row=2, column=0, sticky=E+W)
button_2.grid(row=2, column=1, sticky=E+W)
button_3.grid(row=2, column=2, sticky=E+W)
button_4.grid(row=2, column=3, sticky=E+W)
button_5.grid(row=2, column=4, sticky=E+W)


frame1.grid(row=0, column=0, sticky=ALL)


root.mainloop()
