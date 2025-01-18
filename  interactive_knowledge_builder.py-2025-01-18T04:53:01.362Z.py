
import random
import requests
import json

# Define the topics and their corresponding facts and quizzes
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The largest known prime number as of 2021 has 23 million digits.",
            "The first commercial jet flight took place in 1952."
        ],
        "quizzes": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            },
            {
                "question": "Which scientist is known for the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Marie Curie", "Stephen Hawking"],
                "answer": 1
            },
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Mars", "Saturn", "Jupiter", "Uranus"],
                "answer": 2
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 and had only one button.",
            "The first commercial email was sent in 1971 by Ray Tomlinson.",
            "The first smartphone was the IBM Simon, released in 1992."
        ],
        "quizzes": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "Which company developed the first commercially successful graphical user interface (GUI)?",
                "options": ["Apple", "Microsoft", "IBM", "Xerox"],
                "answer": 3
            },
            {
                "question": "What is the name of the first web browser, developed at CERN in 1990?",
                "options": ["Mosaic", "Netscape Navigator", "Internet Explorer", "World Wide Web"],
                "answer": 3
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers."
        ],
        "quizzes": [
            {
                "question": "In what year did the American Civil War begin?",
                "options": ["1861", "1865", "1914", "1939"],
                "answer": 0
            },
            {
                "question": "Which ancient civilization is known for its pyramids?",
                "options": ["Greek", "Roman", "Egyptian", "Mayan"],
                "answer": 2
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "Franklin D. Roosevelt"],
                "answer": 2
            }
        ]
    },
    "general": {
        "facts": [
            "Butterflies taste with their feet.",
            "The average person walks the equivalent of 5 times around the world in their lifetime.",
            "The first product to have a barcode was Wrigley's gum."
        ],
        "quizzes": [
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Liver", "Skin", "Brain"],
                "answer": 2
            },
            {
                "question": "What is the tallest mammal in the world?",
                "options": ["Elephant", "Giraffe", "Hippopotamus", "Rhinoceros"],
                "answer": 1
            },
            {
                "question": "Which country is known as the 'Land of the Rising Sun'?",
                "options": ["China", "Japan", "India", "South Korea"],
                "answer": 1
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the specified topic.
    """
    return random.choice(topics[topic]["facts"])

def get_quiz(topic):
    """
    Retrieves a random quiz from the specified topic.
    """
    quiz = random.choice(topics[topic]["quizzes"])
    return quiz

def main():
    """
    The main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")

    chosen_topic = input("Enter your choice: ").lower()
    if chosen_topic not in topics:
        print("Invalid topic. Please try again.")
        return

    print(f"\nHere's a random fact about {chosen_topic.capitalize()}:")
    print(get_random_fact(chosen_topic))

    quiz = get_quiz(chosen_topic)
    print(f"\nNow, let's test your knowledge with a quiz!")
    print(quiz["question"])
    for i, option in enumerate(quiz["options"]):
        print(f"{i+1}. {option}")

    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == quiz["answer"]:
        print("Correct! You're a knowledge master.")
    else:
        print("Oops, that's not the right answer. Better luck next time.")

if __name__ == "__main__":
    main()
