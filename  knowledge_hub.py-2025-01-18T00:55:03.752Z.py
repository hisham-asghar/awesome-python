
import random
import requests
import json

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the chosen topic using a public API or predefined database.
    """
    # Replace with your actual data source or API
    facts = {
        "science": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "A group of porcupines is called a prickle."
        ],
        "technology": [
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The first text message was sent on December 3, 1992, by Neil Papworth.",
            "The first programmable computer, the ENIAC, was completed in 1946 and weighed 30 tons."
        ],
        "history": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Colosseum in Rome was built in the 1st century AD and could hold up to 80,000 spectators.",
            "The Pyramids of Giza were built around 2560–2540 BC."
        ],
        "general": [
            "A group of porcupines is called a prickle.",
            "The first product to have a barcode was Wrigley's gum.",
            "Apples are more effective at waking you up in the morning than coffee."
        ]
    }
    
    if topic in facts:
        return random.choice(facts[topic])
    else:
        return "Sorry, that topic is not available."

def quiz(topic):
    """
    Provides a multiple-choice quiz for the chosen topic, fetching questions and answers from a public API or predefined database.
    """
    # Replace with your actual quiz data source or API
    quizzes = {
        "science": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            },
            {
                "question": "Which planet in our solar system is known as the 'Red Planet'?",
                "options": ["Mars", "Jupiter", "Venus", "Saturn"],
                "answer": 0
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Evaporation"],
                "answer": 0
            }
        ],
        "technology": [
            {
                "question": "What is the name of the first commercially successful web browser?",
                "options": ["Internet Explorer", "Netscape Navigator", "Mozilla Firefox", "Google Chrome"],
                "answer": 1
            },
            {
                "question": "Which company developed the first personal computer, the MITS Altair 8800?",
                "options": ["Apple", "Microsoft", "IBM", "MITS"],
                "answer": 3
            },
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            }
        ],
        "history": [
            {
                "question": "In what year did the American Civil War begin?",
                "options": ["1861", "1865", "1914", "1939"],
                "answer": 0
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "John Adams"],
                "answer": 1
            },
            {
                "question": "What event marked the end of World War II?",
                "options": ["D-Day", "Pearl Harbor", "Atomic bombings of Hiroshima and Nagasaki", "Fall of Berlin"],
                "answer": 2
            }
        ],
        "general": [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "Which country is known as the 'Land of the Rising Sun'?",
                "options": ["China", "Japan", "South Korea", "North Korea"],
                "answer": 1
            },
            {
                "question": "What is the name of the largest mammal on Earth?",
                "options": ["African Elephant", "Blue Whale", "Sperm Whale", "Humpback Whale"],
                "answer": 1
            }
        ]
    }
    
    if topic in quizzes:
        quiz_data = random.choice(quizzes[topic])
        print(quiz_data["question"])
        for i, option in enumerate(quiz_data["options"]):
            print(f"{i+1}. {option}")
        
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer - 1 == quiz_data["answer"]:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", quiz_data["options"][quiz_data["answer"]])
    else:
        print("Sorry, that topic is not available.")

def main():
    print("Welcome to the Interactive Knowledge Hub!")
    print("Please select a topic:")
    print("1. Science")
    print("2. Technology")
    print("3. History")
    print("4. General")
    
    topic_choice = int(input("Enter your choice (1-4): "))
    
    topics = ["science", "technology", "history", "general"]
    
    if 1 <= topic_choice <= 4:
        topic = topics[topic_choice - 1]
        print("\nRandom fact about", topic.capitalize() + ":")
        print(get_random_fact(topic))
        print("\nNow, let's test your knowledge with a quiz!")
        quiz(topic)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
