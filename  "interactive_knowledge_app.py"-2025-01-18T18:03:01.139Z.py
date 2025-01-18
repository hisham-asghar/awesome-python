
import json
import random
import requests

TOPICS = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "A group of porcupines is called a prickle."
        ],
        "quizzes": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "Which planet in our solar system has the most moons?",
                "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
                "answer": "Saturn"
            },
            {
                "question": "What is the name of the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": "Photosynthesis"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer bug was a real bug (a moth) trapped in a Harvard Mark II computer.",
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The word 'byte' is a combination of the words 'binary' and 'digit'."
        ],
        "quizzes": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "Which company is known for creating the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": "Google"
            },
            {
                "question": "What is the name of the first successful web browser?",
                "options": ["Internet Explorer", "Safari", "Mozilla Firefox", "Mosaic"],
                "answer": "Mosaic"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first person convicted of speeding was going 8 mph."
        ],
        "quizzes": [
            {
                "question": "In what year was the Declaration of Independence signed?",
                "options": ["1776", "1789", "1812", "1865"],
                "answer": "1776"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
                "answer": "George Washington"
            },
            {
                "question": "Which ancient civilization is known for building the pyramids?",
                "options": ["Aztec", "Inca", "Maya", "Egyptian"],
                "answer": "Egyptian"
            }
        ]
    },
    "general": {
        "facts": [
            "A 'jiffy' is an actual unit of time, equivalent to one-hundredth of a second.",
            "Apples are more effective at waking you up in the morning than coffee.",
            "The first product to have a barcode was Wrigley's gum."
        ],
        "quizzes": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "What is the tallest mammal in the world?",
                "options": ["Elephant", "Giraffe", "Hippopotamus", "Rhinoceros"],
                "answer": "Giraffe"
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": "AB"
            }
        ]
    }
}

def interactive_knowledge_app():
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")

    for topic in TOPICS:
        print(f"- {topic.capitalize()}")

    topic_choice = input("Enter your choice: ").lower()

    if topic_choice in TOPICS:
        print(f"\nHere's a random fact about {topic_choice.capitalize()}:")
        print(random.choice(TOPICS[topic_choice]["facts"]))

        print(f"\nNow, let's test your {topic_choice.capitalize()} knowledge with a quiz!")
        quiz_questions = TOPICS[topic_choice]["quizzes"]
        score = 0

        for quiz_question in quiz_questions:
            print(quiz_question["question"])
            for i, option in enumerate(quiz_question["options"]):
                print(f"{i+1}. {option}")

            user_answer = input("Enter your answer (1-4): ")
            if quiz_question["options"][int(user_answer) - 1] == quiz_question["answer"]:
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")

        print(f"\nYour final score is {score} out of {len(quiz_questions)}.")
    else:
        print("Invalid topic choice. Please try again.")

interactive_knowledge_app()
