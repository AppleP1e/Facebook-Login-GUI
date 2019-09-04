#Imports all the stuff you need
from tkinter import *
import tkinter.messagebox as Tkm
import time
import selenium
import webbrowser 

#Creates the window, sets parameters
root = Tk()
root.title("WebAppLauncher")
root.geometry("200x250+120+150") 



#Quits the app completely after you confirm. 
def DestroyAll():
    if Tkm.askokcancel("Quit", "Do you really want to quit?"):
        sys.exit() 

#Facebook Login process
def LoginToFB():
    #Creates a new window (still part of )
    LogPage = Toplevel()
    LogPage.title("Facebook Login")
    LogPage.geometry("170x100+50+50")

    E_mail = Label(LogPage, text = "E-mail")
    E_mail.pack()
    EmailEntry = Entry(LogPage, textvariable = StringVar)
    EmailEntry.pack()
    
    Password = Label(LogPage, text = "Password")
    Password.pack()
    Password_Entry = Entry(LogPage, textvariable = StringVar)
    Password_Entry.pack()


    def DestroyWin():
        LogPage.destroy()

    CloseButton = Button(LogPage, text = "Close", command = DestroyWin)
    CloseButton.pack(side = BOTTOM)
    
    mainloop()
#def LoginToAtlas():


#def LoginToKhan():


#def LoginToMKP():



#button_call = Button(root, text = "Log in") - Alternative method. I could use this variable as a param of my buttons. Didnt really worked for me in phase one. 

#Creates all of the window widgets. 
FBtext = Label(root, text = "Facebook")
FBtext.pack(side = TOP, fill = X)
FBbutton = Button(root, text = "Log in", command = LoginToFB)
FBbutton.pack()

Atlastext = Label(root, text = "Atlas.cz")
Atlastext.pack()
Atlasbutton = Button(root, text = "Log in")
Atlasbutton.pack()

Khantext = Label(root, text = "Khan Academy")
Khantext.pack()
Khanbutton = Button(root, text = "Log in")
Khanbutton.pack()

MKPtext = Label(root, text = "Knihovna Praha")
MKPtext.pack() 
MKPbutton = Button(root, text = "Log in")
MKPbutton.pack()

CloseButton = Button(root, text = "Close", command = DestroyAll)
CloseButton.pack(side = BOTTOM)

mainloop()