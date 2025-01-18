Here is the raw Python code extracted from the JSON:

```python
import random
import json
import requests

# Define the topics and their associated facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human brain has approximately 86 billion neurons.",
            "The largest known prime number as of 2022 has 23 million digits.",
            "Neutron stars are the collapsed cores of massive stars that can be as dense as an atomic nucleus."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            },
            {
                "question": "What is the process by which plants convert light energy into chemical energy?",
                "options": ["Photosynthesis", "Respiration", "Evaporation", "Transpiration"],
                "answer": 0
            },
            {
                "question": "What is the name of the force that keeps objects in orbit around a larger object?",
                "options": ["Gravity", "Friction", "Centrifugal force", "Inertia"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, was completed in 1946 and weighed 30 tons.",
            "The first commercial microprocessor, the Intel 4004, was released in 1971 and had 2,300 transistors.",
            "The world's first website was launched in 1991 and was about the World Wide Web project itself."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "What is the name of the protocol used for sending and receiving email?",
                "options": ["HTTP", "SMTP", "FTP", "DNS"],
                "answer": 1
            },
            {
                "question": "What is the name of the data structure used to store key-value pairs?",
                "options": ["List", "Tuple", "Dictionary", "Set"],
                "answer": 2
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers."
        ],
        "quiz_questions": [
            {
                "question": "What year was the Declaration of Independence signed?",
                "options": ["1776", "1789", "1812", "1865"],
                "answer": 0
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "Franklin D. Roosevelt"],
                "answer": 2
            },
            {
                "question": "What was the name of the ancient Greek city-state known for its democracy?",
                "options": ["Sparta", "Athens", "Corinth", "Thebes"],
                "answer": 1
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.",
            "The largest ocean on Earth is the Pacific Ocean, covering an area of about 63 million square miles."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Earth", "Mars", "Jupiter", "Saturn"],
                "answer": 2
            },
            {
                "question": "What is the currency used in Japan?",
                "options": ["Dollar", "Euro", "Yen", "Pound"],
                "answer": 2
            },
            {
                "question": "What is the name of the largest river in the world?",
                "options": ["Amazon", "Nile", "Mississippi", "Yangtze"],
                "answer": 1
            }
        ]
    }
}

def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")
    return input("Enter your choice: ").lower()

def display_fact(topic):
    fact = random.choice(topics[topic]["facts"])
    print(f"Here's an interesting fact about {topic.capitalize()}:")
    print(fact)

def quiz(topic):
    print(f"Let's test your {topic.capitalize()} knowledge!")
    score = 0
    questions = topics[topic]["quiz_questions"]
    for question in questions:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer - 1 == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score is {score} out of {len(questions)}.")

def main():
    topic = display_menu()
    display_fact(topic)
    quiz(topic)

if __name__ == "__main__":
    main()
