
import random
import requests
import json

# Define the topics and their associated facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 206 bones.",
            "The largest planet in our solar system is Jupiter.",
            "Photosynthesis is the process by which plants convert sunlight into energy.",
        ],
        "quiz_questions": [
            {
                "question": "What is the chemical formula for water?",
                "options": ["H2O", "CO2", "O2", "CH4"],
                "answer": 0
            },
            {
                "question": "Which organ in the human body is responsible for pumping blood?",
                "options": ["Lungs", "Heart", "Liver", "Kidneys"],
                "answer": 1
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Respiration", "Photosynthesis", "Transpiration", "Digestion"],
                "answer": 1
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989.",
            "The first smartphone was the IBM Simon, released in 1992.",
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "Which company is known for producing the iPhone?",
                "options": ["Samsung", "Google", "Apple", "Microsoft"],
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
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.",
            "The American Civil War lasted from 1861 to 1865.",
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Mesopotamia", "Ancient Egypt", "Ancient Greece", "Ancient China"],
                "answer": 1
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "Benjamin Franklin"],
                "answer": 2
            },
            {
                "question": "Which event is considered the starting point of World War I?",
                "options": ["The sinking of the Lusitania", "The assassination of Archduke Franz Ferdinand", "The bombing of Pearl Harbor", "The Battle of the Somme"],
                "answer": 1
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The tallest mammal is the giraffe.",
            "The largest ocean on Earth is the Pacific Ocean.",
            "The Mona Lisa is a painting by the Italian Renaissance artist Leonardo da Vinci.",
        ],
        "quiz_questions": [
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Saturn", "Jupiter", "Uranus", "Neptune"],
                "answer": 1
            },
            {
                "question": "Which country is known for the Great Barrier Reef?",
                "options": ["Australia", "Brazil", "Canada", "India"],
                "answer": 0
            },
            {
                "question": "Who is the author of the Harry Potter book series?",
                "options": ["J.K. Rowling", "Stephen King", "J.R.R. Tolkien", "Agatha Christie"],
                "answer": 0
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Returns a random fact from the chosen topic.
    """
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    """
    Returns a random quiz question and its options from the chosen topic.
    """
    quiz_question = random.choice(topics[topic]["quiz_questions"])
    return quiz_question["question"], quiz_question["options"], quiz_question["answer"]

def main():
    """
    The main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    chosen_topic = input("Enter your choice: ").lower()
    if chosen_topic not in topics:
        print("Invalid topic. Please try again.")
        return

    print(f"\nHere's a random fact about {chosen_topic.capitalize()}:")
    print(get_random_fact(chosen_topic))

    print("\nTime for a quiz!")
    score = 0
    for _ in range(3):
        question, options, answer = get_quiz_question(chosen_topic)
        print(question)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): ")) - 1
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"\nYour final score is {score}/3.")

if __name__ == "__main__":
    main()
