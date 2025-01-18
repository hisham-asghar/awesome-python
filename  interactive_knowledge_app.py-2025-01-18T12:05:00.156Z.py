
import random
import requests
import json

# Define the topics and their respective facts and quizzes
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Hubble Space Telescope can see approximately 13.4 billion light-years away.",
            "Cats have fewer toes on their back paws than their front paws."
        ],
        "quizzes": [
            {
                "question": "What is the main function of the human heart?",
                "options": ["To pump blood throughout the body", "To digest food", "To control breathing"],
                "answer": 0
            },
            {
                "question": "Which planet in our solar system has the most moons?",
                "options": ["Jupiter", "Saturn", "Neptune"],
                "answer": 0
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 and had only one button.",
            "The first commercial microprocessor, the Intel 4004, was released in 1971.",
            "The internet was originally called ARPANET, which was developed in the 1960s by the U.S. Department of Defense."
        ],
        "quizzes": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "Python", "C++"],
                "answer": 1
            },
            {
                "question": "Which company is known for developing the Android operating system?",
                "options": ["Apple", "Microsoft", "Google"],
                "answer": 2
            },
            {
                "question": "What is the name of the first commercially successful web browser?",
                "options": ["Netscape Navigator", "Internet Explorer", "Mozilla Firefox"],
                "answer": 0
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa was painted by the Italian artist Leonardo da Vinci between 1503 and 1519.",
            "The first successful powered flight was made by the Wright brothers in 1903."
        ],
        "quizzes": [
            {
                "question": "What year did the American Civil War begin?",
                "options": ["1861", "1865", "1914"],
                "answer": 0
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "George Washington", "Thomas Jefferson"],
                "answer": 1
            },
            {
                "question": "In what year did the Berlin Wall fall?",
                "options": ["1989", "1991", "1995"],
                "answer": 0
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2021 has 23,249,425 digits.",
            "The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.",
            "The first Olympic Games were held in 776 BC in Olympia, Greece."
        ],
        "quizzes": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean"],
                "answer": 2
            },
            {
                "question": "Which country is known as the 'Land of the Rising Sun'?",
                "options": ["China", "Japan", "South Korea"],
                "answer": 1
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Saturn", "Jupiter", "Neptune"],
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
        print(f"{i}. {option}")
    user_answer = int(input("Enter your answer (0-2): "))
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
    for topic in topics:
        print(f"- {topic.capitalize()}")
    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        quiz = get_quiz(selected_topic)
        score = run_quiz(quiz)
        print(f"\nYour score: {score} out of 1")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
