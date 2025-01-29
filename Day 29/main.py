from tkinter import *;
from tkinter import messagebox;
import random;
import pyperclip;

FONT = ('verdana', 12);

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def random_password():
    nr_letters = random.randint(8,10);
    nr_numbers = random.randint(2,4);
    nr_symbols = random.randint(2,4);

    password_letters = [random.choice(letters) for _ in range(nr_letters)];
    number_letters = [random.choice(numbers) for _ in range(nr_numbers)];
    symbol_letters = [random.choice(symbols) for _ in range(nr_symbols)];

    my_password = password_letters + number_letters + symbol_letters;

    random.shuffle(my_password);

    final_password = "".join(my_password);

    return final_password;

def password_generator():

    password = password_entry.get();

    if len(password) > 0:
        password_entry.delete(0, END);
    
    my_password = random_password();    
    password_entry.insert(0, my_password);
    pyperclip.copy(my_password);
    


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    website = website_entry.get();
    email = email_entry.get();
    password = password_entry.get();

    if website == "" or email == "" or password == "":
        messagebox.showwarning(message="Please don't leave any fields empty!", title='Oops');
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?")

        if is_ok:
            with open('Day 29/data.txt', "a") as file:
                file.write(f"{website} | {email} | {password}\n");
            website_entry.delete(0, END);
            password_entry.delete(0, END);

# ---------------------------- UI SETUP ------------------------------- #

window = Tk();
window.title('Password Manager');
window.config(padx=20, pady=20);

canvas = Canvas(width=200, height=200);
logo_image = PhotoImage(file = 'Day 29/logo.png');
canvas.create_image(100,100, image = logo_image);
canvas.grid(row=0, column=1);

#labels;
website_label = Label(text="Website:", font=FONT);
website_label.grid(row=1, column=0);

email_label = Label(text="Email/Username:", font=FONT);
email_label.grid(row=2, column=0);

password_label = Label(text="Password:", font=FONT);
password_label.grid(row=3, column=0);

#entries
website_entry = Entry(width=36);
website_entry.focus();
website_entry.grid(row=1, column=1, columnspan=2);

email_entry = Entry(width=36);
email_entry.insert(0, 'tajale01@gmail.com');
email_entry.grid(row=2, column=1, columnspan=2);

password_entry = Entry(width=22);
password_entry.grid(row=3, column=1);

#buttons
generate_password = Button(text='Generate Password', command=password_generator);
generate_password.grid(row=3, column=2);

add_button = Button(text="Add", width=37, command=save_password);
add_button.grid(row=4, column=1, columnspan=2);



window.mainloop();