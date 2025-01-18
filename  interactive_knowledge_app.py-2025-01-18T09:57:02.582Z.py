
import random
import requests
import json

# Define the topics and their corresponding facts/quizzes
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest planet in the solar system is Venus, not Mercury.",
            "Bees can fly higher than the tallest building."
        ],
        "quizzes": [
            {
                "question": "What is the main function of the human heart?",
                "options": ["To pump blood", "To filter waste", "To produce oxygen"],
                "answer": "To pump blood"
            },
            {
                "question": "Which of these is not a state of matter?",
                "options": ["Solid", "Liquid", "Plasma", "Energy"],
                "answer": "Energy"
            },
            {
                "question": "What is the name of the largest moon of Saturn?",
                "options": ["Titan", "Ganymede", "Europa", "Callisto"],
                "answer": "Titan"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, weighed 30 tons and took up 1,800 square feet.",
            "The first iPhone was released in 2007.",
            "The internet was originally called ARPANET and was created by the US Department of Defense."
        ],
        "quizzes": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "Which company created the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": "Google"
            },
            {
                "question": "What is the name of the first commercially successful web browser?",
                "options": ["Netscape Navigator", "Internet Explorer", "Mozilla Firefox", "Google Chrome"],
                "answer": "Netscape Navigator"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza were built around 2560–2540 BC.",
            "The first successful powered flight was made by the Wright brothers in 1903."
        ],
        "quizzes": [
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Egyptians", "Greeks", "Mayans", "Mesopotamians"],
                "answer": "Mesopotamians"
            },
            {
                "question": "Which event marked the end of World War II?",
                "options": ["The D-Day landings", "The bombing of Hiroshima and Nagasaki", "The fall of Berlin", "The surrender of Japan"],
                "answer": "The surrender of Japan"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
                "answer": "George Washington"
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2022 has 23 million digits.",
            "The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.",
            "The largest known star in the universe is VY Canis Majoris, which is over 1,500 times the size of the Sun."
        ],
        "quizzes": [
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": "AB"
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "What is the name of the longest river in the world?",
                "options": ["Nile River", "Amazon River", "Yangtze River", "Mississippi River"],
                "answer": "Nile River"
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
    return random.choice(quizzes)

def run_quiz(quiz):
    """
    Runs the interactive quiz for the user.
    """
    print(quiz["question"])
    for i, option in enumerate(quiz["options"], start=1):
        print(f"{i}. {option}")

    while True:
        user_answer = input("Enter your answer (1-4): ")
        if user_answer.isdigit() and 1 <= int(user_answer) <= len(quiz["options"]):
            if quiz["options"][int(user_answer) - 1] == quiz["answer"]:
                print("Correct!")
            else:
                print("Incorrect. The correct answer is:", quiz["answer"])
            break
        else:
            print("Invalid input. Please try again.")

def main():
    """
    Main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    while True:
        user_topic = input("Enter your choice: ").lower()
        if user_topic in topics:
            print("\nHere's a random fact about", user_topic.capitalize() + ":")
            print(get_random_fact(user_topic))
            print("\nNow, let's test your knowledge with a quiz!")
            run_quiz(get_random_quiz(user_topic))
            break
        else:
            print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
