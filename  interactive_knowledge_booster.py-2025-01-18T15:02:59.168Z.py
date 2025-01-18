
import random
import requests
import json

# Define the topics and their respective facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest planet in the Solar System is Venus, not Mercury.",
            "Bees can fly higher than the tallest building."
        ],
        "quiz_questions": [
            {
                "question": "What is the main component of the Earth's atmosphere?",
                "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Argon"],
                "answer": 1
            },
            {
                "question": "What is the name of the force that keeps planets in orbit around the Sun?",
                "options": ["Gravity", "Centrifugal force", "Electromagnetic force", "Friction"],
                "answer": 0
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Respiration", "Photosynthesis", "Transpiration", "Fermentation"],
                "answer": 1
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 and had only one button.",
            "The first mobile phone call was made on April 3, 1973.",
            "The first commercial website was launched in 1991."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "What is the name of the search engine founded by Larry Page and Sergey Brin?",
                "options": ["Bing", "Yahoo", "Google", "DuckDuckGo"],
                "answer": 2
            },
            {
                "question": "What is the name of the operating system developed by Apple Inc.?",
                "options": ["Windows", "Linux", "macOS", "Android"],
                "answer": 2
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza are the only remaining wonder of the ancient world.",
            "The Magna Carta was a document that placed limits on the power of the English monarchy."
        ],
        "quiz_questions": [
            {
                "question": "In what year did Christopher Columbus reach the Americas?",
                "options": ["1492", "1776", "1620", "1215"],
                "answer": 0
            },
            {
                "question": "What was the name of the first successful powered flight, made by the Wright brothers?",
                "options": ["The Flyer", "The Biplane", "The Glider", "The Monoplane"],
                "answer": 0
            },
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Mesopotamia", "Egypt", "Greece", "China"],
                "answer": 2
            }
        ]
    },
    "general": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal in the world is the giraffe.",
            "The Mona Lisa has no eyebrows, as it was the fashion in Renaissance Florence to shave them off."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Earth", "Mars", "Jupiter", "Saturn"],
                "answer": 2
            },
            {
                "question": "What is the capital city of Australia?",
                "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
                "answer": 3
            },
            {
                "question": "What is the name of the longest river in the world?",
                "options": ["Amazon", "Nile", "Mississippi", "Yangtze"],
                "answer": 1
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
    print(f"\nHere's a random fact about {topic.capitalize()}:")
    print(random.choice(topics[topic]["facts"]))

def quiz(topic):
    print(f"\nTime for a {topic.capitalize()} quiz!")
    score = 0
    for question in topics[topic]["quiz_questions"]:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer - 1 == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"\nYour final score is {score} out of {len(topics[topic]['quiz_questions'])}")

def main():
    topic = display_menu()
    display_fact(topic)
    quiz(topic)

if __name__ == "__main__":
    main()
