
import random
import requests
import json

# Define the topics and their associated facts/quizzes
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The sun is about 93 million miles away from Earth.",
            "The largest known prime number as of 2022 has over 23 million digits."
        ],
        "quizzes": [
            {
                "question": "What is the name of the process where plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": 0
            },
            {
                "question": "Which scientist is known for developing the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Galileo Galilei"],
                "answer": 1
            },
            {
                "question": "What is the name of the force that attracts objects with mass towards each other?",
                "options": ["Electromagnetic force", "Gravitational force", "Strong nuclear force", "Weak nuclear force"],
                "answer": 1
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The first commercial microprocessor was the Intel 4004, released in 1971.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989."
        ],
        "quizzes": [
            {
                "question": "What is the name of the operating system developed by Apple Inc.?",
                "options": ["Windows", "Linux", "macOS", "Android"],
                "answer": 2
            },
            {
                "question": "Which company is known for manufacturing popular smartphones?",
                "options": ["Apple", "Samsung", "Google", "All of the above"],
                "answer": 3
            },
            {
                "question": "What is the name of the programming language that is widely used for web development?",
                "options": ["Java", "C++", "Python", "JavaScript"],
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
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Mesopotamia", "Egypt", "Greece", "China"],
                "answer": 2
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "Benjamin Franklin"],
                "answer": 2
            },
            {
                "question": "Which event is known as the turning point of World War II in Europe?",
                "options": ["D-Day", "Battle of Stalingrad", "Battle of Britain", "Pearl Harbor"],
                "answer": 1
            }
        ]
    },
    "general": {
        "facts": [
            "The largest known prime number as of 2022 has over 23 million digits.",
            "The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and raises the structure.",
            "The first product to have a barcode was Wrigley's gum."
        ],
        "quizzes": [
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Liver", "Skin", "Brain"],
                "answer": 2
            },
            {
                "question": "What is the name of the tallest mammal on Earth?",
                "options": ["Elephant", "Giraffe", "Hippopotamus", "Rhinoceros"],
                "answer": 1
            },
            {
                "question": "Which country is known as the Land of the Rising Sun?",
                "options": ["China", "Japan", "South Korea", "India"],
                "answer": 1
            }
        ]
    }
}

def get_random_fact(topic):
    return random.choice(topics[topic]["facts"])

def get_quiz(topic):
    quiz = random.choice(topics[topic]["quizzes"])
    return quiz

def run_quiz(quiz):
    print(quiz["question"])
    for i, option in enumerate(quiz["options"]):
        print(f"{i+1}. {option}")
    
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == quiz["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz["options"][quiz["answer"]])

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print("\nHere's a random fact about", selected_topic.capitalize(), ":")
        print(get_random_fact(selected_topic))
        
        print("\nNow, let's test your knowledge with a quiz!")
        quiz = get_quiz(selected_topic)
        run_quiz(quiz)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
