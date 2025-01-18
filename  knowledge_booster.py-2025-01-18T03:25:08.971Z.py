Here is the raw Python code without any additional commentary:

import random
import requests
import json

def get_random_fact(topic):
    facts = {
        "science": [
            "The human body contains enough DNA to stretch from the Sun to Pluto and back again.",
            "Cats have fewer toes on their back paws than their front paws.",
            "Bees can fly higher than the tallest building."
        ],
        "technology": [
            "The first electronic computer, ENIAC, weighed 30 tons and took up 1800 square feet.",
            "The first computer mouse was invented in 1964 and used a wooden shell, a metal ball, and two gear wheels.",
            "The largest hard drive ever produced had a capacity of 60 terabytes."
        ],
        "history": [
            "The Great Wall of China is the only man-made object visible from space.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first person convicted of speeding was going 8 mph."
        ],
        "general": [
            "A group of porcupines is called a prickle.",
            "The average person walks the equivalent of 5 times around the world in their lifetime.",
            "Apples are more effective at waking you up in the morning than coffee."
        ]
    }
    return random.choice(facts[topic])

def quiz(topic):
    quizzes = {
        "science": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            },
            {
                "question": "Which planet in our solar system has the most moons?",
                "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
                "answer": 0
            }
        ],
        "technology": [
            {
                "question": "What was the first commercially successful smartphone?",
                "options": ["iPhone", "BlackBerry", "Nokia N95", "Palm Treo"],
                "answer": 0
            },
            {
                "question": "What is the primary function of a computer's motherboard?",
                "options": ["Storing data", "Connecting components", "Providing power", "Processing information"],
                "answer": 1
            }
        ],
        "history": [
            {
                "question": "Which ancient civilization is known for building the Pyramids?",
                "options": ["Aztecs", "Mayans", "Egyptians", "Romans"],
                "answer": 2
            },
            {
                "question": "What was the name of the first successful powered flight by the Wright brothers?",
                "options": ["The Flyer", "The Glider", "The Biplane", "The Monoplane"],
                "answer": 0
            }
        ],
        "general": [
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Brain", "Heart", "Liver", "Skin"],
                "answer": 3
            },
            {
                "question": "Which is the fastest land animal?",
                "options": ["Cheetah", "Gazelle", "Lion", "Zebra"],
                "answer": 0
            }
        ]
    }
    quiz_data = random.choice(quizzes[topic])
    print(quiz_data["question"])
    for i, option in enumerate(quiz_data["options"]):
        print(f"{i+1}. {option}")
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == quiz_data["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is", quiz_data["options"][quiz_data["answer"]])

def main():
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    topics = ["Science", "Technology", "History", "General"]
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")
    user_choice = int(input("Enter your choice (1-4): "))
    topic = topics[user_choice - 1].lower()
    
    print(f"\nHere's a random {topic} fact:")
    print(get_random_fact(topic))
    
    print(f"\nNow, let's test your {topic} knowledge with a quiz!")
    quiz(topic)

if __name__ == "__main__":
    main()