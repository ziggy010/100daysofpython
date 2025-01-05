class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0;
        self.questions_list = q_list;
        self.score = 0;
    
    def still_has_questions(self):
        if self.question_number < len(self.questions_list):
            return True;
        else:
            print(f"\nYou've completed the quiz\nYour final score was: {self.score}/{self.question_number}.");
            return False;

    def next_question(self):
        current_question = self.questions_list[self.question_number];
        self.question_number += 1;
        user_answer = input(f"\nQ.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer);

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1;
            print("\nYou got it right!")
        else:
            print("\nYou got it wrong!");
        
        print("\nThe correct answer was: ", correct_answer);
        print(f"\nYour current score is: {self.score}/{self.question_number}");