
import random
import requests
import json

def get_random_fact(topic):
    """Fetch a random fact or concept from the selected topic."""
    facts = {
        "science": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Earth's core is as hot as the surface of the Sun.",
            "A single cloud can weigh more than 1 million pounds."
        ],
        "technology": [
            "The first computer virus was called 'The Creeper' and was created in 1971.",
            "The first email was sent in 1971 by Ray Tomlinson.",
            "The first smartphone was the IBM Simon, released in 1992."
        ],
        "history": [
            "The Great Wall of China is the only man-made structure visible from space.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The Titanic was the first ship to use the SOS distress signal."
        ],
        "general": [
            "A group of flamingos is called a 'flamboyance'.",
            "The first product to have a barcode was Wrigley's gum.",
            "The king of hearts is the only king without a mustache on a standard playing card."
        ]
    }
    return random.choice(facts[topic])

def quiz(topic):
    """Provide a multiple-choice quiz on the selected topic."""
    quizzes = {
        "science": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Hg"],
                "answer": 0
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Jupiter", "Saturn", "Mars", "Venus"],
                "answer": 0
            }
        ],
        "technology": [
            {
                "question": "What does 'www' stand for in a web address?",
                "options": ["World Wide Web", "World Web Worm", "Worldwide Web Consortium", "Web World Wide"],
                "answer": 0
            },
            {
                "question": "What is the name of the first commercially available personal computer?",
                "options": ["Apple I", "Commodore 64", "IBM PC", "Altair 8800"],
                "answer": 3
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
            }
        ],
        "general": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": 2
            }
        ]
    }
    quiz_data = random.choice(quizzes[topic])
    print(quiz_data["question"])
    for i, option in enumerate(quiz_data["options"]):
        print(f"{i+1}. {option}")
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == quiz_data["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_data["options"][quiz_data["answer"]])

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Select a topic:")
    topics = ["Science", "Technology", "History", "General"]
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")
    topic_choice = int(input("Enter your choice (1-4): ")) - 1
    topic = topics[topic_choice].lower()

    print(f"\nHere's a random fact about {topics[topic_choice]}:")
    print(get_random_fact(topic))

    print("\nLet's test your knowledge with a quiz!")
    quiz(topic)

if __name__ == "__main__":
    main()
