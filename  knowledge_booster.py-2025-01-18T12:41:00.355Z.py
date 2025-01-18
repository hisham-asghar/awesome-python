
import random
import json
import requests

# Define topics and their corresponding facts and quiz questions
topics = {
    "Science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The first successful kidney transplant was performed in 1954.",
            "The largest known prime number as of 2022 has 23 million digits."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the process by which plants convert light energy into chemical energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": 0
            },
            {
                "question": "Which scientist is known for developing the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"],
                "answer": 1
            },
            {
                "question": "What is the name of the closest planet to the Sun?",
                "options": ["Mars", "Venus", "Mercury", "Earth"],
                "answer": 2
            }
        ]
    },
    "Technology": {
        "facts": [
            "The first electronic computer, ENIAC, was completed in 1946 and weighed 30 tons.",
            "The first commercial smartphone, the IBM Simon, was introduced in 1992.",
            "The world's first website was launched on August 6, 1991."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "JavaScript"],
                "answer": 2
            },
            {
                "question": "Which company is known for creating the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": 2
            },
            {
                "question": "What is the name of the first commercially successful web browser?",
                "options": ["Mozilla Firefox", "Google Chrome", "Microsoft Internet Explorer", "Netscape Navigator"],
                "answer": 3
            }
        ]
    },
    "History": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Silk Road was a network of trade routes that connected the East and West from the 2nd century BCE to the 18th century CE.",
            "The Renaissance was a cultural movement that spanned from the 14th to the 17th century, originating in Italy."
        ],
        "quiz_questions": [
            {
                "question": "In what year did the United States declare its independence?",
                "options": ["1776", "1787", "1812", "1865"],
                "answer": 0
            },
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Egyptians", "Greeks", "Romans", "Mayans"],
                "answer": 1
            },
            {
                "question": "What was the name of the first successful powered flight, conducted by the Wright brothers?",
                "options": ["The Wright Flyer", "The Kitty Hawk", "The Spirit of St. Louis", "The Concorde"],
                "answer": 0
            }
        ]
    },
    "General Knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal in the world is the giraffe.",
            "The Mona Lisa has no eyebrows, as it was the fashion in Renaissance Florence to shave them off."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "Which country is known as the 'Land of the Rising Sun'?",
                "options": ["China", "Japan", "South Korea", "North Korea"],
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

def get_random_fact(topic):
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    question = random.choice(topics[topic]["quiz_questions"])
    return question

def run_quiz(topic):
    question = get_quiz_question(topic)
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    
    while True:
        user_answer = input("Enter your answer (1-4): ")
        if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
            if int(user_answer) - 1 == question["answer"]:
                print("Correct!")
                return
            else:
                print("Incorrect. Try again.")
        else:
            print("Invalid input. Please enter a number from 1 to 4.")

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    
    while True:
        user_topic = input("Enter your topic choice: ")
        if user_topic in topics:
            print(f"Random fact about {user_topic}: {get_random_fact(user_topic)}")
            run_quiz(user_topic)
            break
        else:
            print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
