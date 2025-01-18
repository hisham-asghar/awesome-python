
import random
import requests
import json

# Define a dictionary of topics and their associated facts and quizzes
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The first digital computer was the ENIAC, which was completed in 1946.",
            "The largest known prime number as of 2022 has 23 million digits."
        ],
        "quizzes": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "Which scientist is known for the theory of relativity?",
                "options": ["Isaac Newton", "Galileo Galilei", "Albert Einstein", "Marie Curie"],
                "answer": "Albert Einstein"
            },
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Mars", "Jupiter", "Saturn", "Neptune"],
                "answer": "Jupiter"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, weighed 30 tons and took up 1800 square feet.",
            "The first commercial microprocessor was the Intel 4004, released in 1971.",
            "The world's first webcam was used to monitor a coffee pot at the University of Cambridge."
        ],
        "quizzes": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "Which company is known for producing the iPhone?",
                "options": ["Samsung", "Google", "Apple", "Microsoft"],
                "answer": "Apple"
            },
            {
                "question": "What is the name of the first web browser?",
                "options": ["Google Chrome", "Mozilla Firefox", "Internet Explorer", "Mosaic"],
                "answer": "Mosaic"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first emperor of the Qin dynasty, Qin Shi Huang, was buried with an army of over 8,000 terracotta soldiers."
        ],
        "quizzes": [
            {
                "question": "Which ancient civilization is known for building the pyramids?",
                "options": ["Mesopotamia", "Indus Valley", "Ancient Greece", "Ancient Egypt"],
                "answer": "Ancient Egypt"
            },
            {
                "question": "What was the name of the first successful powered flight, conducted by the Wright brothers?",
                "options": ["The Wright Flyer", "The Spirit of St. Louis", "The Kitty Hawk", "The Concorde"],
                "answer": "The Wright Flyer"
            },
            {
                "question": "Which event is considered the start of World War I?",
                "options": ["The assassination of Archduke Franz Ferdinand", "The bombing of Pearl Harbor", "The fall of the Berlin Wall", "The Cuban Missile Crisis"],
                "answer": "The assassination of Archduke Franz Ferdinand"
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2022 has 23 million digits.",
            "The world's oldest known cave paintings were found in Indonesia and are over 45,000 years old.",
            "The longest recorded flight of a chicken is 13 seconds."
        ],
        "quizzes": [
            {
                "question": "What is the capital city of Australia?",
                "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
                "answer": "Canberra"
            },
            {
                "question": "Which country is known as the 'Land of the Rising Sun'?",
                "options": ["China", "Japan", "South Korea", "India"],
                "answer": "Japan"
            },
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Liver", "Lungs", "Skin"],
                "answer": "Skin"
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the specified topic.
    """
    return random.choice(topics[topic]["facts"])

def get_random_quiz(topic):
    """
    Retrieves a random quiz from the specified topic.
    """
    return random.choice(topics[topic]["quizzes"])

def run_quiz(quiz):
    """
    Runs the interactive quiz for the user.
    """
    score = 0
    print(f"Question: {quiz['question']}")
    for i, option in enumerate(quiz['options']):
        print(f"{i+1}. {option}")
    user_answer = input("Enter your answer (1-4): ")
    if quiz['options'][int(user_answer) - 1] == quiz['answer']:
        print("Correct!")
        score = 1
    else:
        print("Incorrect. The correct answer is:", quiz['answer'])
    return score

def main():
    """
    Main function that runs the interactive knowledge script.
    """
    print("Welcome to the Interactive Knowledge Script!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in topics:
        print(f"\nYour selected topic is: {selected_topic.capitalize()}")
        print(get_random_fact(selected_topic))
        print("\nTime for a quiz!")
        quiz = get_random_quiz(selected_topic)
        score = run_quiz(quiz)
        print(f"\nYour score is: {score}/1")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
