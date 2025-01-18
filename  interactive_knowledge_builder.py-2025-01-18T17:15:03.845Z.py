
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has over 600 muscles.",
            "The Milky Way galaxy contains an estimated 100-400 billion stars.",
            "The first successful kidney transplant was performed in 1954."
        ],
        "quiz": [
            {
                "question": "What is the name of the chemical element with the symbol 'H'?",
                "options": ["Helium", "Hydrogen", "Helium", "Hydron"],
                "answer": 1
            },
            {
                "question": "What is the name of the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Evaporation"],
                "answer": 0
            },
            {
                "question": "What is the name of the force that attracts objects with mass towards each other?",
                "options": ["Gravity", "Friction", "Electromagnetic force", "Strong nuclear force"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989.",
            "The first smartphone was the IBM Simon, released in 1992."
        ],
        "quiz": [
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
                "question": "What is the name of the device used to input data into a computer?",
                "options": ["Keyboard", "Monitor", "Printer", "Mouse"],
                "answer": 3
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza was built around 2560–2540 BC.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.",
            "The Gutenberg Bible, the first printed book in the West, was published in 1455."
        ],
        "quiz": [
            {
                "question": "What is the name of the ancient Greek philosopher who is considered the father of Western philosophy?",
                "options": ["Plato", "Aristotle", "Socrates", "Pythagoras"],
                "answer": 2
            },
            {
                "question": "What is the name of the event that marked the beginning of World War I?",
                "options": ["The assassination of Archduke Franz Ferdinand", "The bombing of Pearl Harbor", "The fall of the Berlin Wall", "The Cuban Missile Crisis"],
                "answer": 0
            },
            {
                "question": "What is the name of the ancient Egyptian queen known for her beauty and power?",
                "options": ["Nefertiti", "Cleopatra", "Hatshepsut", "Neferkare"],
                "answer": 1
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2022 has 23.3 million digits.",
            "The tallest known tree in the world is a coast redwood named Hyperion, measuring 115.7 meters (379.7 feet) tall.",
            "The first commercial airline flight took place on January 1, 1914, between St. Petersburg and Tampa, Florida."
        ],
        "quiz": [
            {
                "question": "What is the name of the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "What is the name of the currency used in the United States?",
                "options": ["Euro", "Pound", "Yen", "Dollar"],
                "answer": 3
            },
            {
                "question": "What is the name of the largest continent in the world?",
                "options": ["Africa", "Asia", "Europe", "North America"],
                "answer": 1
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

def get_quiz_question(topic):
    """
    Retrieves a random quiz question from the specified topic.
    """
    quiz_questions = topics[topic]["quiz"]
    question = random.choice(quiz_questions)
    return question

def run_quiz(topic):
    """
    Runs a quiz for the specified topic.
    """
    question = get_quiz_question(topic)
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == question["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", question["options"][question["answer"]])

def main():
    """
    Main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print(f"You selected the {selected_topic.capitalize()} topic.")
        print(get_random_fact(selected_topic))
        print("\nNow let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
