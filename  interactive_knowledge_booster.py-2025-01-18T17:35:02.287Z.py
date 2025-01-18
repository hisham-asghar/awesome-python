
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has over 600 muscles.",
            "The largest known prime number has over 23 million digits.",
            "Ants stretch when they wake up and yawn in the same way that humans do."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the force that attracts objects with mass towards each other?",
                "options": ["Friction", "Gravity", "Magnetism", "Electromagnetism"],
                "answer": 1
            },
            {
                "question": "Which scientist is known for developing the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Galileo Galilei"],
                "answer": 1
            },
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Mars", "Jupiter", "Saturn", "Uranus"],
                "answer": 1
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer virus, called 'Creeper', was created as an experiment in 1971.",
            "The first commercial smartphone was the IBM Simon, released in 1992.",
            "The first electronic computer, ENIAC, was completed in 1946 and weighed over 30 tons."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "What is the name of the company that created the first commercially successful personal computer?",
                "options": ["Apple", "Microsoft", "IBM", "Dell"],
                "answer": 2
            },
            {
                "question": "What is the name of the technology that allows devices to communicate wirelessly?",
                "options": ["Ethernet", "Wi-Fi", "Bluetooth", "NFC"],
                "answer": 1
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for building the Pyramids?",
                "options": ["Aztecs", "Incas", "Egyptians", "Mayans"],
                "answer": 2
            },
            {
                "question": "Which event marked the end of World War II?",
                "options": ["The D-Day Invasion", "The Atomic Bombings of Hiroshima and Nagasaki", "The Battle of Stalingrad", "The Fall of Berlin"],
                "answer": 1
            },
            {
                "question": "Who is considered the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
                "answer": 2
            }
        ]
    },
    "general": {
        "facts": [
            "A group of flamingos is called a flamboyance.",
            "The first product to have a barcode was Wrigley's gum.",
            "The King of Hearts is the only king without a mustache on a standard playing card."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Arctic Ocean", "Indian Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "What is the name of the largest mammal on Earth?",
                "options": ["Elephant", "Whale", "Giraffe", "Hippopotamus"],
                "answer": 1
            },
            {
                "question": "What is the name of the smallest continent in the world?",
                "options": ["Australia", "Europe", "Asia", "Antarctica"],
                "answer": 0
            }
        ]
    }
}

def get_random_fact(topic):
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    quiz_question = random.choice(topics[topic]["quiz_questions"])
    return quiz_question

def run_quiz(topic):
    quiz_question = get_quiz_question(topic)
    print(quiz_question["question"])
    for i, option in enumerate(quiz_question["options"]):
        print(f"{i+1}. {option}")
    
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer == quiz_question["answer"] + 1:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_question["options"][quiz_question["answer"]])

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print("\nHere's a random fact about", selected_topic.capitalize() + ":")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
