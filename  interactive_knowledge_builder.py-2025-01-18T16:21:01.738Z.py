
import random
import requests
import json

# Define the topics and their corresponding facts and quizzes
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The largest known prime number as of 2022 has 23 million digits.",
            "The first successful kidney transplant was performed in 1954."
        ],
        "quizzes": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Hg"],
                "answer": 0
            },
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Mars", "Jupiter", "Saturn", "Neptune"],
                "answer": 1
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Evaporation"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 and had only one button.",
            "The first commercial text message was sent on December 3, 1992.",
            "The first smartphone was the IBM Simon, released in 1992."
        ],
        "quizzes": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "What is the name of the company that created the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": 2
            },
            {
                "question": "What is the name of the first commercially successful web browser?",
                "options": ["Netscape Navigator", "Internet Explorer", "Mozilla Firefox", "Google Chrome"],
                "answer": 0
            }
        ]
    },
    "history": {
        "facts": [
            "The first known written language was Sumerian cuneiform, developed in Mesopotamia around 3500 BC.",
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa was painted by Leonardo da Vinci between 1503 and 1519."
        ],
        "quizzes": [
            {
                "question": "Which ancient civilization is known for its pyramids?",
                "options": ["Aztec", "Inca", "Egyptian", "Mayan"],
                "answer": 2
            },
            {
                "question": "What was the name of the first successful powered flight, which took place in 1903?",
                "options": ["The Wright Flyer", "The Kitty Hawk", "The Spirit of St. Louis", "The Bleriot XI"],
                "answer": 0
            },
            {
                "question": "Which ancient Greek philosopher is known for his contributions to mathematics and philosophy?",
                "options": ["Plato", "Socrates", "Aristotle", "Pythagoras"],
                "answer": 3
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2022 has 23 million digits.",
            "The tallest known tree in the world is a coast redwood named Hyperion, standing at 380 feet.",
            "The largest known prime number as of 2022 has 23 million digits."
        ],
        "quizzes": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Pacific Ocean", "Indian Ocean", "Arctic Ocean"],
                "answer": 1
            },
            {
                "question": "What is the name of the longest river in the world?",
                "options": ["Amazon River", "Nile River", "Mississippi River", "Yangtze River"],
                "answer": 1
            },
            {
                "question": "What is the name of the largest continent on Earth?",
                "options": ["Asia", "Africa", "North America", "South America"],
                "answer": 0
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

def main():
    """
    Runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))

        print("\nNow, let's test your knowledge with a quiz!")
        quiz = get_quiz(selected_topic)
        print(quiz["question"])
        for i, option in enumerate(quiz["options"]):
            print(f"{i+1}. {option}")

        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer - 1 == quiz["answer"]:
            print("Correct! Well done.")
        else:
            print("Oops, that's not the right answer. Better luck next time!")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
