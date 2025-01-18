
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has over 600 muscles.",
            "The largest known prime number as of 2023 has over 23 million digits.",
            "The first successful kidney transplant was performed in 1954."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Evaporation", "Transpiration"],
                "answer": "Photosynthesis"
            },
            {
                "question": "What is the name of the closest planet to the Sun?",
                "options": ["Venus", "Mars", "Mercury", "Earth"],
                "answer": "Mercury"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964.",
            "The first commercial smartphone was the IBM Simon, released in 1992.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "What is the name of the operating system developed by Apple Inc.?",
                "options": ["Windows", "Linux", "macOS", "Android"],
                "answer": "macOS"
            },
            {
                "question": "What is the name of the company that developed the first commercially successful web browser?",
                "options": ["Microsoft", "Google", "Mozilla", "Netscape"],
                "answer": "Netscape"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China was built over 2,000 years ago.",
            "The Pyramids of Giza in Egypt were built around 2560–2540 BC.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD."
        ],
        "quiz_questions": [
            {
                "question": "What was the name of the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "Benjamin Franklin"],
                "answer": "George Washington"
            },
            {
                "question": "In what year did the American Civil War begin?",
                "options": ["1861", "1776", "1945", "1917"],
                "answer": "1861"
            },
            {
                "question": "What was the name of the ancient Greek philosopher who is considered the father of modern philosophy?",
                "options": ["Plato", "Socrates", "Aristotle", "Pythagoras"],
                "answer": "Socrates"
            }
        ]
    },
    "general": {
        "facts": [
            "The tallest mammal is the giraffe.",
            "The largest ocean on Earth is the Pacific Ocean.",
            "The Mona Lisa is a painting by the Italian Renaissance artist Leonardo da Vinci."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Earth", "Mars", "Jupiter", "Saturn"],
                "answer": "Jupiter"
            },
            {
                "question": "What is the name of the currency used in Japan?",
                "options": ["Euro", "Dollar", "Yen", "Pound"],
                "answer": "Yen"
            },
            {
                "question": "What is the name of the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the selected topic.
    """
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    """
    Retrieves a random quiz question and its options from the selected topic.
    """
    quiz_question = random.choice(topics[topic]["quiz_questions"])
    return quiz_question

def run_quiz(topic):
    """
    Runs a quiz for the selected topic.
    """
    quiz_question = get_quiz_question(topic)
    print(f"Question: {quiz_question['question']}")
    for i, option in enumerate(quiz_question['options']):
        print(f"{i+1}. {option}")
    
    user_answer = input("Enter the number of your answer: ")
    if quiz_question['options'][int(user_answer) - 1] == quiz_question['answer']:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_question['answer'])

def main():
    """
    Main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
