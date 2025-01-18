Here is the raw Python code extracted from the JSON:

import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Milky Way galaxy contains an estimated 200 billion stars.",
            "Diamonds are the hardest known natural material on Earth."
        ],
        "quiz": [
            {
                "question": "What is the main component of the Earth's atmosphere?",
                "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"],
                "answer": 1
            },
            {
                "question": "Which scientist is credited with developing the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Galileo Galilei"],
                "answer": 1
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, was completed in 1946 and weighed 30 tons.",
            "The internet was originally called ARPANET and was created in 1969 by the U.S. Department of Defense.",
            "The first mobile phone call was made in 1973 by Martin Cooper of Motorola."
        ],
        "quiz": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "Which company is known for creating the popular search engine Google?",
                "options": ["Apple", "Microsoft", "Amazon", "Alphabet"],
                "answer": 3
            },
            {
                "question": "What is the name of the device used to input data into a computer?",
                "options": ["Monitor", "Printer", "Keyboard", "Mouse"],
                "answer": 3
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.",
            "The first successful powered flight was made by the Wright brothers in 1903."
        ],
        "quiz": [
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Mesopotamia", "Egypt", "Greece", "China"],
                "answer": 2
            },
            {
                "question": "What was the name of the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "Benjamin Franklin"],
                "answer": 2
            },
            {
                "question": "Which event is considered the start of World War I?",
                "options": ["The assassination of Archduke Franz Ferdinand", "The bombing of Pearl Harbor", "The Cuban Missile Crisis", "The fall of the Berlin Wall"],
                "answer": 0
            }
        ]
    },
    "general": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The largest planet in our solar system is Jupiter.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off."
        ],
        "quiz": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "Which country is known as the 'Land of the Rising Sun'?",
                "options": ["China", "Japan", "South Korea", "India"],
                "answer": 1
            },
            {
                "question": "What is the name of the tallest mountain in the world?",
                "options": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
                "answer": 0
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
    print(f"\nFact about {topic.capitalize()}:\n{fact}")

def quiz(topic):
    print(f"\nTime for a {topic.capitalize()} quiz!")
    score = 0
    for question in topics[topic]["quiz"]:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): ")) - 1
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"\nYour final score is {score} out of {len(topics[topic]['quiz'])}")

def main():
    topic = display_menu()
    display_fact(topic)
    quiz(topic)

if __name__ == "__main__":
    main()