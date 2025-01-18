
import random
import json
import requests

# Dictionary to store topics and their associated facts and quizzes
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion meaning the iron heats up, the particles get slightly farther apart, and the tower grows."
        ],
        "quizzes": [
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Jupiter", "Saturn", "Neptune", "Mars"],
                "answer": 0
            },
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, weighed 30 tons and took up 1800 square feet.",
            "The first domain name ever registered was Symbolics.com on March 15, 1985."
        ],
        "quizzes": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "What is the name of the first commercially successful smartphone?",
                "options": ["iPhone", "BlackBerry", "Nokia 3310", "Motorola Razr"],
                "answer": 1
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off."
        ],
        "quizzes": [
            {
                "question": "In what year did the United States declare independence?",
                "options": ["1776", "1789", "1812", "1865"],
                "answer": 0
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "Benjamin Franklin"],
                "answer": 2
            }
        ]
    },
    "general": {
        "facts": [
            "The first product to have a barcode was Wrigley's gum.",
            "A group of porcupines is called a prickle."
        ],
        "quizzes": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "Which country is known as the Land of the Rising Sun?",
                "options": ["China", "Japan", "India", "South Korea"],
                "answer": 1
            }
        ]
    }
}

def get_random_fact(topic):
    return random.choice(topics[topic]["facts"])

def get_random_quiz(topic):
    quiz = random.choice(topics[topic]["quizzes"])
    return quiz

def run_quiz(quiz):
    print(quiz["question"])
    for i, option in enumerate(quiz["options"]):
        print(f"{i+1}. {option}")
    
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == quiz["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is", quiz["options"][quiz["answer"]])

def main():
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print("\nHere's a random fact about", selected_topic.capitalize() + ":")
        print(get_random_fact(selected_topic))
        
        print("\nNow, let's test your knowledge with a quiz!")
        quiz = get_random_quiz(selected_topic)
        run_quiz(quiz)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
