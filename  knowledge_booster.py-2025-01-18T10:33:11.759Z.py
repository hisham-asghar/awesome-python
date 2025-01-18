Here is the raw Python code extracted from the JSON:

```python
import random
import json
import requests

# Define the topics and their respective facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has over 600 muscles.",
            "The Earth is the only planet in our solar system with liquid water on its surface.",
            "Bioluminescence is the production and emission of light by a living organism."
        ],
        "quiz_questions": [
            {
                "question": "What is the primary function of the human heart?",
                "options": ["To pump blood", "To generate energy", "To filter waste"],
                "answer": 0
            },
            {
                "question": "Which of these is a renewable energy source?",
                "options": ["Coal", "Oil", "Solar"],
                "answer": 2
            },
            {
                "question": "What is the name of the process where plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Fermentation"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer virus was created in 1983 and was called the 'Elk Cloner'.",
            "The first mobile phone call was made on April 3, 1973 by Martin Cooper of Motorola.",
            "The world's first electronic computer, ENIAC, was completed in 1946 and occupied a 30-by-50-foot room."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python"],
                "answer": 2
            },
            {
                "question": "What is the primary function of a microprocessor?",
                "options": ["To store data", "To process data", "To generate power"],
                "answer": 1
            },
            {
                "question": "Which of these is a type of computer memory?",
                "options": ["RAM", "CPU", "Motherboard"],
                "answer": 0
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The first Olympic Games were held in 776 BC in Olympia, Greece.",
            "The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Mesopotamia", "Egypt", "India"],
                "answer": 0
            },
            {
                "question": "What was the name of the first successful powered flight, conducted by the Wright brothers?",
                "options": ["The Flyer", "The Glider", "The Biplane"],
                "answer": 0
            },
            {
                "question": "Which event marked the end of World War II?",
                "options": ["D-Day", "The Holocaust", "The atomic bombings of Hiroshima and Nagasaki"],
                "answer": 2
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal is the giraffe.",
            "The Great Wall of China is the longest man-made structure in the world."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Pacific Ocean", "Indian Ocean"],
                "answer": 1
            },
            {
                "question": "Which country is known as the 'Land of the Rising Sun'?",
                "options": ["China", "Japan", "Korea"],
                "answer": 1
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB-"],
                "answer": 2
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
    print(f"Did you know? {fact}")

def run_quiz(topic):
    score = 0
    for question in topics[topic]["quiz_questions"]:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-3): ")) - 1
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score is {score} out of {len(topics[topic]['quiz_questions'])}")

def main():
    topic = display_menu()
    display_fact(topic)
    run_quiz(topic)

if __name__ == "__main__":
    main()
