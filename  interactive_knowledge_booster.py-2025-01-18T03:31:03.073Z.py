
import json
import random
import requests

def interactive_knowledge_booster():
    """
    A Python script that helps users increase their knowledge interactively.
    """
    topics = {
        "1": "Science",
        "2": "Technology",
        "3": "History",
        "4": "General Knowledge"
    }

    def display_menu():
        """
        Displays the topic selection menu.
        """
        print("Welcome to the Knowledge Booster!")
        print("Please select a topic:")
        for key, value in topics.items():
            print(f"{key}. {value}")

    def get_random_fact(topic):
        """
        Fetches a random fact or concept from the selected topic.
        """
        facts = {
            "Science": [
                "The human body has around 60,000 miles of blood vessels.",
                "The Earth's core is as hot as the surface of the Sun.",
                "A single cloud can weigh more than 1 million pounds."
            ],
            "Technology": [
                "The first electronic computer, ENIAC, weighed 30 tons and took up 1,800 square feet.",
                "The first mobile phone call was made in 1973 by Martin Cooper of Motorola.",
                "The world's first programmable computer was the ENIAC, completed in 1946."
            ],
            "History": [
                "The Pyramids of Giza were built around 2560–2540 BC.",
                "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.",
                "The Mona Lisa was painted by Leonardo da Vinci between 1503 and 1519."
            ],
            "General Knowledge": [
                "The largest organ in the human body is the skin.",
                "The tallest mammal in the world is the giraffe.",
                "The Great Wall of China is the longest man-made structure in the world."
            ]
        }
        return random.choice(facts[topic])

    def quiz_questions(topic):
        """
        Provides a multiple-choice quiz for the selected topic.
        """
        questions = {
            "Science": [
                {
                    "question": "What is the chemical symbol for gold?",
                    "options": ["Au", "Ag", "Cu", "Fe"],
                    "answer": "Au"
                },
                {
                    "question": "Which planet in our solar system is known as the 'Red Planet'?",
                    "options": ["Mars", "Jupiter", "Saturn", "Venus"],
                    "answer": "Mars"
                },
                {
                    "question": "What is the process by which plants convert sunlight into energy?",
                    "options": ["Photosynthesis", "Respiration", "Transpiration", "Evaporation"],
                    "answer": "Photosynthesis"
                }
            ],
            "Technology": [
                {
                    "question": "What does 'CPU' stand for?",
                    "options": ["Central Processing Unit", "Computer Power Unit", "Compact Processing Unit", "Central Power Unit"],
                    "answer": "Central Processing Unit"
                },
                {
                    "question": "Which company developed the first commercial personal computer?",
                    "options": ["Apple", "IBM", "Microsoft", "Commodore"],
                    "answer": "IBM"
                },
                {
                    "question": "What is the name of the programming language created by Guido van Rossum?",
                    "options": ["Java", "C++", "Python", "Ruby"],
                    "answer": "Python"
                }
            ],
            "History": [
                {
                    "question": "In what year did the United States declare independence?",
                    "options": ["1776", "1789", "1812", "1865"],
                    "answer": "1776"
                },
                {
                    "question": "Which ancient civilization built the Colosseum in Rome?",
                    "options": ["Greeks", "Romans", "Egyptians", "Mayans"],
                    "answer": "Romans"
                },
                {
                    "question": "What was the name of the first successful powered flight by the Wright brothers?",
                    "options": ["The Flyer", "The Glider", "The Biplane", "The Monoplane"],
                    "answer": "The Flyer"
                }
            ],
            "General Knowledge": [
                {
                    "question": "What is the largest ocean on Earth?",
                    "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
                    "answer": "Pacific Ocean"
                },
                {
                    "question": "What is the rarest blood type?",
                    "options": ["A", "B", "AB", "O"],
                    "answer": "AB"
                },
                {
                    "question": "What is the capital city of Australia?",
                    "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
                    "answer": "Canberra"
                }
            ]
        }
        return random.choice(questions[topic])

    def run_quiz(topic):
        """
        Runs the multiple-choice quiz for the selected topic.
        """
        question = quiz_questions(topic)
        print(f"\nQuestion: {question['question']}")
        for i, option in enumerate(question['options'], start=1):
            print(f"{i}. {option}")
        user_answer = input("Enter your answer (1-4): ")
        if question['options'][int(user_answer) - 1] == question['answer']:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {question['answer']}.")

    def main():
        display_menu()
        topic_choice = input("Enter your choice (1-4): ")
        if topic_choice in topics:
            topic = topics[topic_choice]
            print(f"\nYour selected topic is: {topic}")
            print(get_random_fact(topic))
            run_quiz(topic)
        else:
            print("Invalid choice. Please try again.")

    if __name__ == "__main__":
        main()

    return {
        "python_code": inspect.getsource(interactive_knowledge_booster),
        "filename": "interactive_knowledge_booster.py"
    }
