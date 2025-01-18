
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "Antarctica is the coldest, driest, and windiest continent.",
            "The largest known prime number as of 2022 has 23 million digits."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            },
            {
                "question": "Which scientist is known for the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Galileo Galilei"],
                "answer": 1
            },
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Liver", "Skin", "Lungs"],
                "answer": 2
            }
        ]
    },
    "technology": {
        "facts": [
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The world's first webcam was used to monitor a coffee pot at the University of Cambridge.",
            "The first smartphone was the IBM Simon, released in 1992."
        ],
        "quiz_questions": [
            {
                "question": "What does 'CPU' stand for?",
                "options": ["Central Processing Unit", "Computer Power Unit", "Compact Processing Unit", "Computational Power Unit"],
                "answer": 0
            },
            {
                "question": "Which company developed the first graphical user interface (GUI)?",
                "options": ["Apple", "Microsoft", "Xerox", "IBM"],
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
            "The first commercial airplane flight took place on January 1, 1914, between St. Petersburg and Tampa, Florida."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for building the pyramids?",
                "options": ["Mesopotamia", "Indus Valley", "Ancient Greece", "Ancient Egypt"],
                "answer": 3
            },
            {
                "question": "What year did the United States declare independence?",
                "options": ["1776", "1789", "1812", "1865"],
                "answer": 0
            },
            {
                "question": "Which event is known as the 'turning point' of World War II?",
                "options": ["D-Day", "Battle of Stalingrad", "Pearl Harbor", "Atomic bombings of Hiroshima and Nagasaki"],
                "answer": 1
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The Eiffel Tower can be 15 cm taller during the summer, as the hot weather causes the iron to expand.",
            "A group of porcupines is called a prickle.",
            "The first product to have a barcode was Wrigley's gum."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "What is the tallest mammal in the world?",
                "options": ["Elephant", "Giraffe", "Rhinoceros", "Hippopotamus"],
                "answer": 1
            },
            {
                "question": "Which country is known as the 'Land of the Rising Sun'?",
                "options": ["China", "Japan", "South Korea", "Thailand"],
                "answer": 1
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the specified topic.
    """
    facts = topics[topic]["facts"]
    return random.choice(facts)

def get_quiz_question(topic):
    """
    Retrieves a random quiz question and its options from the specified topic.
    """
    quiz_questions = topics[topic]["quiz_questions"]
    question = random.choice(quiz_questions)
    return question["question"], question["options"], question["answer"]

def run_quiz(topic):
    """
    Runs a quiz for the specified topic.
    """
    score = 0
    for _ in range(3):
        question, options, answer = get_quiz_question(topic)
        print(question)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer - 1 == answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score is {score}/3.")

def main():
    """
    Runs the interactive knowledge-building program.
    """
    print("Welcome to the Interactive Knowledge-Building Program!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")
    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in topics:
        print(f"You have selected the '{selected_topic.capitalize()}' topic.")
        print(get_random_fact(selected_topic))
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
