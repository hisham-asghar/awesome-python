
import random
import requests
import json

def get_random_fact(topic):
    """Fetches a random fact or concept from the given topic."""
    facts = {
        "science": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest planet in the solar system is Venus, not Mercury.",
            "Honey is the only food that does not spoil."
        ],
        "technology": [
            "The first computer virus was created in 1983 and was called 'The Elk Cloner'.",
            "The first commercial internet service provider (ISP) was launched in 1989.",
            "The first smartphone was the IBM Simon, released in 1992."
        ],
        "history": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza were built around 2560–2540 BC.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD."
        ],
        "general": [
            "A group of flamingos is called a 'flamboyance'.",
            "The first product to have a barcode was Wrigley's gum.",
            "The first person convicted of speeding was going 8 mph."
        ]
    }
    return random.choice(facts[topic])

def quiz(topic):
    """Provides a multiple-choice quiz on the given topic."""
    questions = {
        "science": [
            {"question": "What is the largest planet in our solar system?", "options": ["Jupiter", "Saturn", "Mars", "Venus"], "answer": 0},
            {"question": "What is the name of the process by which plants convert sunlight into energy?", "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"], "answer": 0},
            {"question": "What is the name of the force that attracts objects with mass towards each other?", "options": ["Gravity", "Friction", "Electromagnetism", "Nuclear force"], "answer": 0}
        ],
        "technology": [
            {"question": "What is the name of the first computer programming language?", "options": ["FORTRAN", "COBOL", "BASIC", "PASCAL"], "answer": 0},
            {"question": "What is the name of the device that converts digital signals into analog signals?", "options": ["Modem", "Router", "Switch", "Printer"], "answer": 0},
            {"question": "What is the name of the process by which data is transmitted over the internet?", "options": ["Packet switching", "Circuit switching", "Multiplexing", "Modulation"], "answer": 0}
        ],
        "history": [
            {"question": "In what year was the Declaration of Independence signed?", "options": ["1776", "1789", "1812", "1865"], "answer": 0},
            {"question": "Who was the first president of the United States?", "options": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "Theodore Roosevelt"], "answer": 0},
            {"question": "What was the name of the ancient Egyptian civilization that built the pyramids?", "options": ["Mesopotamia", "Sumeria", "Babylon", "Ancient Egypt"], "answer": 3}
        ],
        "general": [
            {"question": "What is the name of the largest ocean on Earth?", "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"], "answer": 0},
            {"question": "What is the name of the largest mammal on Earth?", "options": ["Elephant", "Whale", "Giraffe", "Hippopotamus"], "answer": 1},
            {"question": "What is the name of the tallest mountain in the world?", "options": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"], "answer": 0}
        ]
    }

    print(f"Welcome to the {topic.upper()} quiz!")
    print("Answer the multiple-choice questions by entering the corresponding number.")

    score = 0
    for q in questions[topic]:
        print(q["question"])
        for i, option in enumerate(q["options"]):
            print(f"{i}. {option}")
        user_answer = int(input("Your answer: "))
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score is {score} out of {len(questions[topic])}.")

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    print("1. Science")
    print("2. Technology")
    print("3. History")
    print("4. General Knowledge")

    topic_choice = int(input("Enter the number of your chosen topic: "))
    topics = ["science", "technology", "history", "general"]
    topic = topics[topic_choice - 1]

    print(f"\nHere's a random fact about {topic}:")
    print(get_random_fact(topic))

    print("\nNow let's test your knowledge with a quiz!")
    quiz(topic)

if __name__ == "__main__":
    main()
