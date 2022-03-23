from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# data file
def generate_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_entry.delete(0, END)
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #     password += char

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    webs = website_entry.get()
    emails = email_entry.get()
    passwords = password_entry.get()
    new_data = {
        webs: {
            "email": emails,
            "password": passwords,
        }
    }


    if len(webs) == 0 or len(passwords) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you have't left any fields empty.")
    else:
        # is_ok = messagebox.askokcancel(title=webs, message=f"These are the details entered: \nEmail: {emails} \nPassword: {passwords} \nIs it ok to save?")
        # if is_ok:
        try:
            with open("data.json", "r") as data_file:
                # data_file.write(f"{webs} | {emails} | {passwords}\n")

                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

                # Saving updated data
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    webs = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if webs in data:
            emails = data[webs]["email"]
            passwords = data[webs]["password"]
            messagebox.showinfo(title=webs, message=f"Email: {emails}\nPassword: {passwords}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {webs} exists.")



# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
padlock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0)

# Lables
website = Label(text="Website:")
website.grid(column=0, row=1)
email = Label(text="Email/Username:")
email.grid(column=0, row=2)
password = Label(text="Password:")
password.grid(column=0, row=3)

# Entry
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "miglenaruskova@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
search = Button(text="Search", width=13, command=find_password)
search.grid(column=2, row=1)
generate = Button(text="Generate Password", command=generate_password)
generate.grid(column=2, row=3)
add = Button(text="Add", width=36, command=save)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
