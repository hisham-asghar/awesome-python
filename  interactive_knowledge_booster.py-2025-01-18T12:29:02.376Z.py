
import random
import requests
import json

def get_fact(topic):
    """
    Fetches a random fact or concept from the chosen topic using a public API or predefined database.
    """
    facts = {
        "science": [
            "The human body has around 100 trillion cells.",
            "The largest known prime number as of 2022 has 23 million digits.",
            "The Milky Way galaxy contains an estimated 100 to 400 billion stars."
        ],
        "technology": [
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The world's first programmable computer was the ENIAC, which was completed in 1946.",
            "The internet was initially called ARPANET and was created in 1969 by the U.S. Department of Defense."
        ],
        "history": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.",
            "The first successful powered flight by the Wright brothers took place on December 17, 1903."
        ],
        "general": [
            "The largest known prime number as of 2022 has 23 million digits.",
            "The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and raises the structure.",
            "A group of flamingos is called a flamboyance."
        ]
    }
    
    if topic in facts:
        return random.choice(facts[topic])
    else:
        return "Sorry, that topic is not available."

def quiz(topic):
    """
    Provides an interactive quiz for the chosen topic with multiple-choice questions.
    """
    questions = {
        "science": [
            {"question": "What is the chemical symbol for gold?", "answers": ["Au", "Ag", "Cu", "Fe"], "correct": 0},
            {"question": "What is the largest planet in our solar system?", "answers": ["Mars", "Venus", "Jupiter", "Saturn"], "correct": 2},
            {"question": "What is the process by which plants convert sunlight into energy?", "answers": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"], "correct": 0}
        ],
        "technology": [
            {"question": "What does 'CPU' stand for?", "answers": ["Central Processing Unit", "Computer Power Unit", "Computer Processing Unit", "Central Power Unit"], "correct": 0},
            {"question": "What is the name of the first commercially available personal computer?", "answers": ["Apple II", "IBM PC", "Commodore 64", "Atari 800"], "correct": 1},
            {"question": "What is the name of the programming language created by Guido van Rossum?", "answers": ["Java", "C++", "Python", "JavaScript"], "correct": 2}
        ],
        "history": [
            {"question": "In what year did World War I begin?", "answers": ["1914", "1939", "1945", "1918"], "correct": 0},
            {"question": "Who was the first president of the United States?", "answers": ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "James Madison"], "correct": 1},
            {"question": "What was the name of the first successful powered flight by the Wright brothers?", "answers": ["The Flyer", "The Wright Flyer", "The Kitty Hawk", "The Glider"], "correct": 1}
        ],
        "general": [
            {"question": "What is the largest ocean on Earth?", "answers": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "correct": 3},
            {"question": "What is the tallest mammal in the world?", "answers": ["Elephant", "Giraffe", "Rhinoceros", "Hippopotamus"], "correct": 1},
            {"question": "What is the name of the longest river in the world?", "answers": ["Amazon River", "Nile River", "Mississippi River", "Yangtze River"], "correct": 1}
        ]
    }
    
    if topic in questions:
        print("Welcome to the interactive quiz!")
        print("Answer the multiple-choice questions to test your knowledge.")
        
        score = 0
        for q in questions[topic]:
            print(f"\nQuestion: {q['question']}")
            for i, answer in enumerate(q['answers']):
                print(f"{i+1}. {answer}")
            
            user_answer = int(input("Enter your answer (1-4): "))
            if user_answer - 1 == q['correct']:
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")
        
        print(f"\nYour final score: {score}/{len(questions[topic])}")
    else:
        print("Sorry, that topic is not available.")

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    print("1. Science")
    print("2. Technology")
    print("3. History")
    print("4. General")
    
    topic_choice = input("Enter the number of the topic (1-4): ")
    
    if topic_choice == "1":
        topic = "science"
    elif topic_choice == "2":
        topic = "technology"
    elif topic_choice == "3":
        topic = "history"
    elif topic_choice == "4":
        topic = "general"
    else:
        print("Invalid choice. Exiting...")
        return
    
    print(f"\nHere's a random fact about {topic}:")
    print(get_fact(topic))
    
    print("\nNow let's test your knowledge with a quiz!")
    quiz(topic)

if __name__ == "__main__":
    main()
