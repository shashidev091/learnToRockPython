from data import question_data
from quiz_brain import QuizBrain


class Question:
    def __init__(self, text, ans):
        self.text = text
        self.answer = ans

    def __str__(self):
        return "text: " + str(self.text) + ", answer: " + self.answer


question_bank = []

for question in question_data:
    question_text = question['text']
    question_answer = question["answer"]
    new_questions = Question(question_text, question_answer)
    question_bank.append(new_questions)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
else:
    print("you've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")
