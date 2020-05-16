"""
Created on Sat Oct 19 23:18:18 2019

@author: Sadiq and Manoj
"""

# !/usr/bin/python3
from tkinter import Tk , scrolledtext , Menu , filedialog , END,Label ,messagebox,simpledialog
from tkinter import *
import os

root = Tk(className = " Text Editor")
TextArea = scrolledtext.ScrolledText(root, width = 500 , height = 100)


def newfile():
    if len(TextArea.get('1.0' , END+'-1c')) >0:
        if messagebox.askyesno("Save","Do you want to save?"):
            savefile()
            
        else:        
            TextArea.delete('1.0',END)
    
    root.title("TEXT EDITOR")
    
def quitapp():
    root.destroy()

def openfile():
    
    file = filedialog.askopenfile(parent = root ,title = "Select file",filetypes=(("Text file","*.txt"),("All files", "*-*")))
    root.title(os.path.basename(file.name) +  "- TEXT EDITOR")
    
    if file != None:
        contents = file.read()
        TextArea.insert('1.0' , contents)
        file.close()

def savefile():
    file = filedialog.asksaveasfile(mode = 'w' , filetypes = (("jpeg files","*.jpg"),("all files","*.*"),("Text File","*.txt"),("HTML file","*.html")))
    
    if file != None:
        data = TextArea.get('1.0' , END+'-1c')
        file.write(data)
        file.close()

def findInFile():
    findString = simpledialog.askstring("Find....","Enter text")
    textData = TextArea.get('1.0' , END)
    occurances = textData.upper().count(findString.upper())
    if textData.upper().count(findString.upper()) > 0:    
        label = messagebox.showinfo("Results ",findString + " has " + str(occurances) +" occurances." )
    else:
        label = messagebox.showinfo("Results","Sorry\nNot present")   
    
#Edit Menu Funtion	
def cutfile():
    TextArea.event_generate("<<Cut>>")
    
def copyfile():
    TextArea.event_generate("<<Copy>>")
    
def pastefile():
    TextArea.event_generate("<<Paste>>")
    
def exitRoot():
    if messagebox.askyesno("Quit","Are you sure you want to quit ?"):
        root.destroy()

def about():
    label = messagebox.showinfo("About", "A python alternative to Notepad!\nVerion 0.0.1    05-11-2019\nDesigned by Sadiq Manoj and Pavan")

#Style Menu Funtion	
def Arial():
	TextArea.config(font = "Arial")
	
def Calibri():
	TextArea.config(font = "Calibri")

def Courier():
	TextArea.config(font = "Courier")
	
def Helvetica():
	TextArea.config(font = "Helvetica")
	
def Times():
	TextArea.config(font = "Times")

def Comic():
	TextArea.config(font = "Symbol")

#Background Menu Funtion	
def Black():
	TextArea.config(background = "black",fg = "white")

def White():
	TextArea.config(background = "white",fg = "black")
	
def Green():
	TextArea.config(background = "Green")
	
def Yellow():
	TextArea.config(background = "yellow")

#Color Menu Funtion	
def bWhite():
	TextArea.config(fg = "white")
	
def bBlack():
	TextArea.config(fg = "black")
	
def bRed():
	TextArea.config(fg = "red")
	
def bBlue():
	TextArea.config(fg = "blue")

#Creating a menu
menu = Menu(root)
root.config(menu = menu)
fileMenu = Menu(menu)
menu.add_cascade(label = "File" , menu = fileMenu )
fileMenu.add_command(label = "New" ,command = newfile)
fileMenu.add_command(label = "Open" , command = openfile)
fileMenu.add_command(label = "Save" , command = savefile)
fileMenu.add_command(label = "Find" , command = findInFile)

fileMenu.add_separator()
fileMenu.add_command(label = "Exit", command = exitRoot )

#Creating help menu bar
helpMenu = Menu(menu)
menu.add_cascade(label="Edit",menu=helpMenu)
helpMenu.add_command(label = "Cut" ,  command = cutfile)
helpMenu.add_command(label = "Copy" ,  command = copyfile)
helpMenu.add_command(label = "Paste" ,  command = pastefile)

#Creating font menu bar
fontmenu = Menu(menu)
menu.add_cascade(label="Style",menu=fontmenu)
fontmenu.add_command(label = "Calibri" ,  command = Calibri)
fontmenu.add_command(label = "Arial" ,  command = Arial)
fontmenu.add_command(label = "Courier" ,  command = Courier)
fontmenu.add_command(label = "Helvetica" ,  command = Helvetica)
fontmenu.add_command(label = "Times" ,  command = Times)
fontmenu.add_command(label = "Symbol" ,  command = Comic)

#Creating  background menu bar
backmenu = Menu(menu)
menu.add_cascade(label="Background",menu=backmenu)
backmenu.add_command(label = "Black" ,  command = Black)
backmenu.add_command(label = "White" ,  command = White)
backmenu.add_command(label = "Green" ,  command = Green)
backmenu.add_command(label = "Yellow" ,  command = Yellow)

#Creating color menu bar
colormenu = Menu(menu)
menu.add_cascade(label="Color",menu=colormenu)
colormenu.add_command(label = "White" ,  command = bWhite)
colormenu.add_command(label = "Black" ,  command = bBlack)
colormenu.add_command(label = "Red" ,  command = bRed)
colormenu.add_command(label = "Blue" ,  command = bBlue)

#Creating about menu bar
menu.add_cascade(label = "About",command = about)


TextArea.pack()

root.mainloop()

