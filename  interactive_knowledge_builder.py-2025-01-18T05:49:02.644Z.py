
import random
import requests
import json

# Define the topics and their associated data
topics = {
    "science": {
        "facts": [
            "The human body has over 60,000 miles of blood vessels.",
            "The first programmable computer was invented in 1936 by Alan Turing.",
            "The largest known prime number as of 2022 has 23 million digits."
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
                "options": ["Gravity", "Friction", "Magnetism", "Electricity"],
                "answer": "Gravity"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first mobile phone call was made in 1973 by Martin Cooper of Motorola.",
            "The internet was originally called ARPANET and was created in 1969 by the U.S. Department of Defense.",
            "The first computer virus, called 'Creeper', was created in 1971 as an experiment."
        ],
        "quiz_questions": [
            {
                "question": "What does the term 'CPU' stand for?",
                "options": ["Central Processing Unit", "Computer Power Unit", "Cyber Processor Unit", "Central Power Unit"],
                "answer": "Central Processing Unit"
            },
            {
                "question": "What is the name of the first commercially successful web browser?",
                "options": ["Mosaic", "Netscape Navigator", "Internet Explorer", "Google Chrome"],
                "answer": "Netscape Navigator"
            },
            {
                "question": "What is the name of the programming language used to create websites?",
                "options": ["Python", "Java", "C++", "HTML"],
                "answer": "HTML"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa was painted by the Italian Renaissance artist, Leonardo da Vinci, between 1503 and 1519.",
            "The first successful powered flight was made by the Wright brothers in 1903."
        ],
        "quiz_questions": [
            {
                "question": "What year was the United States of America founded?",
                "options": ["1776", "1789", "1812", "1865"],
                "answer": "1776"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "James Madison"],
                "answer": "George Washington"
            },
            {
                "question": "What was the name of the ancient Egyptian civilization that built the pyramids?",
                "options": ["Mesopotamian", "Babylonian", "Sumerian", "Pharaonic"],
                "answer": "Pharaonic"
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2022 has 23 million digits.",
            "The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.",
            "The largest known prime number as of 2022 has 23 million digits."
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
                "question": "What is the name of the largest continent on Earth?",
                "options": ["Asia", "Africa", "Europe", "North America"],
                "answer": "Asia"
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
    Retrieves a random quiz question and its options from the given topic.
    """
    quiz_question = random.choice(topics[topic]["quiz_questions"])
    return quiz_question["question"], quiz_question["options"]

def check_answer(topic, answer):
    """
    Checks if the user's answer is correct for the given topic.
    """
    quiz_question = random.choice(topics[topic]["quiz_questions"])
    return quiz_question["answer"] == answer

def main():
    """
    The main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge-Building Script!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))

        print("\nTime for a quiz!")
        question, options = get_quiz_question(selected_topic)
        print(question)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

        user_answer = input("Enter your answer (1-4): ")
        if check_answer(selected_topic, options[int(user_answer)-1]):
            print("Correct!")
        else:
            print("Incorrect. Better luck next time!")
    else:
        print(f"Sorry, '{selected_topic}' is not a valid topic. Please try again.")

if __name__ == "__main__":
    main()
