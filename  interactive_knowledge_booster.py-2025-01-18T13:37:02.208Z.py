
import random
import requests
import json

# Define the topics and their corresponding facts/quizzes
topics = {
    "Science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The first successful heart transplant was performed in 1967 by Dr. Christiaan Barnard.",
            "Pluto was discovered in 1930 by Clyde Tombaugh."
        ],
        "quizzes": [
            {
                "question": "What is the name of the scientist who proposed the theory of relativity?",
                "options": ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "Marie Curie"],
                "answer": 0
            },
            {
                "question": "Which planet in our solar system has the most moons?",
                "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
                "answer": 0
            },
            {
                "question": "What is the name of the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": 0
            }
        ]
    },
    "Technology": {
        "facts": [
            "The first computer virus, called 'Creeper', was created in 1971.",
            "The first commercially available personal computer was the Altair 8800, released in 1975.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989."
        ],
        "quizzes": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "Which company developed the first commercially successful smartphone?",
                "options": ["Apple", "Samsung", "BlackBerry", "Nokia"],
                "answer": 2
            },
            {
                "question": "What is the name of the operating system developed by Microsoft?",
                "options": ["Linux", "macOS", "Windows", "Android"],
                "answer": 2
            }
        ]
    },
    "History": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Renaissance period in Europe lasted from the 14th to the 17th century.",
            "The American Civil War took place from 1861 to 1865."
        ],
        "quizzes": [
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "John Adams"],
                "answer": 1
            },
            {
                "question": "In what year did World War II end?",
                "options": ["1945", "1939", "1918", "1955"],
                "answer": 0
            },
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Egyptians", "Greeks", "Romans", "Mayans"],
                "answer": 1
            }
        ]
    },
    "General Knowledge": {
        "facts": [
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The name 'Jeep' came from the abbreviation of the term 'general purpose' vehicle, which was GP.",
            "Honey is the only food that does not spoil. Honey found in the tombs of Egyptian pharaohs has been tasted by archaeologists and found edible."
        ],
        "quizzes": [
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Liver", "Skin", "Brain"],
                "answer": 2
            },
            {
                "question": "Which country is known as the 'Land of the Rising Sun'?",
                "options": ["China", "Japan", "India", "South Korea"],
                "answer": 1
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": 2
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the selected topic.
    """
    facts = topics[topic]["facts"]
    return random.choice(facts)

def get_quiz(topic):
    """
    Retrieves a random quiz from the selected topic.
    """
    quizzes = topics[topic]["quizzes"]
    quiz = random.choice(quizzes)
    return quiz

def display_menu():
    """
    Displays the menu of available topics.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    topic = input("Enter your choice: ")
    return topic

def run_quiz(quiz):
    """
    Runs the quiz and returns the user's score.
    """
    score = 0
    print(f"\nQuestion: {quiz['question']}")
    for i, option in enumerate(quiz['options']):
        print(f"{i+1}. {option}")
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == quiz['answer']:
        print("Correct!")
        score = 1
    else:
        print("Incorrect. The correct answer is:", quiz['options'][quiz['answer']])
    return score

def main():
    """
    The main function that runs the interactive knowledge booster.
    """
    topic = display_menu()
    if topic in topics:
        fact = get_random_fact(topic)
        print(f"\nFact about {topic}: {fact}")
        quiz = get_quiz(topic)
        score = run_quiz(quiz)
        print(f"\nYour score: {score}/1")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
