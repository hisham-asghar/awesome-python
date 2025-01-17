
import random
import requests
import json

# Define the topics and their respective facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 100 trillion cells.",
            "The Milky Way galaxy contains an estimated 100-400 billion stars.",
            "Helium is the second most abundant element in the universe."
        ],
        "quizzes": [
            {
                "question": "What is the chemical symbol for the element gold?",
                "options": ["Au", "Ag", "Fe", "Cu"],
                "answer": "Au"
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": "Photosynthesis"
            },
            {
                "question": "What is the name of the force that attracts objects with mass towards each other?",
                "options": ["Gravity", "Friction", "Magnetism", "Electricity"],
                "answer": "Gravity"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The internet was originally called ARPANET, created by the U.S. Department of Defense.",
            "The first digital camera was developed by Kodak in 1975."
        ],
        "quizzes": [
            {
                "question": "What is the name of the process by which a computer converts human-readable code into machine-readable instructions?",
                "options": ["Compiling", "Interpreting", "Encoding", "Decoding"],
                "answer": "Compiling"
            },
            {
                "question": "What is the name of the protocol that allows computers to communicate with each other over the internet?",
                "options": ["TCP/IP", "HTTP", "SMTP", "FTP"],
                "answer": "TCP/IP"
            },
            {
                "question": "What is the name of the device that converts analog signals into digital signals?",
                "options": ["Modem", "Router", "Switch", "Analog-to-digital converter"],
                "answer": "Analog-to-digital converter"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Magna Carta, signed in 1215, is considered one of the most important legal documents in the history of democracy.",
            "The Renaissance period in Europe lasted from the 14th to the 17th century."
        ],
        "quizzes": [
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
                "question": "What was the name of the ancient Greek civilization that flourished from the 8th to the 6th century BC?",
                "options": ["Roman", "Egyptian", "Mesopotamian", "Greek"],
                "answer": "Greek"
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2022 has 23,249,425 digits.",
            "The tallest mammal is the giraffe, which can reach heights of up to 6 meters.",
            "The largest known prime number as of 2022 has 23,249,425 digits."
        ],
        "quizzes": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Pacific", "Atlantic", "Indian", "Arctic"],
                "answer": "Pacific"
            },
            {
                "question": "Which country is known as the 'Land of the Rising Sun'?",
                "options": ["China", "Japan", "India", "Korea"],
                "answer": "Japan"
            },
            {
                "question": "What is the name of the tallest mountain in the world?",
                "options": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
                "answer": "Mount Everest"
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
    Retrieves a random quiz question from the specified topic.
    """
    quizzes = topics[topic]["quizzes"]
    quiz = random.choice(quizzes)
    return quiz

def run_quiz(topic):
    """
    Runs a quiz for the specified topic.
    """
    quiz = get_quiz_question(topic)
    print(quiz["question"])
    for i, option in enumerate(quiz["options"]):
        print(f"{i+1}. {option}")
    user_answer = int(input("Enter your answer (1-4): "))
    if quiz["options"][user_answer-1] == quiz["answer"]:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {quiz['answer']}")

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
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
