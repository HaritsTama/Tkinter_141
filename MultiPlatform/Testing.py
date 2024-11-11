# Button
import tkinter 
import tkinter.messagebox 
top = tkinter.Tk() 
def helloCallBack(): 
    tkinter.messagebox.showinfo( "Hello Python", "Hello World") 
B = tkinter.Button(top, text ="Hello", command = helloCallBack) 
B.pack() 
top.mainloop()

# Canvas
import tkinter as tk
from tkinter import messagebox

top = tk.Tk()
C = tk.Canvas(top, bg="blue", height=250, width=300)
coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")
C.pack()
top.mainloop() 

# Check Button
import tkinter as tk
from tkinter import messagebox

top = tk.Tk()
CheckVar1 = tk.IntVar()
CheckVar2 = tk.IntVar()
C1 = tk.Checkbutton(top, text="Music", variable=CheckVar1,
onvalue=1, offvalue=0, height=5, width=20)
C2 = tk.Checkbutton(top, text="Video", variable=CheckVar2,
onvalue=1, offvalue=0, height=5, width=20)
C1.pack()
C2.pack()
top.mainloop()

# Entry
import tkinter as tk
top = tk.Tk()
L1 = tk.Label(top, text="User Name")
L1.pack(side=tk.LEFT)
E1 = tk.Entry(top, bd=5)
E1.pack(side=tk.RIGHT)
top.mainloop()

# Frame
import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
bottomframe = tk.Frame(root)
bottomframe.pack(side=tk.BOTTOM)
redbutton = tk.Button(frame, text="Red", fg="red")
redbutton.pack(side=tk.LEFT)
greenbutton = tk.Button(frame, text="Brown", fg="brown")
greenbutton.pack(side=tk.LEFT)
bluebutton = tk.Button(frame, text="Blue", fg="blue")
bluebutton.pack(side=tk.LEFT)
blackbutton = tk.Button(bottomframe, text="Black", fg="black")
blackbutton.pack(side=tk.BOTTOM)
root.mainloop()

# Label
import tkinter as tk

root = tk.Tk()
var = tk.StringVar()
label = tk.Label(root, textvariable=var, relief=tk.RAISED)
var.set("Hey!? How are you doing?")
label.pack()

root.mainloop()

# List Box
import tkinter as tk
from tkinter import messagebox
top = tk.Tk()
Lb1 = tk.Listbox(top)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")
Lb1.pack()
top.mainloop()

# Menubutton
import tkinter as tk
from tkinter import messagebox

top = tk.Tk()
mb = tk.Menubutton(top, text="condiments", relief=tk.RAISED)
mb.grid()
mb.menu = tk.Menu(mb, tearoff=0)
mb["menu"] = mb.menu
mayoVar = tk.IntVar()
ketchVar = tk.IntVar()
mb.menu.add_checkbutton(label="mayo", variable=mayoVar)
mb.menu.add_checkbutton(label="ketchup", variable=ketchVar)

mb.pack()
top.mainloop()

# Message
import tkinter as tk

root = tk.Tk()

var = tk.StringVar()
label = tk.Message(root, textvariable=var, relief=tk.RAISED)

var.set("Hey!? How are you doing?")
label.pack()
root.mainloop()

# Radiobutton
import tkinter as tk

def sel():
    selection = "You selected the option " + str(var.get())
    label.config(text=selection)
root = tk.Tk()
var = tk.IntVar()
R1 = tk.Radiobutton(root, text="Option 1", variable=var, value=1, command=sel)
R1.pack(anchor=tk.W)
R2 = tk.Radiobutton(root, text="Option 2", variable=var, value=2, command=sel)
R2.pack(anchor=tk.W)
R3 = tk.Radiobutton(root, text="Option 3", variable=var, value=3, command=sel)
R3.pack(anchor=tk.W)
label = tk.Label(root)
label.pack()
root.mainloop()

# Scale
import tkinter as tk

def sel():
    selection = "Value = " + str(var.get())
    label.config(text=selection)

root = tk.Tk()
var = tk.DoubleVar()
scale = tk.Scale(root, variable=var)
scale.pack(anchor=tk.CENTER)

button = tk.Button(root, text="Get Scale Value", command=sel)
button.pack(anchor=tk.CENTER)

label = tk.Label(root)
label.pack()
root.mainloop()

# Scrollbar
import tkinter as tk

root = tk.Tk()
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

mylist = tk.Listbox(root, yscrollcommand=scrollbar.set)
for line in range(100):
    mylist.insert(tk.END, "This is line number " + str(line))

mylist.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=mylist.yview)

root.mainloop()

# Text
import tkinter as tk

def onclick():
    pass
root = tk.Tk()
text = tk.Text(root)
text.insert(tk.INSERT, "Hello.....")
text.insert(tk.END, "Bye Bye.....")
text.pack()
text.tag_add("here", "1.0", "1.4")
text.tag_add("start", "1.8", "1.13")
text.tag_config("here", background="yellow", foreground="blue")
text.tag_config("start", background="black", foreground="green")
root.mainloop()

# Toplevel
import tkinter as tk

root = tk.Tk()
top = tk.Toplevel()

top.mainloop()

# Spinbox
import tkinter as tk

master = tk.Tk()

w = tk.Spinbox(master, from_=0, to=10)
w.pack()

master.mainloop()

# Panned Window
import tkinter as tk

m1 = tk.PanedWindow(orient=tk.HORIZONTAL)
m1.pack(fill=tk.BOTH, expand=1)

left = tk.Label(m1, text="left pane")
m1.add(left)

m2 = tk.PanedWindow(m1, orient=tk.VERTICAL)
m1.add(m2)

top = tk.Label(m2, text="top pane")
m2.add(top)

bottom = tk.Label(m2, text="bottom pane")
m2.add(bottom)

tk.mainloop()

# Label Frame
import tkinter as tk

root = tk.Tk()

labelframe = tk.LabelFrame(root, text="This is a LabelFrame")
labelframe.pack(fill="both", expand="yes")

left = tk.Label(labelframe, text="Inside the LabelFrame")
left.pack()

root.mainloop()
