
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and thus increases in height.",
            "A single cloud can weigh more than 1 million pounds."
        ],
        "quiz": [
            {
                "question": "What is the name of the force that keeps planets in orbit around the Sun?",
                "options": ["Gravity", "Centrifugal force", "Electromagnetic force", "Friction"],
                "answer": 0
            },
            {
                "question": "Which scientist is known for the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Marie Curie"],
                "answer": 1
            },
            {
                "question": "What is the name of the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Evaporation"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, weighed 30 tons and took up 1,800 square feet of space.",
            "The word 'robot' was first used in a 1920 science fiction play called 'Rossum's Universal Robots'.",
            "The first mobile phone call was made on April 3, 1973, by Martin Cooper of Motorola."
        ],
        "quiz": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "JavaScript"],
                "answer": 2
            },
            {
                "question": "Which company developed the first commercial graphical user interface (GUI) for personal computers?",
                "options": ["Apple", "Microsoft", "IBM", "Xerox"],
                "answer": 3
            },
            {
                "question": "What is the name of the technology that allows devices to connect to the internet without a physical cable?",
                "options": ["Ethernet", "Wi-Fi", "Bluetooth", "Cellular"],
                "answer": 1
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off."
        ],
        "quiz": [
            {
                "question": "Which ancient civilization is known for its pyramids?",
                "options": ["Aztec", "Inca", "Maya", "Egyptian"],
                "answer": 3
            },
            {
                "question": "What was the name of the first successful space mission to land a human on the Moon?",
                "options": ["Apollo 8", "Apollo 11", "Gemini 3", "Mercury-Redstone 3"],
                "answer": 1
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
            "A group of flamingos is called a flamboyance.",
            "Bananas are slightly radioactive.",
            "The first product to have a barcode was Wrigley's gum."
        ],
        "quiz": [
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Liver", "Skin", "Brain"],
                "answer": 2
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
                "answer": 0
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": 2
            }
        ]
    }
}

def display_menu():
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

def get_random_fact(topic):
    facts = topics[topic]["facts"]
    return random.choice(facts)

def quiz(topic):
    quiz_questions = topics[topic]["quiz"]
    score = 0

    for question in quiz_questions:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")

        user_answer = int(input("Enter your answer (1-4): ")) - 1
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")

    print(f"Your final score is {score}/{len(quiz_questions)}")

def main():
    display_menu()
    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
