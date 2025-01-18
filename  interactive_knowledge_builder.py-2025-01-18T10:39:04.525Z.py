
import random
import requests
import json

# Dictionary to store topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The largest known prime number as of 2022 has 23 million digits.",
            "Neutron stars are the collapsed cores of massive stars, with a density of over a billion tons per cubic centimeter."
        ],
        "quiz_questions": [
            {
                "question": "What is the speed of light in a vacuum?",
                "options": ["300,000 km/s", "186,000 mi/s", "Both A and B", "None of the above"],
                "answer": "Both A and B"
            },
            {
                "question": "What is the name of the largest known prime number as of 2022?",
                "options": ["Mersenne Prime", "Fermat Prime", "Euler Prime", "Leech Prime"],
                "answer": "Mersenne Prime"
            },
            {
                "question": "What is the main function of a neutron star?",
                "options": ["Emitting light", "Absorbing matter", "Collapsing under its own gravity", "Repelling other stars"],
                "answer": "Collapsing under its own gravity"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer bug was a real moth found trapped in a Harvard Mark II computer in 1947.",
            "The largest hard drive ever made was 60 terabytes, released by Seagate in 2016.",
            "The first electronic computer, ENIAC, was completed in 1946 and weighed 30 tons."
        ],
        "quiz_questions": [
            {
                "question": "What was the name of the first computer bug?",
                "options": ["Moth", "Beetle", "Fly", "Caterpillar"],
                "answer": "Moth"
            },
            {
                "question": "What was the weight of the first electronic computer, ENIAC?",
                "options": ["10 tons", "20 tons", "30 tons", "40 tons"],
                "answer": "30 tons"
            },
            {
                "question": "What was the capacity of the largest hard drive ever made?",
                "options": ["10 TB", "30 TB", "60 TB", "100 TB"],
                "answer": "60 TB"
            }
        ]
    },
    "history": {
        "facts": [
            "The first Olympic Games were held in 776 BC in Olympia, Greece.",
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off."
        ],
        "quiz_questions": [
            {
                "question": "In what year were the first Olympic Games held?",
                "options": ["500 BC", "776 BC", "1000 BC", "1200 BC"],
                "answer": "776 BC"
            },
            {
                "question": "What is the length of the Great Wall of China?",
                "options": ["5,000 miles", "8,000 miles", "13,000 miles", "20,000 miles"],
                "answer": "13,000 miles"
            },
            {
                "question": "Why did the Mona Lisa have no eyebrows?",
                "options": ["It was a fashion trend", "She lost them in an accident", "The painter forgot to add them", "It was a stylistic choice"],
                "answer": "It was a fashion trend"
            }
        ]
    },
    "general": {
        "facts": [
            "The first person convicted of speeding was going 8 mph.",
            "A group of porcupines is called a prickle.",
            "The first product to have a barcode was Wrigley's gum."
        ],
        "quiz_questions": [
            {
                "question": "What was the speed of the first person convicted of speeding?",
                "options": ["5 mph", "8 mph", "10 mph", "15 mph"],
                "answer": "8 mph"
            },
            {
                "question": "What is a group of porcupines called?",
                "options": ["A quill", "A prickle", "A spike", "A quiver"],
                "answer": "A prickle"
            },
            {
                "question": "What was the first product to have a barcode?",
                "options": ["Coca-Cola", "Wrigley's gum", "Bread", "Milk"],
                "answer": "Wrigley's gum"
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

def get_quiz_question(topic):
    """
    Retrieves a random quiz question from the selected topic.
    """
    quiz_questions = topics[topic]["quiz_questions"]
    question = random.choice(quiz_questions)
    return question

def run_quiz(topic):
    """
    Runs a quiz for the selected topic, with multiple-choice questions.
    """
    score = 0
    num_questions = 3
    for _ in range(num_questions):
        question = get_quiz_question(topic)
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = input("Enter the number of your answer: ")
        if question["options"][int(user_answer) - 1] == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", question["answer"])
    print(f"Your final score is: {score}/{num_questions}")

def main():
    """
    The main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()
    if selected_topic not in topics:
        print("Invalid topic. Please try again.")
        return

    print(f"You've selected the {selected_topic.capitalize()} topic.")
    print(get_random_fact(selected_topic))
    print("Now, let's test your knowledge with a quiz!")
    run_quiz(selected_topic)

if __name__ == "__main__":
    main()
