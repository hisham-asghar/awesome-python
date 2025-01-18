
import random
import requests
import json

# Define the topics and their associated facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The largest known prime number as of 2021 has 23 million digits.",
            "The first successful kidney transplant was performed in 1954."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "What is the process by which plants convert light energy into chemical energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": "Photosynthesis"
            },
            {
                "question": "What is the name of the force that attracts objects with mass towards each other?",
                "options": ["Gravity", "Friction", "Electromagnetism", "Nuclear force"],
                "answer": "Gravity"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 and had only one button.",
            "The first commercial email service was launched in 1971 by Ray Tomlinson.",
            "The first smartphone was the IBM Simon, released in 1992."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "What is the name of the most widely used search engine in the world?",
                "options": ["Bing", "Yahoo", "DuckDuckGo", "Google"],
                "answer": "Google"
            },
            {
                "question": "What is the name of the technology that allows devices to communicate wirelessly?",
                "options": ["Bluetooth", "Wi-Fi", "Ethernet", "Infrared"],
                "answer": "Bluetooth"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers.",
            "The Declaration of Independence was signed on July 4, 1776."
        ],
        "quiz_questions": [
            {
                "question": "What was the name of the first successful computer operating system?",
                "options": ["MS-DOS", "Windows", "Linux", "macOS"],
                "answer": "MS-DOS"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
                "answer": "George Washington"
            },
            {
                "question": "What was the name of the ancient Greek philosopher who is considered the father of Western philosophy?",
                "options": ["Plato", "Socrates", "Aristotle", "Pythagoras"],
                "answer": "Socrates"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.",
            "The largest known prime number as of 2021 has 23 million digits.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "What is the name of the tallest mountain in the world?",
                "options": ["K2", "Everest", "Kangchenjunga", "Makalu"],
                "answer": "Everest"
            },
            {
                "question": "What is the name of the largest continent on Earth?",
                "options": ["Africa", "Asia", "North America", "South America"],
                "answer": "Asia"
            }
        ]
    }
}

def display_menu():
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    topic = input("Enter your choice: ").lower()
    return topic

def display_fact(topic):
    fact = random.choice(topics[topic]["facts"])
    print(f"\nFact about {topic.capitalize()}:")
    print(fact)

def run_quiz(topic):
    print(f"\nTime for a {topic.capitalize()} quiz!")
    score = 0
    questions = topics[topic]["quiz_questions"]
    for question in questions:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = input("Enter your answer (1-4): ")
        if question["options"][int(user_answer) - 1] == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"\nYour final score is {score} out of {len(questions)}.")

def main():
    topic = display_menu()
    display_fact(topic)
    run_quiz(topic)

if __name__ == "__main__":
    main()
