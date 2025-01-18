
import random
import requests
import json

# Define the topics and their associated facts/quizzes
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "A group of porcupines is called a prickle."
        ],
        "quizzes": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Fe", "Cu"],
                "answer": "Au"
            },
            {
                "question": "Which planet in our solar system has the most moons?",
                "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
                "answer": "Saturn"
            },
            {
                "question": "What is the name of the largest moon of Saturn?",
                "options": ["Titan", "Ganymede", "Callisto", "Io"],
                "answer": "Titan"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 and cost $15,000.",
            "The first text message was sent on December 3, 1992, and said 'Merry Christmas'.",
            "The first commercial jet flight took place on July 27, 1949, with the de Havilland Comet."
        ],
        "quizzes": [
            {
                "question": "What is the name of the first programmable computer?",
                "options": ["ENIAC", "UNIVAC", "Z1", "MARK I"],
                "answer": "ENIAC"
            },
            {
                "question": "Which company developed the first commercial smartphone?",
                "options": ["Apple", "Samsung", "Nokia", "BlackBerry"],
                "answer": "BlackBerry"
            },
            {
                "question": "What is the name of the first internet-connected appliance?",
                "options": ["Toaster", "Refrigerator", "Microwave", "Dishwasher"],
                "answer": "Toaster"
            }
        ]
    },
    "history": {
        "facts": [
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first commercial flight took place on January 1, 1914, from St. Petersburg, Florida, to Tampa, Florida.",
            "The Great Wall of China is the only man-made structure visible from space."
        ],
        "quizzes": [
            {
                "question": "What year was the Declaration of Independence signed?",
                "options": ["1776", "1789", "1812", "1865"],
                "answer": "1776"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
                "answer": "George Washington"
            },
            {
                "question": "What was the name of the first successful powered flight?",
                "options": ["The Wright Flyer", "The Spirit of St. Louis", "The Concorde", "The Apollo 11"],
                "answer": "The Wright Flyer"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The Eiffel Tower can be 15 cm taller during the summer, as the hot weather causes the iron to expand.",
            "A 'jiffy' is an actual unit of time, equivalent to one-thousandth of a second.",
            "The first product to have a barcode was Wrigley's gum."
        ],
        "quizzes": [
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Liver", "Skin", "Brain"],
                "answer": "Skin"
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": "AB"
            },
            {
                "question": "What is the name of the tallest mountain in the world?",
                "options": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
                "answer": "Mount Everest"
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

def get_random_quiz(topic):
    """
    Retrieves a random quiz from the specified topic.
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
    return user_answer.strip()

def main():
    """
    Runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    chosen_topic = input("Enter your choice: ").lower()

    if chosen_topic in topics:
        print(f"\nHere's a random fact about {chosen_topic.capitalize()}:")
        print(get_random_fact(chosen_topic))

        print("\nNow, let's test your knowledge with a quiz!")
        quiz = get_random_quiz(chosen_topic)
        user_answer = run_quiz(quiz)
        if user_answer == quiz["answer"]:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {quiz['answer']}.")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
