
import random
import requests
import json

# Dictionary to store topics and their facts/quizzes
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest planet in the solar system is Venus, not Mercury.",
            "Sharks have been around for over 400 million years, predating the dinosaurs."
        ],
        "quizzes": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "Which scientist is credited with the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Galileo Galilei"],
                "answer": "Albert Einstein"
            },
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Liver", "Skin", "Brain"],
                "answer": "Skin"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, was developed in 1946 and weighed over 30 tons.",
            "The first mobile phone call was made on April 3, 1973, by Martin Cooper of Motorola.",
            "The world's first website was launched on August 6, 1991, by Tim Berners-Lee."
        ],
        "quizzes": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "What is the name of the first commercially successful personal computer?",
                "options": ["Apple II", "IBM PC", "Commodore 64", "Atari 800"],
                "answer": "Commodore 64"
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
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers.",
            "The Pyramids of Giza in Egypt were built around 2560-2540 BC."
        ],
        "quizzes": [
            {
                "question": "What year was the Declaration of Independence signed?",
                "options": ["1776", "1789", "1812", "1865"],
                "answer": "1776"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "Benjamin Franklin"],
                "answer": "George Washington"
            },
            {
                "question": "What was the name of the first successful satellite launched into space?",
                "options": ["Apollo", "Sputnik", "Voyager", "Hubble"],
                "answer": "Sputnik"
            }
        ]
    },
    "general": {
        "facts": [
            "A group of jellyfish is called a 'smack'.",
            "The tallest mammal in the world is the giraffe.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off."
        ],
        "quizzes": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": "AB"
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
    Returns a random fact from the selected topic.
    """
    return random.choice(topics[topic]["facts"])

def get_random_quiz(topic):
    """
    Returns a random quiz from the selected topic.
    """
    return random.choice(topics[topic]["quizzes"])

def run_quiz(quiz):
    """
    Runs the quiz and returns the result.
    """
    print(quiz["question"])
    for i, option in enumerate(quiz["options"]):
        print(f"{i+1}. {option}")
    
    user_answer = input("Enter your answer (1-4): ")
    if quiz["options"][int(user_answer) - 1] == quiz["answer"]:
        return True
    else:
        return False

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
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        
        print("\nNow, let's test your knowledge with a quiz!")
        quiz = get_random_quiz(selected_topic)
        if run_quiz(quiz):
            print("Congratulations! You got the answer correct.")
        else:
            print("Oops, that's not the right answer. Better luck next time!")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
