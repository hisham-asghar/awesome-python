
import random
import requests
import json

# Define the topics and their respective facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The largest known prime number as of 2022 has 23 million digits.",
            "The first successful kidney transplant was performed in 1954."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the process where water changes from a liquid to a gas?",
                "options": ["Evaporation", "Condensation", "Sublimation", "Precipitation"],
                "answer": 0
            },
            {
                "question": "Which scientist is known for developing the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"],
                "answer": 1
            },
            {
                "question": "What is the name of the process where plants convert sunlight, water, and carbon dioxide into glucose?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": 0
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer virus, called 'Creeper', was created in 1971.",
            "The first commercial smartphone was the IBM Simon, released in 1992.",
            "The first digital camera was invented by Kodak in 1975."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the process where data is converted into a form that can be processed by a computer?",
                "options": ["Digitization", "Encryption", "Compression", "Transmission"],
                "answer": 0
            },
            {
                "question": "Which company is known for developing the first commercially successful web browser?",
                "options": ["Microsoft", "Apple", "Google", "Netscape"],
                "answer": 3
            },
            {
                "question": "What is the name of the programming language that is widely used for web development?",
                "options": ["Java", "Python", "C++", "JavaScript"],
                "answer": 3
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci.",
            "The first successful powered flight took place on December 17, 1903, by the Wright brothers."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Mesopotamia", "Egypt", "Greece", "China"],
                "answer": 2
            },
            {
                "question": "Which event marked the beginning of World War I?",
                "options": ["The assassination of Archduke Franz Ferdinand", "The bombing of Pearl Harbor", "The fall of the Berlin Wall", "The Cuban Missile Crisis"],
                "answer": 0
            },
            {
                "question": "Which famous explorer is credited with discovering the Americas?",
                "options": ["Christopher Columbus", "Vasco da Gama", "Marco Polo", "Ferdinand Magellan"],
                "answer": 0
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and causes the structure to grow.",
            "A group of flamingos is called a flamboyance.",
            "The first person convicted of speeding was going 8 mph."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Liver", "Skin", "Brain"],
                "answer": 2
            },
            {
                "question": "Which country is known as the 'Land of the Rising Sun'?",
                "options": ["China", "Japan", "India", "South Korea"],
                "answer": 1
            },
            {
                "question": "What is the name of the largest moon of Saturn?",
                "options": ["Titan", "Ganymede", "Callisto", "Europa"],
                "answer": 0
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the selected topic.
    """
    facts = topics[topic]["facts"]
    return random.choice(facts)

def get_quiz_question(topic):
    """
    Retrieves a random quiz question from the selected topic.
    """
    quiz_questions = topics[topic]["quiz_questions"]
    question = random.choice(quiz_questions)
    return question

def run_quiz(topic):
    """
    Runs a quiz for the selected topic.
    """
    question = get_quiz_question(topic)
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    
    while True:
        try:
            user_answer = int(input("Enter your answer (1-4): "))
            if user_answer < 1 or user_answer > 4:
                print("Invalid answer. Please try again.")
            elif user_answer - 1 == question["answer"]:
                print("Correct!")
                break
            else:
                print("Incorrect. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    """
    Main function that runs the interactive knowledge exploration.
    """
    print("Welcome to the Interactive Knowledge Exploration!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")
    
    while True:
        selected_topic = input("Enter your choice: ").lower()
        if selected_topic in topics:
            print(f"\nRandom fact about {selected_topic.capitalize()}:")
            print(get_random_fact(selected_topic))
            print("\nNow, let's test your knowledge!")
            run_quiz(selected_topic)
            break
        else:
            print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
