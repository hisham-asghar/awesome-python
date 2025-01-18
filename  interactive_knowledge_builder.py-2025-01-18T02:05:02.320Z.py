
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The first digital computer, ENIAC, was completed in 1946.",
            "Helium is the second most abundant element in the universe."
        ],
        "quiz_questions": [
            {
                "question": "What is the name of the first digital computer?",
                "options": ["ENIAC", "UNIVAC", "COLOSSUS", "MARK I"],
                "answer": "ENIAC"
            },
            {
                "question": "Which element is the second most abundant in the universe?",
                "options": ["Hydrogen", "Helium", "Oxygen", "Nitrogen"],
                "answer": "Helium"
            },
            {
                "question": "Approximately how many miles of blood vessels are in the human body?",
                "options": ["10,000", "30,000", "60,000", "100,000"],
                "answer": "60,000"
            }
        ]
    },
    "technology": {
        "facts": [
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The first mobile phone call was made on April 3, 1973, by Martin Cooper of Motorola.",
            "The World Wide Web was invented by Tim Berners-Lee in 1989."
        ],
        "quiz_questions": [
            {
                "question": "Who invented the World Wide Web?",
                "options": ["Bill Gates", "Steve Jobs", "Tim Berners-Lee", "Linus Torvalds"],
                "answer": "Tim Berners-Lee"
            },
            {
                "question": "What year was the first mobile phone call made?",
                "options": ["1973", "1983", "1993", "2003"],
                "answer": "1973"
            },
            {
                "question": "Which company delivered the first commercial computer, the UNIVAC I, in 1951?",
                "options": ["IBM", "Apple", "Microsoft", "UNIVAC"],
                "answer": "UNIVAC"
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Wall of China was built over 2,000 years ago, between the 3rd century BC and the 17th century AD.",
            "The first Olympic Games were held in 776 BC in Olympia, Greece.",
            "The Gutenberg Bible, the first major book printed in the West using movable type, was published in 1455."
        ],
        "quiz_questions": [
            {
                "question": "In what year were the first Olympic Games held?",
                "options": ["776 BC", "500 BC", "200 AD", "1896 AD"],
                "answer": "776 BC"
            },
            {
                "question": "When was the Gutenberg Bible, the first major book printed in the West using movable type, published?",
                "options": ["1355", "1455", "1555", "1655"],
                "answer": "1455"
            },
            {
                "question": "Over what period was the Great Wall of China built?",
                "options": ["3rd century BC to 17th century AD", "5th century BC to 15th century AD", "1st century BC to 10th century AD", "7th century BC to 19th century AD"],
                "answer": "3rd century BC to 17th century AD"
            }
        ]
    },
    "general_knowledge": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "Apples are more effective at waking you up in the morning than coffee."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Brain", "Liver", "Skin"],
                "answer": "Skin"
            },
            {
                "question": "Why does the Mona Lisa have no eyebrows?",
                "options": ["She shaved them off", "It was the fashion in Renaissance Florence to shave them off", "She was born without eyebrows", "The painting was damaged"],
                "answer": "It was the fashion in Renaissance Florence to shave them off"
            },
            {
                "question": "Which is more effective at waking you up in the morning, apples or coffee?",
                "options": ["Apples", "Coffee", "They are equally effective", "Neither are effective"],
                "answer": "Apples"
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the given topic.
    """
    facts = topics[topic]["facts"]
    return random.choice(facts)

def get_quiz_question(topic):
    """
    Retrieves a random quiz question and its options from the given topic.
    """
    quiz_questions = topics[topic]["quiz_questions"]
    question = random.choice(quiz_questions)
    return question

def run_quiz(topic):
    """
    Runs a quiz for the given topic.
    """
    question = get_quiz_question(topic)
    print(f"Question: {question['question']}")
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    user_answer = input("Enter your answer (1-4): ")
    if user_answer.strip() == question["answer"]:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {question['answer']}")

def main():
    """
    The main function that runs the interactive knowledge-building program.
    """
    print("Welcome to the Interactive Knowledge-Building Program!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nTime for a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
