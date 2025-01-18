
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Milky Way galaxy contains an estimated 100 to 400 billion stars.",
            "The largest known prime number as of 2021 has 23 million digits."
        ],
        "quiz": [
            {
                "question": "What is the main function of the human heart?",
                "options": ["To pump blood through the body", "To filter waste from the blood", "To produce insulin", "To control breathing"],
                "answer": 0
            },
            {
                "question": "What is the name of the closest star to Earth?",
                "options": ["Sirius", "Proxima Centauri", "Betelgeuse", "Polaris"],
                "answer": 1
            },
            {
                "question": "What is the name of the process by which plants convert sunlight into energy?",
                "options": ["Respiration", "Photosynthesis", "Combustion", "Evaporation"],
                "answer": 1
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 and had only one button.",
            "The largest hard drive ever made had a capacity of 60 terabytes.",
            "The first commercial text message was sent on December 3, 1992."
        ],
        "quiz": [
            {
                "question": "What is the name of the first commercially successful smartphone?",
                "options": ["iPhone", "BlackBerry", "Nokia 3310", "Motorola RAZR"],
                "answer": 1
            },
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "What is the name of the technology that allows devices to connect to the internet without a physical connection?",
                "options": ["Bluetooth", "Wi-Fi", "Ethernet", "Cellular"],
                "answer": 1
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers."
        ],
        "quiz": [
            {
                "question": "What year was the Declaration of Independence signed?",
                "options": ["1776", "1789", "1812", "1865"],
                "answer": 0
            },
            {
                "question": "What was the name of the first successful space mission to land a human on the Moon?",
                "options": ["Apollo 11", "Sputnik 1", "Gemini 3", "Mercury-Redstone 3"],
                "answer": 0
            },
            {
                "question": "Which ancient civilization is known for building the pyramids?",
                "options": ["Aztecs", "Incas", "Mayans", "Egyptians"],
                "answer": 3
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2021 has 23 million digits.",
            "The first commercial jet flight took place in 1952, with the de Havilland Comet.",
            "The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall."
        ],
        "quiz": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": 2
            },
            {
                "question": "What is the name of the largest moon of Saturn?",
                "options": ["Titan", "Ganymede", "Callisto", "Io"],
                "answer": 0
            }
        ]
    }
}

def display_menu():
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    return input("Enter your choice: ").lower()

def display_fact(topic):
    fact = random.choice(topics[topic]["facts"])
    print(f"Did you know? {fact}")

def run_quiz(topic):
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
    print(f"Your final score is {score}/{len(topics[topic]['quiz'])}")

def main():
    topic = display_menu()
    display_fact(topic)
    run_quiz(topic)

if __name__ == "__main__":
    main()
