from tkinter import *
from functools import partial

def validateLogin(username, password):
    global tkwindow
    if username=='user' and password=='pass':
        main_scr()
        tkwindow.quit()
	return

#window
tkWindow = Tk()  
tkWindow.geometry('400x400')  
tkWindow.title('Login')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name")
usernameLabel.place(relx=0.15,rely=0.33,anchor=CENTER)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username)
usernameEntry.place(relx=0.55,rely=0.33,anchor=CENTER)

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password")
passwordLabel.place(relx=0.15,rely=0.66,anchor=CENTER) 
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*')
passwordEntry.place(relx=0.55,rely=0.66,anchor=CENTER)  
validateLogin = partial(validateLogin, username, password)
loginButton = Button(tkWindow, text="Login", command=validateLogin)
loginButton.place(relx=0.5,rely=0.8,anchor=CENTER)  

tkWindow.mainloop()