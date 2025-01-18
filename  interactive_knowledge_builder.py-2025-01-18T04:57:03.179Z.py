
import random
import requests
import json

# Define a dictionary of topics and their associated facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The largest known prime number as of 2023 has 23 million digits.",
            "The first successful kidney transplant was performed in 1954."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": "Photosynthesis"
            },
            {
                "question": "What is the name of the force that attracts objects with mass towards each other?",
                "options": ["Gravity", "Friction", "Buoyancy", "Centrifugal force"],
                "answer": "Gravity"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The world's first programmable computer was the ENIAC, completed in 1946.",
            "The first commercial microprocessor was the Intel 4004, released in 1971."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "What is the name of the technology that allows devices to connect to the internet wirelessly?",
                "options": ["Bluetooth", "Wi-Fi", "Ethernet", "LAN"],
                "answer": "Wi-Fi"
            },
            {
                "question": "What is the name of the software that translates high-level programming languages into machine-readable code?",
                "options": ["Compiler", "Interpreter", "Debugger", "IDE"],
                "answer": "Compiler"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramids of Giza were built around 2560-2540 BCE.",
            "The first successful powered flight was made by the Wright brothers in 1903.",
            "The Gutenberg Bible, the first major book printed in the West using movable type, was published in 1455."
        ],
        "quiz_questions": [
            {
                "question": "What year was the United States Declaration of Independence signed?",
                "options": ["1776", "1789", "1812", "1848"],
                "answer": "1776"
            },
            {
                "question": "What was the name of the first successful voyage around the world?",
                "options": ["The Magellan Expedition", "The Columbus Voyage", "The Lewis and Clark Expedition", "The Silk Road"],
                "answer": "The Magellan Expedition"
            },
            {
                "question": "What was the name of the ancient Egyptian civilization that built the pyramids?",
                "options": ["Mesopotamians", "Phoenicians", "Mayans", "Egyptians"],
                "answer": "Egyptians"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal is the giraffe.",
            "The largest planet in our solar system is Jupiter."
        ],
        "quiz_questions": [
            {
                "question": "What is the capital city of Australia?",
                "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
                "answer": "Canberra"
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "What is the name of the largest mammal on Earth?",
                "options": ["Elephant", "Hippopotamus", "Blue Whale", "Sperm Whale"],
                "answer": "Blue Whale"
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the given topic.
    """
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    """
    Retrieves a random quiz question from the given topic.
    """
    quiz_question = random.choice(topics[topic]["quiz_questions"])
    return quiz_question

def run_quiz(topic):
    """
    Runs a quiz for the given topic.
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
    Main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge-Building Script!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in topics:
        print("\nHere's a random fact about", selected_topic.capitalize() + ":")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
