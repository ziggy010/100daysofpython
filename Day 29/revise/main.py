from tkinter import *;
from tkinter import messagebox;
import random;
import json;


BACKGROUND_COLOR = "#B1DDC6"
FONT_DETAIL = ('verdana', 14);


window = Tk();
window.title('Password Manager');
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR);


def random_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    random_letter = [random.choice(letters) for _ in range(random.randint(4,6))];
    random_number = [random.choice(numbers) for _ in range(random.randint(2,4))];
    random_symbol = [random.choice(symbols) for _ in range(random.randint(2,4))];

    random_password = random_letter + random_number + random_symbol;
    random.shuffle(random_password);

    final_password = "".join(random_password);

    random_entry_password = password_entry.get();

    if len(random_entry_password) > 0:
        password_entry.delete(0, END);
    password_entry.insert(0, final_password);
    


def add():
    website = website_entry.get();
    email = email_entry.get();
    password = password_entry.get();
    new_data = {
        website : {
            'Email' : email,
            'Password' : password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title='Oops', message="Please fill up all the fields!");
    else:
        is_ok = messagebox.askokcancel(title={website}, message=f"These are the details you provided:\nEmail: {email}\nPassword:{password}\nWould you like to save this data?")
    
    if is_ok:
        try:
            with open('Day 29/revise/data.json') as file:
                data = json.load(file);
        except:
            with open("Day 29/revise/data.json", 'w') as file:
                json.dump(new_data, file,  indent=4);
        else:
            if website in data:
                yes_or_no = messagebox.askokcancel(title=website, message=f"You already have data for {website}, would you like to update it?");
                if yes_or_no:
                    pass;
            else:
                data.update(new_data);
                with open('Day 29/revise/data.json', 'w') as file:
                    json.dump(data, file, indent=4);
        finally:
            website_entry.delete(0, END);
            password_entry.delete(0, END);

def search():
    website = website_entry.get();

    try:

        with open('Day 29/revise/data.json') as file:
            data = json.load(file);
    except:
        messagebox.showerror(title="Oops!", message="No password saved yet!");
    
    else:
        if website in data:
            email = data[website]['Email'];
            password = data[website]['Password'];
            messagebox.showinfo(title=website, message=f"Details for {website} is:\nEmail: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Oops!", message=f"No password saved for {website}")



canvas = Canvas(height=224, width=200, bg=BACKGROUND_COLOR, highlightthickness=0);
logo_image = PhotoImage(file = "Day 29/revise/logo.png");
canvas.create_image(112, 100, image = logo_image);
canvas.grid(row=0, column=1);

#labels
website_label = Label(text = 'Website: ',  font = FONT_DETAIL, bg=BACKGROUND_COLOR);
website_label.grid(row = 1, column = 0);

email_label = Label(text = 'Email/Username:', font = FONT_DETAIL, bg=BACKGROUND_COLOR);
email_label.grid(row = 2, column = 0);

password_label = Label(text = "Password: ", font= FONT_DETAIL, bg=BACKGROUND_COLOR);
password_label.grid(row= 3, column=0);

#entries
website_entry = Entry(width=22, bg=BACKGROUND_COLOR, highlightthickness=0);
website_entry.focus();
website_entry.grid(row=1, column=1);

email_entry = Entry(width=36, bg=BACKGROUND_COLOR, highlightthickness=0);
email_entry.insert(0, 'tajale01@gmail.com');
email_entry.grid(row=2, column=1, columnspan=2);

password_entry = Entry(width=22, bg=BACKGROUND_COLOR, highlightthickness=0);
password_entry.grid(row=3, column=1);

#buttons;
generate_button = Button(text='Generate Password', bg=BACKGROUND_COLOR, highlightthickness=0, command=random_password);
generate_button.grid(row=3, column=2);

add_button = Button(text = "Add", width=36, bg=BACKGROUND_COLOR, highlightthickness=0, command=add);
add_button.grid(row=4, column=1, columnspan=2);

search_button = Button(text="Search", bg = BACKGROUND_COLOR, highlightthickness=0, width=14, command=search);
search_button.grid(row=1, column=2);


window.mainloop();