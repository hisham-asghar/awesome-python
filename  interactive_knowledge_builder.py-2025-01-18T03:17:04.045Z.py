
import random
import requests
import json

# Define the topics and their associated facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The first moon landing was in 1969 by the Apollo 11 mission.",
            "Photosynthesis is the process by which plants convert sunlight into energy."
        ],
        "quiz_questions": [
            {
                "question": "What is the main gas produced by plants during photosynthesis?",
                "options": ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"],
                "answer": 0
            },
            {
                "question": "What is the name of the first manned mission to land on the moon?",
                "options": ["Apollo 8", "Apollo 11", "Apollo 13", "Gemini 7"],
                "answer": 1
            },
            {
                "question": "How many miles of blood vessels are in the human body?",
                "options": ["10,000", "30,000", "60,000", "100,000"],
                "answer": 2
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer virus was created in 1983 and was called the 'Brain' virus.",
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The first smartphone was the IBM Simon, released in 1992."
        ],
        "quiz_questions": [
            {
                "question": "What was the name of the first computer virus?",
                "options": ["Brain", "ILOVEYOU", "WannaCry", "Stuxnet"],
                "answer": 0
            },
            {
                "question": "What year was the first commercial computer, the UNIVAC I, delivered?",
                "options": ["1945", "1951", "1962", "1975"],
                "answer": 1
            },
            {
                "question": "What was the name of the first smartphone?",
                "options": ["iPhone", "BlackBerry", "Android", "IBM Simon"],
                "answer": 3
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza in Egypt were built around 2560–2540 BC.",
            "The Magna Carta, a document that limited the power of the English monarch, was signed in 1215."
        ],
        "quiz_questions": [
            {
                "question": "Approximately how long is the Great Wall of China?",
                "options": ["5,000 miles", "10,000 miles", "13,000 miles", "20,000 miles"],
                "answer": 2
            },
            {
                "question": "Around what year were the Pyramids of Giza built?",
                "options": ["2000 BC", "2500 BC", "3000 BC", "3500 BC"],
                "answer": 1
            },
            {
                "question": "In what year was the Magna Carta signed?",
                "options": ["1215", "1492", "1776", "1945"],
                "answer": 0
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The largest continent in the world is Asia, covering about 17,212,000 square miles.",
            "The tallest mammal in the world is the giraffe, which can grow up to 20 feet tall."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Liver", "Skin", "Brain"],
                "answer": 2
            },
            {
                "question": "What is the largest continent in the world?",
                "options": ["Africa", "North America", "South America", "Asia"],
                "answer": 3
            },
            {
                "question": "What is the tallest mammal in the world?",
                "options": ["Elephant", "Rhinoceros", "Hippopotamus", "Giraffe"],
                "answer": 3
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
    Retrieves a random quiz question from the selected topic.
    """
    question = random.choice(topics[topic]["quiz_questions"])
    return question["question"], question["options"], question["answer"]

def main():
    """
    The main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Select a topic to get started:")

    while True:
        for topic in topics:
            print(f"- {topic.capitalize()}")
        selected_topic = input("Enter a topic or 'quit' to exit: ").lower()

        if selected_topic == "quit":
            print("Goodbye!")
            break

        if selected_topic in topics:
            print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
            print(get_random_fact(selected_topic))

            print("\nNow, let's test your knowledge with a quiz!")
            question, options, answer = get_quiz_question(selected_topic)
            print(question)
            for i, option in enumerate(options):
                print(f"{i+1}. {option}")

            user_answer = int(input("Enter the number of your answer: "))
            if user_answer - 1 == answer:
                print("Correct!")
            else:
                print("Incorrect. The correct answer is:", options[answer])

            print("\nThanks for playing! Let's explore another topic.")
        else:
            print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
