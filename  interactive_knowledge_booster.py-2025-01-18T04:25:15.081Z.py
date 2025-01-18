Here is the raw Python code extracted from the JSON:

import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The largest known prime number as of 2023 has over 23 million digits.",
            "The first successful kidney transplant was performed in 1954."
        ],
        "quiz": [
            {
                "question": "What is the name of the process by which plants convert light energy into chemical energy?",
                "options": ["Photosynthesis", "Respiration", "Combustion", "Evaporation"],
                "answer": 0
            },
            {
                "question": "Which scientist is known for developing the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"],
                "answer": 1
            },
            {
                "question": "What is the chemical symbol for the element gold?",
                "options": ["Au", "Ag", "Hg", "Fe"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, was completed in 1946 and weighed over 30 tons.",
            "The first commercial microprocessor, the Intel 4004, was released in 1971.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989."
        ],
        "quiz": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "Which company is known for creating the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": 2
            },
            {
                "question": "What is the name of the process by which data is transmitted between computers?",
                "options": ["Printing", "Encryption", "Networking", "Rendering"],
                "answer": 2
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Magna Carta, a charter of rights, was signed in 1215 and is considered one of the most important documents in history.",
            "The first successful powered flight by the Wright brothers took place in 1903."
        ],
        "quiz": [
            {
                "question": "In what year was the United States Declaration of Independence signed?",
                "options": ["1776", "1789", "1812", "1865"],
                "answer": 0
            },
            {
                "question": "Which ancient civilization is known for its advanced engineering and architectural achievements?",
                "options": ["Mesopotamia", "Ancient Greece", "Ancient Egypt", "Ancient Rome"],
                "answer": 2
            },
            {
                "question": "What was the name of the first successful voyage around the world?",
                "options": ["The Magellan Expedition", "The Columbus Voyage", "The Lewis and Clark Expedition", "The Explorers Club Expedition"],
                "answer": 0
            }
        ]
    },
    "general": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest building in the world is the Burj Khalifa in Dubai, United Arab Emirates.",
            "The largest moon of Saturn is Titan, which is larger than the planet Mercury."
        ],
        "quiz": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "What is the capital city of Australia?",
                "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
                "answer": 3
            },
            {
                "question": "Which planet in our solar system is known as the 'Red Planet'?",
                "options": ["Venus", "Mars", "Jupiter", "Saturn"],
                "answer": 1
            }
        ]
    }
}

def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    print()

def get_random_fact(topic):
    facts = topics[topic]["facts"]
    return random.choice(facts)

def run_quiz(topic):
    quiz_questions = topics[topic]["quiz"]
    score = 0
    for question in quiz_questions:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): ")) - 1
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score is: {score}/{len(quiz_questions)}")

def main():
    display_menu()
    selected_topic = input("Enter your topic choice: ").lower()
    if selected_topic in topics:
        print("\nHere's a random fact about", selected_topic.capitalize() + ":")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()