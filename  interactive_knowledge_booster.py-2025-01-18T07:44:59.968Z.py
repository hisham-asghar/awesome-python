
import random
import requests
import json

def get_random_fact(topic):
    """Fetch a random fact or concept for the given topic."""
    facts = {
        "science": [
            "The sun is 93 million miles away from the Earth.",
            "DNA is made up of four chemical building blocks: adenine, guanine, cytosine, and thymine.",
            "The human brain has approximately 86 billion neurons."
        ],
        "technology": [
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989.",
            "The first smartphone was the IBM Simon, released in 1992."
        ],
        "history": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.",
            "The Renaissance period in Europe lasted from the 14th to the 17th century."
        ],
        "general": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal in the world is the giraffe.",
            "The largest ocean on Earth is the Pacific Ocean."
        ]
    }
    return random.choice(facts[topic])

def get_quiz_question(topic):
    """Fetch a multiple-choice quiz question for the given topic."""
    quiz_questions = {
        "science": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            },
            {
                "question": "Which planet in our solar system is known as the 'Red Planet'?",
                "options": ["Mars", "Jupiter", "Saturn", "Venus"],
                "answer": 0
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": 0
            }
        ],
        "technology": [
            {
                "question": "What is the name of the first web browser?",
                "options": ["Google Chrome", "Mozilla Firefox", "Internet Explorer", "WorldWideWeb"],
                "answer": 3
            },
            {
                "question": "Which company developed the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": 2
            },
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            }
        ],
        "history": [
            {
                "question": "Which ancient civilization built the Colosseum in Rome?",
                "options": ["Greeks", "Romans", "Egyptians", "Aztecs"],
                "answer": 1
            },
            {
                "question": "What year did the United States declare independence?",
                "options": ["1776", "1789", "1812", "1865"],
                "answer": 0
            },
            {
                "question": "Which famous explorer discovered America in 1492?",
                "options": ["Christopher Columbus", "Vasco da Gama", "Ferdinand Magellan", "Marco Polo"],
                "answer": 0
            }
        ],
        "general": [
            {
                "question": "What is the largest animal in the world?",
                "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
                "answer": 1
            },
            {
                "question": "What is the capital city of Australia?",
                "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
                "answer": 3
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": 2
            }
        ]
    }
    return random.choice(quiz_questions[topic])

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    print("1. Science")
    print("2. Technology")
    print("3. History")
    print("4. General Knowledge")

    topic_choice = input("Enter the number of your choice: ")

    if topic_choice == "1":
        topic = "science"
    elif topic_choice == "2":
        topic = "technology"
    elif topic_choice == "3":
        topic = "history"
    elif topic_choice == "4":
        topic = "general"
    else:
        print("Invalid choice. Exiting.")
        return

    print(f"\nYour chosen topic is: {topic.capitalize()}")
    print(get_random_fact(topic))

    quiz_question = get_quiz_question(topic)
    print(f"\nTest your knowledge with this multiple-choice question:")
    print(quiz_question["question"])
    for i, option in enumerate(quiz_question["options"]):
        print(f"{i+1}. {option}")

    user_answer = int(input("Enter the number of your answer: "))
    if user_answer - 1 == quiz_question["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_question["options"][quiz_question["answer"]])

    print("\nThank you for using the Interactive Knowledge Booster!")

if __name__ == "__main__":
    main()
