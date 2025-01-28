from tkinter import *;

window = Tk();
window.title('Mile to Km Converter');
window.minsize(width=300, height = 130);
window.config(padx=15, pady=15);

FONT = ("verdana", 13);
ANSWER = 0;

def calculate():
    user= int(user_input.get());
    
    answer_label['text'] = str(round(user * 1.6));

#userinput
user_input = Entry(width=10);
user_input.grid(row=0, column=1);

#label
miles_label = Label(text='Miles', font=FONT);
miles_label.grid(row=0, column=2);

#label1 
label1 = Label(text="is equal to ", font=FONT);
label1.grid(row=1, column=0);

#answer label
answer_label = Label(text=ANSWER, font=FONT);
answer_label.grid(row=1, column=1);

#km lable
km_label = Label(text='Km', font=FONT);
km_label.grid(row=1, column=2);

#button
my_button = Button(text='Calculate', font=FONT, command=calculate);
my_button.grid(row=2, column=1);





window.mainloop();