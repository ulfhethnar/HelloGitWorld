import tkinter as tk
import random
import string
import configparser

class PasswordGenerator:
    def __init__(self, length, special_char):
        self.length = int(length)
        self.special_char = special_char

    def let_gen(self):
        base_dict = {1: string.ascii_uppercase, 2: string.ascii_lowercase, 3: string.digits, 4: "!@#$&"}

        if self.special_char:
            return base_dict[1] + base_dict[2] + base_dict[3] + base_dict[4]
        else:
            return base_dict[1] + base_dict[2] + base_dict[3]

    def pass_gen(self):
        return "".join([random.choice(self.let_gen()) for i in range(self.length)])

class WriteList:
    def __init__(self, site, username, password):
        self.site = site
        self.username = username
        self.password = password

    def add_section(self): #writing into the config file eventually
        section_var = ("Site: " + self.site, "Username: " + self.username, "Password: " + self.password)
#        text_field.delete("1.0", tk.END)
#        text_field.insert("1.0", section_var)

class MainWindow:
    def __init__(self, window):
        window.geometry("300x300")
        window.resizable(0, 0)

        tk.Label(window, text="Enter site or game:").grid(row=0, padx=3)
        tk.Label(window, text="Enter username:").grid(row=1, padx=3)
        tk.Label(window, text="Enter password length:").grid(row=2, padx=3)

        special_char_opt = tk.BooleanVar()
        tk.Checkbutton(window, text="Special Characters", variable=special_char_opt).grid(row=3, padx=3)

        site_entry = tk.Entry(window)
        site_entry.grid(row=0, column=1)

        username_entry = tk.Entry(window)
        username_entry.grid(row=1, column=1)

        length_entry = tk.Entry(window)
        length_entry.grid(row=2, column=1)

        text_field = tk.Text(window, height=6, width=25)
        text_field.place(x=50, y=125)

        tk.Button(window, text="Exit", command=window.quit).place(x=50, y=250)
        tk.Button(window, text="Generate").place(x=150, y=250)

#def main():
#    gen_site =
#    gen_username =
#    gen_length =

#    get_pass = PasswordGenerator(gen_length, special_char_opt)
#    generate_entry = WriteList(gen_site, gen_username, get_pass.pass_gen())
#    generate_entry.add_section()

main_window = tk.Tk()
start_up = MainWindow(main_window)
main_window.mainloop()




