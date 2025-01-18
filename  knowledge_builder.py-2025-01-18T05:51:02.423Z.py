
import random
import requests
import json

# Define the topics and their corresponding facts/quizzes
topics = {
    "science": {
        "facts": [
            "The human body has about 60,000 miles of blood vessels.",
            "The largest known prime number as of 2022 has 23 million digits.",
            "The Milky Way galaxy contains an estimated 100 to 400 billion stars."
        ],
        "quizzes": [
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Jupiter", "Saturn", "Mars", "Venus"],
                "answer": 0
            },
            {
                "question": "Which element is the most abundant in the Earth's crust?",
                "options": ["Oxygen", "Silicon", "Aluminum", "Iron"],
                "answer": 0
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
            "The first computer virus, called 'Creeper', was created in 1971.",
            "The first commercial microprocessor was the Intel 4004, released in 1971.",
            "The internet was originally called ARPANET, and was developed in the 1960s by the U.S. Department of Defense."
        ],
        "quizzes": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "What is the name of the device that converts digital signals into analog signals?",
                "options": ["Modem", "Router", "Switch", "Codec"],
                "answer": 3
            },
            {
                "question": "Which company developed the first commercial graphical user interface (GUI) for personal computers?",
                "options": ["Apple", "Microsoft", "IBM", "Xerox"],
                "answer": 3
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers.",
            "The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci between 1503 and 1519."
        ],
        "quizzes": [
            {
                "question": "What was the name of the first successful powered flight?",
                "options": ["The Wright Flyer", "The Kitty Hawk", "The Biplane", "The Glider"],
                "answer": 0
            },
            {
                "question": "Which ancient civilization is known for building the Pyramids of Giza?",
                "options": ["Mesopotamia", "Indus Valley", "Aztec", "Ancient Egypt"],
                "answer": 3
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
                "answer": 2
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The largest moon of Saturn is Titan, which is larger than the planet Mercury.",
            "The tallest mammal in the world is the giraffe, which can grow up to 18 feet tall."
        ],
        "quizzes": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
                "answer": 0
            },
            {
                "question": "Which of the following is not a primary color?",
                "options": ["Red", "Blue", "Yellow", "Green"],
                "answer": 3
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": 2
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
    for i, option in enumerate(quiz["options"]):
        print(f"{i+1}. {option}")
    
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == quiz["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz["options"][quiz["answer"]])

def main():
    """
    The main function that runs the interactive knowledge-building script.
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
        run_quiz(get_random_quiz(chosen_topic))
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
