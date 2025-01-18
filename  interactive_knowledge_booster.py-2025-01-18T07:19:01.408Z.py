
import random
import requests
import json

def get_random_fact(topic):
    """Fetches a random fact or concept from the selected topic."""
    facts = {
        "science": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "A group of porcupines is called a prickle."
        ],
        "technology": [
            "The first electronic computer, ENIAC, weighed 30 tons and took up 1,800 square feet.",
            "The first commercial microprocessor, the Intel 4004, was released in 1971 and had 2,300 transistors.",
            "The term 'bug' was first used in computing in 1947 when a moth was found in a Harvard Mark II computer."
        ],
        "history": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and the structure grows.",
            "The first product to have a barcode was Wrigley's gum."
        ],
        "general": [
            "A group of porcupines is called a prickle.",
            "Fingernails grow nearly 4 times faster than toenails.",
            "Apples are more effective at waking you up in the morning than coffee."
        ]
    }
    return random.choice(facts[topic])

def quiz(topic):
    """Provides a multiple-choice quiz on the selected topic."""
    quizzes = {
        "science": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            },
            {
                "question": "Which planet in our solar system has the most moons?",
                "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
                "answer": 0
            },
            {
                "question": "What is the name of the force that holds atoms together in a molecule?",
                "options": ["Gravitational force", "Electromagnetic force", "Strong nuclear force", "Weak nuclear force"],
                "answer": 2
            }
        ],
        "technology": [
            {
                "question": "What does 'HTML' stand for?",
                "options": ["Hyper Text Markup Language", "Hyper Text Management Language", "Hyper Text Modeling Language", "Hyper Text Markup Lexicon"],
                "answer": 0
            },
            {
                "question": "Which company developed the first commercial microprocessor?",
                "options": ["Intel", "IBM", "Apple", "Microsoft"],
                "answer": 0
            },
            {
                "question": "What is the name of the first electronic computer?",
                "options": ["ENIAC", "UNIVAC", "MARK I", "COLOSSUS"],
                "answer": 0
            }
        ],
        "history": [
            {
                "question": "Which ancient civilization built the Pyramids of Giza?",
                "options": ["Mesopotamians", "Egyptians", "Greeks", "Romans"],
                "answer": 1
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "Benjamin Franklin"],
                "answer": 2
            },
            {
                "question": "Which event marked the end of World War II?",
                "options": ["D-Day", "Pearl Harbor", "Atomic bombings of Hiroshima and Nagasaki", "Battle of Stalingrad"],
                "answer": 2
            }
        ],
        "general": [
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Liver", "Skin", "Brain"],
                "answer": 2
            },
            {
                "question": "What is the tallest mammal in the world?",
                "options": ["Elephant", "Giraffe", "Hippopotamus", "Rhinoceros"],
                "answer": 1
            },
            {
                "question": "What is the rarest blood type?",
                "options": ["A", "B", "AB", "O"],
                "answer": 2
            }
        ]
    }
    
    # Select a random quiz question from the chosen topic
    question = random.choice(quizzes[topic])
    
    # Print the question and options
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    
    # Get user's answer
    user_answer = int(input("Enter your answer (1-4): "))
    
    # Check if the user's answer is correct
    if user_answer - 1 == question["answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", question["options"][question["answer"]])

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    print("1. Science")
    print("2. Technology")
    print("3. History")
    print("4. General Knowledge")
    
    topic_choice = int(input("Enter your choice (1-4): "))
    
    topics = ["science", "technology", "history", "general"]
    chosen_topic = topics[topic_choice - 1]
    
    print(f"\nYour chosen topic is: {chosen_topic.capitalize()}")
    print(get_random_fact(chosen_topic))
    print("\nNow let's test your knowledge with a quiz!")
    quiz(chosen_topic)

if __name__ == "__main__":
    main()
