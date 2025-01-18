
import random
import requests
import json

# Define the topics and their corresponding facts and quizzes
topics = {
    "science": {
        "facts": [
            "The human brain has approximately 86 billion neurons.",
            "The largest known prime number as of 2022 has 23 million digits.",
            "The hottest planet in the Solar System is Venus, with an average surface temperature of 462°C (864°F)."
        ],
        "quizzes": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "What is the name of the largest moon of Saturn?",
                "options": ["Titan", "Ganymede", "Callisto", "Europa"],
                "answer": "Titan"
            },
            {
                "question": "Which scientist is known for developing the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Galileo Galilei"],
                "answer": "Albert Einstein"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented by Douglas Engelbart in 1964.",
            "The first commercial email service was launched by CompuServe in 1979.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989."
        ],
        "quizzes": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "Which company developed the first commercially successful smartphone?",
                "options": ["Apple", "Samsung", "Nokia", "BlackBerry"],
                "answer": "BlackBerry"
            },
            {
                "question": "What is the name of the first programmable computer?",
                "options": ["ENIAC", "UNIVAC", "MARK I", "COLOSSUS"],
                "answer": "ENIAC"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 21,000 kilometers (13,000 miles).",
            "The Pyramids of Giza in Egypt were built around 2560-2540 BCE, making them over 4,500 years old.",
            "The Roman Empire lasted for over 400 years, from the 27 BC to 476 AD."
        ],
        "quizzes": [
            {
                "question": "What was the name of the ancient Egyptian civilization's writing system?",
                "options": ["Hieroglyphics", "Cuneiform", "Runes", "Pictographs"],
                "answer": "Hieroglyphics"
            },
            {
                "question": "Which ancient Greek philosopher is known for his contributions to mathematics and philosophy?",
                "options": ["Plato", "Aristotle", "Socrates", "Pythagoras"],
                "answer": "Pythagoras"
            },
            {
                "question": "What was the name of the first permanent English settlement in North America?",
                "options": ["Jamestown", "Plymouth Colony", "Massachusetts Bay Colony", "New Amsterdam"],
                "answer": "Jamestown"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest ocean on Earth is the Pacific Ocean, covering an area of about 63 million square miles.",
            "The highest mountain in the world is Mount Everest, with a peak elevation of 29,032 feet (8,849 meters) above sea level.",
            "The largest mammal on Earth is the blue whale, which can grow up to 30 meters (98 feet) in length and weigh up to 180 metric tons."
        ],
        "quizzes": [
            {
                "question": "What is the largest continent by land area?",
                "options": ["Asia", "Africa", "North America", "South America"],
                "answer": "Asia"
            },
            {
                "question": "What is the smallest planet in our solar system?",
                "options": ["Mercury", "Venus", "Mars", "Pluto"],
                "answer": "Mercury"
            },
            {
                "question": "What is the currency used in Japan?",
                "options": ["Yen", "Dollar", "Euro", "Pound"],
                "answer": "Yen"
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
    Runs the quiz and returns the user's score.
    """
    score = 0
    print(quiz["question"])
    for option in quiz["options"]:
        print(f"- {option}")
    user_answer = input("Enter your answer: ")
    if user_answer.lower() == quiz["answer"].lower():
        print("Correct!")
        score = 1
    else:
        print("Incorrect. The correct answer is:", quiz["answer"])
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
        print("\nHere's a random fact about", selected_topic.capitalize() + ":")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        quiz = get_random_quiz(selected_topic)
        score = run_quiz(quiz)
        print(f"Your score: {score} out of 1")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
