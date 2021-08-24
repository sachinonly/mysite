from tkinter import *

app = Tk()

labelText=StringVar()
labelText.set("Enter directory of log files")
labelDir=Label(app, textvariable=labelText, height=4)
labelDir.pack(side="left")

directory=StringVar(None)
dirname=Entry(app,textvariable=directory,width=50)
dirname.pack(side="left")

app.mainloop()