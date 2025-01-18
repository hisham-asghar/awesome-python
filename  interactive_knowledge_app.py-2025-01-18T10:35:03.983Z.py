
import random
import requests
import json

# Define the topics and their respective facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The largest known prime number as of 2022 has 23 million digits.",
            "The deepest known cave in the world is Veryovkina Cave in Abkhazia, Georgia, with a depth of 2,212 meters (7,257 feet)."
        ],
        "quiz": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            },
            {
                "question": "What is the name of the theory that describes the relationship between energy and matter?",
                "options": ["Quantum theory", "Relativity theory", "String theory", "Big Bang theory"],
                "answer": 0
            },
            {
                "question": "What is the name of the scientist who developed the theory of general relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Marie Curie"],
                "answer": 1
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The first email was sent in 1971 by Ray Tomlinson.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989."
        ],
        "quiz": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "What is the name of the company that developed the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": 2
            },
            {
                "question": "What is the name of the device that converts digital signals into analog signals?",
                "options": ["Modem", "Router", "Switch", "Amplifier"],
                "answer": 0
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza in Egypt was built around 2560–2540 BCE.",
            "The Roman Empire lasted from 27 BCE to 476 CE.",
            "The first successful powered flight was made by the Wright brothers in 1903."
        ],
        "quiz": [
            {
                "question": "What was the name of the first president of the United States?",
                "options": ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "Franklin D. Roosevelt"],
                "answer": 2
            },
            {
                "question": "What was the name of the war that took place from 1939 to 1945?",
                "options": ["World War I", "World War II", "Korean War", "Vietnam War"],
                "answer": 1
            },
            {
                "question": "What was the name of the ancient civilization that built the Machu Picchu ruins?",
                "options": ["Aztec", "Inca", "Maya", "Olmec"],
                "answer": 1
            }
        ]
    },
    "general": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal is the giraffe.",
            "The largest ocean on Earth is the Pacific Ocean."
        ],
        "quiz": [
            {
                "question": "What is the name of the largest continent on Earth?",
                "options": ["Asia", "Africa", "North America", "Europe"],
                "answer": 0
            },
            {
                "question": "What is the name of the largest river in the world?",
                "options": ["Amazon River", "Nile River", "Mississippi River", "Yangtze River"],
                "answer": 1
            },
            {
                "question": "What is the name of the currency used in Japan?",
                "options": ["Dollar", "Euro", "Yen", "Pound"],
                "answer": 2
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

def get_quiz_question(topic):
    """
    Retrieves a random quiz question from the selected topic.
    """
    quiz_questions = topics[topic]["quiz"]
    question = random.choice(quiz_questions)
    return question

def run_quiz(topic):
    """
    Runs the interactive quiz for the selected topic.
    """
    question = get_quiz_question(topic)
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == question["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is", question["options"][question["answer"]])

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
        print(f"\nFact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nNow let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
