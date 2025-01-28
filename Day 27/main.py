from tkinter import *;

window = Tk();
window.title('my GUI app');
window.minsize(width = 500, height = 300);

def button_clicked():
    my_label['text'] = user_input.get();

my_label = Label(text='Im a label', font=('verdana', 20, 'italic'));
my_label.grid(column=0, row=0);

user_input = Entry(width=10);
user_input.grid(column=3, row=2);

my_button = Button(text='Click me', command=button_clicked);
my_button.grid(column=1, row=1);

new_button = Button(text='click me too');
new_button.grid(column=2, row=0);










window.mainloop();