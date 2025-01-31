from tkinter import *;
import pandas;
import random;

BACKGROUND_COLOR = "#B1DDC6"

# ---------------- create new flash card ----------------

data = pandas.read_csv('Day 31/data/french_words.csv');
data_list = [{row.French: row.English} for index, row in data.iterrows()];
random_word = {}

def generate_new_flash():
    global random_word, flip_timer;
    random_word = random.choice(data_list);
    window.after_cancel(flip_timer);
    for item, value in random_word.items():
        random_french = item;

    canvas.itemconfig(word, text = random_french, fill = 'black');
    canvas.itemconfig(language, text = "French", fill = 'black');
    canvas.itemconfig(card_image, image = card_front_image);
    flip_timer = window.after(3000, func=flip_card);

def flip_card():
    for item, value in random_word.items():
        random_english = value;

    canvas.itemconfig(card_image,image = card_back_image);
    canvas.itemconfig(language, fill = 'white', text = "English");
    canvas.itemconfig(word, fill = 'white', text = random_english);


# ---------------- UI ----------------

window = Tk();
window.title('Flashy');
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR);

flip_timer = window.after(3000, func=flip_card);

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0);
card_front_image = PhotoImage(file = "Day 31/images/card_front.png");
card_back_image = PhotoImage(file = 'Day 31/images/card_back.png');
card_image = canvas.create_image(400, 263, image =card_front_image);
canvas.grid(row=0, column=0, columnspan=2);

#text in canvas
language = canvas.create_text(400, 150,  text = 'French', font = ("verdana", 40, 'italic'));
word = canvas.create_text(400, 263, text = 'Trouve', font = ('verdana', 60, 'bold'));
# change_image();

generate_new_flash();

wrong_image = PhotoImage(file = 'Day 31/images/wrong.png');
wrong_button = Button(image=wrong_image, highlightthickness=0, command=generate_new_flash);
wrong_button.grid(row=1, column=0);

right_image = PhotoImage(file = 'Day 31/images/right.png');
right_button = Button(image = right_image, highlightthickness=0, command=generate_new_flash);
right_button.grid(row=1, column=1);



window.mainloop();
