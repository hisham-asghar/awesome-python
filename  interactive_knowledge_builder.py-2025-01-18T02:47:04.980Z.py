
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The largest known prime number as of 2022 has 23 million digits.",
            "A single teaspoon of neutron star material would weigh over 1 billion tons on Earth.",
            "The human body contains enough DNA to stretch from the Sun to Pluto and back 17 times."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the largest known prime number as of 2022?",
                "options": ["23 million digits", "1 billion tons", "Pluto and back 17 times"],
                "answer": 0
            },
            {
                "question": "How much would a single teaspoon of neutron star material weigh on Earth?",
                "options": ["23 million digits", "1 billion tons", "Pluto and back 17 times"],
                "answer": 1
            },
            {
                "question": "How far could the DNA in the human body stretch?",
                "options": ["23 million digits", "1 billion tons", "Pluto and back 17 times"],
                "answer": 2
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer virus, called 'Creeper', was created in 1971 as an experiment.",
            "The first commercial microprocessor, the Intel 4004, was released in 1971 and had a clock speed of 740 kHz.",
            "The first email was sent by Ray Tomlinson in 1971, who also introduced the use of the '@' symbol in email addresses."
        ],
        "quiz_questions": [
            {
                "question": "What was the name of the first computer virus?",
                "options": ["Creeper", "Intel 4004", "Ray Tomlinson"],
                "answer": 0
            },
            {
                "question": "What was the clock speed of the first commercial microprocessor, the Intel 4004?",
                "options": ["Creeper", "740 kHz", "Ray Tomlinson"],
                "answer": 1
            },
            {
                "question": "Who introduced the use of the '@' symbol in email addresses?",
                "options": ["Creeper", "Intel 4004", "Ray Tomlinson"],
                "answer": 2
            }
        ]
    },
    "history": {
        "facts": [
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers.",
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows, as it was the fashion in Renaissance Florence to shave them off."
        ],
        "quiz_questions": [
            {
                "question": "When did the first successful powered flight take place?",
                "options": ["December 17, 1903", "13,000 miles", "Renaissance Florence"],
                "answer": 0
            },
            {
                "question": "What is the length of the Great Wall of China?",
                "options": ["December 17, 1903", "13,000 miles", "Renaissance Florence"],
                "answer": 1
            },
            {
                "question": "Why does the Mona Lisa have no eyebrows?",
                "options": ["December 17, 1903", "13,000 miles", "Renaissance Florence"],
                "answer": 2
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and the tower grows in height.",
            "A group of porcupines is called a prickle.",
            "The first product to have a barcode was Wrigley's gum."
        ],
        "quiz_questions": [
            {
                "question": "How much taller can the Eiffel Tower get during the summer?",
                "options": ["15 cm", "prickle", "Wrigley's gum"],
                "answer": 0
            },
            {
                "question": "What is a group of porcupines called?",
                "options": ["15 cm", "prickle", "Wrigley's gum"],
                "answer": 1
            },
            {
                "question": "What was the first product to have a barcode?",
                "options": ["15 cm", "prickle", "Wrigley's gum"],
                "answer": 2
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
    
    user_answer = int(input("Enter your answer (1-3): "))
    if user_answer - 1 == quiz_question["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_question["options"][quiz_question["answer"]])

def main():
    """
    Main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print(f"Here's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
