# Day 17
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def make_question_list():
    question_list = []
    for question in question_data:
        new_question = Question(question["text"], question["answer"])
        question_list.append(new_question)
    return question_list


def main():
    question_list = make_question_list()
    quiz = QuizBrain(question_list)
    while quiz.still_has_questions():
        quiz.next_question()

    print("You've completed the quiz!")
    print(f"Your final score was {quiz.score}/{quiz.question_number}.")


if __name__ == "__main__":
    main()
