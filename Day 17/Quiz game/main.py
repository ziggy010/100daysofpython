from question_model import Question;
from data import question_data;
from quiz_brain import QuizBrain;

question_bank = [];

for item in question_data:
    question_bank.append(Question(text=item["text"], answer=item["answer"]));

my_question = QuizBrain(q_list=question_bank);

while my_question.still_has_questions():
    my_question.next_question();

