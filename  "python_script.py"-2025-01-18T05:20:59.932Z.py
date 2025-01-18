
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The largest known prime number as of 2022 has 23 million digits.",
            "The first successful kidney transplant was performed in 1954."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "Which scientist is famous for the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Marie Curie"],
                "answer": "Albert Einstein"
            },
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Liver", "Skin", "Brain"],
                "answer": "Skin"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first programmable computer was the ENIAC, which was completed in 1946.",
            "The first commercial smartphone was the IBM Simon, released in 1992.",
            "The first digital camera was developed by Kodak in 1975."
        ],
        "quiz_questions": [
            {
                "question": "Which company developed the first personal computer?",
                "options": ["Apple", "Microsoft", "IBM", "Commodore"],
                "answer": "IBM"
            },
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "What is the name of the first web browser?",
                "options": ["Google Chrome", "Mozilla Firefox", "Internet Explorer", "Mosaic"],
                "answer": "Mosaic"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza in Egypt were built around 2500 BC.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD."
        ],
        "quiz_questions": [
            {
                "question": "Who was the first president of the United States?",
                "options": ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "John Adams"],
                "answer": "George Washington"
            },
            {
                "question": "In what year did the American Civil War begin?",
                "options": ["1861", "1776", "1945", "1939"],
                "answer": "1861"
            },
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Greeks", "Egyptians", "Mayans", "Babylonians"],
                "answer": "Babylonians"
            }
        ]
    },
    "general": {
        "facts": [
            "The tallest mammal is the giraffe, which can grow up to 18 feet tall.",
            "The largest known prime number as of 2022 has 23 million digits.",
            "The Mona Lisa has no eyebrows, as it was the fashion in Renaissance Florence to shave them off."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "Who wrote the famous novel 'To Kill a Mockingbird'?",
                "options": ["Harper Lee", "Ernest Hemingway", "J.K. Rowling", "Maya Angelou"],
                "answer": "Harper Lee"
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": "AB"
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
    print(f"\nHere's an interesting fact about {topic.capitalize()}:")
    print(f"- {fact}")

def run_quiz(topic):
    print(f"\nTime for a {topic.capitalize()} quiz!")
    score = 0
    for question in topics[topic]["quiz_questions"]:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = input("Enter your answer (1-4): ")
        if question["options"][int(user_answer) - 1] == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"\nYour final score is {score} out of {len(topics[topic]['quiz_questions'])}")

def main():
    topic = display_menu()
    display_fact(topic)
    run_quiz(topic)

if __name__ == "__main__":
    main()
