
import random
import requests
import json

# Dictionary to store topics and their corresponding facts and quizzes
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest temperature ever recorded on Earth was 154°F (68°C) in Death Valley, California.",
            "Cats have fewer toes on their back paws than their front paws."
        ],
        "quizzes": [
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
                "question": "What is the name of the theory that explains how species evolve over time?",
                "options": ["Relativity", "Quantum Mechanics", "Atomic Theory", "Natural Selection"],
                "answer": "Natural Selection"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, weighed 30 tons and took up 1800 square feet of space.",
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The first microprocessor, the Intel 4004, was released in 1971 and had 2,300 transistors."
        ],
        "quizzes": [
            {
                "question": "Which company developed the first commercially successful smartphone?",
                "options": ["Apple", "Samsung", "BlackBerry", "Nokia"],
                "answer": "BlackBerry"
            },
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "Which technology company was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne?",
                "options": ["Microsoft", "Amazon", "Google", "Apple"],
                "answer": "Apple"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza in Egypt were built around 2560–2540 BC, and are the oldest and largest of the three pyramids.",
            "The Eiffel Tower was built in 1889 for the Paris World's Fair and was the tallest structure in the world at the time."
        ],
        "quizzes": [
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Mesopotamia", "Egypt", "Greece", "China"],
                "answer": "Mesopotamia"
            },
            {
                "question": "Which event marked the end of World War II in Europe?",
                "options": ["D-Day Invasion", "Battle of Stalingrad", "Fall of Berlin", "Atomic Bombings of Hiroshima and Nagasaki"],
                "answer": "Fall of Berlin"
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
            "The largest known prime number as of 2023 has 23,249,425 digits.",
            "The tallest mammal is the giraffe, which can grow up to 18 feet tall.",
            "The largest known prime number as of 2023 has 23,249,425 digits."
        ],
        "quizzes": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "Which country is known as the Land of the Rising Sun?",
                "options": ["China", "Japan", "South Korea", "India"],
                "answer": "Japan"
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
    return random.choice(topics[topic]["facts"])

def get_random_quiz(topic):
    """
    Retrieves a random quiz from the specified topic.
    """
    return random.choice(topics[topic]["quizzes"])

def run_quiz(quiz):
    """
    Runs the specified quiz and returns the user's score.
    """
    score = 0
    print(quiz["question"])
    for i, option in enumerate(quiz["options"]):
        print(f"{i+1}. {option}")
    user_answer = input("Enter your answer (1-4): ")
    if quiz["options"][int(user_answer) - 1] == quiz["answer"]:
        print("Correct!")
        score = 1
    else:
        print("Incorrect. The correct answer is:", quiz["answer"])
    return score

def main():
    """
    Main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    while True:
        print("\nSelect a topic:")
        for topic in topics.keys():
            print(f"- {topic.capitalize()}")
        chosen_topic = input("Enter your choice: ").lower()
        if chosen_topic not in topics:
            print("Invalid topic. Please try again.")
            continue

        print("\nHere's a random fact about", chosen_topic.capitalize() + ":")
        print(get_random_fact(chosen_topic))

        print("\nNow, let's test your knowledge with a quiz!")
        quiz = get_random_quiz(chosen_topic)
        score = run_quiz(quiz)
        print(f"Your score: {score} out of 1")

        if input("Do you want to try another topic? (y/n) ").lower() != "y":
            break

if __name__ == "__main__":
    main()
