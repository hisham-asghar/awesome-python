
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Milky Way galaxy contains an estimated 100-400 billion stars.",
            "Honey is the only food that does not spoil."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical formula for water?",
                "options": ["H2O", "CO2", "NaCl", "O2"],
                "answer": 0
            },
            {
                "question": "Which scientist is famous for the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"],
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
            "The first computer mouse was invented in 1964 and had only one button.",
            "The first text message was sent on December 3, 1992, and said 'Merry Christmas'.",
            "The first commercial smartphone was the IBM Simon, released in 1992."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the operating system developed by Apple?",
                "options": ["Windows", "Linux", "macOS", "Android"],
                "answer": 2
            },
            {
                "question": "Which company is responsible for the development of the World Wide Web?",
                "options": ["Microsoft", "Apple", "Google", "CERN"],
                "answer": 3
            },
            {
                "question": "What is the name of the programming language used to create websites?",
                "options": ["Java", "Python", "C++", "HTML"],
                "answer": 3
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
                "question": "What was the name of the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "Benjamin Franklin"],
                "answer": 2
            },
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Mesopotamia", "Ancient Egypt", "Ancient Greece", "Ancient China"],
                "answer": 2
            },
            {
                "question": "What was the name of the war that lasted from 1939 to 1945?",
                "options": ["World War I", "World War II", "Vietnam War", "Korean War"],
                "answer": 1
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.",
            "The largest known prime number as of 2022 has 23 million digits.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "Who wrote the famous novel 'To Kill a Mockingbird'?",
                "options": ["Harper Lee", "Ernest Hemingway", "Maya Angelou", "F. Scott Fitzgerald"],
                "answer": 0
            },
            {
                "question": "What is the national animal of Canada?",
                "options": ["Beaver", "Moose", "Polar Bear", "Caribou"],
                "answer": 0
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
    return question

def run_quiz(topic):
    """
    Runs a quiz for the specified topic, allowing the user to answer multiple-choice questions.
    """
    score = 0
    num_questions = 3
    for i in range(num_questions):
        question = get_quiz_question(topic)
        print(f"Question {i+1}: {question['question']}")
        for j, option in enumerate(question["options"]):
            print(f"{j+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): ")) - 1
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score is {score}/{num_questions}")

def main():
    """
    Displays a menu for the user to select a topic, and then runs the corresponding quiz.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Select a topic:")
    for topic in topics:
        print(f"{topic.capitalize()}")
    chosen_topic = input("Enter your choice: ").lower()
    if chosen_topic in topics:
        print(f"Here's a random fact about {chosen_topic.capitalize()}:")
        print(get_random_fact(chosen_topic))
        print("\nNow, let's test your knowledge!")
        run_quiz(chosen_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
