
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Earth is the only planet in our solar system with liquid water on its surface.",
            "The fastest animal on Earth is the peregrine falcon, which can reach speeds of up to 240 mph during a dive."
        ],
        "quiz": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Mars", "Jupiter", "Saturn", "Uranus"],
                "answer": "Jupiter"
            },
            {
                "question": "What is the process by which plants convert light energy into chemical energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Evaporation"],
                "answer": "Photosynthesis"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented by Douglas Engelbart in 1964.",
            "The first web page was created by Tim Berners-Lee in 1990.",
            "The first digital camera was invented by Steven Sasson in 1975."
        ],
        "quiz": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "What is the name of the company that created the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": "Google"
            },
            {
                "question": "What is the name of the device that converts digital signals into analog signals?",
                "options": ["Modem", "Router", "Printer", "Scanner"],
                "answer": "Modem"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza in Egypt were built around 2560-2540 BC.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD."
        ],
        "quiz": [
            {
                "question": "What year was the United States Declaration of Independence signed?",
                "options": ["1776", "1789", "1812", "1865"],
                "answer": "1776"
            },
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Greeks", "Romans", "Egyptians", "Mayans"],
                "answer": "Mayans"
            },
            {
                "question": "What was the name of the first successful powered flight, made by the Wright brothers?",
                "options": ["Kitty Hawk", "Spirit of St. Louis", "Apollo 11", "Concorde"],
                "answer": "Kitty Hawk"
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number has over 23 million digits.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "A group of porcupines is called a prickle."
        ],
        "quiz": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "What is the tallest mammal in the world?",
                "options": ["Elephant", "Giraffe", "Hippopotamus", "Rhinoceros"],
                "answer": "Giraffe"
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": "AB"
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
    quiz_question = random.choice(topics[topic]["quiz"])
    return quiz_question

def run_quiz(topic):
    """
    Runs a quiz for the specified topic.
    """
    quiz_question = get_quiz_question(topic)
    print(quiz_question["question"])
    for i, option in enumerate(quiz_question["options"]):
        print(f"{i+1}. {option}")
    user_answer = input("Enter your answer (1-4): ")
    if quiz_question["options"][int(user_answer) - 1] == quiz_question["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_question["answer"])

def main():
    """
    The main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    chosen_topic = input("Enter your choice: ").lower()
    if chosen_topic in topics:
        print("\nHere's a random fact about", chosen_topic.capitalize() + ":")
        print(get_random_fact(chosen_topic))
        print("\nNow let's test your knowledge with a quiz!")
        run_quiz(chosen_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
