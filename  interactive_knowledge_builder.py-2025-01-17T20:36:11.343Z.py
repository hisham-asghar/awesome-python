
import random
import requests
import json

# Define the topics and their respective facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest temperature ever recorded on Earth was 154°F (68°C) in Death Valley, California.",
            "The largest known prime number as of 2022 has 23 million digits."
        ],
        "quizzes": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "Which planet in our solar system has the most moons?",
                "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
                "answer": "Jupiter"
            },
            {
                "question": "What is the process called when water changes from a liquid to a gas?",
                "options": ["Condensation", "Evaporation", "Sublimation", "Precipitation"],
                "answer": "Evaporation"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The first mobile phone call was made on April 3, 1973, by Martin Cooper of Motorola.",
            "The internet was initially called ARPANET, which was created by the U.S. Department of Defense in 1969."
        ],
        "quizzes": [
            {
                "question": "What does the acronym 'HTML' stand for?",
                "options": ["Hyper Text Markup Language", "Hyperlink Text Markup Language", "Hyper Text Markup Layout", "Hyperlink Text Markup Layout"],
                "answer": "Hyper Text Markup Language"
            },
            {
                "question": "Which company developed the first commercially successful smartphone?",
                "options": ["Apple", "Samsung", "BlackBerry", "Nokia"],
                "answer": "BlackBerry"
            },
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first computer bug was a dead moth found trapped in a relay of the Harvard Mark II computer in 1947."
        ],
        "quizzes": [
            {
                "question": "What year was the Declaration of Independence signed?",
                "options": ["1776", "1789", "1812", "1865"],
                "answer": "1776"
            },
            {
                "question": "Which ancient civilization built the pyramids?",
                "options": ["Romans", "Greeks", "Egyptians", "Mayans"],
                "answer": "Egyptians"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "Benjamin Franklin"],
                "answer": "George Washington"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and raises the structure.",
            "Apples are more effective at waking you up in the morning than coffee."
        ],
        "quizzes": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "What is the tallest mammal?",
                "options": ["Elephant", "Giraffe", "Rhinoceros", "Hippopotamus"],
                "answer": "Giraffe"
            },
            {
                "question": "Which country is known as the 'Land of the Rising Sun'?",
                "options": ["China", "Japan", "South Korea", "North Korea"],
                "answer": "Japan"
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

def check_answer(topic, answer):
    """
    Checks if the user's answer is correct for the current quiz question.
    """
    quiz = random.choice(topics[topic]["quizzes"])
    return answer.lower() == quiz["answer"].lower()

def main():
    """
    The main function that runs the interactive knowledge-building program.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    while True:
        user_topic = input("Enter your topic choice: ").lower()
        if user_topic in topics:
            break
        else:
            print("Invalid topic. Please try again.")

    print(f"\nHere's a random fact about {user_topic.capitalize()}:")
    print(get_random_fact(user_topic))

    print("\nNow, let's test your knowledge with a quiz!")
    question, options = get_quiz_question(user_topic)
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    user_answer = input("Enter your answer (1-4): ")
    if check_answer(user_topic, user_answer):
        print("Correct! You're a knowledge master.")
    else:
        print("Oops, that's not the right answer. Better luck next time!")

    print("\nThank you for using the Interactive Knowledge Builder. Have a great day!")

if __name__ == "__main__":
    main()
