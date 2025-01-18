
import random
import requests
import json

# Define the topics and their corresponding facts and quizzes
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Milky Way galaxy contains an estimated 100 to 400 billion stars.",
            "Diamonds are formed from carbon under extreme heat and pressure deep within the Earth's mantle."
        ],
        "quizzes": [
            {
                "question": "What is the primary function of the human heart?",
                "options": ["To pump blood", "To filter toxins", "To produce oxygen", "To regulate body temperature"],
                "answer": 0
            },
            {
                "question": "What is the name of the largest planet in our solar system?",
                "options": ["Mars", "Jupiter", "Saturn", "Neptune"],
                "answer": 1
            },
            {
                "question": "Which of the following is a non-renewable energy source?",
                "options": ["Solar", "Wind", "Hydroelectric", "Fossil fuels"],
                "answer": 3
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented by Douglas Engelbart in 1964.",
            "The internet was initially called ARPANET, created by the U.S. Department of Defense in 1969.",
            "The first smartphone was the IBM Simon, released in 1992."
        ],
        "quizzes": [
            {
                "question": "What was the name of the first web browser?",
                "options": ["Google Chrome", "Mozilla Firefox", "Microsoft Edge", "Mosaic"],
                "answer": 3
            },
            {
                "question": "What is the name of the programming language used to create websites?",
                "options": ["Java", "Python", "C++", "HTML"],
                "answer": 3
            },
            {
                "question": "Which company developed the first commercial microprocessor?",
                "options": ["Apple", "IBM", "Intel", "Microsoft"],
                "answer": 2
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza in Egypt were built around 2560–2540 BC.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD."
        ],
        "quizzes": [
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Egyptians", "Greeks", "Mayans", "Chinese"],
                "answer": 1
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "Benjamin Franklin"],
                "answer": 2
            },
            {
                "question": "Which event marked the beginning of World War I?",
                "options": ["The assassination of Archduke Franz Ferdinand", "The attack on Pearl Harbor", "The fall of the Berlin Wall", "The Cuban Missile Crisis"],
                "answer": 0
            }
        ]
    },
    "general": {
        "facts": [
            "A group of flamingos is called a flamboyance.",
            "The world's largest desert is Antarctica, which is a desert due to its low precipitation.",
            "The tallest mammal in the world is the giraffe, which can grow up to 18 feet tall."
        ],
        "quizzes": [
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Lungs", "Skin", "Liver"],
                "answer": 2
            },
            {
                "question": "What is the capital city of Australia?",
                "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
                "answer": 3
            },
            {
                "question": "What is the name of the largest moon of Saturn?",
                "options": ["Titan", "Ganymede", "Callisto", "Io"],
                "answer": 0
            }
        ]
    }
}

def display_menu():
    print("Welcome to the Interactive Knowledge Hub!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    return input("Enter your choice: ").lower()

def display_fact(topic):
    fact = random.choice(topics[topic]["facts"])
    print(f"Here's a random fact about {topic.capitalize()}:")
    print(f"- {fact}")

def display_quiz(topic):
    quiz = random.choice(topics[topic]["quizzes"])
    print(f"Let's test your {topic.capitalize()} knowledge!")
    print(quiz["question"])
    for i, option in enumerate(quiz["options"]):
        print(f"{i+1}. {option}")
    user_answer = int(input("Enter your answer (1-4): ")) - 1
    if user_answer == quiz["answer"]:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {quiz['options'][quiz['answer']]}")

def main():
    topic = display_menu()
    display_fact(topic)
    display_quiz(topic)

if __name__ == "__main__":
    main()
