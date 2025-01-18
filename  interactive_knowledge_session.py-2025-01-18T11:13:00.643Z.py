
import random
import requests
import json

# Define the topics and their associated facts and quiz questions
topics = {
    "science": [
        {
            "fact": "The human body has around 60,000 miles of blood vessels.",
            "quiz": {
                "question": "How many miles of blood vessels does the human body have?",
                "options": ["30,000", "45,000", "60,000", "75,000"],
                "answer": 2
            }
        },
        {
            "fact": "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "quiz": {
                "question": "Why does the Mona Lisa have no eyebrows?",
                "options": ["It was fashionable to shave them off in Renaissance Florence",
                           "She was born without eyebrows",
                           "The painting was damaged over time",
                           "The artist forgot to paint them"],
                "answer": 0
            }
        }
    ],
    "technology": [
        {
            "fact": "The first electronic computer, ENIAC, weighed 30 tons and took up 1800 square feet.",
            "quiz": {
                "question": "How much did the first electronic computer, ENIAC, weigh?",
                "options": ["10 tons", "20 tons", "30 tons", "40 tons"],
                "answer": 2
            }
        },
        {
            "fact": "The first mobile phone call was made on April 3, 1973, by Martin Cooper of Motorola.",
            "quiz": {
                "question": "Who made the first mobile phone call?",
                "options": ["Steve Jobs", "Alexander Graham Bell", "Martin Cooper", "Nikola Tesla"],
                "answer": 2
            }
        }
    ],
    "history": [
        {
            "fact": "The Mona Lisa has no visible eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "quiz": {
                "question": "Why does the Mona Lisa have no eyebrows?",
                "options": ["It was fashionable to shave them off in Renaissance Florence",
                           "She was born without eyebrows",
                           "The painting was damaged over time",
                           "The artist forgot to paint them"],
                "answer": 0
            }
        },
        {
            "fact": "The Great Wall of China is the only man-made structure visible from space.",
            "quiz": {
                "question": "Which of the following statements about the Great Wall of China is true?",
                "options": ["It is the longest wall in the world",
                           "It is the only man-made structure visible from space",
                           "It was built to keep out Mongol invaders",
                           "All of the above"],
                "answer": 3
            }
        }
    ],
    "general": [
        {
            "fact": "A group of porcupines is called a prickle.",
            "quiz": {
                "question": "What is a group of porcupines called?",
                "options": ["Quill", "Prickle", "Spike", "Quiver"],
                "answer": 1
            }
        },
        {
            "fact": "The first product to have a barcode was Wrigley's gum.",
            "quiz": {
                "question": "What was the first product to have a barcode?",
                "options": ["Coca-Cola", "Bread", "Wrigley's gum", "Milk"],
                "answer": 2
            }
        }
    ]
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the selected topic.
    """
    return random.choice(topics[topic])["fact"]

def get_quiz(topic):
    """
    Retrieves a random quiz question and options from the selected topic.
    """
    quiz = random.choice(topics[topic])["quiz"]
    return quiz["question"], quiz["options"], quiz["answer"]

def run_quiz(topic):
    """
    Runs an interactive quiz for the selected topic.
    """
    question, options, answer = get_quiz(topic)
    print(question)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer - 1 == answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {options[answer]}.")

def main():
    """
    Main function that displays the topic menu and runs the interactive knowledge session.
    """
    print("Welcome to the Interactive Knowledge Session!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")
    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in topics:
        print(f"\nYour selected topic is: {selected_topic.capitalize()}")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
