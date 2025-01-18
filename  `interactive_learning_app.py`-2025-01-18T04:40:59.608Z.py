
import json
import random
import requests

# Define the topics and their corresponding facts and quizzes
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Milky Way galaxy contains an estimated 100 to 400 billion stars.",
            "The largest known prime number as of 2023 has 23 million digits."
        ],
        "quizzes": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            },
            {
                "question": "Which planet in our solar system has the most moons?",
                "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
                "answer": 0
            },
            {
                "question": "What is the name of the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, was completed in 1946 and weighed 30 tons.",
            "The first commercial microprocessor, the Intel 4004, was released in 1971.",
            "The internet was originally called ARPANET and was created by the U.S. Department of Defense in 1969."
        ],
        "quizzes": [
            {
                "question": "What does 'HTML' stand for?",
                "options": ["Hypertext Markup Language", "Hypertext Markup Linking", "Hypertext Markup Logic", "Hypertext Markup Lingo"],
                "answer": 0
            },
            {
                "question": "What is the name of the first commercially successful smartphone?",
                "options": ["iPhone", "BlackBerry", "Nokia 9000 Communicator", "Motorola RAZR"],
                "answer": 1
            },
            {
                "question": "Which company developed the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": 2
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.",
            "The Declaration of Independence was signed on July 4, 1776."
        ],
        "quizzes": [
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "Benjamin Franklin"],
                "answer": 2
            },
            {
                "question": "What year did World War II end?",
                "options": ["1945", "1939", "1942", "1950"],
                "answer": 0
            },
            {
                "question": "Which ancient civilization is known for building the Colosseum?",
                "options": ["Greek", "Roman", "Egyptian", "Mesopotamian"],
                "answer": 1
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2023 has 23 million digits.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "A group of flamingos is called a flamboyance."
        ],
        "quizzes": [
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": 2
            },
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Liver", "Skin", "Brain"],
                "answer": 2
            },
            {
                "question": "What is the tallest mammal?",
                "options": ["Elephant", "Giraffe", "Moose", "Hippopotamus"],
                "answer": 1
            }
        ]
    }
}

def interactive_learning_app():
    print("Welcome to the Interactive Learning App!")
    print("Select a topic to explore:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    chosen_topic = input("Enter your choice: ").lower()

    if chosen_topic not in topics:
        print("Invalid topic. Please try again.")
        return

    print(f"You selected: {chosen_topic.capitalize()}")
    print(f"Here's a random fact about {chosen_topic}:")
    print(random.choice(topics[chosen_topic]["facts"]))

    print("\nNow, let's test your knowledge with a quiz!")
    quiz = random.choice(topics[chosen_topic]["quizzes"])
    print(quiz["question"])
    for i, option in enumerate(quiz["options"]):
        print(f"{i+1}. {option}")

    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == quiz["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz["options"][quiz["answer"]])

    print("\nThanks for using the Interactive Learning App!")
