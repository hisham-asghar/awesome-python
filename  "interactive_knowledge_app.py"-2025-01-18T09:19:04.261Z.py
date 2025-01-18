
import random
import requests
import json

# Define the topics and their corresponding facts and quizzes
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest planet in the solar system is Venus, not Mercury.",
            "Diamonds are the hardest known natural material on Earth."
        ],
        "quizzes": [
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Combustion", "Evaporation"],
                "answer": 0
            },
            {
                "question": "Which of these is not a fundamental force in physics?",
                "options": ["Gravity", "Electromagnetism", "Strong nuclear force", "Friction"],
                "answer": 3
            },
            {
                "question": "What is the name of the theory that describes the origin of the universe?",
                "options": ["Big Bang Theory", "String Theory", "Theory of Relativity", "Quantum Theory"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 and had only one button.",
            "The first smartphone was the IBM Simon, released in 1992.",
            "The largest hard disk drive ever produced had a capacity of 5.25 terabytes."
        ],
        "quizzes": [
            {
                "question": "Which of these is not a type of computer memory?",
                "options": ["RAM", "ROM", "CPU", "SSD"],
                "answer": 2
            },
            {
                "question": "What does the acronym 'HTML' stand for?",
                "options": ["Hyper Text Markup Language", "High-level Text Markup Language", "Hyperlink Text Markup Language", "Hyper Text Machine Language"],
                "answer": 0
            },
            {
                "question": "Which company developed the first commercially successful smartphone?",
                "options": ["Apple", "Samsung", "BlackBerry", "Nokia"],
                "answer": 2
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The first successful powered flight took place in 1903, piloted by the Wright brothers.",
            "The Mona Lisa has no eyebrows, as it was the fashion in Renaissance Florence to shave them off."
        ],
        "quizzes": [
            {
                "question": "Which ancient civilization is known for its pyramids?",
                "options": ["Mesopotamia", "Indus Valley", "Egypt", "China"],
                "answer": 2
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "Benjamin Franklin"],
                "answer": 2
            },
            {
                "question": "What was the name of the first successful powered flight?",
                "options": ["The Wright Flyer", "The Kitty Hawk", "The Spirit of St. Louis", "The Biplane"],
                "answer": 0
            }
        ]
    },
    "general": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal is the giraffe.",
            "The largest ocean on Earth is the Pacific Ocean."
        ],
        "quizzes": [
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Mars", "Jupiter", "Saturn", "Uranus"],
                "answer": 1
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": 2
            },
            {
                "question": "What is the largest mammal in the world?",
                "options": ["Elephant", "Hippopotamus", "Blue Whale", "Polar Bear"],
                "answer": 2
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the specified topic.
    """
    return random.choice(topics[topic]["facts"])

def get_random_quiz(topic):
    """
    Retrieves a random quiz from the specified topic.
    """
    return random.choice(topics[topic]["quizzes"])

def run_quiz(quiz):
    """
    Runs the specified quiz and returns the user's score.
    """
    score = 0
    print(quiz["question"])
    for i, option in enumerate(quiz["options"]):
        print(f"{i+1}. {option}")
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == quiz["answer"]:
        print("Correct!")
        score = 1
    else:
        print("Incorrect.")
    return score

def main():
    """
    The main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in topics:
        print(f"You selected: {selected_topic.capitalize()}")
        print(get_random_fact(selected_topic))
        quiz = get_random_quiz(selected_topic)
        score = run_quiz(quiz)
        print(f"Your score: {score}/1")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
