#Imports all the stuff you need
from tkinter import *
import tkinter.messagebox as Tkm
from selenium import webdriver 



#Creates the window, sets parameters
root = Tk()
root.title("WebAppLauncher")
root.geometry("200x150+120+150") 



#Quits the app completely after you confirm. 
def DestroyAll():
    if Tkm.askokcancel("Quit", "Do you really want to quit?"):
        sys.exit() 
        driver.quit()
#Facebook Login process
def LoginToFB():
    
    #Creates a new window 
    LogPage = Toplevel()
    LogPage.title("Facebook Login")
    LogPage.geometry("300x140+50+50")

    #global E_mail

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
        driver.get('https://www.facebook.com/login/device-based/regular/login/')
        
        E_mail_value = EmailEntry.get() 
        Password_value = Password_Entry.get() #That way we get values entered into entries as strings and we can manipulate with them that way. Yay!

        emailElem = driver.find_element_by_id("email") 
        emailElem.send_keys(E_mail_value) #This finds element of email field and then it takes our new strings and passes them on.

        Password_value = driver.find_element_by_id("pass")
        Password_value = driver.send_keys(Password_value) #Same thing as above, only with password. 

        clicker = driver.find_element_by_id("loginbutton")
        clicker.click() #After passing all the information above, the code locates the login button and finally clicks on it. 

#I used this page for helping me with this code: https://www.quora.com/Does-Facebook-provide-any-API-to-log-in-to-an-account-with-Python
#And this page: https://www.geeksforgeeks.org/facebook-login-using-python/
    def DestroyWin():
        
        LogPage.destroy()
        driver.quit()
   
    LogButton = Button(LogPage, text = "Log in",command =  PassInfo)
    LogButton.pack()

    CloseButton = Button(LogPage, text = "Close", command = DestroyWin)
    CloseButton.pack(side = BOTTOM)
    
    mainloop()
    # Login to Atlas mail
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

# A work of Vladimír Blažek for "Introduction to Python" course held at PřF UK and led by RNDr. Jiří Makovička, CSc.
# A free program distributed under MIT license. Aviliable on GitHub/AppleP1e

# A list of sources I used to write the code:
# * https://naucse.python.cz/
# *https://www.geeksforgeeks.org/ 
# *https://www.python.org/
# *https://www.seleniumhq.org/selenium-ide/

# This program is using Selenium module and geckodriver by Mozilla. 


