
import json
import random
import requests
from datetime import datetime

def knowledge_booster():
    """
    An interactive Python script that helps users increase their knowledge across various topics.
    """
    topics = {
        "1": "Science",
        "2": "Technology",
        "3": "History",
        "4": "General Knowledge"
    }

    def display_menu():
        """
        Displays the topic selection menu for the user.
        """
        print("Welcome to the Knowledge Booster!")
        print("Please select a topic:")
        for key, value in topics.items():
            print(f"{key}. {value}")
        topic_choice = input("Enter the number of your choice: ")
        return topic_choice

    def get_random_fact(topic):
        """
        Retrieves a random fact or concept related to the selected topic.
        """
        facts = {
            "Science": [
                "The human body contains around 60,000 miles of blood vessels.",
                "The hottest planet in the Solar System is Venus, not Mercury.",
                "The largest known prime number as of 2022 has 23 million digits."
            ],
            "Technology": [
                "The first electronic computer, ENIAC, was completed in 1946 and weighed 30 tons.",
                "The first commercial microprocessor was the Intel 4004, released in 1971.",
                "The World Wide Web was invented by Tim Berners-Lee in 1989."
            ],
            "History": [
                "The Pyramids of Giza were built around 2560–2540 BC.",
                "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.",
                "The first successful powered flight by the Wright brothers took place in 1903."
            ],
            "General Knowledge": [
                "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
                "The largest organ in the human body is the skin.",
                "The first product to have a barcode was Wrigley's gum."
            ]
        }
        return random.choice(facts[topic])

    def quiz_question(topic):
        """
        Generates a multiple-choice quiz question related to the selected topic.
        """
        quiz_data = {
            "Science": [
                {
                    "question": "What is the chemical symbol for gold?",
                    "options": ["Au", "Ag", "Cu", "Fe"],
                    "answer": 0
                },
                {
                    "question": "Which planet in our solar system has the most moons?",
                    "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
                    "answer": 0
                },
                {
                    "question": "What is the process by which plants convert sunlight into energy?",
                    "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                    "answer": 0
                }
            ],
            "Technology": [
                {
                    "question": "What is the name of the first commercially successful web browser?",
                    "options": ["Internet Explorer", "Mosaic", "Netscape Navigator", "Google Chrome"],
                    "answer": 2
                },
                {
                    "question": "Which company developed the first personal computer, the Altair 8800?",
                    "options": ["Apple", "Microsoft", "IBM", "MITS"],
                    "answer": 3
                },
                {
                    "question": "What is the name of the programming language created by Guido van Rossum?",
                    "options": ["Java", "C++", "Python", "Ruby"],
                    "answer": 2
                }
            ],
            "History": [
                {
                    "question": "In what year did the American Civil War begin?",
                    "options": ["1861", "1865", "1775", "1914"],
                    "answer": 0
                },
                {
                    "question": "Who was the first president of the United States?",
                    "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "Theodore Roosevelt"],
                    "answer": 2
                },
                {
                    "question": "Which ancient civilization is known for building the Pyramids of Giza?",
                    "options": ["Mesopotamia", "Indus Valley", "Ancient Greece", "Ancient Egypt"],
                    "answer": 3
                }
            ],
            "General Knowledge": [
                {
                    "question": "What is the largest organ in the human body?",
                    "options": ["Heart", "Liver", "Brain", "Skin"],
                    "answer": 3
                },
                {
                    "question": "What is the tallest mammal in the world?",
                    "options": ["Elephant", "Giraffe", "Hippopotamus", "Rhinoceros"],
                    "answer": 1
                },
                {
                    "question": "Which country is known as the 'Land of the Rising Sun'?",
                    "options": ["China", "Japan", "South Korea", "India"],
                    "answer": 1
                }
            ]
        }
        question = random.choice(quiz_data[topic])
        return question

    def run_quiz(topic):
        """
        Runs the multiple-choice quiz for the selected topic.
        """
        question = quiz_question(topic)
        print(f"Question: {question['question']}")
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter the number of your answer: ")) - 1
        if user_answer == question["answer"]:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", question["options"][question["answer"]])

    def main():
        """
        The main function that orchestrates the knowledge booster experience.
        """
        topic_choice = display_menu()
        if topic_choice in topics:
            selected_topic = topics[topic_choice]
            print(f"\nYou have selected the topic: {selected_topic}")
            print(get_random_fact(selected_topic))
            print("\nNow, let's test your knowledge with a quiz!")
            run_quiz(selected_topic)
        else:
            print("Invalid choice. Please try again.")

    main()

knowledge_booster()
