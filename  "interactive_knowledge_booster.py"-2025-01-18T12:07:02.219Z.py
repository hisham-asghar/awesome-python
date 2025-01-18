
import random
import json
import requests

# Define topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest planet in the Solar System is Venus, not Mercury.",
            "The largest known prime number as of 2023 has over 23 million digits."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "Which scientist is known for the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Galileo Galilei"],
                "answer": "Albert Einstein"
            },
            {
                "question": "What is the name of the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, weighed 30 tons and took up 1800 square feet of space.",
            "The first commercially available personal computer was the Altair 8800, released in 1975.",
            "The world's first text message was sent on December 3, 1992, and it said 'Merry Christmas'."
        ],
        "quiz_questions": [
            {
                "question": "What does the acronym 'CPU' stand for?",
                "options": ["Central Processing Unit", "Computer Power Unit", "Compact Processing Unit", "Central Power Unit"],
                "answer": "Central Processing Unit"
            },
            {
                "question": "Which company is known for creating the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
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
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first emperor of the Qin dynasty, Qin Shi Huang, was buried with a life-size terracotta army."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for building the pyramids?",
                "options": ["Mesopotamia", "Aztec", "Greek", "Egyptian"],
                "answer": "Egyptian"
            },
            {
                "question": "What was the name of the first successful powered flight by the Wright brothers?",
                "options": ["Spirit of St. Louis", "Kitty Hawk", "Wright Flyer", "Concorde"],
                "answer": "Wright Flyer"
            },
            {
                "question": "Which event is considered the start of World War I?",
                "options": ["Assassination of Archduke Franz Ferdinand", "Invasion of Poland", "Attack on Pearl Harbor", "Fall of the Berlin Wall"],
                "answer": "Assassination of Archduke Franz Ferdinand"
            }
        ]
    },
    "general knowledge": {
        "facts": [
            "The Mona Lisa has no visible eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first novel ever written was The Tale of Genji, by the Japanese noblewoman Murasaki Shikibu, in the early 11th century.",
            "A 'jiffy' is an actual unit of time, equivalent to one-thousandth of a second."
        ],
        "quiz_questions": [
            {
                "question": "Which planet in our solar system is known as the 'Red Planet'?",
                "options": ["Mars", "Jupiter", "Saturn", "Venus"],
                "answer": "Mars"
            },
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Liver", "Skin", "Brain"],
                "answer": "Skin"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
                "answer": "George Washington"
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
    print(f"Here's a random fact about {topic.capitalize()}:")
    print(f"- {fact}")

def run_quiz(topic):
    print(f"Let's test your {topic.capitalize()} knowledge!")
    score = 0
    questions = topics[topic]["quiz_questions"]
    for question in questions:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = input("Enter your answer (1-4): ")
        if question["options"][int(user_answer) - 1] == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", question["answer"])
    print(f"Your final score is {score} out of {len(questions)}.")

def main():
    topic = display_menu()
    display_fact(topic)
    run_quiz(topic)

if __name__ == "__main__":
    main()
