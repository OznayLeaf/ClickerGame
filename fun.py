from tkinter import *

window = Tk()
window.title("Clicker Game!")

Icon = PhotoImage(file="emoji.png")

window.iconphoto(True, Icon)

Label = Label(window, text="0")
Label.config(font=("Arial", 50, "bold"))

Label.pack()

count = 0

def Click():
	global count
	count+=1
	Label.config(text=str(count))

button = Button(window, text="Click Me!")
button.pack()

button.config(font=("Arial", 50, "bold"), bg="#ff0000", activebackground="#bf3300")
button.config(command=Click)


window.mainloop()