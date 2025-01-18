Here is the raw Python code extracted from the JSON:

import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The first person to suggest that the Earth orbits the Sun was Galileo Galilei.",
            "Bioluminescence is the production and emission of light by a living organism."
        ],
        "quizzes": [
            {
                "question": "What is the primary function of the human heart?",
                "options": ["To pump blood", "To filter waste", "To produce energy"],
                "answer": 0
            },
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Mars", "Jupiter", "Saturn"],
                "answer": 1
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented by Douglas Engelbart in 1964.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989.",
            "The first commercial smartphone was the IBM Simon, released in 1992."
        ],
        "quizzes": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "Python", "C++"],
                "answer": 1
            },
            {
                "question": "Which of these is not a type of computer memory?",
                "options": ["RAM", "ROM", "GPU"],
                "answer": 2
            },
            {
                "question": "What is the name of the first successful search engine?",
                "options": ["Google", "Yahoo", "AltaVista"],
                "answer": 2
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza in Egypt were built around 2560–2540 BC.",
            "The Magna Carta, one of the most influential legal documents in history, was signed in 1215."
        ],
        "quizzes": [
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Egyptians", "Greeks", "Mayans"],
                "answer": 1
            },
            {
                "question": "What was the name of the first emperor of the Roman Empire?",
                "options": ["Julius Caesar", "Augustus", "Nero"],
                "answer": 1
            },
            {
                "question": "Which event marked the end of the Middle Ages in Europe?",
                "options": ["The Renaissance", "The Crusades", "The Fall of Constantinople"],
                "answer": 2
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The longest word in the English language is 'pneumonoultramicroscopicsilicovolcanoconiosis'.",
            "The tallest mammal in the world is the giraffe."
        ],
        "quizzes": [
            {
                "question": "What is the name of the currency used in Japan?",
                "options": ["Yen", "Won", "Peso"],
                "answer": 0
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean"],
                "answer": 2
            },
            {
                "question": "Who is credited with inventing the telephone?",
                "options": ["Thomas Edison", "Alexander Graham Bell", "Nikola Tesla"],
                "answer": 1
            }
        ]
    }
}

def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

def get_random_fact(topic):
    facts = topics[topic]["facts"]
    return random.choice(facts)

def get_quiz_question(topic):
    quizzes = topics[topic]["quizzes"]
    quiz = random.choice(quizzes)
    return quiz

def run_quiz(quiz):
    print(quiz["question"])
    for i, option in enumerate(quiz["options"]):
        print(f"{i+1}. {option}")
    user_answer = int(input("Enter your answer (1-3): ")) - 1
    if user_answer == quiz["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz["options"][quiz["answer"]])

def main():
    display_menu()
    topic = input("Enter your topic choice: ").lower()
    if topic in topics:
        print(get_random_fact(topic))
        quiz = get_quiz_question(topic)
        run_quiz(quiz)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()