
import random
import requests
import json

# Define the topics and their corresponding facts and quizzes
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The largest known prime number as of 2022 has 23 million digits.",
            "The first successful kidney transplant was performed in 1954."
        ],
        "quizzes": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "Which scientist is known for the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Marie Curie", "Galileo Galilei"],
                "answer": "Albert Einstein"
            },
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Mars", "Saturn", "Jupiter", "Neptune"],
                "answer": "Jupiter"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The first commercial text message was sent on December 3, 1992.",
            "The world's first webcam was used to monitor a coffee pot at the University of Cambridge in 1991."
        ],
        "quizzes": [
            {
                "question": "What does 'HTML' stand for?",
                "options": ["Hyper Text Markup Language", "Hyperlink Text Markup Language", "Hyper Text Markup Linking", "Hyper Text Machine Language"],
                "answer": "Hyper Text Markup Language"
            },
            {
                "question": "Which company developed the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": "Google"
            },
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The first Olympic Games were held in 776 BC in Olympia, Greece.",
            "The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci."
        ],
        "quizzes": [
            {
                "question": "In which year did the American Civil War begin?",
                "options": ["1861", "1865", "1775", "1914"],
                "answer": "1861"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "John Adams"],
                "answer": "George Washington"
            },
            {
                "question": "Which ancient civilization built the pyramids in Giza?",
                "options": ["Mesopotamian", "Aztec", "Egyptian", "Roman"],
                "answer": "Egyptian"
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2022 has 23 million digits.",
            "The world's largest desert is Antarctica, which is a desert because of its low precipitation.",
            "The first commercial jet flight took place in 1952 with the de Havilland Comet."
        ],
        "quizzes": [
            {
                "question": "What is the tallest mammal in the world?",
                "options": ["Elephant", "Giraffe", "Rhinoceros", "Hippopotamus"],
                "answer": "Giraffe"
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "Which country is known as the 'Land of the Rising Sun'?",
                "options": ["China", "Japan", "South Korea", "India"],
                "answer": "Japan"
            }
        ]
    }
}

def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    return input("Enter your choice: ").lower()

def display_fact(topic):
    fact = random.choice(topics[topic]["facts"])
    print(f"\nFact about {topic.capitalize()}:")
    print(fact)

def display_quiz(topic):
    quiz = random.choice(topics[topic]["quizzes"])
    print(f"\nQuiz about {topic.capitalize()}:")
    print(quiz["question"])
    for i, option in enumerate(quiz["options"], start=1):
        print(f"{i}. {option}")
    user_answer = input("Enter your answer (1-4): ")
    if quiz["options"][int(user_answer) - 1] == quiz["answer"]:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {quiz['answer']}")

def main():
    topic = display_menu()
    display_fact(topic)
    display_quiz(topic)

if __name__ == "__main__":
    main()
