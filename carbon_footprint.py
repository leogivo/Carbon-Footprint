#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Antonio Frighetto"
__author__ = "Leonardo Givoli"
__date__ = "Friday 25/09/2015"

from Tkinter import *
from PIL import ImageTk, Image
import tkMessageBox
import ttk
import sys
import os

OPTION_COUNTRY = ["Select a country...",
                  "Austria",
                  "Belgium",
                  "Bulgaria",
                  "Germany"]

# class Application(tk.Tk):
#     def __init__(self, window):
#         self.window = window
# def checkKindOfFootprint():
#     if start.get() == "Carbon Footprint":
#         carbonFootprint()
#     else:
#         waterFootprint()
class buttonMenu:
    def save(self):
        CarbonWaterFile = open('Carbon and Water.txt','w')
        CarbonWaterFile.write('Esempio')
        CarbonWaterFile.close()
        tkMessageBox.showinfo("Windows","File Save")

    def Exit(self):
        mainWindow.destroy()

def menu():
    menu = Menu(mainWindow)
    mainWindow.config(menu=menu)
    button=buttonMenu()
    subMenu = Menu(menu)
    menu.add_cascade(label="File",menu=subMenu)
    subMenu.add_command(label="Save Project",command=button.save)
    subMenu.add_separator()
    subMenu.add_command(label="Exit",command=button.Exit)


def showFrontmostApp(arg):
    if sys.platform.startswith('darwin'):
        os.system('''/usr/bin/osascript -e 'tell application "System Events" to set frontmost of process "Python" to true' ''')
    else:
        arg.attributes("-topmost", True)

def carbonFootprint():
    # ls = ['From 0 to 4', 'From 4 to 10', 'From 11 to 18']
    # myList = Listbox(myFrame)
    # for item in ls:
    # myList.insert(0, item)
    # myList.pack()
    selectCountryLabel = Label(myFrame, text = "Please select your home country: ").pack(anchor=W, padx=10, pady=45)#place(x=10, y=45)
    country = StringVar(myFrame)
    country.set(OPTION_COUNTRY[0])
    selectCountryList = OptionMenu(myFrame, country, *OPTION_COUNTRY).pack(anchor=N, padx=240, pady=0)

    chooseComponentsLabel = Label(myFrame, text = "How many people are in your household? ").place(x=10, y=105)
    familiarNumber = StringVar(myFrame)
    familiarNumber.set("1")
    chooseComponentsList = OptionMenu(myFrame, familiarNumber, "1", "2", "3", "4", "5", "6", "7").place(x=270, y=102)

    energyLabel = Label(myFrame, text= "Enter your consumption of each type of energy. Electricity (kWh): ").place(x=10, y=135)
    electricityEntry = Entry(myFrame, width=8).place(x=415, y=132)
    naturalGasEntry = Entry(myFrame, width=8)
    #row = Frame(myFrame)

def waterFootprint():
    water = Entry(myFrame, width=8).place(x=515, y=132)

def main():
    global start, myFrame, mainWindow
    mainWindow = Tk()
    menu()
    myFrame = Frame(mainWindow)
    myFrame.pack(side = LEFT, fill = BOTH, expand = True, padx = 10, pady=10)
    mainWindow.resizable(0,0) #resizable option is not alloweds
    mainWindow.geometry("800x500+275+200")
    mainWindow.title("Carbon & Water Footprint")
    mainWindow.configure(background="white")
    # Setting an intro label a starting label
    introLabel = Label(myFrame, text = "Welcome to the Carbon & Water Footprint calculator!", font = "Verdana 14")
    introLabel.pack(anchor=CENTER, pady=5)  #place = place on the screen
    start = StringVar(myFrame)
    start.set("Carbon Footprint")
    selectFootprint = Label(myFrame, text = "What do you wish to calculate? ").pack(anchor=CENTER, pady=10)
    # selectFootprintList = OptionMenu(myFrame, start, "Carbon Footprint", "Water Footprint")
    # selectFootprintList.place(x=205, y=40)#pack(anchor=N, fill = Y, padx=250, pady=0)#place(x=210, y=30)
    # selectFootprintList.config(width=20)

    # Creating a canvas where an image can be inserted
    myCanvas = Canvas(myFrame, width=327, height=400)
    myCanvas.place(x=10, y=70)#pack(side = "bottom", fill = "both", expand = "yes")
    img = Image.open("C:\Users\Givo\DEsktop\Carbon Footprint\Immagini\Orma_carbon2.jpg")
    myCanvas.image = ImageTk.PhotoImage(img)
    myCanvas.create_image(200,200, image=myCanvas.image)

    # Creating two main buttons
    carbonButton = Button(myFrame, text = "Start Carbon Footprint", command=carbonFootprint)
    carbonButton.place(x=340, y=180)
    carbonButton.configure(width=20)
    waterButton = Button(myFrame, text = "Start Water Footprint", command=waterFootprint, state=DISABLED)
    waterButton.place(x=340,y=290)
    waterButton.configure(width=20)

    showFrontmostApp(mainWindow)
    mainWindow.mainloop()

if __name__ == '__main__':
    main()
