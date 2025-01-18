
import random
import requests
import json

# Define the topics and their corresponding facts and quizzes
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Milky Way galaxy contains an estimated 200-400 billion stars.",
            "Honey is the only food that does not spoil."
        ],
        "quizzes": [
            {
                "question": "What is the main function of the human heart?",
                "options": ["Pumping blood", "Breathing", "Digestion", "Metabolism"],
                "answer": 0
            },
            {
                "question": "What is the name of the nearest star to our solar system?",
                "options": ["Andromeda", "Sirius", "Proxima Centauri", "Betelgeuse"],
                "answer": 2
            },
            {
                "question": "Which element is the most abundant in the universe?",
                "options": ["Hydrogen", "Helium", "Oxygen", "Carbon"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, was completed in 1946 and weighed 30 tons.",
            "The first commercial smartphone, the IBM Simon, was introduced in 1992.",
            "The internet was originally called ARPANET and was created in 1969."
        ],
        "quizzes": [
            {
                "question": "What does the acronym 'CPU' stand for?",
                "options": ["Central Processing Unit", "Computer Power Unit", "Compact Processor Unit", "Central Power Unit"],
                "answer": 0
            },
            {
                "question": "Which company developed the first graphical user interface (GUI)?",
                "options": ["Apple", "Microsoft", "Xerox", "IBM"],
                "answer": 2
            },
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first successful powered flight was made by the Wright brothers in 1903."
        ],
        "quizzes": [
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Egyptians", "Greeks", "Mayans", "Chinese"],
                "answer": 1
            },
            {
                "question": "What was the name of the first successful manned space mission?",
                "options": ["Apollo 11", "Sputnik 1", "Vostok 1", "Mercury-Redstone 3"],
                "answer": 2
            },
            {
                "question": "Which event marked the end of World War II in Europe?",
                "options": ["D-Day", "VE Day", "Hiroshima bombing", "Fall of Berlin"],
                "answer": 1
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2022 has 23 million digits.",
            "The largest known snowflake had a diameter of 15 inches.",
            "The longest word in the English language is 'pneumonoultramicroscopicsilicovolcanoconiosis'."
        ],
        "quizzes": [
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
                "answer": 0
            },
            {
                "question": "Which country is known as the 'Land of the Rising Sun'?",
                "options": ["China", "Japan", "South Korea", "Taiwan"],
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
    return random.choice(topics[topic]["facts"])

def get_quiz(topic):
    """
    Retrieves a random quiz from the selected topic.
    """
    quiz = random.choice(topics[topic]["quizzes"])
    return quiz

def run_quiz(quiz):
    """
    Runs the interactive quiz.
    """
    print(quiz["question"])
    for i, option in enumerate(quiz["options"]):
        print(f"{i+1}. {option}")
    user_answer = int(input("Enter your answer (1-4): ")) - 1
    if user_answer == quiz["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz["options"][quiz["answer"]])

def main():
    """
    The main function that runs the interactive knowledge application.
    """
    print("Welcome to the Interactive Knowledge Application!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in topics:
        print("\nHere's a random fact about", selected_topic.capitalize() + ":")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(get_quiz(selected_topic))
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
