
import random
import requests
import json

# Define a dictionary of topics and their corresponding facts/quizzes
topics = {
    "science": {
        "facts": ["The human body has around 60,000 miles of blood vessels.", "The hottest planet in the solar system is Venus.", "Cats have fewer toes on their back paws than their front paws."],
        "quizzes": [
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Earth", "Jupiter", "Mars", "Saturn"],
                "answer": 2
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Evaporation", "Transpiration"],
                "answer": 1
            },
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": 1
            }
        ]
    },
    "technology": {
        "facts": ["The first computer mouse was invented in 1964.", "The first commercial text message was sent in 1992.", "The first digital camera was developed in 1975."],
        "quizzes": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 3
            },
            {
                "question": "What is the name of the company that created the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": 3
            },
            {
                "question": "What is the name of the device that allows you to access the internet wirelessly?",
                "options": ["Router", "Modem", "Laptop", "Smartphone"],
                "answer": 4
            }
        ]
    },
    "history": {
        "facts": ["The Great Wall of China is the longest man-made structure in the world.", "The first successful powered flight was made by the Wright brothers in 1903.", "The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci."],
        "quizzes": [
            {
                "question": "What year did the American Revolutionary War begin?",
                "options": ["1776", "1775", "1783", "1789"],
                "answer": 2
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "James Madison"],
                "answer": 2
            },
            {
                "question": "What was the name of the ancient civilization that built the pyramids in Egypt?",
                "options": ["Aztec", "Inca", "Maya", "Egyptian"],
                "answer": 4
            }
        ]
    },
    "general": {
        "facts": ["The Eiffel Tower can be 15 cm taller during the summer, as the hot weather causes the iron to expand.", "The first product to have a barcode was Wrigley's gum.", "A group of porcupines is called a prickle."],
        "quizzes": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 4
            },
            {
                "question": "What is the name of the largest mammal on Earth?",
                "options": ["Elephant", "Blue Whale", "Hippopotamus", "Giraffe"],
                "answer": 2
            },
            {
                "question": "What is the name of the tallest mountain in the world?",
                "options": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
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
    print(f"Here's a random fact about {topic.capitalize()}:\n{fact}")

def run_quiz(topic):
    print(f"Let's test your {topic.capitalize()} knowledge!")
    score = 0
    for quiz in topics[topic]["quizzes"]:
        print(quiz["question"])
        for i, option in enumerate(quiz["options"], start=1):
            print(f"{i}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer == quiz["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score is: {score}/{len(topics[topic]['quizzes'])}")

def main():
    topic = display_menu()
    display_fact(topic)
    run_quiz(topic)

if __name__ == "__main__":
    main()
