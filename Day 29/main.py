from tkinter import *;
from tkinter import messagebox;
from random import randint, choice, shuffle;
import pyperclip;
import json;


FONT = ('verdana', 12);

#generate password
def random_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    list_letter = [choice(letters) for _ in range(randint(8,10))];
    list_number = [choice(numbers) for _ in range(randint(2,4))];
    list_symbol = [choice(symbols) for _ in range(randint(2,4))];

    final_password_list = list_letter + list_number + list_symbol;

    shuffle(final_password_list);

    final_password = "".join(final_password_list);

    return final_password;



def generate_password():
    password = password_entry.get();

    if len(password) > 0:
        password_entry.delete(0, END);

    my_password = random_password();
    password_entry.insert(0, my_password);
    pyperclip.copy(my_password);

#save to file. 

def save_password():
    website = website_entry.get();
    password = password_entry.get();
    email = email_entry.get();
    new_data = {
        website :{
            "email" : email,
            "password" : password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops!", message="Please fill out all the fields");
    else:
        try:
            with open("Day 29/data.json", 'r') as file:
                data = json.load(file);
        except:
            with open("Day 29/data.json", 'w') as file:
                json.dump(new_data, file, indent=4);
        else:
            #we update the data
            data.update(new_data)
            #we write it in json file
            with open("Day 29/data.json", 'w') as file:
                json.dump(data, file, indent=4);

        finally:
            website_entry.delete(0, END);
            password_entry.delete(0, END);


def search():
    website = website_entry.get();
    try:
        with open('Day 29/data.json') as file:
            data = json.load(file);
    except:
        messagebox.showerror(title="Oops!", message="No password saved yet!");
    else:
        if website in data:
            mail = data[website]['email'];
            password = data[website]['password'];
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}");
        else:
            messagebox.showerror(title="Oops", message="No info regarding this website.");

#UI part

window = Tk();
window.title("Password Manager");
window.config(padx=20, pady=20);

canvas = Canvas(width=200, height=200);
logo_image = PhotoImage(file = 'Day 29/logo.png');
canvas.create_image(100, 100, image = logo_image);
canvas.grid(row=0, column=1);

#labels
website_label = Label(text="Website:", font=FONT);
website_label.grid(row=1, column=0);

email_label = Label(text="Email/Username:", font=FONT);
email_label.grid(row=2, column=0);

password_label= Label(text="Password", font=FONT);
password_label.grid(row=3, column=0);

#entries
website_entry = Entry(width=22);
website_entry.focus();
website_entry.grid(row=1, column=1);

email_entry = Entry(width=36);
email_entry.insert(0, 'tajale01@gmail.com');
email_entry.grid(row=2, column=1, columnspan=2);

password_entry = Entry(width=22);
password_entry.grid(row=3, column=1);

#buttons
generate_password_button = Button(text="Generate Password", command=generate_password);
generate_password_button.grid(row=3, column=2);

add_button = Button(text="Add", width=37, command=save_password);
add_button.grid(row=4, column=1, columnspan=2);

search_button = Button(text="Search", width=13, command=search);
search_button.grid(row=1, column=2);

window.mainloop();