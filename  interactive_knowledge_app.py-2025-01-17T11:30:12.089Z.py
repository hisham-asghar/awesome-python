```python
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest planet in the solar system is Venus, not Mercury.",
            "Sharks have been on Earth for over 400 million years, predating the dinosaurs."
        ],
        "quiz_questions": [
            {
                "question": "What is the main component of the Earth's atmosphere?",
                "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"],
                "answer": 1
            },
            {
                "question": "What is the name of the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Evaporation"],
                "answer": 0
            },
            {
                "question": "Which of these is not a state of matter?",
                "options": ["Solid", "Liquid", "Gas", "Plasma"],
                "answer": 3
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 and had only one button.",
            "The world's first electronic computer, ENIAC, was unveiled in 1946 and weighed over 30 tons.",
            "The first commercial microprocessor, the Intel 4004, was released in 1971 and had a clock speed of 740 kHz."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "Which of these is not a common type of computer memory?",
                "options": ["RAM", "ROM", "GPU", "SSD"],
                "answer": 2
            },
            {
                "question": "What is the name of the device used to input data into a computer?",
                "options": ["Monitor", "Keyboard", "Mouse", "Printer"],
                "answer": 2
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The first successful powered flight by the Wright brothers took place in 1903 and lasted 12 seconds.",
            "The Mona Lisa was painted by Leonardo da Vinci between 1503 and 1519."
        ],
        "quiz_questions": [
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
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
                "answer": 2
            }
        ]
    },
    "general": {
        "facts": [
            "The world's largest desert is Antarctica, not the Sahara.",
            "The tallest mammal in the world is the giraffe.",
            "The largest organ in the human body is the skin."
        ],
        "quiz_questions": [
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": 2
            },
            {
                "question": "Which of these is not a primary color?",
                "options": ["Red", "Blue", "Yellow", "Green"],
                "answer": 3
            },
            {
                "question": "What is the largest planet in the solar system?",
                "options": ["Earth", "Mars", "Jupiter", "Saturn"],
                "answer": 2
            }
        ]
    }
}

def interactive_knowledge_app():
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")

    chosen_topic = input("Enter your choice: ").lower()

    if chosen_topic in topics:
        print(f"\nYou have chosen the {chosen_topic.capitalize()} topic.")
        print("Here's a random fact:")
        print(random.choice(topics[chosen_topic]["facts"]))

        print("\nNow, let's test your knowledge with a quiz!")
        score = 0
        for question in topics[chosen_topic]["quiz_questions"]:
            print(question["question"])
            for i, option in enumerate(question["options"]):
                print(f"{i+1}. {option}")
            user_answer = int(input("Enter your answer (1-4): "))
            if user_answer == question["answer"] + 1:
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")
        print(f"\nYour final score is {score} out of {len(topics[chosen_topic]['quiz_questions'])}.")
    else:
        print("Sorry, that's not a valid topic. Please try again.")

interactive_knowledge_app()
```