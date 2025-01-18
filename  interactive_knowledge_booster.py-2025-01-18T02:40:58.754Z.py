
import random
import requests
import json

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the selected topic using a public API or predefined database.
    """
    # Replace this with your actual API call or database lookup
    facts = {
        "science": ["The human body has 206 bones.", "The largest planet in our solar system is Jupiter.", "DNA is the genetic material that carries the instructions for the development and functioning of living organisms."],
        "technology": ["The first computer mouse was invented in 1964.", "The World Wide Web was invented in 1989 by Tim Berners-Lee.", "Artificial intelligence (AI) is the ability of a computer or a robot to perform tasks that would require human intelligence."],
        "history": ["The Pyramids of Giza in Egypt were built around 2560-2540 BC.", "The Roman Empire lasted from 27 BC to 476 AD.", "The American Civil War took place from 1861 to 1865."],
        "general": ["The largest ocean on Earth is the Pacific Ocean.", "The tallest mammal is the giraffe.", "The Mona Lisa was painted by Leonardo da Vinci."]
    }
    return random.choice(facts[topic])

def quiz(topic):
    """
    Provides a multiple-choice quiz for the selected topic.
    """
    # Replace this with your actual quiz questions and answers
    quizzes = {
        "science": [
            {
                "question": "What is the chemical symbol for gold?",
                "choices": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            },
            {
                "question": "Which planet is known as the 'Red Planet'?",
                "choices": ["Venus", "Mars", "Saturn", "Jupiter"],
                "answer": 1
            }
        ],
        "technology": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "choices": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "What is the name of the company that created the Android operating system?",
                "choices": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": 2
            }
        ],
        "history": [
            {
                "question": "Which ancient civilization built the Great Pyramid of Giza?",
                "choices": ["Aztec", "Inca", "Egyptian", "Roman"],
                "answer": 2
            },
            {
                "question": "What year did the United States declare independence?",
                "choices": ["1776", "1789", "1812", "1865"],
                "answer": 0
            }
        ],
        "general": [
            {
                "question": "What is the largest mammal in the world?",
                "choices": ["Elephant", "Whale", "Giraffe", "Hippopotamus"],
                "answer": 1
            },
            {
                "question": "Who painted the Mona Lisa?",
                "choices": ["Michelangelo", "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci"],
                "answer": 3
            }
        ]
    }
    
    quiz_data = random.choice(quizzes[topic])
    print(quiz_data["question"])
    for i, choice in enumerate(quiz_data["choices"]):
        print(f"{i+1}. {choice}")
    
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == quiz_data["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_data["choices"][quiz_data["answer"]])

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Select a topic:")
    print("1. Science")
    print("2. Technology")
    print("3. History")
    print("4. General")
    
    topic_choice = int(input("Enter your choice (1-4): "))
    
    topics = ["science", "technology", "history", "general"]
    selected_topic = topics[topic_choice - 1]
    
    print(f"\nRandom fact about {selected_topic}:")
    print(get_random_fact(selected_topic))
    
    print(f"\nNow, let's test your knowledge with a {selected_topic} quiz!")
    quiz(selected_topic)

if __name__ == "__main__":
    main()
