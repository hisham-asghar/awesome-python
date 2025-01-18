
import random
import requests
import json

# Define the topics and their corresponding API endpoints
topics = {
    '1': 'Science',
    '2': 'Technology',
    '3': 'History',
    '4': 'General Knowledge'
}

def get_random_fact(topic):
    """
    Retrieves a random fact or concept for the given topic.
    """
    if topic == '1':
        # Science facts
        facts = [
            "The human body contains around 60,000 miles of blood vessels.",
            "The Earth is the only planet in our solar system with liquid water on its surface.",
            "The largest known prime number as of 2021 has 23,249,425 digits."
        ]
    elif topic == '2':
        # Technology facts
        facts = [
            "The first electronic computer, ENIAC, was completed in 1946 and weighed 30 tons.",
            "The first mobile phone call was made on April 3, 1973, by Martin Cooper of Motorola.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989."
        ]
    elif topic == '3':
        # History facts
        facts = [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first electric traffic light was installed in Cleveland, Ohio, in 1914."
        ]
    elif topic == '4':
        # General knowledge facts
        facts = [
            "The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and raises the structure.",
            "A 'jiffy' is an actual unit of time, measuring one-thousandth of a second.",
            "The first product to have a barcode was Wrigley's gum."
        ]
    else:
        return "Invalid topic selection."

    return random.choice(facts)

def quiz(topic):
    """
    Provides a multiple-choice quiz for the given topic.
    """
    if topic == '1':
        # Science quiz
        questions = [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "What is the primary function of the human heart?",
                "options": ["To pump blood", "To filter waste", "To produce insulin", "To generate electricity"],
                "answer": "To pump blood"
            },
            {
                "question": "What is the name of the largest moon of Saturn?",
                "options": ["Titan", "Europa", "Ganymede", "Callisto"],
                "answer": "Titan"
            }
        ]
    elif topic == '2':
        # Technology quiz
        questions = [
            {
                "question": "What is the name of the first programmable computer?",
                "options": ["ENIAC", "UNIVAC", "Apple I", "Commodore 64"],
                "answer": "ENIAC"
            },
            {
                "question": "What is the name of the software that translates high-level programming languages into machine code?",
                "options": ["Compiler", "Interpreter", "Assembler", "Linker"],
                "answer": "Compiler"
            },
            {
                "question": "What is the name of the first commercial web browser?",
                "options": ["Netscape Navigator", "Internet Explorer", "Mozilla Firefox", "Google Chrome"],
                "answer": "Netscape Navigator"
            }
        ]
    elif topic == '3':
        # History quiz
        questions = [
            {
                "question": "What year was the Declaration of Independence signed?",
                "options": ["1776", "1787", "1812", "1865"],
                "answer": "1776"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
                "answer": "George Washington"
            },
            {
                "question": "What was the name of the first successful powered flight by the Wright brothers?",
                "options": ["The Flyer", "The Kitty Hawk", "The Wright Flyer", "The Glider"],
                "answer": "The Wright Flyer"
            }
        ]
    elif topic == '4':
        # General knowledge quiz
        questions = [
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Jupiter", "Saturn", "Mars", "Neptune"],
                "answer": "Jupiter"
            },
            {
                "question": "What is the capital city of Australia?",
                "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
                "answer": "Canberra"
            },
            {
                "question": "What is the name of the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            }
        ]
    else:
        return "Invalid topic selection."

    # Randomly select a question and display it
    question = random.choice(questions)
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")

    # Get the user's answer
    user_answer = input("Enter your answer (1-4): ")

    # Check if the user's answer is correct
    if user_answer == question["answer"]:
        return "Correct!"
    else:
        return "Incorrect. The correct answer is: " + question["answer"]

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic_id, topic_name in topics.items():
        print(f"{topic_id}. {topic_name}")

    topic_choice = input("Enter the number of the topic (1-4): ")

    if topic_choice in topics:
        print("\nHere's a random fact or concept about", topics[topic_choice] + ":")
        print(get_random_fact(topic_choice))
        print("\nNow, let's test your knowledge with a quiz!")
        print(quiz(topic_choice))
    else:
        print("Invalid topic selection. Please try again.")

if __name__ == "__main__":
    main()
