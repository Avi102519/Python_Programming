from tkinter import *
import random,string
import pyperclip #Python library to for copying the text to clipboard 

root= Tk() #Creates main application Window
root.geometry("400x400") #Set the window size to 400x400 pixels
root.resizable(0,0) #Disables window resizing by the user
root.title("PYTHON PROJECT - PASSWORD GENERATOR") #title of the window

Label(root,text="PASSWORD GENERATOR",font="arial 15 bold").pack() #top label of the window
Label(root,text='Python',font='arial 15 bold').pack(side=BOTTOM) #bottom label of the window

pass_label = Label(root, text="PASSWORD LENGTH",font="arial 10 bold").pack() #Creates a label prompting the user to select the password length
pass_len = IntVar() # A Tkinter variable class that holds integer values. it used to select a pwd length 
length = Spinbox(root, from_=8, to=32, textvariable=pass_len, width=15).pack() #A widget that allows the user to select a pwd len between 8 and 32 characters.the selected length is stored in pass_len 
pass_str = StringVar() #A atkinter variable class that holds string values.It is used to store the generated pwd

def generator(): #function used to generate random pwd
    password = [] #initilizes an empty string to store the pwd
    # Ensuring at least one charachet from each type(Upper case,Lower case,Digits,Punctuation)
    if pass_len.get() >= 4:
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.ascii_lowercase))
        password.append(random.choice(string.digits))
        password.append(random.choice(string.punctuation))
        
        # Filling the rest of the password length with random characters
        for _ in range(pass_len.get() - 4):
            password.append(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation))
        
        # Shuffling the password list to ensure randomness
        random.shuffle(password)
    else:
        # If the password length is less than 4, we just fill it with random characters
        for _ in range(pass_len.get()):
            password.append(random.choice(string.ascii_uppercase +string.ascii_lowercase + string.digits + string.punctuation))
        
        # Convert list to string and set it to the StringVar
    pass_str.set("".join(password))
    # Copy the password to clipboard
def Copy_password():
    pyperclip.copy(pass_str.get())
    
Button(root, text="GENERATE PASSWORD", command=generator).pack(pady=5) #calls the Generator function to generate a pwd when clicked
Entry(root, textvariable=pass_str).pack()
Button(root, text="COPY TO CLIPBOARD", command=Copy_password).pack(pady=5) #calls the Copy_pwd function to copy the generated pwd,which is boumd to the pass_str variable.
root.mainloop() #starts the Tkinter event loop,which keeps the application running and responsive to user interactions.
    
 #This project provides a simple yet effective tool for generating random passwords, with the option to copy them to the clipboard for easy use. It's an excellent example of how to combine Python's standard libraries with third-party modules to create a functional application with a graphical user interface.   
    