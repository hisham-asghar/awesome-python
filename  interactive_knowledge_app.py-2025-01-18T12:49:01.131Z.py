
import random
import requests
import json

# Define the topics and their associated facts and quizzes
topics = {
    "science": {
        "facts": [
            "The human body has around 100 trillion cells.",
            "The largest known prime number as of 2022 has 23 million digits.",
            "Neutron stars are the collapsed cores of massive stars, with a density greater than that of an atomic nucleus."
        ],
        "quizzes": [
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Jupiter", "Saturn", "Mars", "Venus"],
                "answer": 0
            },
            {
                "question": "Which scientist is known for developing the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Galileo Galilei"],
                "answer": 1
            },
            {
                "question": "What is the name of the process where water changes from a liquid to a gas?",
                "options": ["Condensation", "Evaporation", "Precipitation", "Transpiration"],
                "answer": 1
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, the ENIAC, was completed in 1946 and weighed over 30 tons.",
            "The world's first programmable computer, the Z1, was built by German engineer Konrad Zuse in 1936.",
            "The first commercial microprocessor, the Intel 4004, was released in 1971 and had a clock speed of 740 kHz."
        ],
        "quizzes": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "JavaScript"],
                "answer": 2
            },
            {
                "question": "Which company is known for developing the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": 2
            },
            {
                "question": "What is the name of the first successful commercial web browser?",
                "options": ["Mozilla Firefox", "Google Chrome", "Microsoft Internet Explorer", "Netscape Navigator"],
                "answer": 3
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Magna Carta, a document that established the principle of limited government, was signed in 1215.",
            "The Renaissance, a period of cultural, artistic, political, and scientific advancement, began in the 14th century in Italy."
        ],
        "quizzes": [
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomical knowledge?",
                "options": ["Babylonian", "Egyptian", "Greek", "Chinese"],
                "answer": 2
            },
            {
                "question": "Which event is known as the start of the American Revolutionary War?",
                "options": ["Battle of Lexington and Concord", "Boston Tea Party", "Declaration of Independence", "Battle of Saratoga"],
                "answer": 0
            },
            {
                "question": "Which ancient civilization is known for its advanced engineering, including the construction of the Hanging Gardens of Babylon?",
                "options": ["Mesopotamian", "Indus Valley", "Mayan", "Incan"],
                "answer": 0
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2022 has 23 million digits.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "A group of porcupines is called a prickle."
        ],
        "quizzes": [
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Liver", "Brain", "Skin"],
                "answer": 3
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": 2
            },
            {
                "question": "What is the name of the longest river in the world?",
                "options": ["Amazon", "Nile", "Mississippi", "Yangtze"],
                "answer": 1
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
    Runs the quiz and returns the user's score.
    """
    score = 0
    print(quiz["question"])
    for i, option in enumerate(quiz["options"]):
        print(f"{i+1}. {option}")
    user_answer = int(input("Enter your answer (1-4): ")) - 1
    if user_answer == quiz["answer"]:
        print("Correct!")
        score = 1
    else:
        print("Incorrect.")
    return score

def main():
    """
    The main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")
    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in topics:
        print(f"You selected: {selected_topic.capitalize()}")
        print(get_random_fact(selected_topic))
        quiz = get_quiz(selected_topic)
        score = run_quiz(quiz)
        print(f"Your score: {score} out of 1")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
