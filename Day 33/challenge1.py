from tkinter import *;
import requests;


def get_quote():
    response = requests.get('https://api.kanye.rest');
    data = response.json();
    quote = data['quote'];
    canvas.itemconfig(kanye_quote, text = data['quote']);


window = Tk();
window.title('Kanye Says....');
window.config(padx=50, pady=50);

canvas = Canvas(width=300, height=414);
background_img = PhotoImage(file = 'Day 33/background.png');
canvas.grid(row = 0, column = 0);

canvas.create_image(150, 207, image = background_img);

kanye_quote = canvas.create_text(150, 207, text = '', font = ('verdana', 25, 'bold'), fill = 'white', width = 250);

get_quote();

kanye_img = PhotoImage(file = 'Day 33/kanye.png');
kanye_button = Button(image=kanye_img, command=get_quote);
kanye_button.grid(row=1, column=0);


window.mainloop();