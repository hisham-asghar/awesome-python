
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 100 trillion cells.",
            "The largest known prime number as of 2023 has 23 million digits.",
            "The first successful organ transplant was a kidney transplant performed in 1954."
        ],
        "quiz": [
            {
                "question": "What is the fastest-growing organ in the human body?",
                "choices": ["Brain", "Liver", "Skin", "Heart"],
                "answer": "Liver"
            },
            {
                "question": "What is the rarest blood type?",
                "choices": ["A", "B", "AB", "O"],
                "answer": "AB-"
            },
            {
                "question": "Which scientist is credited with developing the theory of relativity?",
                "choices": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Galileo Galilei"],
                "answer": "Albert Einstein"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The first commercial jet airliner was the de Havilland Comet, which entered service in 1952.",
            "The first programmable computer was the ENIAC, which was completed in 1946."
        ],
        "quiz": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "choices": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "What is the name of the first website ever created?",
                "choices": ["Google.com", "Yahoo.com", "Amazon.com", "http://info.cern.ch"],
                "answer": "http://info.cern.ch"
            },
            {
                "question": "What is the name of the first social media platform?",
                "choices": ["Facebook", "Twitter", "MySpace", "Friendster"],
                "answer": "Friendster"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci.",
            "The Roman Empire lasted for over 1,000 years, from the 8th century BC to the 5th century AD."
        ],
        "quiz": [
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "choices": ["Egyptians", "Greeks", "Mayans", "Babylonians"],
                "answer": "Babylonians"
            },
            {
                "question": "Which European country was the first to establish permanent colonies in the Americas?",
                "choices": ["Spain", "Portugal", "England", "France"],
                "answer": "Spain"
            },
            {
                "question": "Which event is considered the start of the Industrial Revolution?",
                "choices": ["The invention of the steam engine", "The discovery of electricity", "The creation of the first factory", "The development of the telegraph"],
                "answer": "The invention of the steam engine"
            }
        ]
    },
    "general": {
        "facts": [
            "The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands and raises the structure.",
            "A group of flamingos is called a flamboyance.",
            "The largest known prime number as of 2023 has 23 million digits."
        ],
        "quiz": [
            {
                "question": "What is the largest ocean on Earth?",
                "choices": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "Which country has the most natural lakes?",
                "choices": ["Canada", "Russia", "United States", "Brazil"],
                "answer": "Canada"
            },
            {
                "question": "What is the rarest blood type?",
                "choices": ["A", "B", "AB", "O"],
                "answer": "AB-"
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
    Retrieves a random quiz question and its choices from the specified topic.
    """
    quiz_questions = topics[topic]["quiz"]
    question = random.choice(quiz_questions)
    return question

def run_quiz(topic):
    """
    Runs a quiz for the specified topic.
    """
    question = get_quiz_question(topic)
    print(f"Question: {question['question']}")
    for i, choice in enumerate(question["choices"], start=1):
        print(f"{i}. {choice}")

    user_answer = input("Enter your answer (1-4): ")
    if user_answer.isdigit() and 1 <= int(user_answer) <= 4 and question["choices"][int(user_answer) - 1] == question["answer"]:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {question['answer']}")

def main():
    """
    Main function that displays the menu and runs the interactive knowledge session.
    """
    print("Welcome to the Interactive Knowledge Session!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()
    if selected_topic not in topics:
        print("Invalid topic. Please try again.")
        return

    print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
    print(get_random_fact(selected_topic))
    print("\nNow, let's test your knowledge with a quiz!")
    run_quiz(selected_topic)

if __name__ == "__main__":
    main()
