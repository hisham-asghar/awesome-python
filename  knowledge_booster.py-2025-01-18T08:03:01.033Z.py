
import random
import requests
import json

# Function to display the main menu
def display_menu():
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    print("1. Science")
    print("2. Technology")
    print("3. History")
    print("4. General Knowledge")
    print("5. Exit")

# Function to display a random fact or concept for the selected topic
def display_topic_info(topic):
    facts = {
        "Science": [
            "The human body has around 60,000 miles of blood vessels.",
            "The first digital computer, ENIAC, was completed in 1946 and weighed over 30 tons.",
            "The Milky Way galaxy contains an estimated 100 to 400 billion stars."
        ],
        "Technology": [
            "The first mobile phone call was made on April 3, 1973 by Martin Cooper of Motorola.",
            "The first commercial website, www.info.cern.ch, was launched on August 6, 1991.",
            "The first programmable computer, the ENIAC, was Turing-complete, meaning it could solve a large class of computational problems."
        ],
        "History": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Mona Lisa was painted by Leonardo da Vinci between 1503 and 1519.",
            "The Magna Carta was signed in 1215, establishing the principle that everyone is subject to the law, even the king."
        ],
        "General Knowledge": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal is the giraffe, which can reach heights of up to 6 meters (20 feet).",
            "The Eiffel Tower can be 15 cm taller during the summer, when thermal expansion causes the iron to expand."
        ]
    }

    print(f"\nHere's a random fact about {topic}:")
    print(random.choice(facts[topic]))

# Function to display the quiz for the selected topic
def display_quiz(topic):
    quizzes = {
        "Science": [
            {"question": "What is the chemical symbol for gold?", "options": ["Au", "Ag", "Cu", "Fe"], "answer": 0},
            {"question": "What is the process by which plants convert sunlight into energy?", "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"], "answer": 0},
            {"question": "What is the name of the force that keeps planets in orbit around the Sun?", "options": ["Gravity", "Friction", "Centrifugal force", "Electromagnetic force"], "answer": 0}
        ],
        "Technology": [
            {"question": "What is the name of the first successful electronic computer?", "options": ["ENIAC", "UNIVAC", "IBM 704", "MARK I"], "answer": 0},
            {"question": "What is the name of the programming language created by Guido van Rossum?", "options": ["Java", "C++", "Python", "Ruby"], "answer": 2},
            {"question": "What is the name of the company that created the first commercially successful smartphone?", "options": ["Apple", "Samsung", "Nokia", "BlackBerry"], "answer": 3}
        ],
        "History": [
            {"question": "In what year was the Declaration of Independence signed?", "options": ["1776", "1787", "1812", "1865"], "answer": 0},
            {"question": "Who was the first president of the United States?", "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"], "answer": 2},
            {"question": "What was the name of the first successful powered flight by the Wright brothers?", "options": ["The Spirit of St. Louis", "The Kitty Hawk", "The Wright Flyer", "The Orville"], "answer": 2}
        ],
        "General Knowledge": [
            {"question": "What is the largest planet in our solar system?", "options": ["Jupiter", "Saturn", "Uranus", "Neptune"], "answer": 0},
            {"question": "What is the name of the longest river in the world?", "options": ["Nile", "Amazon", "Yangtze", "Mississippi"], "answer": 0},
            {"question": "What is the name of the largest mammal on Earth?", "options": ["Elephant", "Hippopotamus", "Rhinoceros", "Blue Whale"], "answer": 3}
        ]
    }

    print(f"\nTime for a {topic} quiz! Try your best!")
    score = 0
    for quiz in quizzes[topic]:
        print(quiz["question"])
        for i, option in enumerate(quiz["options"]):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer - 1 == quiz["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score: {score}/{len(quizzes[topic])}")

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        display_topic_info("Science")
    elif choice == "2":
        display_topic_info("Technology")
    elif choice == "3":
        display_topic_info("History")
    elif choice == "4":
        display_topic_info("General Knowledge")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

    input("\nPress Enter to continue...")
