
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The first successful kidney transplant was performed in 1954.",
            "The largest known prime number as of 2023 has 23 million digits."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "What is the name of the force that attracts objects with mass towards each other?",
                "options": ["Gravity", "Friction", "Electricity", "Magnetism"],
                "answer": "Gravity"
            },
            {
                "question": "Which scientist is known for developing the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Marie Curie"],
                "answer": "Albert Einstein"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The first mobile phone call was made on April 3, 1973, by Martin Cooper of Motorola.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "What is the name of the first successful search engine, created by Larry Page and Sergey Brin?",
                "options": ["Yahoo", "Bing", "Google", "AltaVista"],
                "answer": "Google"
            },
            {
                "question": "What is the name of the company that created the first personal computer, the Apple I?",
                "options": ["Microsoft", "IBM", "Dell", "Apple"],
                "answer": "Apple"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza in Egypt is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Magna Carta, a landmark document in the history of democracy, was signed in 1215 by King John of England.",
            "The first moon landing occurred on July 20, 1969, when Neil Armstrong and Buzz Aldrin landed on the moon as part of the Apollo 11 mission."
        ],
        "quiz_questions": [
            {
                "question": "In what year did the American Civil War begin?",
                "options": ["1861", "1865", "1914", "1939"],
                "answer": "1861"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "Franklin D. Roosevelt"],
                "answer": "George Washington"
            },
            {
                "question": "What was the name of the ancient civilization that built the Pyramids of Giza?",
                "options": ["Mayans", "Aztecs", "Incas", "Egyptians"],
                "answer": "Egyptians"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest known prime number as of 2023 has 23 million digits.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "A group of porcupines is called a prickle."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Arctic Ocean", "Indian Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "Who wrote the novel 'To Kill a Mockingbird'?",
                "options": ["Harper Lee", "Ernest Hemingway", "Maya Angelou", "J.K. Rowling"],
                "answer": "Harper Lee"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Mars", "Saturn", "Jupiter", "Uranus"],
                "answer": "Jupiter"
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the specified topic.
    """
    facts = topics[topic]["facts"]
    return random.choice(facts)

def get_quiz_question(topic):
    """
    Retrieves a random quiz question and its options from the specified topic.
    """
    quiz_questions = topics[topic]["quiz_questions"]
    question = random.choice(quiz_questions)
    return question

def run_quiz(topic):
    """
    Runs a quiz for the specified topic, with multiple-choice questions.
    """
    score = 0
    num_questions = 3
    for _ in range(num_questions):
        question = get_quiz_question(topic)
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = input("Enter your answer (1-4): ")
        if question["options"][int(user_answer) - 1] == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score is {score}/{num_questions}.")

def main():
    """
    The main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    chosen_topic = input("Enter your choice: ").lower()

    if chosen_topic in topics:
        print(f"\nHere's a random fact about {chosen_topic.capitalize()}:")
        print(get_random_fact(chosen_topic))
        print("\nNow let's test your knowledge with a quiz!")
        run_quiz(chosen_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
