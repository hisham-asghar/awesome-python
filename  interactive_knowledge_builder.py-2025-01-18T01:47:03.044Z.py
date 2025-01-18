
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The largest known prime number as of 2021 has 23 million digits.",
            "The first digital computer, the ENIAC, was completed in 1946."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the first digital computer?",
                "options": ["ENIAC", "UNIVAC", "MARK I", "COLOSSUS"],
                "answer": 0
            },
            {
                "question": "How many miles of blood vessels are in the human body?",
                "options": ["20,000 miles", "40,000 miles", "60,000 miles", "80,000 miles"],
                "answer": 2
            },
            {
                "question": "What is the largest known prime number as of 2021?",
                "options": ["10 million digits", "15 million digits", "20 million digits", "23 million digits"],
                "answer": 3
            }
        ]
    },
    "technology": {
        "facts": [
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The first computer mouse was invented by Douglas Engelbart in 1964.",
            "The first smartphone, the IBM Simon, was introduced in 1992."
        ],
        "quiz_questions": [
            {
                "question": "What year was the first commercial computer, the UNIVAC I, delivered?",
                "options": ["1945", "1951", "1955", "1960"],
                "answer": 1
            },
            {
                "question": "Who invented the first computer mouse?",
                "options": ["Steve Jobs", "Bill Gates", "Douglas Engelbart", "Tim Berners-Lee"],
                "answer": 2
            },
            {
                "question": "What year was the first smartphone, the IBM Simon, introduced?",
                "options": ["1985", "1992", "1998", "2007"],
                "answer": 1
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Magna Carta, a landmark document in English history, was signed in 1215.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers."
        ],
        "quiz_questions": [
            {
                "question": "When was the Magna Carta signed?",
                "options": ["1215", "1492", "1776", "1945"],
                "answer": 0
            },
            {
                "question": "What year did the Wright brothers make the first successful powered flight?",
                "options": ["1901", "1903", "1905", "1908"],
                "answer": 1
            },
            {
                "question": "Which is the oldest and largest of the three pyramids in the Giza pyramid complex?",
                "options": ["Great Pyramid of Giza", "Pyramid of Khafre", "Pyramid of Menkaure", "Sphinx"],
                "answer": 0
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first product to have a barcode was Wrigley's gum."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Liver", "Skin", "Brain"],
                "answer": 2
            },
            {
                "question": "What did the Mona Lisa not have?",
                "options": ["Nose", "Ears", "Eyebrows", "Smile"],
                "answer": 2
            },
            {
                "question": "What was the first product to have a barcode?",
                "options": ["Coca-Cola", "Bread", "Wrigley's gum", "Toilet paper"],
                "answer": 2
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
    num_questions = 3
    for _ in range(num_questions):
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
    print(f"Your final score: {score}/{num_questions}")

def main():
    """
    Main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge-Building Script!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")
    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in topics:
        print(f"Here's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nNow let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
