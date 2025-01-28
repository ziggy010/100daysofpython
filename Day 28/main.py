
from tkinter import *;
import math;


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    count_down(5*60);

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count/60);
    count_sec = count % 60;
    canvas.itemconfig(timer_canvas_text, text = f"{count_min}:{count_sec}")

    if count > 0:
        window.after(1000, count_down, count-1);


# ---------------------------- UI SETUP ------------------------------- #


window = Tk();
window.title('Pomodoro');
window.config(padx=100, pady=50, bg=YELLOW);

#timer label
timer_label = Label(text='Timer', font=(FONT_NAME, 40, 'bold'), fg=GREEN, bg=YELLOW);
timer_label.grid(row = 0, column=1);

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0);
tomato_image = PhotoImage(file = 'Day 28/tomato.png');
canvas.create_image(100, 112, image = tomato_image);
timer_canvas_text = canvas.create_text(100,130, text = '00:00', font = (FONT_NAME, 35, 'bold'), fill = 'white');
canvas.grid(row=1, column=1);

#buttons
start_button = Button(text='Start', command=start_timer);
start_button.grid(row=2, column=0);

reset_button = Button(text="Reset");
reset_button.grid(row=2, column=2);

tick_label = Label(text="✅", bg=YELLOW);
tick_label.grid(row=3, column=1);





window.mainloop();