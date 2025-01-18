
import random
import json
import requests

# Define the topics and their respective facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest planet in the solar system is Venus, not Mercury.",
            "Honey is the only food that does not spoil."
        ],
        "quiz_questions": [
            {
                "question": "Which of the following is the largest planet in our solar system?",
                "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
                "answer": "Jupiter"
            },
            {
                "question": "What is the name of the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Evaporation"],
                "answer": "Photosynthesis"
            },
            {
                "question": "Which of the following is the smallest planet in our solar system?",
                "options": ["Mercury", "Mars", "Venus", "Earth"],
                "answer": "Mercury"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, weighed 30 tons and took up 1,800 square feet.",
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The first mobile phone call was made in 1973 by Martin Cooper of Motorola."
        ],
        "quiz_questions": [
            {
                "question": "What does the abbreviation 'CPU' stand for?",
                "options": ["Central Processing Unit", "Computer Processing Unit", "Central Power Unit", "Computer Power Unit"],
                "answer": "Central Processing Unit"
            },
            {
                "question": "Which of the following is a type of computer memory?",
                "options": ["RAM", "GPU", "Motherboard", "Monitor"],
                "answer": "RAM"
            },
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers.",
            "The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for building the Colosseum?",
                "options": ["Greeks", "Romans", "Egyptians", "Mayans"],
                "answer": "Romans"
            },
            {
                "question": "What was the name of the first English colony in North America?",
                "options": ["Jamestown", "Plymouth Rock", "Roanoke", "New Amsterdam"],
                "answer": "Jamestown"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "Benjamin Franklin"],
                "answer": "George Washington"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal is the giraffe.",
            "The largest ocean on Earth is the Pacific Ocean."
        ],
        "quiz_questions": [
            {
                "question": "What is the capital city of Australia?",
                "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
                "answer": "Canberra"
            },
            {
                "question": "Which of these is not a primary color?",
                "options": ["Red", "Blue", "Yellow", "Green"],
                "answer": "Green"
            },
            {
                "question": "What is the largest bone in the human body?",
                "options": ["Femur", "Tibia", "Humerus", "Fibula"],
                "answer": "Femur"
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the chosen topic.
    """
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    """
    Retrieves a random quiz question from the chosen topic.
    """
    return random.choice(topics[topic]["quiz_questions"])

def run_quiz(topic):
    """
    Runs a quiz for the chosen topic.
    """
    quiz_question = get_quiz_question(topic)
    print(quiz_question["question"])
    for i, option in enumerate(quiz_question["options"]):
        print(f"{i+1}. {option}")

    user_answer = input("Enter your answer (1-4): ")
    if quiz_question["options"][int(user_answer) - 1] == quiz_question["answer"]:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {quiz_question['answer']}")

def main():
    """
    Main function that handles the interactive knowledge app.
    """
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    chosen_topic = input("Enter your choice: ").lower()
    if chosen_topic in topics:
        print(f"\nRandom fact about {chosen_topic.capitalize()}:")
        print(get_random_fact(chosen_topic))
        print("\nNow let's test your knowledge!")
        run_quiz(chosen_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
