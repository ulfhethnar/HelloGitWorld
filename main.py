import tkinter as tk
from tkinter import messagebox as mb
import random
import string
import configparser
from time import strftime

def passlength(e3):    #gets the length of the password to be generated
    plength = e3.get()
    try:
        plnum = int(plength)
        return plnum
    except ValueError:
        mb.showerror("Error", "Please Input a Number.")
        return(passlength())

def letgen(opt1):    #generates base string
    basedict = {1 : string.ascii_uppercase, 2 : string.ascii_lowercase, 3 : string.digits, 4 : "!@#$%&"}

    if opt1.get() == True:
        return basedict[1] + basedict[2] + basedict[3] + basedict[4]
    else:
        return basedict[1] + basedict[2] + basedict[3]

def passgen():  # generates the password
    return "".join([random.choice(letgen(opt1)) for i in range(passlength(e3))])

def check(config, site, usename):
    if config.has_option(site, usename):
        return True
    else:
        return False

def newpass():
    if mb.askyesno("Username Exists", "Username already exists. Do you want to create a new password?"):
        return True
    else:
        return False

def writePWList(config, path, site, usename, password):
    if config.has_section(site):
        config.set(str(site), str(usename), password)
    else:
        config.add_section(site)
        config.set(str(usename), str(usename), password)

    with open(path, 'w') as config_file:
        config.write(config_file)

def time():
    current = strftime("%a %b %Y" + "\n" + "%I:%M:%S %p")
    clock.config(text=current)
    clock.after(1000, time)

def viewpass():
    if opt2.get():
        e4.place(x=50, y=125)
        return True
    else:
        e4.place_forget()
        return False

def main():
    config = configparser.ConfigParser()
    path = 'PWList.ini'
    config.read(path)
    site = e1.get()
    usename = e2.get()

    if check(config, site, usename) == True:
        if newpass() == True:
            password = passgen()
            writePWList(config, path, site, usename, password)
            view = viewpass()
            if view == True:
                e4.delete("1.0", tk.END)
                e4.insert(tk.END, password)
            else:
                window.quit
        else:
            window.quit
    else:
        password = passgen()
        writePWList(config, path, site, usename, password)
        view = viewpass()
        if view == True:
            e4.delete("1.0", tk.END)
            e4.insert(tk.END, contents)
        else:
            window.quit

window = tk.Tk()
opt1 = tk.BooleanVar()
opt2 = tk.BooleanVar()
clock = tk.Label(window)

window.title("PassGen")
window.geometry("300x300")
window.resizable(0, 0)

tk.Label(window, text="Enter site or game:").grid(row=0, padx=3)
tk.Label(window, text="Enter username:").grid(row=1, padx=3)
tk.Label(window, text="Enter length of password:").grid(row=2, padx=3)
tk.Checkbutton(window, text="Special Characters", variable=opt1).grid(row=3, padx=3)
tk.Checkbutton(window, text="Show Password", variable=opt2, command=viewpass).grid(row=4, padx=3)

e1 = tk.Entry(window)
e2 = tk.Entry(window)
e3 = tk.Entry(window)
e4 = tk.Text(window, height=6, width=25)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
clock.grid(row=3, column=1)

tk.Button(window, text="Exit", command=window.quit, bg="red").place(x=50, y=250)
tk.Button(window, text="Generate Password", command=main, bg="green").place(x=150, y=250)

time()

window.mainloop()