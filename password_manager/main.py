import tkinter
from PIL import ImageTk, Image
import random
from tkinter import ttk


def generatePassword():

    small_letters = "abcdefghijklmnopqrstuvwxyz"
    capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    signs = "^°!§$%&/()=?{[]}\*+~#-_<>|"

    # Password length
    password_length = 15

    # Order and amount of letters, numbers and signs
    order = [small_letters, capital_letters, numbers, signs]
    random.shuffle(order)  # Shuffled order

    first_type_number = random.randint(0, password_length)
    second_type_number = random.randint(0, password_length - first_type_number)
    third_type_number = random.randint(0, password_length - first_type_number - second_type_number)
    fourth_type_number = password_length - first_type_number - second_type_number - third_type_number

    first_type = order[0]
    second_type = order[1]
    third_type = order[2]
    fourth_type = order[3]

    # for loops for generating actual password
    func_password = ""
    for j in range(0, first_type_number):
        func_password += str(random.choice(first_type))
    for k in range(first_type_number, first_type_number + second_type_number):
        func_password += str(random.choice(second_type))
    for l in range(first_type_number + second_type_number, first_type_number + second_type_number + third_type_number):
        func_password += str(random.choice(third_type))
    for m in range(first_type_number + second_type_number + third_type_number,
                   first_type_number + second_type_number + third_type_number + fourth_type_number):
        func_password += str(random.choice(fourth_type))

    # Shuffle generated password to prevent repetition of the same type behind each other
    list_password = list(func_password)
    random.shuffle(list_password)
    final_password = ""
    final_password = final_password.join(list_password)

    return final_password


def setText():

    password_entry.delete(0, "end")
    password_entry.insert(0, generatePassword())


window = tkinter.Tk()
window.title("Password Manager")

window_width = 800
window_height = 500

# get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

img = ImageTk.PhotoImage(Image.open("logo.png"))
panel = tkinter.Label(window, image=img)
panel.pack(side="top", fill="both", expand=0)

website = tkinter.Label(window, text="Website", )
website.place(x=200, y=250)
website.config(font=('Arial', 15))
website_entry = tkinter.Entry(window)
website_entry.place(x=300, y=255, width=300, height=25)

email = tkinter.Label(window, text="Email")
email.place(x=200, y=300)
email.config(font=('Arial', 15))
email_entry = tkinter.Entry(window)
email_entry.place(x=300, y=305, width=300, height=25)

password = tkinter.Label(window, text="Password")
password.place(x=200, y=350)
password.config(font=('Arial', 15))
password_entry = tkinter.Entry(window)
password_entry.place(x=300, y=355, width=150, height=25)
generate_button = ttk.Button(window, text="Generate Password", command=lambda: setText())
generate_button.place(x=500, y=355)

add_button = ttk.Button(window, text="Add", command=lambda: add())
add_button.place(x=300, y=400)


def add():
    f = open("database.txt", "a")
    f.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}")
    website_entry.delete(0, "end")
    email_entry.delete(0, "end")
    password_entry.delete(0, "end")


window.mainloop()
