import os

# Shorthands for development
pause = lambda: os.system("pause")


first_quiz = {
    
    "first" : {
        "question" : "Which programming language is the youngest among these?",
        "answer_one" : "Javascript",
        "answer_two" : "Python",
        "answer_three" : "Haskell",
        "answer_correct" : "answer_one",
        "background_info" : "Javascript was released in 1995, Haskell in 1990 and Python in 1989."
    },

    "second" : {
        "question" : "What does BDD stand for in the context of software design?",
        "answer_one" : "Behaviour Driven Development",
        "answer_two" : "Behaviourally Destructive Development",
        "answer_three" : "Bad Development Decisions",
        "answer_correct" : "answer_one",
        "background_info" : "Behaviour Driven Development (short: BDD) is a software design concept which urges developers to think about how the software ought to perform instead of thinking about how to build it this result in a more declarative development attitude."
    }
}

second_quiz = {
    "first" : {
        "question" : "Which programming language is the youngest among these?",
        "answer_one" : "Javascript",
        "answer_two" : "Python",
        "answer_three" : "Haskell",
        "answer_correct" : "answer_one",
        "background_info" : "Javascript was released in 1995, Haskell in 1990 and Python in 1989."
    },

    "second" : {
        "question" : "",
        "answer_one" : "",
        "answer_two" : "",
        "answer_three" : "",
        "answer_correct" : "",
        "background_info" : ""
    },

    "third" : {
        "question" : "",
        "answer_one" : "",
        "answer_two" : "",
        "answer_three" : "",
        "answer_correct" : "",
        "background_info" : ""
    }
}


def quiz_engine(quiz):
    print("Welcome to the Quiz Demo!")
    print("Press any key to continue.")
    pause()

print(quiz)