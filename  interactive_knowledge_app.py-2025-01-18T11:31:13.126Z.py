Here is the raw Python code extracted from the JSON:

```python
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The largest known prime number as of 2022 has 23 million digits.",
            "The first digital computer, ENIAC, weighed 30 tons and took up 1,800 square feet."
        ],
        "quiz": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Hg"],
                "answer": 0
            },
            {
                "question": "What is the name of the process where water changes from a liquid to a gas?",
                "options": ["Condensation", "Evaporation", "Sublimation", "Precipitation"],
                "answer": 1
            },
            {
                "question": "What is the name of the force that attracts objects with mass towards each other?",
                "options": ["Gravity", "Friction", "Electromagnetism", "Buoyancy"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented by Douglas Engelbart in 1964.",
            "The first commercial email service was launched in 1978 by CompuServe.",
            "The world's first programmable computer, the ENIAC, was completed in 1946."
        ],
        "quiz": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "What is the name of the company that created the first commercial web browser, Mosaic?",
                "options": ["Apple", "Microsoft", "Netscape", "IBM"],
                "answer": 2
            },
            {
                "question": "What is the name of the device that converts digital signals into analog signals?",
                "options": ["Modem", "Router", "Switch", "Amplifier"],
                "answer": 0
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Magna Carta, a landmark document in the history of democracy, was signed in 1215 in England.",
            "The first successful powered flight was made by the Wright brothers in 1903."
        ],
        "quiz": [
            {
                "question": "What year did Christopher Columbus arrive in the Americas?",
                "options": ["1492", "1498", "1506", "1512"],
                "answer": 0
            },
            {
                "question": "What was the name of the first successful powered flight?",
                "options": ["The Wright Flyer", "The Kitty Hawk", "The Spirit of St. Louis", "The Concorde"],
                "answer": 0
            },
            {
                "question": "What was the name of the first permanent English settlement in North America?",
                "options": ["Jamestown", "Plymouth Colony", "Massachusetts Bay Colony", "New Amsterdam"],
                "answer": 0
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first product to have a barcode was Wrigley's gum.",
            "A group of porcupines is called a prickle."
        ],
        "quiz": [
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Liver", "Skin", "Brain"],
                "answer": 2
            },
            {
                "question": "What is the name of the tallest mountain in the world?",
                "options": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
                "answer": 0
            },
            {
                "question": "What is the name of the longest river in the world?",
                "options": ["Nile", "Amazon", "Mississippi-Missouri", "Yangtze"],
                "answer": 0
            }
        ]
    }
}

def interactive_knowledge_app():
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()
    if selected_topic not in topics:
        print("Invalid topic. Please try again.")
        return

    print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
    print(random.choice(topics[selected_topic]["facts"]))

    print("\nNow, let's test your knowledge with a quiz!")
    quiz_questions = topics[selected_topic]["quiz"]
    score = 0
    for question in quiz_questions:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer - 1 == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"\nYour final score is {score} out of {len(quiz_questions)}")

interactive_knowledge_app()
