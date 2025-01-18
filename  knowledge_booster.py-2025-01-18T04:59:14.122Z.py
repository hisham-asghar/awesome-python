Here is the raw Python code without any additional commentary:

import random
import requests
import json

# Define the topics and their respective facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has 206 bones.",
            "The Milky Way galaxy contains an estimated 200-400 billion stars.",
            "Water is the only substance on Earth that is naturally found in three distinct forms: solid, liquid, and gas."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "Which scientist is known for the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"],
                "answer": "Albert Einstein"
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": "Photosynthesis"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer virus was created in 1983 and was called the 'Brain' virus.",
            "The first mobile phone call was made on April 3, 1973, by Martin Cooper of Motorola.",
            "The internet was initially created as a project of the United States Department of Defense called ARPANET."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the operating system developed by Apple Inc.?",
                "options": ["Windows", "macOS", "Linux", "Android"],
                "answer": "macOS"
            },
            {
                "question": "Which company is known for creating the popular search engine Google?",
                "options": ["Apple", "Microsoft", "Amazon", "Alphabet"],
                "answer": "Alphabet"
            },
            {
                "question": "What is the name of the programming language that is often used for data analysis and machine learning?",
                "options": ["Java", "Python", "C++", "Ruby"],
                "answer": "Python"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Egyptians", "Greeks", "Mayans", "Chinese"],
                "answer": "Mayans"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
                "answer": "George Washington"
            },
            {
                "question": "What year did World War II end?",
                "options": ["1945", "1939", "1941", "1947"],
                "answer": "1945"
            }
        ]
    },
    "general": {
        "facts": [
            "The tallest mammal is the giraffe, which can grow up to 6 meters (19.7 feet) tall.",
            "The largest organ in the human body is the skin.",
            "The largest continent in the world is Asia, covering approximately 17,212,000 square miles."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest ocean in the world?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "What is the currency used in Japan?",
                "options": ["Euro", "Dollar", "Yen", "Renminbi"],
                "answer": "Yen"
            },
            {
                "question": "What is the largest animal on Earth?",
                "options": ["Elephant", "Whale", "Giraffe", "Hippopotamus"],
                "answer": "Whale"
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
    print(f"\nFact about {topic.capitalize()}:")
    print(fact)

def run_quiz(topic):
    print(f"\nTime for a {topic.capitalize()} quiz!")
    score = 0
    for question in topics[topic]["quiz_questions"]:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = input("Enter your answer (1-4): ")
        if user_answer.lower() == question["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"\nYour final score: {score}/{len(topics[topic]['quiz_questions'])}")

def main():
    topic = display_menu()
    display_fact(topic)
    run_quiz(topic)

if __name__ == "__main__":
    main()