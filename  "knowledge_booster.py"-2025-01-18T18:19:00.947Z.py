
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest planet in the solar system is Venus, not Mercury.",
            "Diamonds are formed from compressed carbon deep within the Earth's crust."
        ],
        "quiz": [
            {
                "question": "What is the primary source of energy for most living organisms on Earth?",
                "options": ["Sunlight", "Fossil fuels", "Nuclear fusion", "Geothermal energy"],
                "answer": 0
            },
            {
                "question": "Which of these is NOT a state of matter?",
                "options": ["Solid", "Liquid", "Gas", "Plasma"],
                "answer": 2
            },
            {
                "question": "What is the process by which plants convert sunlight into chemical energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented by Douglas Engelbart in 1964.",
            "The first commercial microprocessor was the Intel 4004, released in 1971.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989."
        ],
        "quiz": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "Which company developed the first commercially successful smartphone?",
                "options": ["Apple", "Samsung", "BlackBerry", "Nokia"],
                "answer": 3
            },
            {
                "question": "What is the name of the first digital computer, developed in the 1930s?",
                "options": ["ENIAC", "UNIVAC", "Colossus", "Z1"],
                "answer": 0
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The first Olympic Games were held in 776 BC in Olympia, Greece.",
            "The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci."
        ],
        "quiz": [
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Egyptians", "Babylonians", "Greeks", "Mayans"],
                "answer": 1
            },
            {
                "question": "What was the name of the first successful powered flight, conducted by the Wright brothers in 1903?",
                "options": ["The Flyer", "The Wright Flyer", "The Kitty Hawk", "The Biplane"],
                "answer": 1
            },
            {
                "question": "Which ancient civilization is known for its impressive architectural achievements, such as the Pyramids of Giza?",
                "options": ["Mesopotamians", "Incas", "Egyptians", "Mayans"],
                "answer": 2
            }
        ]
    },
    "general": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal in the world is the giraffe.",
            "The largest ocean on Earth is the Pacific Ocean."
        ],
        "quiz": [
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
                "question": "What is the largest planet in our solar system?",
                "options": ["Mars", "Saturn", "Jupiter", "Uranus"],
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
    return input("Enter your choice: ").lower()

def display_fact(topic):
    fact = random.choice(topics[topic]["facts"])
    print(f"Here's an interesting fact about {topic.capitalize()}:")
    print(f"- {fact}")

def display_quiz(topic):
    print(f"Let's test your {topic.capitalize()} knowledge!")
    score = 0
    for quiz_question in topics[topic]["quiz"]:
        print(quiz_question["question"])
        for i, option in enumerate(quiz_question["options"]):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): ")) - 1
        if user_answer == quiz_question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Oops, that's not the right answer.")
    print(f"Your final score is {score} out of {len(topics[topic]['quiz'])}")

def main():
    topic = display_menu()
    display_fact(topic)
    display_quiz(topic)

if __name__ == "__main__":
    main()
