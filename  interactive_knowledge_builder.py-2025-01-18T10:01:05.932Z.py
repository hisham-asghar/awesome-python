
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The first product to have a barcode was Wrigley's gum.",
            "A single cloud can weigh more than 1 million pounds."
        ],
        "quiz": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "Which scientist is known for the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Marie Curie", "Galileo Galilei"],
                "answer": "Albert Einstein"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Mars", "Saturn", "Jupiter", "Uranus"],
                "answer": "Jupiter"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 and had only one button.",
            "The first text message was sent on December 3, 1992, and said 'Merry Christmas'.",
            "The first smartphone was the IBM Simon, released in 1992."
        ],
        "quiz": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "Which company developed the first commercial personal computer?",
                "options": ["Apple", "IBM", "Microsoft", "Commodore"],
                "answer": "IBM"
            },
            {
                "question": "What is the name of the protocol used for sending and receiving email?",
                "options": ["HTTP", "FTP", "SMTP", "DNS"],
                "answer": "SMTP"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first person convicted of speeding was Walter Arnold of East Peckham, Kent, UK, in 1896. He was fined 1 shilling for driving at 8 mph (13 km/h), which was twice the legal speed limit of 4 mph (6 km/h)."
        ],
        "quiz": [
            {
                "question": "Which ancient civilization built the Pyramids of Giza?",
                "options": ["Aztecs", "Incas", "Egyptians", "Romans"],
                "answer": "Egyptians"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "Benjamin Franklin"],
                "answer": "George Washington"
            },
            {
                "question": "What was the name of the first successful powered flight by the Wright brothers?",
                "options": ["Kitty Hawk", "Spirit of St. Louis", "Wright Flyer", "Concorde"],
                "answer": "Wright Flyer"
            }
        ]
    },
    "general": {
        "facts": [
            "A group of porcupines is called a prickle.",
            "The first product to be sold with a barcode was Wrigley's gum.",
            "The first person convicted of speeding was Walter Arnold of East Peckham, Kent, UK, in 1896. He was fined 1 shilling for driving at 8 mph (13 km/h), which was twice the legal speed limit of 4 mph (6 km/h)."
        ],
        "quiz": [
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Liver", "Skin", "Brain"],
                "answer": "Skin"
            },
            {
                "question": "Which country is known as the 'Land of the Rising Sun'?",
                "options": ["China", "Japan", "India", "South Korea"],
                "answer": "Japan"
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": "AB"
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
    quiz = topics[topic]["quiz"]
    question = random.choice(quiz)
    return question

def main():
    """
    The main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Choose a topic to learn more:")
    print("1. Science")
    print("2. Technology")
    print("3. History")
    print("4. General")

    topic_choice = input("Enter the number of the topic (1-4): ")

    if topic_choice == "1":
        topic = "science"
    elif topic_choice == "2":
        topic = "technology"
    elif topic_choice == "3":
        topic = "history"
    elif topic_choice == "4":
        topic = "general"
    else:
        print("Invalid choice. Exiting...")
        return

    print(f"\nYou've chosen the {topic.capitalize()} topic.")
    print("Here's a random fact:")
    print(get_random_fact(topic))

    print("\nNow, let's test your knowledge with a quiz!")
    quiz_question = get_quiz_question(topic)
    print(quiz_question["question"])
    for i, option in enumerate(quiz_question["options"]):
        print(f"{i+1}. {option}")

    user_answer = input("Enter the number of your answer: ")
    if quiz_question["options"][int(user_answer) - 1] == quiz_question["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_question["answer"])

    print("\nThank you for using the Interactive Knowledge Builder!")

if __name__ == "__main__":
    main()
