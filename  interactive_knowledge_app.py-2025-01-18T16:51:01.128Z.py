
import random
import json
import requests

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Milky Way galaxy contains an estimated 100-400 billion stars.",
            "Bioluminescence is the production and emission of light by a living organism."
        ],
        "quiz_questions": [
            {
                "question": "What is the primary function of the human heart?",
                "options": ["To pump blood", "To filter waste", "To produce energy"],
                "answer": 0
            },
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Jupiter", "Saturn", "Mars"],
                "answer": 0
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
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The internet was initially created as a project of the U.S. Department of Defense.",
            "The first digital camera was invented in 1975 by Steven Sasson at Eastman Kodak."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "Python", "C++"],
                "answer": 1
            },
            {
                "question": "What is the name of the first successful mobile phone call made in 1973?",
                "options": ["Motorola DynaTAC 8000x", "Nokia 1100", "iPhone"],
                "answer": 0
            },
            {
                "question": "What is the name of the first web browser, created by Tim Berners-Lee?",
                "options": ["Mosaic", "Netscape Navigator", "WorldWideWeb"],
                "answer": 2
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza in Egypt were built around 2560-2540 BC.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD."
        ],
        "quiz_questions": [
            {
                "question": "What was the name of the first president of the United States?",
                "options": ["Abraham Lincoln", "George Washington", "Thomas Jefferson"],
                "answer": 1
            },
            {
                "question": "In what year did World War II end?",
                "options": ["1945", "1939", "1918"],
                "answer": 0
            },
            {
                "question": "What was the name of the ancient Greek philosopher who developed the concept of the atom?",
                "options": ["Socrates", "Plato", "Democritus"],
                "answer": 2
            }
        ]
    },
    "general": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal in the world is the giraffe.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean"],
                "answer": 2
            },
            {
                "question": "What is the name of the largest continent in the world?",
                "options": ["Asia", "Africa", "Europe"],
                "answer": 0
            },
            {
                "question": "What is the name of the largest mammal in the world?",
                "options": ["Elephant", "Blue Whale", "Hippopotamus"],
                "answer": 1
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
    Retrieves a random quiz question from the selected topic.
    """
    quiz_question = random.choice(topics[topic]["quiz_questions"])
    return quiz_question

def run_quiz(topic):
    """
    Runs a quiz for the selected topic.
    """
    quiz_question = get_quiz_question(topic)
    print(quiz_question["question"])
    for i, option in enumerate(quiz_question["options"]):
        print(f"{i+1}. {option}")
    
    user_answer = int(input("Enter the number of your answer: "))
    if user_answer - 1 == quiz_question["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_question["options"][quiz_question["answer"]])

def main():
    """
    Main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print("\nHere's a random fact about", selected_topic.capitalize() + ":")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
