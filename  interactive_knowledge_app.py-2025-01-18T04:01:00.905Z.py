
import random
import requests
import json

# Define the topics and their respective facts and quizzes
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The first successful organ transplant was a kidney transplant performed in 1954.",
            "Honey is the only food that does not spoil."
        ],
        "quizzes": [
            {
                "question": "What is the main function of the human heart?",
                "options": ["To pump blood", "To produce insulin", "To filter waste"],
                "answer": 0
            },
            {
                "question": "Which of these is not a state of matter?",
                "options": ["Solid", "Liquid", "Plasma", "Energy"],
                "answer": 3
            },
            {
                "question": "What is the name of the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The world's first website was launched on August 6, 1991.",
            "The first digital camera was developed by Kodak in 1975."
        ],
        "quizzes": [
            {
                "question": "What does 'RAM' stand for?",
                "options": ["Random Access Memory", "Rapid Access Memory", "Read Access Memory", "Rapid Assimilation Memory"],
                "answer": 0
            },
            {
                "question": "Which company developed the first commercially successful smartphone?",
                "options": ["Apple", "Samsung", "BlackBerry", "Nokia"],
                "answer": 2
            },
            {
                "question": "What is the name of the programming language used to build websites?",
                "options": ["Java", "Python", "HTML", "C++"],
                "answer": 2
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world.",
            "The Pyramids of Giza in Egypt were built around 2560-2540 BC.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD."
        ],
        "quizzes": [
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Mesopotamia", "Greece", "Egypt", "China"],
                "answer": 0
            },
            {
                "question": "What was the name of the first president of the United States?",
                "options": ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "Franklin D. Roosevelt"],
                "answer": 2
            },
            {
                "question": "Which event marked the end of World War I?",
                "options": ["The Treaty of Versailles", "The attack on Pearl Harbor", "The dropping of the atomic bombs", "The fall of the Berlin Wall"],
                "answer": 0
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal in the world is the giraffe.",
            "The longest river in the world is the Nile River in Africa."
        ],
        "quizzes": [
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Earth", "Mars", "Jupiter", "Saturn"],
                "answer": 2
            },
            {
                "question": "What is the currency used in Japan?",
                "options": ["Dollar", "Euro", "Yen", "Pound"],
                "answer": 2
            },
            {
                "question": "Which of these is not a primary color?",
                "options": ["Red", "Blue", "Yellow", "Green"],
                "answer": 3
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

def get_quiz(topic):
    """
    Retrieves a random quiz from the specified topic.
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
    user_answer = int(input("Enter your answer (0-3): "))
    if user_answer == quiz["answer"]:
        print("Correct!")
        score = 1
    else:
        print("Incorrect.")
    return score

def main():
    """
    Main function that runs the interactive knowledge app.
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
        print(f"\nYour score is: {score} out of 1")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
