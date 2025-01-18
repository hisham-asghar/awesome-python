Here is the raw Python code extracted from the JSON:

```python
import random
import json
import requests

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Milky Way galaxy contains an estimated 100 to 400 billion stars.",
            "The first successful kidney transplant was performed in 1954."
        ],
        "quiz": [
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Evaporation"],
                "answer": 0
            },
            {
                "question": "Which scientist is known for the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Galileo Galilei"],
                "answer": 1
            },
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Mars", "Saturn", "Jupiter", "Neptune"],
                "answer": 2
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The internet was originally called ARPANET, established in 1969.",
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
                "question": "What is the name of the technology that allows devices to connect to the internet wirelessly?",
                "options": ["Ethernet", "Bluetooth", "Wi-Fi", "NFC"],
                "answer": 2
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers.",
            "The Eiffel Tower was built in 1889 as the entrance arch to the World's Fair."
        ],
        "quiz": [
            {
                "question": "Which ancient civilization is known for their advanced mathematics and astronomy?",
                "options": ["Egyptians", "Greeks", "Mayans", "Chinese"],
                "answer": 1
            },
            {
                "question": "What was the name of the first successful computer, built in 1936?",
                "options": ["ENIAC", "Colossus", "UNIVAC", "Z1"],
                "answer": 3
            },
            {
                "question": "Which event marked the end of World War II in Europe?",
                "options": ["D-Day", "VE Day", "Pearl Harbor", "Hiroshima bombing"],
                "answer": 1
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2021 has 23,249,425 digits.",
            "The tallest mammal is the giraffe, which can grow up to 18 feet tall.",
            "The oldest known living organism is a bristlecone pine tree in California, estimated to be over 5,000 years old."
        ],
        "quiz": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": 2
            },
            {
                "question": "What is the name of the largest moon of Saturn?",
                "options": ["Titan", "Ganymede", "Callisto", "Io"],
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

def get_quiz_question(topic):
    """
    Retrieves a random quiz question from the specified topic.
    """
    quiz_question = random.choice(topics[topic]["quiz"])
    return quiz_question["question"], quiz_question["options"], quiz_question["answer"]

def run_interactive_knowledge_app():
    """
    Runs the interactive knowledge application.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()
    if selected_topic not in topics:
        print("Invalid topic. Please try again.")
        return

    print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
    print(get_random_fact(selected_topic))

    print("\nNow, let's test your knowledge with a quiz!")
    question, options, answer = get_quiz_question(selected_topic)
    print(question)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == answer:
        print("Correct!")
    else:
        print("Incorrect. Better luck next time!")

    print("\nThank you for using the Interactive Knowledge App!")

if __name__ == "__main__":
    run_interactive_knowledge_app()
