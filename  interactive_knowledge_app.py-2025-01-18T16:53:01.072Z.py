
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has over 60,000 miles of blood vessels.",
            "The hottest planet in the solar system is Venus, not Mercury.",
            "Sharks have been around for over 400 million years, predating the dinosaurs."
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Evaporation"],
                "answer": "Photosynthesis"
            },
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Saturn", "Jupiter", "Uranus", "Neptune"],
                "answer": "Jupiter"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented by Douglas Engelbart in 1964.",
            "The world's first webcam was used to monitor a coffee pot at the University of Cambridge.",
            "The first commercial text message was sent on December 3, 1992."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "What is the name of the popular search engine owned by Alphabet Inc.?",
                "options": ["Bing", "Yahoo", "Google", "DuckDuckGo"],
                "answer": "Google"
            },
            {
                "question": "What is the name of the social media platform that allows users to share short videos?",
                "options": ["Instagram", "Twitter", "TikTok", "Snapchat"],
                "answer": "TikTok"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The first successful powered flight by the Wright brothers took place on December 17, 1903.",
            "The Mona Lisa was painted by the famous Italian artist Leonardo da Vinci."
        ],
        "quiz_questions": [
            {
                "question": "In what year was the United States Declaration of Independence signed?",
                "options": ["1776", "1789", "1812", "1865"],
                "answer": "1776"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "Franklin D. Roosevelt"],
                "answer": "George Washington"
            },
            {
                "question": "Which ancient civilization is known for its impressive pyramids?",
                "options": ["Mesopotamia", "Aztec", "Maya", "Ancient Egypt"],
                "answer": "Ancient Egypt"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The tallest mammal in the world is the giraffe.",
            "The largest ocean on Earth is the Pacific Ocean.",
            "The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion meaning the iron heats up, the particles get further apart and the tower grows."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Saturn", "Jupiter", "Uranus", "Neptune"],
                "answer": "Jupiter"
            },
            {
                "question": "What is the capital city of Australia?",
                "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
                "answer": "Canberra"
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
    Retrieves a random quiz question from the specified topic.
    """
    quiz_questions = topics[topic]["quiz_questions"]
    question = random.choice(quiz_questions)
    return question

def run_quiz(topic):
    """
    Runs a quiz for the specified topic.
    """
    question = get_quiz_question(topic)
    print(f"Question: {question['question']}")
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    
    user_answer = input("Enter the number of your answer: ")
    if question["options"][int(user_answer) - 1] == question["answer"]:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {question['answer']}.")

def main():
    """
    Main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your topic choice: ").lower()
    
    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nNow let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
