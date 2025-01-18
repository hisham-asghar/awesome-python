
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest planet in the solar system is Venus, not Mercury.",
            "Bees can fly higher than the tallest building."
        ],
        "quiz_questions": [
            {
                "question": "What is the main function of the human appendix?",
                "options": ["Digestion", "Immune system", "No known function", "Waste removal"],
                "answer": "No known function"
            },
            {
                "question": "Which of these is not a state of matter?",
                "options": ["Solid", "Liquid", "Gas", "Plasma"],
                "answer": "Plasma"
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A-", "B-", "AB-", "O-"],
                "answer": "AB-"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, weighed 30 tons and took up 1800 square feet.",
            "The first commercial smartphone was the IBM Simon, released in 1992.",
            "The first digital camera was invented in 1975 by Steven Sasson at Eastman Kodak."
        ],
        "quiz_questions": [
            {
                "question": "What was the name of the first web browser?",
                "options": ["Mosaic", "Netscape Navigator", "Internet Explorer", "WorldWideWeb"],
                "answer": "WorldWideWeb"
            },
            {
                "question": "Which company developed the first commercially successful smartphone?",
                "options": ["Apple", "BlackBerry", "Nokia", "IBM"],
                "answer": "BlackBerry"
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
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first successful powered flight lasted only 12 seconds and covered 120 feet."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for their advanced mathematics and astronomy?",
                "options": ["Egyptians", "Greeks", "Mayans", "Babylonians"],
                "answer": "Babylonians"
            },
            {
                "question": "What was the name of the first successful powered flight, made by the Wright brothers?",
                "options": ["The Flyer", "The Kitty Hawk", "The Wright Flyer", "The Airplane"],
                "answer": "The Wright Flyer"
            },
            {
                "question": "Which famous explorer is credited with discovering America?",
                "options": ["Christopher Columbus", "Vasco da Gama", "Ferdinand Magellan", "Marco Polo"],
                "answer": "Christopher Columbus"
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2022 has 23 million digits.",
            "The first product to have a barcode was Wrigley's gum.",
            "The first person convicted of speeding was going 8 mph."
        ],
        "quiz_questions": [
            {
                "question": "What is the rarest M&M color?",
                "options": ["Brown", "Yellow", "Red", "Blue"],
                "answer": "Brown"
            },
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Liver", "Skin", "Brain"],
                "answer": "Skin"
            },
            {
                "question": "What is the largest moon of Saturn?",
                "options": ["Titan", "Ganymede", "Callisto", "Europa"],
                "answer": "Titan"
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the given topic.
    """
    facts = topics[topic]["facts"]
    return random.choice(facts)

def get_quiz_question(topic):
    """
    Retrieves a random quiz question and its options from the given topic.
    """
    quiz_questions = topics[topic]["quiz_questions"]
    question = random.choice(quiz_questions)
    return question["question"], question["options"], question["answer"]

def run_interactive_knowledge_app():
    """
    Runs the interactive knowledge application.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in topics:
        print(f"\nYour selected topic is: {selected_topic.capitalize()}")
        print(get_random_fact(selected_topic))
        print("\nNow let's test your knowledge with a quiz!")

        question, options, answer = get_quiz_question(selected_topic)
        print(f"\n{question}")
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

        user_answer = input("Enter your answer (1-4): ")
        if options[int(user_answer) - 1] == answer:
            print("Correct! You're a knowledge master.")
        else:
            print(f"Incorrect. The correct answer is: {answer}")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    run_interactive_knowledge_app()
