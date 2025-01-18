
import random
import requests
import json

# Dictionary to store topic-specific facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has over 600 muscles.",
            "The Milky Way galaxy contains an estimated 100-400 billion stars.",
            "The first successful vaccine was developed by Edward Jenner in 1796 to prevent smallpox."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "Which scientist is credited with developing the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"],
                "answer": "Albert Einstein"
            },
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Mars", "Jupiter", "Saturn", "Uranus"],
                "answer": "Jupiter"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, was completed in 1946 and weighed 30 tons.",
            "The internet was created in 1969 as a project of the U.S. Department of Defense.",
            "The first mobile phone call was made by Martin Cooper of Motorola in 1973."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "Which technology company is known for its search engine and online services?",
                "options": ["Apple", "Microsoft", "Google", "Amazon"],
                "answer": "Google"
            },
            {
                "question": "What is the name of the first commercially successful web browser?",
                "options": ["Internet Explorer", "Mozilla Firefox", "Google Chrome", "Netscape Navigator"],
                "answer": "Netscape Navigator"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza in Egypt is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Roman Empire lasted from 27 BC to 476 AD, a period of over 400 years.",
            "The first successful powered flight was made by the Wright brothers in 1903."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Egyptians", "Greeks", "Chinese", "Mayans"],
                "answer": "Greeks"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "John Adams"],
                "answer": "George Washington"
            },
            {
                "question": "What was the name of the first successful manned space mission?",
                "options": ["Apollo 11", "Sputnik 1", "Vostok 1", "Mercury-Redstone 3"],
                "answer": "Vostok 1"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The largest desert in the world is Antarctica."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "Who wrote the famous novel 'To Kill a Mockingbird'?",
                "options": ["Harper Lee", "Ernest Hemingway", "F. Scott Fitzgerald", "Maya Angelou"],
                "answer": "Harper Lee"
            },
            {
                "question": "Which country is known for the Eiffel Tower?",
                "options": ["Italy", "Germany", "France", "Spain"],
                "answer": "France"
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the specified topic.
    """
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    """
    Retrieves a random quiz question from the specified topic.
    """
    quiz_question = random.choice(topics[topic]["quiz_questions"])
    return quiz_question

def run_quiz(topic):
    """
    Runs a quiz for the specified topic.
    """
    quiz_question = get_quiz_question(topic)
    print(quiz_question["question"])
    for i, option in enumerate(quiz_question["options"]):
        print(f"{i+1}. {option}")

    user_answer = int(input("Enter your answer (1-4): "))
    if quiz_question["options"][user_answer-1] == quiz_question["answer"]:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {quiz_question['answer']}.")

def main():
    """
    Main function to run the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    print("1. Science")
    print("2. Technology")
    print("3. History")
    print("4. General Knowledge")

    topic_choice = int(input("Enter your choice (1-4): "))

    topic_names = ["science", "technology", "history", "general_knowledge"]
    topic = topic_names[topic_choice - 1]

    print(f"\nHere's a random fact about {topic.replace('_', ' ')}:")
    print(get_random_fact(topic))

    print("\nNow let's test your knowledge with a quiz!")
    run_quiz(topic)

if __name__ == "__main__":
    main()
