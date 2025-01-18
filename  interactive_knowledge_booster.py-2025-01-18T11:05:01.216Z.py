
import random
import requests
import json

# Define topics and their associated facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has over 60,000 miles of blood vessels.",
            "The hottest planet in the solar system is Venus, not Mercury.",
            "The largest known prime number has over 23 million digits."
        ],
        "quiz": [
            {
                "question": "What is the name of the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Evaporation"],
                "answer": 0
            },
            {
                "question": "Which of these is a fundamental force of nature?",
                "options": ["Gravity", "Friction", "Centrifugal force", "Buoyancy"],
                "answer": 0
            },
            {
                "question": "What is the name of the closest star to our solar system?",
                "options": ["Sirius", "Polaris", "Proxima Centauri", "Betelgeuse"],
                "answer": 2
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 and had only one button.",
            "The first digital computer, ENIAC, was completed in 1946 and weighed over 30 tons.",
            "The world's first webcam was used to monitor a coffee pot at the University of Cambridge."
        ],
        "quiz": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "What is the name of the protocol that allows devices to connect to the internet?",
                "options": ["HTTP", "SMTP", "TCP/IP", "FTP"],
                "answer": 2
            },
            {
                "question": "What is the name of the first commercially successful smartphone?",
                "options": ["iPhone", "BlackBerry", "Motorola RAZR", "Nokia 3310"],
                "answer": 0
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first Olympic Games were held in 776 BC in Olympia, Greece."
        ],
        "quiz": [
            {
                "question": "What year did the American Civil War begin?",
                "options": ["1861", "1865", "1776", "1914"],
                "answer": 0
            },
            {
                "question": "What was the name of the first successful powered flight, made by the Wright brothers?",
                "options": ["The Spirit of St. Louis", "The Flyer", "The Kitty Hawk", "The Wright Flyer"],
                "answer": 3
            },
            {
                "question": "What was the name of the first computer programmer?",
                "options": ["Ada Lovelace", "Alan Turing", "Charles Babbage", "Grace Hopper"],
                "answer": 0
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number has over 23 million digits.",
            "The first product to have a barcode was Wrigley's gum.",
            "The name 'Typewriter' is the longest word that can be typed using only the top row of a QWERTY keyboard."
        ],
        "quiz": [
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Mars", "Jupiter", "Saturn", "Neptune"],
                "answer": 1
            },
            {
                "question": "What is the tallest mammal in the world?",
                "options": ["Elephant", "Giraffe", "Hippopotamus", "Rhinoceros"],
                "answer": 1
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            }
        ]
    }
}

def get_random_fact(topic):
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    quiz_question = random.choice(topics[topic]["quiz"])
    return quiz_question["question"], quiz_question["options"], quiz_question["answer"]

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))

        print("\nNow, let's test your knowledge with a quiz!")
        question, options, answer = get_quiz_question(selected_topic)
        print(question)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer - 1 == answer:
            print("Correct! You're a knowledge master.")
        else:
            print("Oops, that's not the right answer. Better luck next time!")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
