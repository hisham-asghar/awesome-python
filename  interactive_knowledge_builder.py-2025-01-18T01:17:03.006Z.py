
import random
import requests
import json

# Define a dictionary of topics and their associated facts and quiz questions
topics = {
    "science": {
        "facts": [
            "The human body has around 60,000 miles of blood vessels.",
            "The Mariana Trench is the deepest part of the world's oceans, reaching a depth of nearly 7 miles.",
            "Bioluminescence is the production and emission of light by a living organism."
        ],
        "quiz_questions": [
            {
                "question": "What is the main function of the human heart?",
                "options": ["To pump blood throughout the body", "To control breathing", "To digest food", "To filter waste"],
                "answer": 0
            },
            {
                "question": "What is the name of the deepest part of the ocean?",
                "options": ["Mariana Trench", "Challenger Deep", "Mindanao Trench", "Kermadec Trench"],
                "answer": 0
            },
            {
                "question": "Which of the following is an example of bioluminescence?",
                "options": ["Fireflies", "Mushrooms", "Coral reefs", "All of the above"],
                "answer": 3
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
                "question": "What was the name of the first commercial computer?",
                "options": ["ENIAC", "UNIVAC I", "IBM 701", "Apple I"],
                "answer": 1
            },
            {
                "question": "Who made the first mobile phone call?",
                "options": ["Steve Jobs", "Bill Gates", "Martin Cooper", "Alexander Graham Bell"],
                "answer": 2
            },
            {
                "question": "Who invented the World Wide Web?",
                "options": ["Steve Jobs", "Tim Berners-Lee", "Linus Torvalds", "Ada Lovelace"],
                "answer": 1
            }
        ]
    },
    "history": {
        "facts": [
            "The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.",
            "The Magna Carta was a charter agreed to by King John of England in 1215, which limited the power of the monarch.",
            "The Renaissance was a cultural movement that spanned the 14th to the 17th century, originating in Italy."
        ],
        "quiz_questions": [
            {
                "question": "Which is the oldest and largest of the three pyramids in the Giza pyramid complex?",
                "options": ["The Pyramid of Khafre", "The Pyramid of Menkaure", "The Great Pyramid of Giza", "The Sphinx"],
                "answer": 2
            },
            {
                "question": "What was the Magna Carta?",
                "options": ["A peace treaty", "A declaration of independence", "A charter that limited the power of the monarch", "A religious document"],
                "answer": 2
            },
            {
                "question": "When did the Renaissance period originate?",
                "options": ["14th to 17th century", "5th to 15th century", "18th to 20th century", "10th to 12th century"],
                "answer": 0
            }
        ]
    },
    "general": {
        "facts": [
            "The largest organ in the human body is the skin.",
            "The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.",
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles."
        ],
        "quiz_questions": [
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Liver", "Skin", "Brain"],
                "answer": 2
            },
            {
                "question": "What is the tallest mammal?",
                "options": ["Elephant", "Rhinoceros", "Giraffe", "Hippopotamus"],
                "answer": 2
            },
            {
                "question": "What is the longest man-made structure in the world?",
                "options": ["The Great Wall of China", "The Suez Canal", "The Trans-Siberian Railway", "The Panama Canal"],
                "answer": 0
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
    return quiz_question["question"], quiz_question["options"], quiz_question["answer"]

def main():
    """
    The main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge-Building Script!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")

    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))

        print("\nNow, let's test your knowledge with a quiz!")
        question, options, answer = get_quiz_question(selected_topic)
        print(question)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

        user_answer = int(input("Enter your answer (1-4): ")) - 1
        if user_answer == answer:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", options[answer])
    else:
        print("Sorry, that topic is not available. Please try again.")

if __name__ == "__main__":
    main()
