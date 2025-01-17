
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "Science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The largest known prime number as of 2021 has 23 million digits.",
            "The first confirmed sighting of a black hole was in 1971."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "What is the name of the closest star to Earth?",
                "options": ["Sirius", "Proxima Centauri", "Betelgeuse", "Polaris"],
                "answer": "Proxima Centauri"
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Evaporation", "Transpiration"],
                "answer": "Photosynthesis"
            }
        ]
    },
    "Technology": {
        "facts": [
            "The first computer virus, called 'Creeper', was created in 1971.",
            "The first commercial text message was sent on December 3, 1992.",
            "The first electric car was developed in Scotland in the 19th century."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "What is the name of the first commercially successful smartphone?",
                "options": ["iPhone", "BlackBerry", "Nokia 3310", "Motorola RAZR"],
                "answer": "BlackBerry"
            },
            {
                "question": "What is the name of the first web browser?",
                "options": ["Internet Explorer", "Mozilla Firefox", "Google Chrome", "Mosaic"],
                "answer": "Mosaic"
            }
        ]
    },
    "History": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first Olympic Games were held in 776 BC in Olympia, Greece."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for building the pyramids?",
                "options": ["Aztecs", "Incas", "Egyptians", "Mayans"],
                "answer": "Egyptians"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
                "answer": "George Washington"
            },
            {
                "question": "What was the name of the first successful powered flight by the Wright brothers?",
                "options": ["Kitty Hawk", "Wright Flyer", "Spirit of St. Louis", "Concorde"],
                "answer": "Wright Flyer"
            }
        ]
    },
    "General Knowledge": {
        "facts": [
            "The largest known prime number as of 2021 has 23 million digits.",
            "The first confirmed sighting of a black hole was in 1971.",
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "What is the tallest mountain in the world?",
                "options": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
                "answer": "Mount Everest"
            },
            {
                "question": "What is the name of the longest river in the world?",
                "options": ["Amazon River", "Nile River", "Mississippi River", "Yangtze River"],
                "answer": "Nile River"
            }
        ]
    }
}

def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    return input("Enter your choice: ")

def display_fact(topic):
    fact = random.choice(topics[topic]["facts"])
    print(f"\nFact about {topic}:")
    print(f"- {fact}")

def run_quiz(topic):
    print(f"\nTime to test your {topic} knowledge!")
    score = 0
    for question in topics[topic]["quiz_questions"]:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = input("Enter your answer (1-4): ")
        if question["options"][int(user_answer) - 1] == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"\nYour final score: {score}/{len(topics[topic]['quiz_questions'])}")

def main():
    topic = display_menu()
    display_fact(topic)
    run_quiz(topic)

if __name__ == "__main__":
    main()
