
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 37.2 trillion cells.",
            "The first computer bug was a real moth found trapped in a Harvard Mark II computer.",
            "The hottest temperature ever recorded on Earth was 154°F (68°C) in Death Valley, California."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "Which scientist is known for the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Marie Curie"],
                "answer": "Albert Einstein"
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Respiration", "Photosynthesis", "Transpiration", "Fermentation"],
                "answer": "Photosynthesis"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, was completed in 1946 and weighed 30 tons.",
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The world's first webcam was created in 1991 to monitor the coffee pot at the University of Cambridge."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "What is the name of the first commercially successful personal computer?",
                "options": ["Apple II", "IBM PC", "Commodore 64", "Atari 800"],
                "answer": "IBM PC"
            },
            {
                "question": "What is the name of the company that created the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": "Google"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci.",
            "The Declaration of Independence was signed in 1776."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization built the Colosseum in Rome?",
                "options": ["Greeks", "Romans", "Egyptians", "Mayans"],
                "answer": "Romans"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "Benjamin Franklin"],
                "answer": "George Washington"
            },
            {
                "question": "Which event marked the beginning of World War I?",
                "options": ["The assassination of Archduke Franz Ferdinand", "The bombing of Pearl Harbor", "The fall of the Berlin Wall", "The Cuban Missile Crisis"],
                "answer": "The assassination of Archduke Franz Ferdinand"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "A 'jiffy' is an actual unit of time, equivalent to one-thousandth (1/1000) of a second.",
            "The word 'sandwich' is named after the 4th Earl of Sandwich, John Montagu."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": "AB"
            },
            {
                "question": "Who wrote the novel 'To Kill a Mockingbird'?",
                "options": ["Harper Lee", "Ernest Hemingway", "F. Scott Fitzgerald", "Maya Angelou"],
                "answer": "Harper Lee"
            }
        ]
    }
}

def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    return input("Enter your choice: ").lower()

def display_fact(topic):
    fact = random.choice(topics[topic]["facts"])
    print(f"Here's an interesting fact about {topic.capitalize()}:")
    print(f"- {fact}")

def run_quiz(topic):
    print(f"Let's test your {topic.capitalize()} knowledge!")
    score = 0
    questions = topics[topic]["quiz_questions"]
    for question in questions:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = input("Enter your answer (1-4): ")
        if question["options"][int(user_answer) - 1] == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score is {score} out of {len(questions)}.")

def main():
    topic = display_menu()
    display_fact(topic)
    run_quiz(topic)

if __name__ == "__main__":
    main()
