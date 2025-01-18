
import random
import requests
import json

# Define the topics and their associated facts/quizzes
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Italy to shave them off.",
            "A group of porcupines is called a prickle."
        ],
        "quizzes": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Mars", "Saturn", "Jupiter", "Neptune"],
                "answer": "Jupiter"
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": "Photosynthesis"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented by Douglas Engelbart in 1964 and consisted of a wooden shell with two metal wheels.",
            "The first text message was sent on December 3, 1992, and read 'Merry Christmas'.",
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951."
        ],
        "quizzes": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "What is the name of the first web browser?",
                "options": ["Internet Explorer", "Mosaic", "Netscape Navigator", "World Wide Web"],
                "answer": "World Wide Web"
            },
            {
                "question": "What is the name of the company that created the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": "Google"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The first Olympic Games were held in 776 BC in Olympia, Greece.",
            "The Mona Lisa was stolen from the Louvre Museum in Paris in 1911 and was missing for two years."
        ],
        "quizzes": [
            {
                "question": "What year was the Declaration of Independence signed?",
                "options": ["1776", "1787", "1812", "1865"],
                "answer": "1776"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "Benjamin Franklin"],
                "answer": "George Washington"
            },
            {
                "question": "What was the name of the first successful powered flight, which took place in 1903?",
                "options": ["The Wright Flyer", "The Spruce Goose", "The Concorde", "The Apollo 11"],
                "answer": "The Wright Flyer"
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2023 has 23 million digits.",
            "The first book ever written on a typewriter was 'The Adventures of Tom Sawyer' by Mark Twain.",
            "The word 'sandwich' is named after the 4th Earl of Sandwich, who is credited with inventing the snack."
        ],
        "quizzes": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "What is the tallest mammal in the world?",
                "options": ["Elephant", "Giraffe", "Hippopotamus", "Rhinoceros"],
                "answer": "Giraffe"
            },
            {
                "question": "What is the name of the largest moon of Saturn?",
                "options": ["Titan", "Ganymede", "Callisto", "Europa"],
                "answer": "Titan"
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

def run_quiz(quiz):
    """
    Runs the quiz and returns the user's answer.
    """
    print(quiz["question"])
    for i, option in enumerate(quiz["options"]):
        print(f"{i+1}. {option}")
    user_answer = input("Enter your answer (1-4): ")
    return user_answer.lower() == quiz["answer"].lower()

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
        
        print("\nNow let's test your knowledge with a quiz!")
        quiz = get_quiz(selected_topic)
        if run_quiz(quiz):
            print("Congratulations! You got the answer right.")
        else:
            print("Oops, that's not the correct answer. Better luck next time!")
    else:
        print("Sorry, that's not a valid topic. Please try again.")

if __name__ == "__main__":
    main()
