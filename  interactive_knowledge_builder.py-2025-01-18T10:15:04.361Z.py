
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The largest known prime number as of 2023 has 23 million digits.",
            "The human body has around 60,000 miles of blood vessels.",
            "The first digital computer, the ENIAC, was completed in 1946 and weighed 30 tons."
        ],
        "quiz": [
            {
                "question": "What is the name of the largest known prime number as of 2023?",
                "options": ["23 million digits", "1 million digits", "100,000 digits", "10,000 digits"],
                "answer": 0
            },
            {
                "question": "Approximately how many miles of blood vessels are in the human body?",
                "options": ["10,000 miles", "30,000 miles", "60,000 miles", "100,000 miles"],
                "answer": 2
            },
            {
                "question": "In what year was the first digital computer, the ENIAC, completed?",
                "options": ["1936", "1946", "1956", "1966"],
                "answer": 1
            }
        ]
    },
    "technology": {
        "facts": [
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The first mobile phone call was made in 1973 by Martin Cooper of Motorola.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989."
        ],
        "quiz": [
            {
                "question": "What was the name of the first commercial computer?",
                "options": ["ENIAC", "UNIVAC I", "Apple I", "IBM 5100"],
                "answer": 1
            },
            {
                "question": "In what year was the first mobile phone call made?",
                "options": ["1963", "1973", "1983", "1993"],
                "answer": 1
            },
            {
                "question": "Who invented the World Wide Web?",
                "options": ["Steve Jobs", "Bill Gates", "Linus Torvalds", "Tim Berners-Lee"],
                "answer": 3
            }
        ]
    },
    "history": {
        "facts": [
            "The Pyramids of Giza were built around 2560–2540 BC.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.",
            "The first successful powered flight by the Wright brothers took place in 1903."
        ],
        "quiz": [
            {
                "question": "Around what years were the Pyramids of Giza built?",
                "options": ["3000-2800 BC", "2800-2600 BC", "2560-2540 BC", "2400-2200 BC"],
                "answer": 2
            },
            {
                "question": "How long did the Roman Empire last?",
                "options": ["200 years", "400 years", "600 years", "800 years"],
                "answer": 1
            },
            {
                "question": "In what year did the Wright brothers' first successful powered flight take place?",
                "options": ["1893", "1903", "1913", "1923"],
                "answer": 1
            }
        ]
    },
    "general": {
        "facts": [
            "The longest word in the English language is 'pneumonoultramicroscopicsilicovolcanoconiosis'.",
            "The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.",
            "The largest ocean on Earth is the Pacific Ocean, which covers an area of about 63 million square miles."
        ],
        "quiz": [
            {
                "question": "What is the longest word in the English language?",
                "options": ["Supercalifragilisticexpialidocious", "Antidisestablishmentarianism", "Pneumonoultramicroscopicsilicovolcanoconiosis", "Hippopotomonstrosesquippedaliophobia"],
                "answer": 2
            },
            {
                "question": "What is the tallest mammal?",
                "options": ["Elephant", "Giraffe", "Moose", "Rhinoceros"],
                "answer": 1
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the selected topic.
    """
    facts = topics[topic]["facts"]
    return random.choice(facts)

def get_quiz_question(topic):
    """
    Retrieves a random quiz question and its options from the selected topic.
    """
    quiz_questions = topics[topic]["quiz"]
    question = random.choice(quiz_questions)
    return question["question"], question["options"], question["answer"]

def main():
    """
    The main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge-Building Script!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()
    if selected_topic not in topics:
        print("Invalid topic. Please try again.")
        return

    print(f"\nYou selected the {selected_topic.capitalize()} topic.")
    print(get_random_fact(selected_topic))
    print("\nNow, let's test your knowledge with a quiz!")

    question, options, answer = get_quiz_question(selected_topic)
    print(question)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")

    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == answer:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", options[answer])

if __name__ == "__main__":
    main()
