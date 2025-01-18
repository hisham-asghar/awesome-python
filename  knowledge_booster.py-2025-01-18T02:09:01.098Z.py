
import random
import requests
import json

# Define the topics and their corresponding facts and quizzes
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest temperature ever recorded on Earth was 154°F (68°C) in Death Valley, California.",
            "A single cloud can weigh more than 1 million pounds."
        ],
        "quizzes": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "Which planet in our solar system has the most moons?",
                "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
                "answer": "Jupiter"
            },
            {
                "question": "What is the process by which plants convert light energy into chemical energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": "Photosynthesis"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 and had only one button.",
            "The first text message was sent on December 3, 1992, and said 'Merry Christmas'.",
            "The first commercial website was launched in 1991 and was for a pizza company."
        ],
        "quizzes": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "What is the name of the first commercially successful web browser?",
                "options": ["Mosaic", "Netscape Navigator", "Internet Explorer", "Google Chrome"],
                "answer": "Netscape Navigator"
            },
            {
                "question": "What is the name of the technology that allows devices to connect to the internet wirelessly?",
                "options": ["Bluetooth", "Wi-Fi", "Ethernet", "Cellular"],
                "answer": "Wi-Fi"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers.",
            "The Mona Lisa has no eyebrows, as it was the fashion in Renaissance-era Italy to shave them off."
        ],
        "quizzes": [
            {
                "question": "In what year was the Declaration of Independence signed?",
                "options": ["1776", "1789", "1812", "1848"],
                "answer": "1776"
            },
            {
                "question": "Which ancient civilization is known for building the pyramids?",
                "options": ["Aztecs", "Incas", "Mayans", "Egyptians"],
                "answer": "Egyptians"
            },
            {
                "question": "What was the name of the first successful powered flight?",
                "options": ["The Wright Flyer", "The Kitty Hawk", "The Biplane", "The Glider"],
                "answer": "The Wright Flyer"
            }
        ]
    },
    "general": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal is the giraffe, which can grow up to 18 feet tall.",
            "The largest moon in our solar system is Ganymede, which is larger than the planet Mercury."
        ],
        "quizzes": [
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": "AB"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Earth", "Mars", "Jupiter", "Saturn"],
                "answer": "Jupiter"
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            }
        ]
    }
}

def display_menu():
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    return input("Enter your choice: ").lower()

def display_fact(topic):
    fact = random.choice(topics[topic]["facts"])
    print(f"Here's an interesting fact about {topic.capitalize()}:")
    print(f"- {fact}")

def display_quiz(topic):
    quiz = random.choice(topics[topic]["quizzes"])
    print(f"Let's test your {topic.capitalize()} knowledge!")
    print(quiz["question"])
    for i, option in enumerate(quiz["options"]):
        print(f"{i+1}. {option}")
    user_answer = input("Enter the number of your answer: ")
    if quiz["options"][int(user_answer) - 1] == quiz["answer"]:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {quiz['answer']}.")

def main():
    topic = display_menu()
    display_fact(topic)
    display_quiz(topic)

if __name__ == "__main__":
    main()
