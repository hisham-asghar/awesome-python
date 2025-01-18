
import random
import requests
import json

def get_fact(topic):
    """Fetch a random fact or concept from the chosen topic."""
    facts = {
        "science": [
            "The human body contains around 60,000 miles of blood vessels.",
            "The Milky Way galaxy contains an estimated 100 to 400 billion stars.",
            "Bioluminescence is the production and emission of light by a living organism."
        ],
        "technology": [
            "The first programmable computer was the ENIAC, which was completed in 1946.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989.",
            "Quantum computers can perform certain calculations exponentially faster than classical computers."
        ],
        "history": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.",
            "The Renaissance was a period of cultural, artistic, political, and economic \"rebirth\" in Europe."
        ],
        "general": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal is the giraffe, with an average height of 4.3 to 5.7 meters.",
            "The largest ocean on Earth is the Pacific Ocean, covering an area of about 63 million square miles."
        ]
    }
    return random.choice(facts[topic])

def quiz(topic):
    """Provide a multiple-choice quiz for the chosen topic."""
    quizzes = {
        "science": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": 0
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Mars", "Jupiter", "Saturn", "Neptune"],
                "answer": 1
            }
        ],
        "technology": [
            {
                "question": "What is the name of the first web browser?",
                "options": ["Google Chrome", "Mozilla Firefox", "Internet Explorer", "Mosaic"],
                "answer": 3
            },
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "What is the name of the first commercially successful smartphone?",
                "options": ["iPhone", "BlackBerry", "Nokia 3310", "Motorola RAZR"],
                "answer": 1
            }
        ],
        "history": [
            {
                "question": "What year was the Declaration of Independence signed?",
                "options": ["1776", "1789", "1812", "1865"],
                "answer": 0
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
                "answer": 2
            },
            {
                "question": "What was the name of the ancient civilization that built the pyramids?",
                "options": ["Aztec", "Inca", "Maya", "Egyptian"],
                "answer": 3
            }
        ],
        "general": [
            {
                "question": "What is the largest mammal in the world?",
                "options": ["Elephant", "Whale", "Giraffe", "Hippopotamus"],
                "answer": 1
            },
            {
                "question": "What is the name of the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Arctic Ocean", "Indian Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "What is the name of the tallest mountain in the world?",
                "options": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
                "answer": 0
            }
        ]
    }
    quiz = random.choice(quizzes[topic])
    print(quiz["question"])
    for i, option in enumerate(quiz["options"]):
        print(f"{i+1}. {option}")
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == quiz["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz["options"][quiz["answer"]])

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Choose a topic:")
    topics = ["Science", "Technology", "History", "General"]
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")
    topic_choice = int(input("Enter your choice (1-4): ")) - 1
    topic = topics[topic_choice].lower()

    print("\nHere's a random fact or concept about", topics[topic_choice], ":")
    print(get_fact(topic))

    print("\nNow, let's test your knowledge with a quiz!")
    quiz(topic)

if __name__ == "__main__":
    main()
