
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The first commercial microprocessor was the Intel 4004, released in 1971.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off."
        ],
        "quiz": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "Which scientist is known for developing the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Marie Curie"],
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
            "The first electronic computer, ENIAC, was completed in 1946 and weighed 30 tons.",
            "The first commercial computer mouse was introduced in 1984 with the Apple Macintosh.",
            "The first text message was sent on December 3, 1992, and it said 'Merry Christmas'."
        ],
        "quiz": [
            {
                "question": "What does 'HTML' stand for?",
                "options": ["Hyper Text Markup Language", "Hyper Text Machine Language", "High-level Text Markup Language", "Hyper Text Markup Lingua"],
                "answer": "Hyper Text Markup Language"
            },
            {
                "question": "Which company developed the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": "Google"
            },
            {
                "question": "What is the name of the first web browser?",
                "options": ["Mozilla Firefox", "Google Chrome", "Safari", "Mosaic"],
                "answer": "Mosaic"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa was stolen from the Louvre museum in Paris in 1911 and was missing for two years.",
            "The first computer bug was a real bug (a moth) trapped in an early computer in 1947."
        ],
        "quiz": [
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "John Adams"],
                "answer": "George Washington"
            },
            {
                "question": "In what year did World War II end?",
                "options": ["1945", "1939", "1941", "1947"],
                "answer": "1945"
            },
            {
                "question": "Which ancient civilization is known for building the pyramids?",
                "options": ["Mesopotamia", "Aztec", "Roman", "Egyptian"],
                "answer": "Egyptian"
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2023 has 23,249,425 digits.",
            "A group of flamingos is called a flamboyance.",
            "The first person convicted of speeding was going 8 mph."
        ],
        "quiz": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "What is the tallest mammal in the world?",
                "options": ["Elephant", "Giraffe", "Hippopotamus", "Rhinoceros"],
                "answer": "Giraffe"
            },
            {
                "question": "Which country is known as the 'Land of the Rising Sun'?",
                "options": ["China", "Japan", "India", "South Korea"],
                "answer": "Japan"
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the given topic.
    """
    facts = topics[topic]["facts"]
    return random.choice(facts)

def get_quiz_question(topic):
    """
    Retrieves a random quiz question and its options from the given topic.
    """
    quiz_questions = topics[topic]["quiz"]
    question = random.choice(quiz_questions)
    return question["question"], question["options"], question["answer"]

def run_interactive_session():
    """
    Runs the interactive knowledge session.
    """
    print("Welcome to the Interactive Knowledge Session!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()
    if selected_topic not in topics:
        print("Invalid topic. Please try again.")
        return

    print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
    print(get_random_fact(selected_topic))

    print("\nNow, let's test your knowledge with a quiz!")
    question, options, answer = get_quiz_question(selected_topic)
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    user_answer = int(input("Enter your answer (1-4): "))
    if options[user_answer - 1] == answer:
        print("Correct! You're a knowledge master.")
    else:
        print(f"Oops, the correct answer is '{answer}'.")

    print("\nThank you for participating! Have a great day.")

if __name__ == "__main__":
    run_interactive_session()
