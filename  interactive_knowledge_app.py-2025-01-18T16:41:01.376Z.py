
import random
import requests
import json

# Define the topics and their associated facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest planet in the solar system is Venus, not Mercury.",
            "The largest known prime number as of 2021 has 23 million digits."
        ],
        "quiz_questions": [
            {
                "question": "Which of the following is not a state of matter?",
                "options": ["Solid", "Liquid", "Plasma", "Emotion"],
                "answer": "Emotion"
            },
            {
                "question": "What is the name of the force that keeps planets in orbit around the Sun?",
                "options": ["Gravity", "Electromagnetism", "Strong nuclear force", "Weak nuclear force"],
                "answer": "Gravity"
            },
            {
                "question": "What is the name of the largest moon of Saturn?",
                "options": ["Titan", "Ganymede", "Io", "Europa"],
                "answer": "Titan"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer virus, called 'Creeper', was created in 1971 as an experiment.",
            "The first commercial microprocessor, the Intel 4004, was introduced in 1971.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "What is the name of the first commercially successful smartphone?",
                "options": ["iPhone", "BlackBerry", "Nokia 3310", "Motorola RAZR"],
                "answer": "BlackBerry"
            },
            {
                "question": "What is the name of the technology that allows devices to connect to the internet without a physical cable?",
                "options": ["Ethernet", "Bluetooth", "Wi-Fi", "Infrared"],
                "answer": "Wi-Fi"
            }
        ]
    },
    "history": {
        "facts": [
            "The first successful powered flight was made by the Wright brothers in 1903.",
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa was painted by Leonardo da Vinci between 1503 and 1519."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for building the pyramids?",
                "options": ["Aztec", "Inca", "Maya", "Egyptian"],
                "answer": "Egyptian"
            },
            {
                "question": "What was the name of the first successful voyage around the world?",
                "options": ["The Odyssey", "The Voyage of the Beagle", "The Magellan Expedition", "The Lewis and Clark Expedition"],
                "answer": "The Magellan Expedition"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "Benjamin Franklin"],
                "answer": "George Washington"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal is the giraffe.",
            "The Great Pyramid of Giza is the only remaining wonder of the ancient world."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Arctic Ocean", "Indian Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "What is the name of the largest continent on Earth?",
                "options": ["Africa", "Asia", "Europe", "Australia"],
                "answer": "Asia"
            },
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Mars", "Jupiter", "Saturn", "Uranus"],
                "answer": "Jupiter"
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
        user_answer = input("Enter your answer (1-4): ")
        if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
            if quiz_question["options"][int(user_answer) - 1] == quiz_question["answer"]:
                print("Correct!")
                return
            else:
                print("Incorrect. Please try again.")
        else:
            print("Invalid input. Please enter a number from 1 to 4.")

def main():
    """
    Main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    while True:
        user_topic = input("Enter your topic choice: ").lower()
        if user_topic in topics:
            print(f"Random fact about {user_topic.capitalize()}: {get_random_fact(user_topic)}")
            run_quiz(user_topic)
            break
        else:
            print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
