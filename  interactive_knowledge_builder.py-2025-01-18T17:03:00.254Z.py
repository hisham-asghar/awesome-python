
import random
import requests
import json

# Define the topics and their respective facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Milky Way galaxy contains an estimated 100-400 billion stars.",
            "The hottest planet in the Solar System is Venus, not Mercury."
        ],
        "quiz": [
            {
                "question": "What is the main component of the Earth's atmosphere?",
                "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Argon"],
                "answer": "Nitrogen"
            },
            {
                "question": "Which scientist is known for the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Galileo Galilei"],
                "answer": "Albert Einstein"
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
            "The first commercially available personal computer was the Apple II, released in 1977.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989."
        ],
        "quiz": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "Which company developed the first successful commercial jet engine?",
                "options": ["Boeing", "Lockheed Martin", "Pratt & Whitney", "General Electric"],
                "answer": "Pratt & Whitney"
            },
            {
                "question": "What is the name of the first programmable computer?",
                "options": ["ENIAC", "UNIVAC", "MARK I", "Z1"],
                "answer": "ENIAC"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza in Egypt were built around 2560–2540 BC.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD."
        ],
        "quiz": [
            {
                "question": "Which ancient civilization is known for its advanced mathematics and astronomy?",
                "options": ["Mesopotamia", "Ancient Greece", "Ancient Egypt", "Indus Valley"],
                "answer": "Ancient Greece"
            },
            {
                "question": "Which event marked the end of the Middle Ages in Europe?",
                "options": ["The Renaissance", "The Crusades", "The Fall of Constantinople", "The Industrial Revolution"],
                "answer": "The Fall of Constantinople"
            },
            {
                "question": "Which country was the first to give women the right to vote?",
                "options": ["United States", "United Kingdom", "New Zealand", "Sweden"],
                "answer": "New Zealand"
            }
        ]
    },
    "general knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal is the giraffe.",
            "The largest planet in our solar system is Jupiter."
        ],
        "quiz": [
            {
                "question": "What is the rarest blood type?",
                "options": ["A-", "B-", "AB-", "O-"],
                "answer": "AB-"
            },
            {
                "question": "Which country is known as the 'Land of the Rising Sun'?",
                "options": ["China", "Japan", "South Korea", "India"],
                "answer": "Japan"
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
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
    quiz_questions = topics[topic]["quiz"]
    question = random.choice(quiz_questions)
    return question

def run_quiz(topic):
    """
    Runs the quiz for the selected topic.
    """
    question = get_quiz_question(topic)
    print(f"Question: {question['question']}")
    for i, option in enumerate(question["options"], start=1):
        print(f"{i}. {option}")

    user_answer = int(input("Enter your answer (1-4): "))
    if question["options"][user_answer - 1] == question["answer"]:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {question['answer']}")

def main():
    """
    Main function to run the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()
    if selected_topic in topics:
        print(f"You selected: {selected_topic.capitalize()}")
        print(get_random_fact(selected_topic))
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
