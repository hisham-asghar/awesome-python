
import random
import requests
import json

def get_random_fact(topic):
    """Fetches a random fact or concept from the chosen topic using a public API or predefined database."""
    facts = {
        "science": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "A group of porcupines is called a prickle."
        ],
        "technology": [
            "The first electronic computer, ENIAC, weighed 30 tons and took up 1,800 square feet.",
            "The first commercial computer, UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The term 'computer bug' was coined after a moth was found stuck in a Harvard Mark II computer in 1947."
        ],
        "history": [
            "The Great Wall of China is the only man-made structure visible from space.",
            "The Mayans predicted the world would end in 2012, but they were wrong.",
            "The first known world map was created in 600 BC by the ancient Greek scholar Anaximander."
        ],
        "general": [
            "Apples are more effective at waking you up in the morning than coffee.",
            "A group of flamingos is called a flamboyance.",
            "The first product to have a barcode was Wrigley's gum."
        ]
    }
    return random.choice(facts[topic])

def quiz(topic):
    """Presents a multiple-choice quiz on the chosen topic using trivia data from a public API or predefined database."""
    quiz_data = {
        "science": [
            {
                "question": "What is the chemical symbol for gold?",
                "choices": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            },
            {
                "question": "Which planet in our solar system is known as the 'Red Planet'?",
                "choices": ["Jupiter", "Venus", "Mars", "Saturn"],
                "answer": 2
            },
            {
                "question": "What is the process by which plants convert light energy into chemical energy?",
                "choices": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": 0
            }
        ],
        "technology": [
            {
                "question": "What is the name of the first programmable computer?",
                "choices": ["ENIAC", "UNIVAC I", "Apple I", "IBM PC"],
                "answer": 0
            },
            {
                "question": "Which company developed the first commercial web browser?",
                "choices": ["Microsoft", "Apple", "Netscape", "Google"],
                "answer": 2
            },
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "choices": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            }
        ],
        "history": [
            {
                "question": "In which year did the Great Fire of London occur?",
                "choices": ["1666", "1215", "1453", "1789"],
                "answer": 0
            },
            {
                "question": "Which ancient civilization built the pyramids of Giza?",
                "choices": ["Egyptians", "Greeks", "Romans", "Mayans"],
                "answer": 0
            },
            {
                "question": "Who was the first president of the United States?",
                "choices": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "Benjamin Franklin"],
                "answer": 2
            }
        ],
        "general": [
            {
                "question": "What is the largest organ in the human body?",
                "choices": ["Heart", "Liver", "Skin", "Brain"],
                "answer": 2
            },
            {
                "question": "What is the rarest blood type?",
                "choices": ["A", "B", "AB", "O"],
                "answer": 2
            },
            {
                "question": "What is the name of the tallest mammal?",
                "choices": ["Elephant", "Giraffe", "Hippopotamus", "Rhinoceros"],
                "answer": 1
            }
        ]
    }
    
    question = random.choice(quiz_data[topic])
    print(question["question"])
    for i, choice in enumerate(question["choices"]):
        print(f"{i+1}. {choice}")
    
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == question["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is", question["choices"][question["answer"]])

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Select a topic:")
    topics = ["Science", "Technology", "History", "General Knowledge"]
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")
    
    topic_choice = int(input("Enter your choice (1-4): "))
    topic = topics[topic_choice - 1].lower()
    
    print("\nHere's a random fact or concept about", topics[topic_choice - 1] + ":")
    print(get_random_fact(topic))
    
    print("\nNow, let's test your knowledge with a quiz!")
    quiz(topic)

if __name__ == "__main__":
    main()
