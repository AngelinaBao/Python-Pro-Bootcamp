from data import question_data
from question import Question
class Answer:
    def __init__(self):
        self.answer = input()
        self.score = 0


    def answer_judgement(self, question_data=question_data):
        for index in range(len(question_data)):
            question = Question(question_data, index)
            answer = input(f"Q.{index+1}: {question.text} (True/False): ").title()
            if answer == question.answer:
                self.score += 1
                print("You got it right!")
            else:
                print("You're wrong.")
            print(f"The correct answer was: {question.answer}")
            print(f"Your current score is: {self.score}/{index+1}\n\n")
        
        print("You've complete the quiz.")
        print(f"your final score is {self.score}/{index+1}")