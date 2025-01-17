
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest planet in the solar system is Venus, not Mercury.",
            "The largest known prime number as of 2021 has 23 million digits."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": 0
            },
            {
                "question": "Which of the following is not a state of matter?",
                "options": ["Solid", "Liquid", "Gas", "Plasma"],
                "answer": 2
            },
            {
                "question": "What is the name of the force that attracts objects with mass towards each other?",
                "options": ["Gravity", "Friction", "Buoyancy", "Centrifugal force"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer bug was a real moth found trapped in a Harvard Mark II computer in 1947.",
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The world's first text message was sent on December 3, 1992, and read 'Merry Christmas'."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "What is the name of the device that converts digital signals into analog signals?",
                "options": ["Router", "Modem", "Switch", "Amplifier"],
                "answer": 1
            },
            {
                "question": "What is the name of the technology that allows devices to communicate wirelessly?",
                "options": ["Bluetooth", "Ethernet", "Wi-Fi", "Infrared"],
                "answer": 2
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers.",
            "The Mona Lisa has no eyebrows, as it was the fashion in Renaissance-era Florence to shave them off."
        ],
        "quiz_questions": [
            {
                "question": "What was the name of the first successful powered flight?",
                "options": ["The Wright Flyer", "The Kitty Hawk", "The Biplane", "The Glider"],
                "answer": 0
            },
            {
                "question": "Which ancient civilization is known for its pyramids?",
                "options": ["Mesopotamia", "Indus Valley", "Egypt", "China"],
                "answer": 2
            },
            {
                "question": "Which European country colonized the most territories worldwide?",
                "options": ["Spain", "Portugal", "France", "United Kingdom"],
                "answer": 3
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and rises.",
            "A group of porcupines is called a prickle.",
            "The first product to have a barcode was Wrigley's gum."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Liver", "Skin", "Brain"],
                "answer": 2
            },
            {
                "question": "What is the name of the tallest mountain in the world?",
                "options": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
                "answer": 0
            },
            {
                "question": "What is the name of the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Returns a random fact from the given topic.
    """
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    """
    Returns a random quiz question and its options from the given topic.
    """
    quiz_question = random.choice(topics[topic]["quiz_questions"])
    return quiz_question["question"], quiz_question["options"]

def check_answer(topic, answer_index):
    """
    Checks if the user's answer is correct for the given topic and answer index.
    """
    quiz_question = random.choice(topics[topic]["quiz_questions"])
    return quiz_question["answer"] == answer_index

def main():
    """
    The main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
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

    score = 0
    for _ in range(3):
        question, options = get_quiz_question(selected_topic)
        print(f"\nQuestion: {question}")
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

        user_answer = int(input("Enter your answer (1-4): "))
        if check_answer(selected_topic, user_answer - 1):
            print("Correct!")
            score += 1
        else:
            print("Incorrect. Better luck next time!")

    print(f"\nYour final score is {score} out of 3.")

if __name__ == "__main__":
    main()
