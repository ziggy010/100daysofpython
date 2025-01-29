
from tkinter import *;
import math;


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
REPS = 0;

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global REPS;
    REPS += 1;

    work_sec = WORK_MIN * 60;
    short_break_sec = SHORT_BREAK_MIN * 60;
    long_break_sec = LONG_BREAK_MIN * 60;

    if REPS % 8 == 0:
        count_down(long_break_sec);
    elif REPS % 2 == 0:
        count_down(short_break_sec);
    else:
        count_down(work_sec);

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count/60);
    count_sec = count % 60;

    if count_sec < 10:
        count_sec = f"0{count_sec}";
    canvas.itemconfig(timer_canvas_text, text = f"{count_min}:{count_sec}")
    


    if count > 0:
        window.after(1000, count_down, count-1);
    else:
        start_timer();


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