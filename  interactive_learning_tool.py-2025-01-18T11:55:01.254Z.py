
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Milky Way galaxy contains an estimated 100 to 400 billion stars.",
            "Honey is the only food that does not spoil."
        ],
        "quizzes": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": "Photosynthesis"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
                "answer": "Jupiter"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The internet was originally called ARPANET, which was created in 1969.",
            "The first digital camera was created in 1975 by Steven Sasson."
        ],
        "quizzes": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "What is the name of the first commercially available personal computer?",
                "options": ["Apple II", "IBM PC", "Commodore 64", "TRS-80"],
                "answer": "IBM PC"
            },
            {
                "question": "What is the name of the technology that allows devices to connect to the internet without wires?",
                "options": ["Bluetooth", "Wi-Fi", "Ethernet", "NFC"],
                "answer": "Wi-Fi"
            }
        ]
    },
    "history": {
        "facts": [
            "The first known written language was cuneiform, developed by the Sumerians in Mesopotamia around 3500 BC.",
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci between 1503 and 1519."
        ],
        "quizzes": [
            {
                "question": "What year was the Declaration of Independence signed?",
                "options": ["1776", "1787", "1812", "1865"],
                "answer": "1776"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "James Madison"],
                "answer": "George Washington"
            },
            {
                "question": "What ancient civilization built the pyramids in Giza?",
                "options": ["Aztecs", "Incas", "Egyptians", "Greeks"],
                "answer": "Egyptians"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The world's largest desert is Antarctica, which is covered in ice.",
            "The tallest mammal in the world is the giraffe.",
            "The human brain contains approximately 86 billion neurons."
        ],
        "quizzes": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": "AB"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
                "answer": "Jupiter"
            }
        ]
    }
}

def get_random_fact(topic):
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    quiz = random.choice(topics[topic]["quizzes"])
    return quiz["question"], quiz["options"], quiz["answer"]

def run_interactive_learning():
    print("Welcome to the Interactive Learning Tool!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()
    if selected_topic not in topics:
        print("Invalid topic. Please try again.")
        return

    print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
    print(get_random_fact(selected_topic))

    print("\nNow, let's test your knowledge with a quiz!")
    question, options, answer = get_quiz_question(selected_topic)
    print(question)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    user_answer = input("Enter your answer (1-4): ")
    if options[int(user_answer) - 1] == answer:
        print("Correct! You're a knowledge master.")
    else:
        print(f"Incorrect. The correct answer is {answer}.")

    print("\nThank you for using the Interactive Learning Tool!")

run_interactive_learning()
