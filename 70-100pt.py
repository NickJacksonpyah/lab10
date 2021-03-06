##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!
# square
square = drawpad.create_rectangle(200,200,300,300)
# line
line = drawpad.create_line(300, 200, 250, 175)
line1 = drawpad.create_line(200, 200, 250, 175)
line2 = drawpad.create_line(230, 300, 230, 270)
square = drawpad.create_rectangle(230, 300, 250, 270)
square1 = drawpad.create_rectangle(270, 185, 250, 160)
root.mainloop()
