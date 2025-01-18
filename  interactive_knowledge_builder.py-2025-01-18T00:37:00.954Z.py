
import random
import requests
import json

def get_random_fact(topic):
    """
    Fetches a random fact or concept from a predefined database for the given topic.
    """
    # Predefined database of facts and concepts
    database = {
        "science": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Milky Way galaxy contains over 200 billion stars.",
            "Photosynthesis is the process by which plants convert light energy into chemical energy."
        ],
        "technology": [
            "The first electronic computer, ENIAC, was completed in 1946 and weighed 30 tons.",
            "The internet was originally called ARPANET and was created by the U.S. Department of Defense.",
            "Quantum computers have the potential to solve certain problems much faster than classical computers."
        ],
        "history": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Magna Carta, signed in 1215, was a landmark document that limited the power of the English monarchy.",
            "The Renaissance was a period of cultural, artistic, political, and economic \"rebirth\" in Europe, lasting from the 14th to the 17th century."
        ],
        "general": [
            "The largest organ in the human body is the skin.",
            "The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and raises the structure.",
            "The first product to have a barcode was Wrigley's gum."
        ]
    }

    # Fetch a random fact from the database for the given topic
    return random.choice(database[topic])

def quiz_question(topic):
    """
    Generates a multiple-choice quiz question for the given topic.
    """
    # Predefined quiz questions and answers
    quiz_data = {
        "science": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            },
            {
                "question": "Which of these is a renewable energy source?",
                "options": ["Coal", "Oil", "Natural Gas", "Solar"],
                "answer": 3
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
            }
        ],
        "history": [
            {
                "question": "Which ancient civilization built the Pyramids of Giza?",
                "options": ["Mesopotamians", "Egyptians", "Greeks", "Romans"],
                "answer": 1
            },
            {
                "question": "Which European country colonized India?",
                "options": ["France", "Spain", "Portugal", "United Kingdom"],
                "answer": 3
            }
        ],
        "general": [
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Mars", "Venus", "Jupiter", "Saturn"],
                "answer": 2
            },
            {
                "question": "Which of these is not a primary color?",
                "options": ["Red", "Blue", "Yellow", "Green"],
                "answer": 3
            }
        ]
    }

    # Fetch a random quiz question and answers from the database for the given topic
    return random.choice(quiz_data[topic])

def main():
    """
    The main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")
    print("1. Science")
    print("2. Technology")
    print("3. History")
    print("4. General Knowledge")

    topic_choice = int(input("Enter your choice (1-4): "))

    topics = ["science", "technology", "history", "general"]
    topic = topics[topic_choice - 1]

    print(f"\nYour chosen topic is: {topic.capitalize()}")
    print(f"Here's a random fact or concept about {topic}:")
    print(get_random_fact(topic))

    print("\nNow, let's test your knowledge with a quiz!")
    quiz_info = quiz_question(topic)
    print(quiz_info["question"])
    for i, option in enumerate(quiz_info["options"]):
        print(f"{i+1}. {option}")

    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == quiz_info["answer"]:
        print("Correct! You're a knowledge master.")
    else:
        print("Oops, that's not the right answer. Better luck next time!")

if __name__ == "__main__":
    main()
