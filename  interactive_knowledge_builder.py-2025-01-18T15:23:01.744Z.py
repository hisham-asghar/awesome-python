
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has over 600 muscles.",
            "The largest known prime number has over 23 million digits.",
            "The first successful kidney transplant was performed in 1954."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "What is the name of the force that keeps planets in orbit around the sun?",
                "options": ["Gravity", "Friction", "Centrifugal force", "Electromagnetic force"],
                "answer": "Gravity"
            },
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Mars", "Jupiter", "Saturn", "Neptune"],
                "answer": "Jupiter"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964.",
            "The largest known prime number has over 23 million digits.",
            "The first successful kidney transplant was performed in 1954."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "What is the name of the first commercially available personal computer?",
                "options": ["Apple I", "IBM PC", "Commodore 64", "Atari 800"],
                "answer": "Apple I"
            },
            {
                "question": "What is the name of the technology that allows devices to connect to the internet wirelessly?",
                "options": ["Ethernet", "Bluetooth", "Wi-Fi", "Cellular data"],
                "answer": "Wi-Fi"
            }
        ]
    },
    "history": {
        "facts": [
            "The first successful kidney transplant was performed in 1954.",
            "The Great Wall of China is over 13,000 miles long.",
            "The Mona Lisa was painted by Leonardo da Vinci."
        ],
        "quiz_questions": [
            {
                "question": "What year did the United States declare its independence?",
                "options": ["1776", "1789", "1812", "1865"],
                "answer": "1776"
            },
            {
                "question": "What was the name of the first successful powered flight, conducted by the Wright brothers?",
                "options": ["The Flyer", "The Kitty Hawk", "The Wright Flyer", "The Biplane"],
                "answer": "The Wright Flyer"
            },
            {
                "question": "What was the name of the first president of the United States?",
                "options": ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "John Adams"],
                "answer": "George Washington"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest known prime number has over 23 million digits.",
            "The first successful kidney transplant was performed in 1954.",
            "The Mona Lisa was painted by Leonardo da Vinci."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "What is the name of the tallest mountain in the world?",
                "options": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
                "answer": "Mount Everest"
            },
            {
                "question": "What is the name of the currency used in the United States?",
                "options": ["Euro", "Pound sterling", "Yen", "US Dollar"],
                "answer": "US Dollar"
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the specified topic.
    """
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    """
    Retrieves a random quiz question from the specified topic.
    """
    quiz_question = random.choice(topics[topic]["quiz_questions"])
    return quiz_question

def run_quiz(topic):
    """
    Runs a quiz for the specified topic.
    """
    quiz_question = get_quiz_question(topic)
    print(quiz_question["question"])
    for i, option in enumerate(quiz_question["options"], start=1):
        print(f"{i}. {option}")
    
    while True:
        try:
            user_answer = int(input("Enter your answer (1-4): "))
            if user_answer < 1 or user_answer > 4:
                print("Invalid answer. Please try again.")
                continue
            if quiz_question["options"][user_answer - 1] == quiz_question["answer"]:
                print("Correct!")
                return
            else:
                print("Incorrect. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    """
    The main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge-Building Script!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    while True:
        selected_topic = input("Enter your topic choice: ").lower()
        if selected_topic in topics:
            print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
            print(get_random_fact(selected_topic))
            print("\nNow, let's test your knowledge with a quiz!")
            run_quiz(selected_topic)
            print("\nGreat job! Would you like to try another topic?")
            continue
        else:
            print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
