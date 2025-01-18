Here is the Python code extracted from the JSON:

import random
import requests
import json

# Define the topics and their associated facts/concepts and quiz questions
topics = {
    "Science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest planet in the solar system is Venus, not Mercury.",
            "Cats have fewer toes on their back paws than their front paws."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            },
            {
                "question": "Which scientist is known for the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Galileo Galilei"],
                "answer": 1
            },
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Brain", "Liver", "Skin"],
                "answer": 3
            }
        ]
    },
    "Technology": {
        "facts": [
            "The first electronic computer, ENIAC, weighed 30 tons and took up 1800 square feet.",
            "The first text message was sent on December 3, 1992, and it said 'Merry Christmas'.",
            "The first commercial smartphone was the IBM Simon, released in 1992."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "What is the name of the first web browser?",
                "options": ["Google Chrome", "Mozilla Firefox", "Microsoft Edge", "Mosaic"],
                "answer": 3
            },
            {
                "question": "What is the name of the first commercially successful personal computer?",
                "options": ["Apple II", "IBM PC", "Commodore 64", "Atari 800"],
                "answer": 1
            }
        ]
    },
    "History": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers.",
            "The Mona Lisa has no eyebrows, as it was the fashion in Renaissance-era Italy to shave them off."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization built the pyramids?",
                "options": ["Greeks", "Romans", "Egyptians", "Mayans"],
                "answer": 2
            },
            {
                "question": "What year did the American Civil War begin?",
                "options": ["1861", "1865", "1914", "1939"],
                "answer": 0
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
                "answer": 2
            }
        ]
    },
    "General Knowledge": {
        "facts": [
            "The largest known prime number as of 2022 has 23 million digits.",
            "The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and rises.",
            "A group of flamingos is called a 'flamboyance'."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "What is the tallest mammal?",
                "options": ["Elephant", "Giraffe", "Hippopotamus", "Rhinoceros"],
                "answer": 1
            },
            {
                "question": "What is the currency used in Japan?",
                "options": ["Yuan", "Euro", "Dollar", "Yen"],
                "answer": 3
            }
        ]
    }
}

def get_random_fact(topic):
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    quiz_question = random.choice(topics[topic]["quiz_questions"])
    return quiz_question

def run_quiz(topic):
    quiz_question = get_quiz_question(topic)
    print(quiz_question["question"])
    for i, option in enumerate(quiz_question["options"]):
        print(f"{i+1}. {option}")

    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == quiz_question["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_question["options"][quiz_question["answer"]])

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")

    selected_topic = input("Enter your choice: ")
    if selected_topic in topics:
        print("\nHere's a random fact about", selected_topic.lower() + ":")
        print(get_random_fact(selected_topic))
        print("\nLet's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()