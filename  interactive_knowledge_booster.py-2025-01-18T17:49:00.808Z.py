
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Milky Way galaxy contains an estimated 200-400 billion stars.",
            "Honey is the only food that does not spoil."
        ],
        "quiz": [
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Jupiter", "Saturn", "Mars", "Neptune"],
                "answer": 0
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Combustion", "Fermentation"],
                "answer": 0
            },
            {
                "question": "What is the chemical symbol for the element gold?",
                "options": ["Au", "Ag", "Cu", "Hg"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The internet was originally called ARPANET, which was developed in 1969.",
            "The first digital camera was invented in 1975 by Steven Sasson."
        ],
        "quiz": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "What is the name of the first commercially successful smartphone?",
                "options": ["iPhone", "BlackBerry", "Nokia 3310", "Motorola RAZR"],
                "answer": 0
            },
            {
                "question": "What is the name of the company that created the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": 2
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza in Egypt were built around 2560-2540 BCE.",
            "The Roman Empire lasted for over 400 years, from 27 BCE to 476 CE."
        ],
        "quiz": [
            {
                "question": "What was the name of the first president of the United States?",
                "options": ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "John Adams"],
                "answer": 1
            },
            {
                "question": "What was the name of the ancient Greek philosopher who is considered the father of western philosophy?",
                "options": ["Socrates", "Plato", "Aristotle", "Pythagoras"],
                "answer": 0
            },
            {
                "question": "What was the name of the ancient Egyptian queen who ruled alongside her husband, Tutankhamun?",
                "options": ["Nefertiti", "Cleopatra", "Hatshepsut", "Neferkare"],
                "answer": 0
            }
        ]
    },
    "general": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first product to have a barcode was Wrigley's gum."
        ],
        "quiz": [
            {
                "question": "What is the largest ocean in the world?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "What is the name of the largest mammal on Earth?",
                "options": ["Elephant", "Hippopotamus", "Giraffe", "Blue Whale"],
                "answer": 3
            },
            {
                "question": "What is the name of the longest river in the world?",
                "options": ["Nile River", "Amazon River", "Yangtze River", "Mississippi River"],
                "answer": 0
            }
        ]
    }
}

def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")
    return input("Enter your choice: ").lower()

def display_fact(topic):
    fact = random.choice(topics[topic]["facts"])
    print(f"Here's a random fact about {topic.capitalize()}:")
    print(f"- {fact}")

def display_quiz(topic):
    print(f"Let's test your {topic.capitalize()} knowledge!")
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
    display_quiz(topic)

if __name__ == "__main__":
    main()
