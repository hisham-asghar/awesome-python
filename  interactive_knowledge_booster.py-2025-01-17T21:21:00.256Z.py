
import random
import requests
import json

# Define the topics and their associated facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human brain is approximately 60% fat.",
            "The world's largest desert is Antarctica, not the Sahara.",
            "A single bolt of lightning can reach temperatures of up to 30,000°C (54,000°F)."
        ],
        "quiz": [
            {
                "question": "What is the main component of the Earth's atmosphere?",
                "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"],
                "answer": 1
            },
            {
                "question": "What is the name of the force that keeps planets in orbit around the Sun?",
                "options": ["Gravity", "Centrifugal force", "Electromagnetic force", "Friction"],
                "answer": 0
            },
            {
                "question": "What is the name of the process by which plants convert sunlight, water, and carbon dioxide into glucose?",
                "options": ["Photosynthesis", "Respiration", "Digestion", "Evaporation"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, weighed 30 tons and took up 1800 square feet.",
            "The first commercial microprocessor was the Intel 4004, released in 1971.",
            "The internet was originally called ARPANET, which was created by the US Department of Defense in 1969."
        ],
        "quiz": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "What is the name of the device that converts digital signals into analog signals?",
                "options": ["Modem", "Router", "Switch", "Amplifier"],
                "answer": 0
            },
            {
                "question": "What is the name of the technology that allows wireless communication between devices?",
                "options": ["Bluetooth", "Ethernet", "Wi-Fi", "Infrared"],
                "answer": 2
            }
        ]
    },
    "history": {
        "facts": [
            "The Pyramids of Giza were built around 2560-2540 BC.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.",
            "The first successful powered flight was made by the Wright brothers in 1903."
        ],
        "quiz": [
            {
                "question": "What was the name of the first successful English settlement in North America?",
                "options": ["Jamestown", "Plymouth Colony", "Roanoke Colony", "St. Augustine"],
                "answer": 0
            },
            {
                "question": "What was the name of the war that lasted from 1939 to 1945?",
                "options": ["World War I", "World War II", "The Cold War", "The Vietnam War"],
                "answer": 1
            },
            {
                "question": "What was the name of the ancient civilization that built the Machu Picchu site in Peru?",
                "options": ["Aztecs", "Incas", "Mayans", "Olmecs"],
                "answer": 1
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest moon of Saturn is Titan, which is larger than the planet Mercury.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "A group of pugs is called a grumble."
        ],
        "quiz": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "What is the name of the tallest mountain in the world?",
                "options": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
                "answer": 0
            },
            {
                "question": "What is the name of the currency used in Japan?",
                "options": ["Yen", "Dollar", "Euro", "Pound"],
                "answer": 0
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
    print(f"\nHere's a random fact about {topic.capitalize()}:")
    print(random.choice(topics[topic]["facts"]))

def run_quiz(topic):
    print(f"\nTime for a {topic.capitalize()} quiz! Answer the multiple-choice questions.")
    score = 0
    for question in topics[topic]["quiz"]:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer == question["answer"] + 1:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"\nYour final score is {score} out of {len(topics[topic]['quiz'])}")

def main():
    topic = display_menu()
    display_fact(topic)
    run_quiz(topic)

if __name__ == "__main__":
    main()
