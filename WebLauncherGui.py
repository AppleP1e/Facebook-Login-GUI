#Imports all the stuff you need
from tkinter import *
import tkinter.messagebox as Tkm
import time
from selenium import webdriver 



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
    
    #Creates a new window 
    LogPage = Toplevel()
    LogPage.title("Facebook Login")
    LogPage.geometry("300x140+50+50")

    E_mail = Label(LogPage, text = "E-mail")
    E_mail.pack()
    EmailEntry = Entry(LogPage, textvariable = StringVar)
    EmailEntry.pack()
    
    Password = Label(LogPage, text = "Password")
    Password.pack()
    Password_Entry = Entry(LogPage, textvariable = StringVar)
    Password_Entry.pack()


    def PassInfo():
        global driver
        driver =  webdriver.Firefox() #This calls the backend GeckoDriver, included in this folder.
        driver.get('https://www.facebook.com/')
       

    def DestroyWin():
        
        LogPage.destroy()
        driver.quit()
   
    LogButton = Button(LogPage, text = "Log in",command =  PassInfo)
    LogButton.pack()

    CloseButton = Button(LogPage, text = "Close", command = DestroyWin)
    CloseButton.pack(side = BOTTOM)
    
    mainloop()
#def LoginToAtlas():
def LoginToAtlas():
    
    #Creates a new window 
    LogPage = Toplevel()
    LogPage.title("Email login")
    LogPage.geometry("300x140+50+50")

    E_mail = Label(LogPage, text = "username")
    E_mail.pack()
    EmailEntry = Entry(LogPage, textvariable = StringVar)
    EmailEntry.pack()
    
    Password = Label(LogPage, text = "Password")
    Password.pack()
    Password_Entry = Entry(LogPage, textvariable = StringVar)
    Password_Entry.pack()


    def PassInfo():
        global driver
        driver =  webdriver.Firefox() #This calls the backend GeckoDriver, included in this folder.
        driver.get('https://atlas.centrum.cz/')
       

    def DestroyWin():
        
        LogPage.destroy()
        driver.quit()
   
    LogButton = Button(LogPage, text = "Log in",command =  PassInfo)
    LogButton.pack()

    CloseButton = Button(LogPage, text = "Close", command = DestroyWin)
    CloseButton.pack(side = BOTTOM)
    
    mainloop()


#Creates all of the window widgets. 
FBtext = Label(root, text = "Facebook")
FBtext.pack(side = TOP, fill = X)
FBbutton = Button(root, text = "Log in", command = LoginToFB)
FBbutton.pack()

Atlastext = Label(root, text = "Atlas.cz")
Atlastext.pack()
Atlasbutton = Button(root, text = "Log in")
Atlasbutton.pack()

CloseButton = Button(root, text = "Close", command = DestroyAll)
CloseButton.pack(side = BOTTOM)

mainloop()


