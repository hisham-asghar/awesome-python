
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The first commercial microprocessor was the Intel 4004, released in 1971.",
            "The Milky Way galaxy contains an estimated 100 to 400 billion stars."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Mars", "Jupiter", "Saturn", "Neptune"],
                "answer": "Jupiter"
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Fermentation"],
                "answer": "Photosynthesis"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, was completed in 1946 and weighed 30 tons.",
            "The term 'bug' to describe a computer error was coined by Grace Hopper in 1947.",
            "The first mobile phone call was made by Martin Cooper of Motorola in 1973."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "What is the name of the first web browser, created by Tim Berners-Lee?",
                "options": ["Mosaic", "Netscape Navigator", "Internet Explorer", "WorldWideWeb"],
                "answer": "WorldWideWeb"
            },
            {
                "question": "What is the name of the company that developed the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": "Google"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa was painted by Leonardo da Vinci between 1503 and 1519.",
            "The first successful powered flight was made by the Wright brothers in 1903."
        ],
        "quiz_questions": [
            {
                "question": "What year was the Declaration of Independence signed?",
                "options": ["1776", "1789", "1812", "1865"],
                "answer": "1776"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
                "answer": "George Washington"
            },
            {
                "question": "What was the name of the ancient Egyptian civilization that built the pyramids?",
                "options": ["Mesopotamia", "Indus Valley", "Aztec", "Ancient Egypt"],
                "answer": "Ancient Egypt"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal is the giraffe, which can reach heights of up to 18 feet.",
            "The largest ocean on Earth is the Pacific Ocean, covering an area of about 63 million square miles."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Jupiter", "Saturn", "Neptune", "Uranus"],
                "answer": "Jupiter"
            },
            {
                "question": "What is the name of the largest freshwater lake in the world?",
                "options": ["Lake Superior", "Lake Victoria", "Lake Baikal", "Lake Tanganyika"],
                "answer": "Lake Baikal"
            },
            {
                "question": "What is the name of the smallest continent in the world?",
                "options": ["Australia", "Europe", "Asia", "Antarctica"],
                "answer": "Australia"
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the specified topic.
    """
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    """
    Retrieves a random quiz question from the specified topic.
    """
    quiz_question = random.choice(topics[topic]["quiz_questions"])
    return quiz_question

def run_quiz(topic):
    """
    Runs a quiz for the specified topic.
    """
    quiz_question = get_quiz_question(topic)
    print(quiz_question["question"])
    for i, option in enumerate(quiz_question["options"]):
        print(f"{i+1}. {option}")

    user_answer = input("Enter your answer (1-4): ")
    if quiz_question["options"][int(user_answer) - 1] == quiz_question["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_question["answer"])

def main():
    """
    The main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()
    if selected_topic in topics:
        print("\nHere's a random fact about", selected_topic.capitalize() + ":")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
