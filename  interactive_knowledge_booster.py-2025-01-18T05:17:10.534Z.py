Here is the raw Python code extracted from the JSON:

import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The first confirmed meteorite impact in the United States occurred in 1807 in Weston, Connecticut.",
            "Honey is the only food that does not spoil. It can be stored for thousands of years."
        ],
        "quizzes": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Ag", "Au", "Cu", "Fe"],
                "answer": 1
            },
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Brain", "Heart", "Lungs", "Skin"],
                "answer": 3
            },
            {
                "question": "Which scientist is known for the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Marie Curie"],
                "answer": 1
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 and cost $15,000.",
            "The first commercial text message was sent on December 3, 1992.",
            "The first digital camera was invented in 1975 and could only store 30 black-and-white images."
        ],
        "quizzes": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "Which company developed the first commercially successful smartphone?",
                "options": ["Apple", "Samsung", "BlackBerry", "Nokia"],
                "answer": 3
            },
            {
                "question": "What is the name of the first web browser?",
                "options": ["Internet Explorer", "Google Chrome", "Mozilla Firefox", "Mosaic"],
                "answer": 3
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza in Egypt were built around 2560–2540 BC.",
            "The first Olympic Games were held in 776 BC in Olympia, Greece."
        ],
        "quizzes": [
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Mesopotamia", "Ancient Egypt", "Ancient Greece", "Ancient China"],
                "answer": 0
            },
            {
                "question": "What was the name of the first successful powered flight, which took place in 1903?",
                "options": ["The Wright Flyer", "The Concorde", "The Spitfire", "The Sopwith Camel"],
                "answer": 0
            },
            {
                "question": "Which famous explorer discovered America in 1492?",
                "options": ["Marco Polo", "Christopher Columbus", "Leif Erikson", "Vasco da Gama"],
                "answer": 1
            }
        ]
    },
    "general": {
        "facts": [
            "The tallest mammal is the giraffe, which can grow up to 18 feet tall.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first person convicted of speeding was going 8 mph."
        ],
        "quizzes": [
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Earth", "Mars", "Jupiter", "Saturn"],
                "answer": 2
            },
            {
                "question": "Which country is known as the 'Land of the Rising Sun'?",
                "options": ["China", "Japan", "South Korea", "India"],
                "answer": 1
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": 2
            }
        ]
    }
}

def interactive_knowledge_booster():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")

    chosen_topic = input("Enter your choice: ").lower()

    if chosen_topic in topics:
        print(f"You've chosen the {chosen_topic.capitalize()} topic.")
        print("Here's a random fact:")
        print(random.choice(topics[chosen_topic]["facts"]))

        print("\nNow, let's test your knowledge with a quiz!")
        quiz_question = random.choice(topics[chosen_topic]["quizzes"])
        print(quiz_question["question"])
        for i, option in enumerate(quiz_question["options"]):
            print(f"{i+1}. {option}")

        user_answer = int(input("Enter the number of your answer: "))
        if user_answer - 1 == quiz_question["answer"]:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", quiz_question["options"][quiz_question["answer"]])
    else:
        print("Invalid topic. Please try again.")

interactive_knowledge_booster()