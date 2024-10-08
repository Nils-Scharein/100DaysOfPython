import tkinter as tk
import pandas as pd
import random as rd
from tkinter import ttk
import numpy as np
import hashlib
import os

# ---------------------------- UI SETUP root -------------------------#

root = tk.Tk()
root.title("Password manager")
root.config(padx=100, pady=50)

# ---------------------------- PASSWORD GENERATOR Class Setup------------------------------- #
class Password_Manager():
    def __init__(self, master):
        # Canvas / Logo Setup
        self.logo = tk.PhotoImage(file="logo.png")
        self.foto_label = tk.Label(master, image=self.logo)
        self.foto_label.grid(column=1, row=0, columnspan=2)
        self.pw = ""
        self.master = master

        if os.path.exists("Passwords.csv"):
            self.df = pd.read_csv("Passwords.csv", index_col=0)
        else:
            self.df = pd.DataFrame(columns=["Website", "E-Mail", "Password"])

        # Layout
        self.website_label = tk.Label(master, text="Website")
        self.website_label.grid(column=0, row=1)
        self.website_entry = tk.Entry(master)
        self.website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")

        self.email_username_label = tk.Label(master, text="Email/Username")
        self.email_username_label.grid(column=0, row=2)
        self.email_username_entry = tk.Entry(master)
        self.email_username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
        self.password_label = tk.Label(master, text="Password")
        self.password_label.grid(column=0, row=3)
        self.password_entry = tk.Entry(master)
        self.password_entry.grid(column=1, row=3, sticky="W")

        self.generate_button = tk.Button(text="Generate Password", command=self.password_generator)
        self.generate_button.grid(column=2, row=3)

        self.add_button = tk.Button(text="Add", command=self.save_password)
        self.add_button.grid(column=1, row=5, columnspan=2, sticky="EW")

    def check_emtpy(self):
        if self.website_entry.get() == "":
            return True
        elif self.email_username_entry.get() == "":
            return True
        elif self.password_entry.get() == "":
            return True
        else:
            return False

    def popupBonus(self):
        popupBonusWindow = tk.Tk()
        popupBonusWindow.wm_title("Window")
        labelBonus = tk.Label(popupBonusWindow, text="Can't leave the spaces empty")
        labelBonus.pack()
        B1 = tk.Button(popupBonusWindow, text="Okay", command=popupBonusWindow.destroy)
        B1.pack()

    def save_password(self):
        if self.check_emtpy():
            self.popupBonus()
        else:
            new_row = pd.DataFrame({
                "Website": [self.website_entry.get()],
                "E-Mail": [self.email_username_entry.get()],
                "Password": [self.password_entry.get()]
            })
            self.df = pd.concat([self.df, new_row], ignore_index=True)
            self.df.to_csv("Passwords.csv", encoding='utf-8')

    def set_text(self, text, entry):
        entry.delete(0, tk.END)
        entry.insert(0, text)
        return

    def password_generator(self):
        buchstaben = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        sonderzeichen = [",", "!", "-", ".", ":", "/", ";", "?"]
        zahlen = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        joined = buchstaben + sonderzeichen + zahlen
        counter = 0
        pw = []
        for i in range(20):
            if counter == 0:
                pw.append(buchstaben[rd.randint(0, len(buchstaben) - 1)].upper())
                counter += 1
            elif counter == 1:
                pw.append(buchstaben[rd.randint(0, len(buchstaben) - 1)].lower())
                counter += 1
            elif counter == 2:
                pw.append(sonderzeichen[rd.randint(0, len(sonderzeichen) - 1)])
                counter += 1
            elif counter == 3:
                pw.append(zahlen[rd.randint(0, len(zahlen) - 1)])
                counter += 1
            else:
                pw.append(joined[rd.randint(0, len(joined) - 1)])
        rd.shuffle(pw)
        pw = "".join(pw)
        self.pw = pw

        self.set_text(self.pw, self.password_entry)

    def select(self):
        selected_item = self.my_tree.selection()[0]
        selected_id = self.my_tree.focus()
        item_index = self.my_tree.index(selected_id)
        self.df.reset_index(drop=True, inplace=True)
        self.my_tree.delete(selected_item)
        self.df = self.df.drop(index=item_index)
        self.df.to_csv("Passwords.csv", encoding='utf-8')

    def open_Data_table(self):
        self.my_tree["column"] = self.df_list
        self.my_tree["show"] = "headings"
        for column in self.my_tree["column"]:
            self.my_tree.heading(column, text=column)

        df_rows = self.df.to_numpy().tolist()
        for row in df_rows:
            self.my_tree.insert("", "end", values=row)

        button_del = tk.Button(self.new_window, text="del", command=self.select)
        button_del.pack()
        self.my_tree.pack(fill="both")

password_manager = Password_Manager(root)

root.mainloop()
