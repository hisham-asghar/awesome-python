
import random
import requests
import json

# Define the topics and their corresponding facts and quizzes
topics = {
    "science": {
        "facts": [
            "The human brain has around 86 billion neurons.",
            "The first successful kidney transplant was performed in 1954.",
            "The largest known prime number as of 2021 has 23,249,425 digits."
        ],
        "quizzes": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            },
            {
                "question": "Which scientist is credited with developing the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Galileo Galilei"],
                "answer": 1
            },
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Saturn", "Jupiter", "Mars", "Venus"],
                "answer": 1
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, was completed in 1946.",
            "The internet was created in 1969 as a project of the U.S. Department of Defense.",
            "The first smartphone was the IBM Simon, released in 1992."
        ],
        "quizzes": [
            {
                "question": "What does 'HTML' stand for?",
                "options": ["Hypertext Markup Language", "Hypertext Machine Language", "Hyper Transmission Markup Language", "High-level Text Markup Language"],
                "answer": 0
            },
            {
                "question": "Which company developed the Android operating system?",
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
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Magna Carta was signed in 1215, establishing the principle that everyone is subject to the law, even the king.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers."
        ],
        "quizzes": [
            {
                "question": "In what year did the United States declare its independence?",
                "options": ["1776", "1789", "1812", "1865"],
                "answer": 0
            },
            {
                "question": "Which ancient civilization built the Colosseum in Rome?",
                "options": ["Greek", "Roman", "Egyptian", "Mesopotamian"],
                "answer": 1
            },
            {
                "question": "What was the name of the first successful voyage around the world?",
                "options": ["The Voyages of Christopher Columbus", "The Expedition of Magellan", "The Circumnavigation of Sir Francis Drake", "The Voyage of the HMS Beagle"],
                "answer": 1
            }
        ]
    },
    "general": {
        "facts": [
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first product to have a barcode was Wrigley's gum.",
            "A group of porcupines is called a prickle."
        ],
        "quizzes": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Pacific Ocean", "Indian Ocean", "Arctic Ocean"],
                "answer": 1
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": 2
            },
            {
                "question": "Which country is known as the 'Land of the Rising Sun'?",
                "options": ["China", "Japan", "India", "South Korea"],
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
    return input("Enter your choice: ").lower()

def display_fact(topic):
    fact = random.choice(topics[topic]["facts"])
    print(f"Here's an interesting fact about {topic.capitalize()}:")
    print(f"- {fact}")

def display_quiz(topic):
    quiz = random.choice(topics[topic]["quizzes"])
    print(f"Let's test your {topic.capitalize()} knowledge!")
    print(quiz["question"])
    for i, option in enumerate(quiz["options"]):
        print(f"{i+1}. {option}")
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == quiz["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz["options"][quiz["answer"]])

def main():
    topic = display_menu()
    display_fact(topic)
    display_quiz(topic)

if __name__ == "__main__":
    main()
