# Python program to create a simple GUI
# calculator using Tkinter

# import everything from tkinter module
from tkinter import *

# globally declare the expression variable 
expression = ""


# Function to update expression
# in the text entry box
def press(num):
	# point out the global expression variable
	global expression

	# concatenation of string
	expression = expression + str(num)

	# update the expression by using set method
	equation.set(expression)

# Function to evaluate the final expression
def equalpress():
	# Try and except statement is used for handling the errors like zero, division error etc.

	# Put that code inside the try block which may generate the error
	try:

		global expression

		# eval function evaluate the expression and str function convert the result into string
		total = str(eval(expression))

		equation.set(total)

		# initialze the expression variable by empty string
		expression = ""

	# if error is generate then handle by the except block
	except:

		equation.set(" error ")
		expression = ""


# Function to clear the contents of text entry box
def clear():
	global expression
	expression = ""
	equation.set("")


# Driver code
if __name__ == "__main__":
	# create a GUI window
	gui = Tk()

	# set the background colour of GUI window
	gui.configure(background="black")

	# set the title of GUI window
	gui.title("Simple Calculator")

	# set the configuration of GUI window
	gui.geometry("300x500")

	# StringVar() is the variable class, we create an instance of this class
	equation = StringVar()

	# create the text entry box for showing the expression .
	lbl = Label(gui, text = "Label", anchor = SE, font = ("Verdana", 20), textvariable = equation, bg = 'black', fg = 'white')
	lbl.pack(expand = True, fill = "both")
	
	#Dividing the screen for buttons using Frames.
	btnrow1 = Frame(gui)
	btnrow1.pack(expand = True, fill = "both")
	
	btnrow2 = Frame(gui)
	btnrow2.pack(expand = True, fill = "both")
	
	btnrow3 = Frame(gui)
	btnrow3.pack(expand = True, fill = "both")
	
	btnrow4 = Frame(gui)
	btnrow4.pack(expand = True, fill = "both")
	
	btnrow5 = Frame(gui)
	btnrow5.pack(expand = True, fill = "both")
	
	#creating the buttons and entering the variables
	# when user press the button, the command or function affiliated to that button is executed .
	button7 = Button(btnrow1, text=' 7 ', fg='black', relief = GROOVE, border = 0,command=lambda: press(7))
	button7.pack(side = LEFT, expand = True, fill = "both")

	button8 = Button(btnrow1, text=' 8 ', fg='black', relief = GROOVE, border = 0,command=lambda: press(8))
	button8.pack(side = LEFT, expand = True, fill = "both")

	button9 = Button(btnrow1, text=' 9 ', fg='black', relief = GROOVE, border = 0,command=lambda: press(9))
	button9.pack(side = LEFT, expand = True, fill = "both")

	multiply = Button(btnrow1, text=' * ',font = ("Verdana", 11,'bold'), fg='chocolate2', relief = GROOVE, border = 0,command=lambda: press("*"))
	multiply.pack(side = LEFT, expand = True, fill = "both")

	button4 = Button(btnrow2, text=' 4 ', fg='black', relief = GROOVE, border = 0,command=lambda: press(4))
	button4.pack(side = LEFT, expand = True, fill = "both")

	button5 = Button(btnrow2, text=' 5 ', fg='black', relief = GROOVE, border = 0,command=lambda: press(5))
	button5.pack(side = LEFT, expand = True, fill = "both")

	button6 = Button(btnrow2, text=' 6 ', fg='black', relief = GROOVE, border = 0,command=lambda: press(6))
	button6.pack(side = LEFT, expand = True, fill = "both")

	minus = Button(btnrow2, text=' - ',font = ("Verdana", 11,'bold'), fg='chocolate2', relief = GROOVE, border = 0,command=lambda: press("-"))
	minus.pack(side = LEFT, expand = True, fill = "both")

	button1 = Button(btnrow3, text=' 1 ', fg='black', relief = GROOVE, border = 0,command=lambda: press(1))
	button1.pack(side = LEFT, expand = True, fill = "both")

	button2 = Button(btnrow3, text=' 2 ', fg='black', relief = GROOVE, border = 0,command=lambda: press(2))
	button2.pack(side = LEFT, expand = True, fill = "both")
	
	button3 = Button(btnrow3, text=' 3 ', fg='black', relief = GROOVE, border = 0,command=lambda: press(3))
	button3.pack(side = LEFT, expand = True, fill = "both")

	plus = Button(btnrow3, text=' + ',font = ("Verdana", 11,'bold'), fg='chocolate2', relief = GROOVE, border = 0,command=lambda: press("+"))
	plus.pack(side = LEFT, expand = True, fill = "both")

	clear = Button(btnrow4, text=' C ',font = ("Verdana", 11,'bold'), fg='chocolate2', relief = GROOVE, border = 0,command=clear)
	clear.pack(side = LEFT, expand = True, fill = "both")

	button0 = Button(btnrow4, text=' 0 ', fg='black', relief = GROOVE, border = 0,command=lambda: press(0))
	button0.pack(side = LEFT, expand = True, fill = "both")
	
	decimal= Button(btnrow4, text=' . ',font = ("Verdana", 11,'bold'), fg='chocolate2', relief = GROOVE, border = 0,command=lambda: press('.'))
	decimal.pack(side = LEFT, expand = True, fill = "both")

	divide = Button(btnrow4, text=' / ',font = ("Verdana", 11,'bold'), fg='chocolate2', relief = GROOVE, border = 0,command=lambda: press("/"))
	divide.pack(side = LEFT, expand = True, fill = "both")

	equal = Button(btnrow5, text=' = ',font = ("Verdana", 11,'bold'), fg='chocolate2', relief = GROOVE, border = 0,command=equalpress)
	equal.pack(side = LEFT, expand = True, fill = "both")

		
	# start the GUI
	gui.mainloop()