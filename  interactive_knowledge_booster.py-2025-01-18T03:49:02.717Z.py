
import random
import json
import requests

# Define the topics and their corresponding facts and quizzes
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest planet in the solar system is Venus, not Mercury.",
            "The largest known prime number as of 2023 has 23 million digits."
        ],
        "quizzes": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "What is the name of the largest moon of Saturn?",
                "options": ["Titan", "Ganymede", "Callisto", "Io"],
                "answer": "Titan"
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Fermentation", "Evaporation"],
                "answer": "Photosynthesis"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, was completed in 1946 and weighed 30 tons.",
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The first smartphone, the IBM Simon, was introduced in 1992."
        ],
        "quizzes": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "What is the name of the company that created the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": "Google"
            },
            {
                "question": "What is the name of the first web browser, created by Tim Berners-Lee?",
                "options": ["Mosaic", "Netscape", "Internet Explorer", "WorldWideWeb"],
                "answer": "WorldWideWeb"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa was stolen from the Louvre Museum in Paris in 1911 and recovered two years later.",
            "The first successful powered flight was made by the Wright brothers in 1903."
        ],
        "quizzes": [
            {
                "question": "What year was the Declaration of Independence signed?",
                "options": ["1776", "1787", "1812", "1865"],
                "answer": "1776"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "John Adams"],
                "answer": "George Washington"
            },
            {
                "question": "What was the name of the ancient Egyptian civilization that built the pyramids?",
                "options": ["Mesopotamians", "Mayans", "Incas", "Egyptians"],
                "answer": "Egyptians"
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2023 has 23 million digits.",
            "The first successful kidney transplant was performed in 1954.",
            "The tallest mammal is the giraffe, which can reach heights of up to 6 meters."
        ],
        "quizzes": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "What is the name of the largest continent on Earth?",
                "options": ["Asia", "Africa", "Europe", "North America"],
                "answer": "Asia"
            },
            {
                "question": "What is the name of the tallest mountain in the world?",
                "options": ["Everest", "K2", "Kangchenjunga", "Lhotse"],
                "answer": "Everest"
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

def main():
    """
    The main function that runs the interactive knowledge-boosting script.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Select a topic to learn about:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    chosen_topic = input("Enter your topic choice: ").lower()
    if chosen_topic in topics:
        print(f"\nHere's a random fact about {chosen_topic.capitalize()}:")
        print(get_random_fact(chosen_topic))

        print("\nNow, let's test your knowledge with a quiz!")
        quiz = get_random_quiz(chosen_topic)
        print(quiz["question"])
        for i, option in enumerate(quiz["options"]):
            print(f"{i+1}. {option}")

        user_answer = input("Enter the number of your answer: ")
        if quiz["options"][int(user_answer) - 1] == quiz["answer"]:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {quiz['answer']}")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
