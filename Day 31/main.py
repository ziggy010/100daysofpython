from tkinter import *;
import pandas;
import random;

BACKGROUND_COLOR = "#B1DDC6"

try:
    my_data = pandas.read_csv('Day 31/data/words_to_learn.csv');
except:
    my_data = pandas.read_csv('Day 31/data/french_words.csv');

data_dict = my_data.to_dict('records');

random_data = {};

def generate_word():
    global random_data;
    window.after_cancel(flip_image);
    random_data = random.choice(data_dict);
    random_french_word = random_data['French'];
    canvas.itemconfig(card_image, image = card_front_image);
    canvas.itemconfig(title_text, fill = 'black', text = 'French')
    canvas.itemconfig(word_text, text = random_french_word, fill = 'black');
    window.after(3000, flip_image);

def right_button():
    data_dict.remove(random_data);
    data = pandas.DataFrame(data_dict);
    data.to_csv("Day 31/data/words_to_learn.csv", index = False);
    generate_word();





def flip_image():
    global random_data;
    random_english_word = random_data['English'];
    canvas.itemconfig(card_image, image = card_back_image);
    canvas.itemconfig(title_text, fill = 'white', text = 'English');
    canvas.itemconfig(word_text, fill = 'white', text = random_english_word);



window = Tk();
window.title('Flashy');
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR);


canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0);
card_front_image = PhotoImage(file = 'Day 31/images/card_front.png');
card_back_image = PhotoImage(file = 'Day 31/images/card_back.png');
card_image = canvas.create_image(400, 263, image = card_front_image);
canvas.grid(row=0, column=0, columnspan=2);

title_text = canvas.create_text(400, 150, text = "French", font = ('verdana', 40, 'italic' ), fill = 'black');
word_text = canvas.create_text(400, 263, font = ('verdana', 60, 'bold'), fill = 'black');
generate_word();


window.after(3000, flip_image);

#buttons
right_button_image = PhotoImage(file = 'Day 31/images/right.png');
right_button = Button(image = right_button_image, highlightthickness=0, command=right_button);
right_button.grid(row=1, column=1);

wrong_button_image = PhotoImage(file = 'Day 31/images/wrong.png');
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=generate_word);
wrong_button.grid(row=1, column=0);


window.mainloop();