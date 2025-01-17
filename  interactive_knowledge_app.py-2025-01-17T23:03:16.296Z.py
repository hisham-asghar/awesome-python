Here is the raw Python code extracted from the JSON:

import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The largest known prime number as of 2022 has 23 million digits.",
            "Neutron stars are the collapsed cores of massive stars, with a density of about a trillion tons per cubic centimeter."
        ],
        "quiz": [
            {
                "question": "Which scientist is known for developing the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Galileo Galilei"],
                "answer": 1
            },
            {
                "question": "What is the name of the smallest particle in the universe?",
                "options": ["Atom", "Electron", "Quark", "Neutrino"],
                "answer": 2
            },
            {
                "question": "Which gas makes up the majority of the Earth's atmosphere?",
                "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Argon"],
                "answer": 1
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, weighed 30 tons and took up 1,800 square feet of floor space.",
            "The first commercial microprocessor was the Intel 4004, released in 1971.",
            "The internet was originally called ARPANET and was created by the U.S. Department of Defense in 1969."
        ],
        "quiz": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "Which company developed the first commercially successful smartphone?",
                "options": ["Apple", "Samsung", "BlackBerry", "Nokia"],
                "answer": 0
            },
            {
                "question": "What is the name of the first web browser created by Tim Berners-Lee?",
                "options": ["Mosaic", "Netscape Navigator", "Internet Explorer", "WorldWideWeb"],
                "answer": 3
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Roman Empire lasted for over 400 years, from the 1st century BC to the 5th century AD.",
            "The Mona Lisa was painted by the famous Italian artist Leonardo da Vinci in the early 16th century."
        ],
        "quiz": [
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Egyptians", "Greeks", "Mayans", "Chinese"],
                "answer": 1
            },
            {
                "question": "Which event marked the beginning of World War I?",
                "options": ["The assassination of Archduke Franz Ferdinand", "The bombing of Pearl Harbor", "The fall of the Berlin Wall", "The Cuban Missile Crisis"],
                "answer": 0
            },
            {
                "question": "Which famous explorer is credited with discovering the Americas?",
                "options": ["Christopher Columbus", "Vasco da Gama", "Ferdinand Magellan", "Marco Polo"],
                "answer": 0
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2022 has 23 million digits.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "A group of flamingos is called a flamboyance."
        ],
        "quiz": [
            {
                "question": "What is the tallest mammal in the world?",
                "options": ["Elephant", "Giraffe", "Rhinoceros", "Hippopotamus"],
                "answer": 1
            },
            {
                "question": "Which country is known as the 'Land of the Rising Sun'?",
                "options": ["China", "Japan", "South Korea", "India"],
                "answer": 1
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": 2
            }
        ]
    }
}

def interactive_knowledge_app():
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in topics:
        print(f"You selected the {selected_topic.capitalize()} topic.")
        print("Here's a random fact:")
        print(random.choice(topics[selected_topic]["facts"]))

        print("\nTime for a quiz! Answer the following multiple-choice questions:")
        score = 0
        for quiz_question in topics[selected_topic]["quiz"]:
            print(quiz_question["question"])
            for i, option in enumerate(quiz_question["options"]):
                print(f"{i+1}. {option}")
            user_answer = int(input("Enter your answer (1-4): "))
            if user_answer == quiz_question["answer"] + 1:
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")
        print(f"Your final score is {score} out of {len(topics[selected_topic]['quiz'])}")
    else:
        print("Invalid topic. Please try again.")

interactive_knowledge_app()