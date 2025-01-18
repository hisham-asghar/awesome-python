
import random
import requests
import json

# Dictionary to store topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest planet in the solar system is Venus, not Mercury.",
            "The largest known prime number as of 2022 has over 23 million digits."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the largest known prime number as of 2022?",
                "options": ["23 million digits", "10 million digits", "100 million digits", "1 billion digits"],
                "answer": 0
            },
            {
                "question": "Which planet in the solar system is the hottest?",
                "options": ["Mercury", "Venus", "Earth", "Mars"],
                "answer": 1
            },
            {
                "question": "Approximately how many miles of blood vessels are there in the human body?",
                "options": ["10,000 miles", "30,000 miles", "60,000 miles", "100,000 miles"],
                "answer": 2
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer virus, called 'Creeper', was created in 1971 as an experiment.",
            "The first commercial text message was sent on December 3, 1992.",
            "The world's first website was launched on August 6, 1991."
        ],
        "quiz_questions": [
            {
                "question": "What was the name of the first computer virus?",
                "options": ["Creeper", "Trojan", "Worm", "Malware"],
                "answer": 0
            },
            {
                "question": "When was the first commercial text message sent?",
                "options": ["1980", "1992", "2000", "2010"],
                "answer": 1
            },
            {
                "question": "When was the world's first website launched?",
                "options": ["1980", "1985", "1991", "1995"],
                "answer": 2
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first known computer programmer was Ada Lovelace, a 19th-century English mathematician."
        ],
        "quiz_questions": [
            {
                "question": "How long is the Great Wall of China?",
                "options": ["5,000 miles", "10,000 miles", "13,000 miles", "20,000 miles"],
                "answer": 2
            },
            {
                "question": "Why does the Mona Lisa have no eyebrows?",
                "options": ["It was the fashion in Renaissance Florence to shave them off.",
                           "The artist forgot to paint them.",
                           "It was a stylistic choice.",
                           "The painting was damaged over time."],
                "answer": 0
            },
            {
                "question": "Who was the first known computer programmer?",
                "options": ["Alan Turing", "Charles Babbage", "Ada Lovelace", "Grace Hopper"],
                "answer": 2
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest known prime number as of 2022 has over 23 million digits.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first known computer programmer was Ada Lovelace, a 19th-century English mathematician."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the largest known prime number as of 2022?",
                "options": ["23 million digits", "10 million digits", "100 million digits", "1 billion digits"],
                "answer": 0
            },
            {
                "question": "Why does the Mona Lisa have no eyebrows?",
                "options": ["It was the fashion in Renaissance Florence to shave them off.",
                           "The artist forgot to paint them.",
                           "It was a stylistic choice.",
                           "The painting was damaged over time."],
                "answer": 0
            },
            {
                "question": "Who was the first known computer programmer?",
                "options": ["Alan Turing", "Charles Babbage", "Ada Lovelace", "Grace Hopper"],
                "answer": 2
            }
        ]
    }
}

def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")
    return input("Enter your choice: ").lower()

def display_fact(topic):
    fact = random.choice(topics[topic]["facts"])
    print(f"Here's a random fact about {topic.capitalize()}:")
    print(f"- {fact}")

def run_quiz(topic):
    print(f"Let's test your {topic.capitalize()} knowledge!")
    score = 0
    for question in topics[topic]["quiz_questions"]:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): ")) - 1
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score is {score} out of {len(topics[topic]['quiz_questions'])}")

def main():
    topic = display_menu()
    display_fact(topic)
    run_quiz(topic)

if __name__ == "__main__":
    main()
