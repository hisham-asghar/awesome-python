
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The first satellite launched into space was Sputnik 1 in 1957.",
            "Photosynthesis is the process by which plants convert sunlight, water, and carbon dioxide into oxygen and energy in the form of sugar."
        ],
        "quiz": [
            {
                "question": "What is the chemical formula for water?",
                "options": ["H2O", "CO2", "CH4"],
                "answer": 0
            },
            {
                "question": "What is the name of the force that pulls objects towards each other?",
                "options": ["Gravity", "Friction", "Electromagnetism"],
                "answer": 0
            },
            {
                "question": "Which scientist is known for developing the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei"],
                "answer": 1
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The term 'bug' in computer programming was coined when a moth was found stuck in a Harvard Mark II computer in 1947.",
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951."
        ],
        "quiz": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python"],
                "answer": 2
            },
            {
                "question": "Which company developed the first commercially successful smartphone?",
                "options": ["Apple", "Samsung", "BlackBerry"],
                "answer": 2
            },
            {
                "question": "What is the name of the first web browser, created by Tim Berners-Lee?",
                "options": ["Mosaic", "Netscape Navigator", "WorldWideWeb"],
                "answer": 2
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers."
        ],
        "quiz": [
            {
                "question": "In what year did World War I begin?",
                "options": ["1914", "1939", "1945"],
                "answer": 0
            },
            {
                "question": "What was the name of the first American president?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington"],
                "answer": 2
            },
            {
                "question": "Which ancient civilization is known for building the pyramids?",
                "options": ["Mesopotamia", "Aztec", "Ancient Egypt"],
                "answer": 2
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2022 has 23 million digits.",
            "The tallest mammal in the world is the giraffe.",
            "There are more possible iterations of a game of chess than there are atoms in the observable universe."
        ],
        "quiz": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 2
            },
            {
                "question": "What is the name of the largest moon of Saturn?",
                "options": ["Titan", "Ganymede", "Callisto"],
                "answer": 0
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB-"],
                "answer": 2
            }
        ]
    }
}

def display_menu():
    print("Welcome to the Interactive Knowledge Hub!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    return input("Enter your choice: ").lower()

def display_fact(topic):
    print(f"\nHere's a random fact about {topic.capitalize()}:")
    print(random.choice(topics[topic]["facts"]))

def run_quiz(topic):
    print(f"\nTime for a {topic.capitalize()} quiz! Answer the following multiple-choice questions:")
    score = 0
    for question in topics[topic]["quiz"]:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-3): ")) - 1
        if user_answer == question["answer"]:
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
