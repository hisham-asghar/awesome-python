
import random
import requests
import json

# Define the topics and their respective facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "A single cloud can weigh more than 1 million pounds.",
            "The hottest temperature ever recorded on Earth was 154°F (68°C) in Death Valley, California."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the force that keeps planets in orbit around the Sun?",
                "options": ["Gravity", "Friction", "Centrifugal force", "Magnetism"],
                "answer": 0
            },
            {
                "question": "Which scientist is known for developing the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Galileo Galilei"],
                "answer": 1
            },
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Mars", "Jupiter", "Saturn", "Uranus"],
                "answer": 1
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 and had only one button.",
            "The first text message was sent on December 3, 1992, and said 'Merry Christmas'.",
            "The word 'robot' was first used in a 1920 science-fiction play called 'R.U.R.' (Rossum's Universal Robots)."
        ],
        "quiz_questions": [
            {
                "question": "What does the abbreviation 'CPU' stand for?",
                "options": ["Central Processing Unit", "Computer Power Unit", "Computerized Processing Unit", "Central Power Unit"],
                "answer": 0
            },
            {
                "question": "Which company is known for creating the first personal computer?",
                "options": ["Apple", "Microsoft", "IBM", "Hewlett-Packard"],
                "answer": 2
            },
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first electric traffic light was installed in Cleveland, Ohio, in 1914."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for building the pyramids?",
                "options": ["Mayans", "Incas", "Egyptians", "Aztecs"],
                "answer": 2
            },
            {
                "question": "What was the name of the first successful powered flight by the Wright brothers?",
                "options": ["The Flyer", "The Glider", "The Biplane", "The Monoplane"],
                "answer": 0
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "Benjamin Franklin"],
                "answer": 2
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "A group of porcupines is called a prickle.",
            "The first product to have a barcode was Wrigley's gum.",
            "The world's largest desert is Antarctica, not the Sahara."
        ],
        "quiz_questions": [
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
                "question": "What is the largest planet in our solar system?",
                "options": ["Mars", "Jupiter", "Saturn", "Uranus"],
                "answer": 1
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
    Retrieves a random quiz question and its options from the given topic.
    """
    quiz_questions = topics[topic]["quiz_questions"]
    question = random.choice(quiz_questions)
    return question

def run_quiz(topic):
    """
    Runs a quiz for the given topic.
    """
    question = get_quiz_question(topic)
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == question["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", question["options"][question["answer"]])

def main():
    """
    The main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.title()}")
    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic.title()}:")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Sorry, that's not a valid topic. Please try again.")

if __name__ == "__main__":
    main()
