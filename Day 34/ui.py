from tkinter import *;
from quiz_brain import QuizBrain;
import time;

THEME_COLOR = "#375362"


class UiInterface:
    def __init__(self, quiz_brain : QuizBrain):
        self.quiz = quiz_brain;
        self.window = Tk();
        self.window.title('Quizzler');

        self.window.config(padx=20, pady=20, bg=THEME_COLOR);

        #score label
        self.score_label = Label(text='Score: 0', bg=THEME_COLOR, highlightthickness=0,fg='white');
        self.score_label.grid(row=0, column=1);

        #canvas
        self.canvas = Canvas(width=300, height=250, bg='white');
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50);

        #canvas text
        self.question_text = self.canvas.create_text(150, 125, text = 'question', font = ('verdana', 20, 'italic'), width = 280, fill = THEME_COLOR);

        #buttons
        self.true_button_image = PhotoImage(file = 'Day 34/images/true.png');
        self.true_button = Button(image=self.true_button_image, highlightthickness=0, command=self.clicked_true_button);
        self.true_button.grid(row=2, column=0);

        self.false_button_image = PhotoImage(file = 'Day 34/images/false.png');
        self.false_button = Button(image=self.false_button_image, highlightthickness=0, command=self.clicked_false_button);
        self.false_button.grid(row=2, column=1);


        self.generate_question();

        self.window.mainloop();

    def generate_question(self):
        self.canvas.configure(bg = 'white');
        if self.quiz.still_has_questions():
            question = self.quiz.next_question();
            self.canvas.itemconfig(self.question_text, text = question);
            self.score_label.config(text = f"Score: {self.quiz.score}");
        else:
            self.canvas.itemconfig(self.question_text, text = "You've reached end of the quiz, thank you for playing!");
            self.true_button.config(state='disabled');
            self.false_button.config(state='disabled');

    def clicked_true_button(self):
        self.give_feedback(self.quiz.check_answer('true'));

    def clicked_false_button(self):
        self.give_feedback(self.quiz.check_answer('false'));
    

    def give_feedback(self,user_answer):
        if user_answer:
            self.canvas.configure(bg = 'green');
        else:
            self.canvas.configure(bg = 'red');
        self.window.after(1000,self.generate_question);

