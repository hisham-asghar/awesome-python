
import random
import requests
import json

# Define topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion meaning the iron heats up, the particles get slightly farther apart, and the tower grows.",
            "A single cloud can weigh more than 1 million pounds."
        ],
        "quizzes": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Hg"],
                "answer": 0
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["O-", "AB+", "B-", "AB-"],
                "answer": 3
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Mars", "Saturn", "Jupiter", "Neptune"],
                "answer": 2
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, weighed 30 tons and took up 1800 square feet.",
            "The first text message was sent on December 3, 1992, and it said 'Merry Christmas'.",
            "The 'qwerty' keyboard layout was designed to slow down typing, not speed it up."
        ],
        "quizzes": [
            {
                "question": "What does 'GUI' stand for?",
                "options": ["Graphical User Interface", "Geospatial User Interface", "Global Unique Identifier", "Graphical Universal Interface"],
                "answer": 0
            },
            {
                "question": "What is the name of the first commercially available personal computer?",
                "options": ["Apple I", "Commodore 64", "IBM PC", "Altair 8800"],
                "answer": 2
            },
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first person convicted of speeding was Walter Arnold of East Peckham, Kent, UK, in 1896. He was fined 1 shilling for driving at 8 mph, which was 5 mph over the speed limit."
        ],
        "quizzes": [
            {
                "question": "What year was the Declaration of Independence signed?",
                "options": ["1776", "1789", "1812", "1865"],
                "answer": 0
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "Benjamin Franklin"],
                "answer": 2
            },
            {
                "question": "What was the name of the first successful powered flight by the Wright brothers?",
                "options": ["The Spirit of St. Louis", "The Wright Flyer", "The Kitty Hawk", "The Orville"],
                "answer": 1
            }
        ]
    },
    "general": {
        "facts": [
            "A group of porcupines is called a prickle.",
            "The first product to have a barcode was Wrigley's gum.",
            "The King of Hearts is the only king without a mustache on a standard playing card."
        ],
        "quizzes": [
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Liver", "Skin", "Lungs"],
                "answer": 2
            },
            {
                "question": "What is the tallest mammal in the world?",
                "options": ["Elephant", "Giraffe", "Hippopotamus", "Rhinoceros"],
                "answer": 1
            },
            {
                "question": "What is the rarest M&M color?",
                "options": ["Brown", "Yellow", "Red", "Blue"],
                "answer": 3
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the specified topic.
    """
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    """
    Retrieves a random quiz question and its options from the specified topic.
    """
    quiz = random.choice(topics[topic]["quizzes"])
    return quiz["question"], quiz["options"]

def check_answer(topic, answer_index):
    """
    Checks if the user's answer is correct for the given quiz question.
    """
    quiz = random.choice(topics[topic]["quizzes"])
    return quiz["answer"] == answer_index

def main():
    """
    The main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))

        print("\nNow, let's test your knowledge with a quiz!")
        question, options = get_quiz_question(selected_topic)
        print(question)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

        user_answer = int(input("Enter your answer (1-4): "))
        if check_answer(selected_topic, user_answer - 1):
            print("Correct! You're a knowledge master.")
        else:
            print("Oops, that's not the right answer. Better luck next time!")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
