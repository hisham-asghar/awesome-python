
import random
import requests
import json

# Dictionary to store topics and their respective facts and quizzes
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The first successful kidney transplant was performed in 1954.",
            "The largest known prime number as of 2022 has 23 million digits."
        ],
        "quizzes": [
            {
                "question": "What is the name of the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": 0
            },
            {
                "question": "Which scientist is known for developing the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"],
                "answer": 1
            },
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Hg"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The internet was initially called ARPANET and was created in 1969.",
            "The first commercial smartphone was the IBM Simon, released in 1992."
        ],
        "quizzes": [
            {
                "question": "What is the name of the programming language that was designed to be easy to read and write?",
                "options": ["Java", "Python", "C++", "Ruby"],
                "answer": 1
            },
            {
                "question": "Which company is known for creating the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": 2
            },
            {
                "question": "What is the name of the protocol that allows devices to communicate on the internet?",
                "options": ["HTTP", "TCP/IP", "SMTP", "FTP"],
                "answer": 1
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers."
        ],
        "quizzes": [
            {
                "question": "Which ancient civilization is known for building the Colosseum?",
                "options": ["Greek", "Roman", "Egyptian", "Mesopotamian"],
                "answer": 1
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
                "answer": 2
            },
            {
                "question": "What was the name of the famous explorer who sailed to the Americas in 1492?",
                "options": ["Marco Polo", "Vasco da Gama", "Ferdinand Magellan", "Christopher Columbus"],
                "answer": 3
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2022 has 23 million digits.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first person convicted of speeding was going 8 mph."
        ],
        "quizzes": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": 2
            },
            {
                "question": "What is the tallest mammal in the world?",
                "options": ["Elephant", "Giraffe", "Hippopotamus", "Rhinoceros"],
                "answer": 1
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
    Runs the quiz and returns the user's score.
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
    Main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in topics:
        print(f"You selected the {selected_topic.capitalize()} topic.")
        print(get_random_fact(selected_topic))
        quiz = get_random_quiz(selected_topic)
        score = run_quiz(quiz)
        print(f"Your score: {score} out of 1")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
