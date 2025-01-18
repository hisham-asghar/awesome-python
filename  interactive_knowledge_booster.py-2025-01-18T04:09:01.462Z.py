
import random
import requests
import json

# Define topics and their associated data
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Milky Way galaxy contains an estimated 100-400 billion stars.",
            "Cats have fewer toes on their back paws than their front paws."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "Which planet in our solar system has the most moons?",
                "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
                "answer": "Saturn"
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
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The first programmable computer was the ENIAC, which was completed in 1946.",
            "The internet was initially created as a military project called ARPANET in the 1960s."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "Which company developed the Android operating system?",
                "options": ["Apple", "Google", "Microsoft", "Samsung"],
                "answer": "Google"
            },
            {
                "question": "What does the abbreviation 'RAM' stand for?",
                "options": ["Random Access Memory", "Rapid Access Memory", "Read Access Memory", "Reliable Access Memory"],
                "answer": "Random Access Memory"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza in Egypt were built around 2560-2540 BC.",
            "The first successful powered flight was made by the Wright brothers in 1903."
        ],
        "quiz_questions": [
            {
                "question": "In which year did the United States declare its independence?",
                "options": ["1776", "1789", "1812", "1865"],
                "answer": "1776"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
                "answer": "George Washington"
            },
            {
                "question": "Which ancient civilization built the city of Machu Picchu?",
                "options": ["Aztecs", "Incas", "Mayans", "Egyptians"],
                "answer": "Incas"
            }
        ]
    },
    "general": {
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
                "question": "What is the largest planet in our solar system?",
                "options": ["Earth", "Mars", "Jupiter", "Saturn"],
                "answer": "Jupiter"
            },
            {
                "question": "Which of these is not a primary color?",
                "options": ["Red", "Blue", "Yellow", "Green"],
                "answer": "Green"
            }
        ]
    }
}

def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    return input("Enter your choice: ").lower()

def display_fact(topic):
    fact = random.choice(topics[topic]["facts"])
    print(f"Here's a random fact about {topic.capitalize()}:")
    print(f"- {fact}")

def run_quiz(topic):
    print(f"Let's test your {topic.capitalize()} knowledge!")
    score = 0
    questions = topics[topic]["quiz_questions"]
    for question in questions:
        print(question["question"])
        for i, option in enumerate(question["options"], start=1):
            print(f"{i}. {option}")
        user_answer = input("Enter your answer (1-4): ")
        if question["options"][int(user_answer) - 1] == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score is {score} out of {len(questions)}.")

def main():
    topic = display_menu()
    display_fact(topic)
    run_quiz(topic)

if __name__ == "__main__":
    main()
