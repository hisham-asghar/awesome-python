
import random
import requests
import json

# Define the topics and their associated facts and quizzes
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Milky Way galaxy contains an estimated 100-400 billion stars.",
            "Bees can flap their wings up to 200 times per second."
        ],
        "quizzes": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            },
            {
                "question": "Which scientist is known for the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Marie Curie"],
                "answer": 1
            },
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Mars", "Saturn", "Jupiter", "Uranus"],
                "answer": 2
            }
        ]
    },
    "technology": {
        "facts": [
            "The first electronic computer, ENIAC, was unveiled in 1946 and weighed 30 tons.",
            "The first commercial smartphone was the IBM Simon, released in 1992.",
            "The internet was initially created for military communication and research purposes."
        ],
        "quizzes": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "Which company developed the first graphical user interface (GUI) for personal computers?",
                "options": ["Apple", "Microsoft", "IBM", "Xerox"],
                "answer": 3
            },
            {
                "question": "What is the name of the first web browser developed by Tim Berners-Lee?",
                "options": ["Mosaic", "Netscape Navigator", "Internet Explorer", "WorldWideWeb"],
                "answer": 3
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza in Egypt were built around 2560-2540 BC.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD."
        ],
        "quizzes": [
            {
                "question": "Which ancient civilization is known for their advanced mathematics and astronomy?",
                "options": ["Egyptians", "Greeks", "Mayans", "Chinese"],
                "answer": 1
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "Franklin D. Roosevelt"],
                "answer": 2
            },
            {
                "question": "Which event is considered the start of World War I?",
                "options": ["The assassination of Archduke Franz Ferdinand", "The bombing of Pearl Harbor", "The fall of the Berlin Wall", "The Cuban Missile Crisis"],
                "answer": 0
            }
        ]
    },
    "general": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal is the giraffe, which can reach heights of up to 6 meters (20 feet).",
            "The largest ocean on Earth is the Pacific Ocean, covering an area of about 63 million square miles."
        ],
        "quizzes": [
            {
                "question": "What is the largest continent in the world by land area?",
                "options": ["Asia", "Africa", "North America", "South America"],
                "answer": 0
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": 2
            },
            {
                "question": "Which planet in our solar system is known as the 'Red Planet'?",
                "options": ["Mars", "Venus", "Jupiter", "Saturn"],
                "answer": 0
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
    Runs the given quiz and returns the user's score.
    """
    score = 0
    print(quiz["question"])
    for i, option in enumerate(quiz["options"]):
        print(f"{i+1}. {option}")
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == quiz["answer"]:
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
    chosen_topic = input("Enter your choice: ").lower()

    if chosen_topic in topics:
        print(f"\nHere's a random fact about {chosen_topic.capitalize()}:")
        print(get_random_fact(chosen_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        quiz = get_random_quiz(chosen_topic)
        score = run_quiz(quiz)
        print(f"\nYour score: {score}/1")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
