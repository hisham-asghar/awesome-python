
import random
import requests
import json

# Define the topics and their respective facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest planet in the solar system is Venus, not Mercury.",
            "Sharks have been around for more than 400 million years."
        ],
        "quiz": [
            {
                "question": "What is the name of the force that keeps objects on the Earth's surface?",
                "options": ["Gravity", "Friction", "Centrifugal force", "Buoyancy"],
                "answer": 0
            },
            {
                "question": "Which of these is not a state of matter?",
                "options": ["Solid", "Liquid", "Gas", "Plasma"],
                "answer": 2
            },
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Hg"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 and had only one button.",
            "The first commercially available personal computer was the Apple II, released in 1977.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989."
        ],
        "quiz": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "Which of these is not a type of computer memory?",
                "options": ["RAM", "ROM", "GPU", "SSD"],
                "answer": 2
            },
            {
                "question": "What does the acronym 'HTTP' stand for?",
                "options": ["Hypertext Transfer Protocol", "High-speed Transmission Technology Protocol", "Hybrid Transmission and Transformation Protocol", "Hyperlinked Text Transmission Protocol"],
                "answer": 0
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza in Egypt were built around 2500 BC.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD."
        ],
        "quiz": [
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Mesopotamia", "Egypt", "Greece", "China"],
                "answer": 2
            },
            {
                "question": "What was the name of the first successful powered flight by the Wright brothers?",
                "options": ["The Flyer", "The Kitty Hawk", "The Wright Flyer", "The Dayton Bomber"],
                "answer": 2
            },
            {
                "question": "Which event marked the beginning of World War I?",
                "options": ["The assassination of Archduke Franz Ferdinand", "The bombing of Pearl Harbor", "The fall of the Berlin Wall", "The Cuban Missile Crisis"],
                "answer": 0
            }
        ]
    },
    "general": {
        "facts": [
            "The tallest mammal is the giraffe, which can reach heights of up to 6 meters.",
            "The largest organ in the human body is the skin.",
            "The largest desert in the world is Antarctica, not the Sahara."
        ],
        "quiz": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Pacific Ocean", "Indian Ocean", "Arctic Ocean"],
                "answer": 1
            },
            {
                "question": "Which of these is not a primary color?",
                "options": ["Red", "Blue", "Yellow", "Green"],
                "answer": 3
            },
            {
                "question": "What is the capital city of Australia?",
                "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
                "answer": 3
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
    print(f"Here's an interesting fact about {topic.capitalize()}:")
    print(fact)

def run_quiz(topic):
    print(f"Let's test your {topic.capitalize()} knowledge!")
    score = 0
    for question in topics[topic]["quiz"]:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): ")) - 1
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", question["options"][question["answer"]])
    print(f"Your score: {score}/{len(topics[topic]['quiz'])}")

def main():
    topic = display_menu()
    display_fact(topic)
    run_quiz(topic)

if __name__ == "__main__":
    main()
