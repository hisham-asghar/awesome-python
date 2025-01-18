Here is the raw Python code without any additional commentary:

import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 206 bones.",
            "The Milky Way galaxy contains an estimated 100-400 billion stars.",
            "The largest known prime number as of 2022 has 23 million digits."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            },
            {
                "question": "What is the process by which plants convert light energy into chemical energy?",
                "options": ["Respiration", "Photosynthesis", "Transpiration", "Fermentation"],
                "answer": 1
            },
            {
                "question": "What is the name of the force that attracts objects with mass towards each other?",
                "options": ["Gravity", "Friction", "Electromagnetism", "Nuclear force"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer virus, called 'Creeper', was detected in 1971.",
            "The largest hard drive commercially available has a capacity of 100TB.",
            "The first electronic computer, ENIAC, was completed in 1946 and weighed over 30 tons."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "What is the name of the technology that allows devices to connect to the internet without a physical cable?",
                "options": ["Bluetooth", "Wi-Fi", "Ethernet", "Cellular"],
                "answer": 1
            },
            {
                "question": "What is the name of the storage device that uses a spinning disk to store data?",
                "options": ["SSD", "USB drive", "Hard disk drive", "Floppy disk"],
                "answer": 2
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers.",
            "The Berlin Wall, which divided East and West Berlin, was constructed in 1961 and fell in 1989."
        ],
        "quiz_questions": [
            {
                "question": "What year was the United States Declaration of Independence signed?",
                "options": ["1776", "1787", "1812", "1865"],
                "answer": 0
            },
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Mesopotamia", "Egypt", "Greece", "China"],
                "answer": 2
            },
            {
                "question": "What was the name of the first successful voyage around the world?",
                "options": ["The Magellan Expedition", "The Columbus Voyage", "The Lewis and Clark Expedition", "The Apollo 11 Mission"],
                "answer": 0
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal in the world is the giraffe.",
            "The largest desert in the world is the Sahara Desert in Africa."
        ],
        "quiz_questions": [
            {
                "question": "What is the capital city of Australia?",
                "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
                "answer": 3
            },
            {
                "question": "Which of these is not a primary color?",
                "options": ["Red", "Blue", "Yellow", "Green"],
                "answer": 3
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Arctic Ocean", "Indian Ocean", "Pacific Ocean"],
                "answer": 3
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the given topic.
    """
    facts = topics[topic]["facts"]
    return random.choice(facts)

def get_quiz_question(topic):
    """
    Retrieves a random quiz question and its options from the given topic.
    """
    quiz_questions = topics[topic]["quiz_questions"]
    question = random.choice(quiz_questions)
    return question["question"], question["options"], question["answer"]

def main():
    """
    Interactively guides the user through the knowledge-building experience.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()
    if selected_topic not in topics:
        print("Invalid topic. Please try again.")
        return

    print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
    print(get_random_fact(selected_topic))

    print("\nNow, let's test your knowledge with a quiz!")
    question, options, answer = get_quiz_question(selected_topic)
    print(question)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == answer:
        print("Correct! Well done.")
    else:
        print("Oops, that's not the right answer. Better luck next time!")

    print("\nThank you for using the Interactive Knowledge Builder. Have a great day!")

if __name__ == "__main__":
    main()