Here is the raw Python code extracted from the JSON:

```python
import random
import requests
import json

def get_random_fact(topic):
    """
    Fetches a random fact or concept from a predefined database for the given topic.
    """
    facts = {
        "science": [
            "The Earth is the only planet in our solar system with liquid water on its surface.",
            "The human body is made up of approximately 60% water.",
            "The speed of light is about 299,792 kilometers per second."
        ],
        "technology": [
            "The first computer mouse was invented by Douglas Engelbart in 1964.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989.",
            "Artificial Intelligence (AI) is the ability of a computer or a robot to perform tasks commonly associated with intelligent beings."
        ],
        "history": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.",
            "The Renaissance was a period of cultural, artistic, political, and economic "rebirth" in Europe, lasting from the 14th to the 17th century."
        ],
        "general": [
            "The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.",
            "The largest ocean on Earth is the Pacific Ocean, covering an area of about 63 million square miles.",
            "The Mona Lisa, painted by Leonardo da Vinci, is one of the most famous paintings in the world."
        ]
    }
    return random.choice(facts[topic])

def get_quiz_question(topic):
    """
    Fetches a multiple-choice quiz question and its answers from a public API or predefined database for the given topic.
    """
    quiz_questions = {
        "science": [
            {
                "question": "What is the chemical symbol for gold?",
                "answers": ["Au", "Ag", "Cu", "Fe"],
                "correct_answer": "Au"
            },
            {
                "question": "Which planet in our solar system is known as the 'Red Planet'?",
                "answers": ["Jupiter", "Mars", "Saturn", "Venus"],
                "correct_answer": "Mars"
            },
            {
                "question": "What is the process by which plants convert sunlight into energy called?",
                "answers": ["Photosynthesis", "Respiration", "Transpiration", "Evaporation"],
                "correct_answer": "Photosynthesis"
            }
        ],
        "technology": [
            {
                "question": "What is the name of the first commercially successful web browser?",
                "answers": ["Internet Explorer", "Mozilla Firefox", "Google Chrome", "Mosaic"],
                "correct_answer": "Mosaic"
            },
            {
                "question": "Which company developed the Android operating system?",
                "answers": ["Apple", "Microsoft", "Google", "Samsung"],
                "correct_answer": "Google"
            },
            {
                "question": "What is the name of the programming language used to create web pages?",
                "answers": ["Java", "Python", "C++", "HTML"],
                "correct_answer": "HTML"
            }
        ],
        "history": [
            {
                "question": "In what year did the United States declare its independence?",
                "answers": ["1776", "1789", "1812", "1865"],
                "correct_answer": "1776"
            },
            {
                "question": "Who was the first president of the United States?",
                "answers": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "Franklin D. Roosevelt"],
                "correct_answer": "George Washington"
            },
            {
                "question": "Which ancient civilization is known for building the Pyramids of Giza?",
                "answers": ["Aztec", "Inca", "Greek", "Egyptian"],
                "correct_answer": "Egyptian"
            }
        ],
        "general": [
            {
                "question": "What is the largest animal on Earth?",
                "answers": ["African Elephant", "Blue Whale", "Sperm Whale", "Asian Elephant"],
                "correct_answer": "Blue Whale"
            },
            {
                "question": "Who wrote the famous novel 'To Kill a Mockingbird'?",
                "answers": ["Ernest Hemingway", "F. Scott Fitzgerald", "Harper Lee", "Maya Angelou"],
                "correct_answer": "Harper Lee"
            },
            {
                "question": "What is the capital city of Australia?",
                "answers": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
                "correct_answer": "Canberra"
            }
        ]
    }
    return random.choice(quiz_questions[topic])

def run_interactive_knowledge_app():
    """
    Runs the interactive knowledge app, allowing users to select a topic, learn a random fact, and take a quiz.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    print("1. Science")
    print("2. Technology")
    print("3. History")
    print("4. General Knowledge")

    topic_choice = input("Enter the number of the topic you'd like to explore: ")

    if topic_choice == "1":
        topic = "science"
    elif topic_choice == "2":
        topic = "technology"
    elif topic_choice == "3":
        topic = "history"
    elif topic_choice == "4":
        topic = "general"
    else:
        print("Invalid choice. Exiting the app.")
        return

    print(f"\nYour chosen topic is: {topic.capitalize()}")
    print(f"Random fact: {get_random_fact(topic)}")

    quiz_question = get_quiz_question(topic)
    print(f"\nMultiple-choice quiz question:")
    print(quiz_question["question"])
    for i, answer in enumerate(quiz_question["answers"]):
        print(f"{i+1}. {answer}")

    user_answer = input("Enter the number of the correct answer: ")
    if quiz_question["answers"][int(user_answer) - 1] == quiz_question["correct_answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_question["correct_answer"])

    print("\nThank you for using the Interactive Knowledge App!")

run_interactive_knowledge_app()
