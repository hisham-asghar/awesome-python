
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The Earth is the only planet in our solar system with liquid water on its surface.",
            "The human body has around 60,000 miles of blood vessels.",
            "Bees can see ultraviolet light, which is invisible to the human eye."
        ],
        "quiz_questions": [
            {
                "question": "What is the primary function of the human heart?",
                "options": ["To pump blood", "To filter waste", "To produce energy", "To regulate body temperature"],
                "answer": 0
            },
            {
                "question": "Which of these is not a state of matter?",
                "options": ["Solid", "Liquid", "Gas", "Plasma"],
                "answer": 3
            },
            {
                "question": "What is the name of the theory that explains how living organisms evolve over time?",
                "options": ["Atomic theory", "Germ theory", "Gravitational theory", "Theory of evolution"],
                "answer": 3
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 and had only one button.",
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The internet was originally called ARPANET, and it was created by the U.S. Department of Defense in 1969."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "Which of these is not a type of computer memory?",
                "options": ["RAM", "ROM", "CPU", "SSD"],
                "answer": 2
            },
            {
                "question": "What is the name of the protocol that allows computers to communicate over the internet?",
                "options": ["HTTP", "HTTPS", "FTP", "TCP/IP"],
                "answer": 3
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.",
            "The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci between 1503 and 1519."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for its advanced engineering and architectural achievements?",
                "options": ["Mesopotamia", "Ancient Greece", "Ancient Rome", "Ancient Egypt"],
                "answer": 3
            },
            {
                "question": "What was the name of the famous explorer who discovered the Americas in 1492?",
                "options": ["Christopher Columbus", "Vasco da Gama", "Hernán Cortés", "Marco Polo"],
                "answer": 0
            },
            {
                "question": "Which event marked the end of World War II in Europe?",
                "options": ["D-Day", "The Battle of Stalingrad", "The Fall of Berlin", "The Atomic Bombings of Hiroshima and Nagasaki"],
                "answer": 2
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first person convicted of speeding was Walter Arnold of East Peckham, Kent, UK, in 1896. He was fined one shilling for driving at 8 mph (13 km/h), exceeding the 2 mph (3 km/h) speed limit."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Earth", "Mars", "Jupiter", "Saturn"],
                "answer": 2
            },
            {
                "question": "What is the name of the tallest mountain in the world?",
                "options": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
                "answer": 0
            },
            {
                "question": "Which country is known for the Taj Mahal?",
                "options": ["India", "China", "Egypt", "Italy"],
                "answer": 0
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
    return quiz_question["question"], quiz_question["options"], quiz_question["answer"]

def main():
    """
    Displays the main menu, allows the user to select a topic, and then provides a random fact and a quiz question.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))

        print("\nNow, let's test your knowledge with a quiz question:")
        question, options, answer = get_quiz_question(selected_topic)
        print(question)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

        user_answer = int(input("Enter the number of your answer: "))
        if user_answer - 1 == answer:
            print("Correct! You're a knowledge champion.")
        else:
            print("Oops, that's not the right answer. Better luck next time!")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
