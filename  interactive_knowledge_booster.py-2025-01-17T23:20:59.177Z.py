
import random
import requests
import json

# Dictionary to store topics and their corresponding facts and quizzes
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest planet in the solar system is Venus, not Mercury.",
            "Cats have fewer toes on their back paws than their front paws."
        ],
        "quizzes": [
            {
                "question": "What is the main component of the sun?",
                "options": ["Hydrogen", "Helium", "Oxygen", "Carbon"],
                "answer": 0
            },
            {
                "question": "Which scientist is known for the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"],
                "answer": 1
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Evaporation"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 and had only one button.",
            "The first commercial text message was sent on December 3, 1992.",
            "The world's first programmable computer was the ENIAC, completed in 1946."
        ],
        "quizzes": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "Which company developed the first commercially successful smartphone?",
                "options": ["Apple", "Samsung", "Nokia", "BlackBerry"],
                "answer": 3
            },
            {
                "question": "What is the name of the first web browser?",
                "options": ["Internet Explorer", "Mozilla Firefox", "Google Chrome", "Mosaic"],
                "answer": 3
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first pizza was invented in Naples, Italy, in the late 18th or early 19th century."
        ],
        "quizzes": [
            {
                "question": "In what year did the United States declare its independence?",
                "options": ["1776", "1789", "1812", "1865"],
                "answer": 0
            },
            {
                "question": "Which ancient civilization is known for building the pyramids?",
                "options": ["Aztecs", "Incas", "Mayans", "Egyptians"],
                "answer": 3
            },
            {
                "question": "What was the name of the first successful powered flight by the Wright brothers?",
                "options": ["Kitty Hawk", "Flyer I", "Spirit of St. Louis", "Wright Flyer"],
                "answer": 1
            }
        ]
    },
    "general": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal is the giraffe.",
            "The largest moon of Saturn is Titan."
        ],
        "quizzes": [
            {
                "question": "What is the tallest building in the world?",
                "options": ["Burj Khalifa", "Shanghai Tower", "Abraj Al-Bait Clock Tower", "One World Trade Center"],
                "answer": 0
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": 2
            }
        ]
    }
}

def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")
    return input("Enter your choice: ").lower()

def display_fact(topic):
    fact = random.choice(topics[topic]["facts"])
    print(f"\nFact about {topic.capitalize()}:\n{fact}")

def display_quiz(topic):
    quiz = random.choice(topics[topic]["quizzes"])
    print(f"\nQuiz about {topic.capitalize()}:")
    print(quiz["question"])
    for i, option in enumerate(quiz["options"]):
        print(f"{i+1}. {option}")
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == quiz["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz["options"][quiz["answer"]])

def main():
    topic = display_menu()
    display_fact(topic)
    display_quiz(topic)

if __name__ == "__main__":
    main()
