import tkinter as tk

from time import strftime

def time():
    current = strftime("%a %b %Y" + "\n" + "%I:%M:%S %p")
    clock.config(text=current)
    clock.after(1000, time)

def toggle():
    if opt2.get():
        e4.place(x=50, y=125)
    else:
        e4.place_forget()

def test():
    contents = e1.get()
    e4.delete("1.0", "end")
    e4.insert("end", contents)

window = tk.Tk()
opt1 = tk.IntVar()
opt2 = tk.BooleanVar()
clock = tk.Label(window)

window.title("PassGen")
window.geometry("300x300")
window.resizable(0, 0)

tk.Label(window, text="Enter site or game:").grid(row=0, padx=3)
tk.Label(window, text="Enter username:").grid(row=1, padx=3)
tk.Label(window, text="Enter length of password:").grid(row=2, padx=3)
tk.Checkbutton(window, text="Special Characters", variable=opt1).grid(row=3, padx=3)
tk.Checkbutton(window, text="Show Password", variable=opt2, command=toggle).grid(row=4, padx=3)

e1 = tk.Entry(window)
e2 = tk.Entry(window)
e3 = tk.Entry(window)
e4 = tk.Text(window, height=6, width=25)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
clock.grid(row=3, column=1)

tk.Button(window, text="Exit", command=window.quit, bg="red").place(x=50, y=250)
tk.Button(window, text="Generate Password", command=test, bg="green").place(x=150, y=250)

time()

window.mainloop()