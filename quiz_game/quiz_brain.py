class QuizBrain:
    """Quiz Brain Class"""

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def check_answer(self, user_answer, correct_answer):
        if (
            user_answer.lower() == correct_answer.lower()
            or user_answer.lower() == correct_answer[0].lower()
        ):
            print("Correct!")
            self.score += 1
        else:
            print("Wrong!")
        print(f"The correct answer is: {correct_answer}")
        print(f"The current score is: {self.score}/{self.question_number}\n")

    def next_question(self):
        """Ask the next question"""
        question_index = self.question_number
        question = self.question_list[question_index]
        user_answer = input(
            f"Q.{question_index+1}: {question.text} (True/False)?\n"
        ).lower()
        self.question_number += 1

        self.check_answer(user_answer, question.answer)

    def still_has_questions(self):
        """Determine if there are any questions remaining"""
        return self.question_number < len(self.question_list)
