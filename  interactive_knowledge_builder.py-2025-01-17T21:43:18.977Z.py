Here is the raw Python code extracted from the JSON:

```python
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has over 600 muscles.",
            "The largest known prime number as of 2022 has over 23 million digits.",
            "The first successful kidney transplant was performed in 1954."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "What is the process of converting light energy into chemical energy called?",
                "options": ["Photosynthesis", "Respiration", "Combustion", "Evaporation"],
                "answer": "Photosynthesis"
            },
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Mars", "Saturn", "Jupiter", "Neptune"],
                "answer": "Jupiter"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first programmable computer was the ENIAC, completed in 1946.",
            "The internet was originally called ARPANET, and was created in 1969.",
            "The first smartphone was the IBM Simon, released in 1992."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "What is the name of the company that created the first commercially successful web browser?",
                "options": ["Microsoft", "Apple", "Google", "Netscape"],
                "answer": "Netscape"
            },
            {
                "question": "What is the name of the first digital computer, built in 1936?",
                "options": ["ENIAC", "UNIVAC", "MARK I", "Z1"],
                "answer": "Z1"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza were built around 2560–2540 BC, and are the oldest and largest of the three main pyramids.",
            "The first successful powered flight was made by the Wright brothers in 1903."
        ],
        "quiz_questions": [
            {
                "question": "What year did the American Civil War begin?",
                "options": ["1861", "1865", "1914", "1939"],
                "answer": "1861"
            },
            {
                "question": "What was the name of the first successful voyage around the world?",
                "options": ["Columbus's voyage", "Magellan's voyage", "Drake's voyage", "Cook's voyage"],
                "answer": "Magellan's voyage"
            },
            {
                "question": "What was the name of the ancient Egyptian queen who ruled from 69 to 30 BC?",
                "options": ["Nefertiti", "Cleopatra", "Hatshepsut", "Neferkare"],
                "answer": "Cleopatra"
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2022 has over 23 million digits.",
            "The first successful kidney transplant was performed in 1954.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Mars", "Saturn", "Jupiter", "Neptune"],
                "answer": "Jupiter"
            },
            {
                "question": "What is the name of the longest river in the world?",
                "options": ["Amazon", "Nile", "Mississippi-Missouri", "Yangtze"],
                "answer": "Nile"
            },
            {
                "question": "What is the name of the tallest mountain in the world?",
                "options": ["K2", "Everest", "Kangchenjunga", "Lhotse"],
                "answer": "Everest"
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the given topic.
    """
    facts = topics[topic]["facts"]
    return random.choice(facts)

def get_quiz_question(topic):
    """
    Retrieves a random quiz question from the given topic.
    """
    quiz_questions = topics[topic]["quiz_questions"]
    question = random.choice(quiz_questions)
    return question

def run_quiz(topic):
    """
    Runs a quiz for the given topic.
    """
    question = get_quiz_question(topic)
    print(f"Question: {question['question']}")
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    
    while True:
        user_answer = input("Enter your answer (1-4): ")
        if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
            if question["options"][int(user_answer)-1] == question["answer"]:
                print("Correct!")
                return
            else:
                print("Incorrect. Please try again.")
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

def main():
    """
    Main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge-Building Script!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    while True:
        user_topic = input("Enter your topic choice: ").lower()
        if user_topic in topics:
            print(f"Here's a random fact about {user_topic.capitalize()}:")
            print(get_random_fact(user_topic))
            print("\nNow, let's test your knowledge with a quiz!")
            run_quiz(user_topic)
            break
        else:
            print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
