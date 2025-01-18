Here is the raw Python code extracted from the JSON:

import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has over 600 muscles.",
            "The Milky Way galaxy contains an estimated 100 to 400 billion stars.",
            "Water is the only substance that exists naturally on Earth in three forms: solid, liquid, and gas."
        ],
        "quiz_questions": [
            {
                "question": "What is the main component of the Earth's atmosphere?",
                "choices": ["Nitrogen", "Oxygen", "Carbon dioxide", "Argon"],
                "answer": 1
            },
            {
                "question": "What is the name of the largest planet in our solar system?",
                "choices": ["Jupiter", "Saturn", "Mars", "Venus"],
                "answer": 0
            },
            {
                "question": "What is the name of the process by which plants convert light energy into chemical energy?",
                "choices": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The internet was originally known as ARPANET, which was created in 1969 by the U.S. Department of Defense.",
            "The first digital camera was invented in 1975 by Steven Sasson, an engineer at Eastman Kodak."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "choices": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "What is the name of the first web browser, created by Tim Berners-Lee in 1990?",
                "choices": ["Mosaic", "Netscape", "Internet Explorer", "WorldWideWeb"],
                "answer": 3
            },
            {
                "question": "What is the name of the company that created the Android operating system?",
                "choices": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": 2
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Roman Empire lasted for over 400 years, from the 27 BC to 476 AD.",
            "The Renaissance was a cultural movement that spanned the 14th to the 17th century, starting in Italy and spreading to the rest of Europe."
        ],
        "quiz_questions": [
            {
                "question": "What year was the Declaration of Independence signed?",
                "choices": ["1776", "1789", "1812", "1865"],
                "answer": 0
            },
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "choices": ["Egyptians", "Greeks", "Mayans", "Chinese"],
                "answer": 1
            },
            {
                "question": "What was the name of the first successful powered flight, conducted by the Wright brothers in 1903?",
                "choices": ["The Flyer", "The Kitty Hawk", "The Biplane", "The Glider"],
                "answer": 0
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.",
            "The largest ocean on Earth is the Pacific Ocean, covering an area of about 63 million square miles."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest planet in our solar system?",
                "choices": ["Jupiter", "Saturn", "Neptune", "Uranus"],
                "answer": 0
            },
            {
                "question": "What is the largest bone in the human body?",
                "choices": ["Femur", "Tibia", "Humerus", "Skull"],
                "answer": 0
            },
            {
                "question": "What is the largest continent on Earth?",
                "choices": ["Asia", "Africa", "North America", "South America"],
                "answer": 0
            }
        ]
    }
}

def interactive_knowledge_booster():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in topics:
        print(f"\nYou've selected the {selected_topic.capitalize()} topic.")
        print("Here's a random fact:")
        print(random.choice(topics[selected_topic]["facts"]))

        print("\nTime for a quiz! Answer the following multiple-choice questions:")
        score = 0
        for question in topics[selected_topic]["quiz_questions"]:
            print(question["question"])
            for i, choice in enumerate(question["choices"]):
                print(f"{i+1}. {choice}")
            user_answer = int(input("Enter your answer (1-4): ")) - 1
            if user_answer == question["answer"]:
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")
        print(f"\nYour final score is {score} out of {len(topics[selected_topic]['quiz_questions'])}.")
    else:
        print("Invalid topic. Please try again.")

interactive_knowledge_booster()