
import random
import requests
import json

# Define the topics and their associated facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The hottest planet in the Solar System is Venus, not Mercury.",
            "Orcas (killer whales) are not actually whales, but the largest members of the dolphin family."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the smallest planet in our solar system?",
                "options": ["Mercury", "Venus", "Earth", "Mars"],
                "answer": "Mercury"
            },
            {
                "question": "Which of these is not a state of matter?",
                "options": ["Solid", "Liquid", "Gas", "Plasma"],
                "answer": "Plasma"
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": "Photosynthesis"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The first programmable computer was the ENIAC, which was completed in 1946.",
            "The world's first website was launched on August 6, 1991, and was about the World Wide Web project itself."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "Which company developed the first commercial smartphone?",
                "options": ["Apple", "Samsung", "Nokia", "BlackBerry"],
                "answer": "BlackBerry"
            },
            {
                "question": "What is the name of the first digital computer?",
                "options": ["ENIAC", "UNIVAC", "IBM 701", "MARK I"],
                "answer": "ENIAC"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza in Egypt were built around 2560–2540 BC.",
            "The French Revolution began in 1789 and ended with the rise of Napoleon Bonaparte in 1799."
        ],
        "quiz_questions": [
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Mesopotamia", "Ancient Egypt", "Ancient Greece", "Ancient China"],
                "answer": "Ancient Greece"
            },
            {
                "question": "What was the name of the first successful powered flight, which took place in 1903?",
                "options": ["The Wright Flyer", "The Bleriot XI", "The Curtiss Pusher", "The Nieuport IV"],
                "answer": "The Wright Flyer"
            },
            {
                "question": "Which event is considered the start of World War I?",
                "options": ["The assassination of Archduke Franz Ferdinand", "The sinking of the Lusitania", "The Battle of the Somme", "The Treaty of Versailles"],
                "answer": "The assassination of Archduke Franz Ferdinand"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.",
            "The largest ocean on Earth is the Pacific Ocean, covering an area of about 63 million square miles."
        ],
        "quiz_questions": [
            {
                "question": "What is the rarest blood type?",
                "options": ["A-", "B+", "AB-", "O-"],
                "answer": "AB-"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
                "answer": "Jupiter"
            },
            {
                "question": "Which country is known as the 'Land of the Rising Sun'?",
                "options": ["China", "Japan", "South Korea", "Taiwan"],
                "answer": "Japan"
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the selected topic.
    """
    return random.choice(topics[topic]["facts"])

def get_quiz_question(topic):
    """
    Retrieves a random quiz question and its options from the selected topic.
    """
    quiz_question = random.choice(topics[topic]["quiz_questions"])
    return quiz_question

def run_quiz(topic):
    """
    Runs a quiz for the selected topic.
    """
    quiz_question = get_quiz_question(topic)
    print(f"Question: {quiz_question['question']}")
    for i, option in enumerate(quiz_question['options']):
        print(f"{i+1}. {option}")
    
    user_answer = input("Enter your answer (1-4): ")
    if quiz_question['options'][int(user_answer) - 1] == quiz_question['answer']:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {quiz_question['answer']}")

def main():
    """
    Main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print(f"\nYour selected topic is: {selected_topic.capitalize()}")
        print(get_random_fact(selected_topic))
        print("\nNow let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
