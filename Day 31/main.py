from tkinter import *;
import pandas;
import random;

BACKGROUND_COLOR = "#B1DDC6"

my_data = pandas.read_csv('Day 31/data/french_words.csv');
data_dict = my_data.to_dict('record');


def generate_word():
    random_data = random.choice(data_dict);

    random_french_word = random_data['French'];

    canvas.itemconfig(word_text, text = random_french_word);














window = Tk();
window.title('Flashy');
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR);

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0);
card_front_image = PhotoImage(file = 'Day 31/images/card_front.png');
canvas.create_image(400, 263, image = card_front_image);
canvas.grid(row=0, column=0, columnspan=2);

title_text = canvas.create_text(400, 150, text = "French", font = ('verdana', 40, 'italic' ));


word_text = canvas.create_text(400, 263, text = 'word', font = ('verdana', 60, 'bold'));

#buttons
right_button_image = PhotoImage(file = 'Day 31/images/right.png');
right_button = Button(image = right_button_image, highlightthickness=0, command=generate_word);
right_button.grid(row=1, column=1);

wrong_button_image = PhotoImage(file = 'Day 31/images/wrong.png');
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=generate_word);
wrong_button.grid(row=1, column=0);


window.mainloop();