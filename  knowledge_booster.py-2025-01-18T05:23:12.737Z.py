Here is the raw Python code without any additional commentary:

import random
import requests
import json

# Define the topics and their associated facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "Bananas are slightly radioactive.",
            "The hottest temperature ever recorded on Earth was 154°F (68°C) in Death Valley, California."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Fe", "Cu"],
                "answer": "Au"
            },
            {
                "question": "Which planet in our solar system has the most moons?",
                "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
                "answer": "Saturn"
            },
            {
                "question": "What is the name of the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Evaporation"],
                "answer": "Photosynthesis"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer virus was created in 1983 and was called the 'Elk Cloner'.",
            "The first smartphone was the IBM Simon, released in 1992.",
            "The first electronic computer, the ENIAC, was completed in 1946 and weighed 30 tons."
        ],
        "quiz_questions": [
            {
                "question": "What does the abbreviation 'CPU' stand for?",
                "options": ["Central Processing Unit", "Computer Power Unit", "Centralized Processing Unit", "Computer Processing Unit"],
                "answer": "Central Processing Unit"
            },
            {
                "question": "Which company developed the first commercially successful graphical user interface (GUI)?",
                "options": ["Apple", "Microsoft", "Xerox", "IBM"],
                "answer": "Xerox"
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
            "The first electric traffic lights were installed in Cleveland, Ohio, in 1914."
        ],
        "quiz_questions": [
            {
                "question": "In what year did the United States declare its independence?",
                "options": ["1776", "1789", "1812", "1865"],
                "answer": "1776"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "James Madison"],
                "answer": "George Washington"
            },
            {
                "question": "What was the name of the ancient Egyptian civilization that built the pyramids?",
                "options": ["Mesopotamians", "Incas", "Mayans", "Egyptians"],
                "answer": "Egyptians"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion meaning the iron heats up, the particles need more space and the tower grows in height.",
            "A group of porcupines is called a prickle."
        ],
        "quiz_questions": [
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
                "question": "Which planet in our solar system is known as the 'Red Planet'?",
                "options": ["Mars", "Jupiter", "Venus", "Saturn"],
                "answer": "Mars"
            }
        ]
    }
}

def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    return input("Enter your choice: ").lower()

def display_fact(topic):
    fact = random.choice(topics[topic]["facts"])
    print(f"\nFact about {topic.capitalize()}:")
    print(fact)

def run_quiz(topic):
    print(f"\nTime for a {topic.capitalize()} quiz!")
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