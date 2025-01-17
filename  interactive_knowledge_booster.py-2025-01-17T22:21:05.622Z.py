
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    '1': 'Science',
    '2': 'Technology',
    '3': 'History',
    '4': 'General Knowledge'
}

def get_random_fact(topic):
    """
    Fetch a random fact or concept for the given topic.
    """
    if topic == '1':
        # Fetch science facts from an API or a predefined database
        facts = [
            "The human body has around 60,000 miles of blood vessels.",
            "The Milky Way galaxy contains an estimated 100-400 billion stars.",
            "A single teaspoon of neutron star material would weigh over 1 billion tons on Earth."
        ]
    elif topic == '2':
        # Fetch technology facts from an API or a predefined database
        facts = [
            "The first electronic computer, ENIAC, was unveiled in 1946 and weighed 30 tons.",
            "The first commercial barcode was scanned on June 26, 1974, at a Marsh supermarket in Troy, Ohio.",
            "The first smartphone was the IBM Simon, released in 1992."
        ]
    elif topic == '3':
        # Fetch historical facts from an API or a predefined database
        facts = [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza were built around 2500 BC and are the oldest and largest of the three main pyramids.",
            "The Roman Empire lasted for over 400 years, from the 1st century BC to the 5th century AD."
        ]
    elif topic == '4':
        # Fetch general knowledge facts from an API or a predefined database
        facts = [
            "The largest organ in the human body is the skin.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first product to have a barcode was Wrigley's gum."
        ]
    else:
        return "Invalid topic selection."

    return random.choice(facts)

def quiz(topic):
    """
    Provide a multiple-choice quiz for the given topic.
    """
    if topic == '1':
        # Science quiz questions and answers
        questions = [
            {
                "question": "What is the primary function of the human heart?",
                "options": ["To pump blood", "To filter waste", "To produce insulin", "To facilitate breathing"],
                "answer": 0
            },
            {
                "question": "Which planet in our solar system is known as the 'Red Planet'?",
                "options": ["Mars", "Jupiter", "Venus", "Saturn"],
                "answer": 0
            },
            {
                "question": "What is the name of the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": 0
            }
        ]
    elif topic == '2':
        # Technology quiz questions and answers
        questions = [
            {
                "question": "What is the name of the first commercially successful web browser?",
                "options": ["Internet Explorer", "Netscape Navigator", "Mozilla Firefox", "Google Chrome"],
                "answer": 1
            },
            {
                "question": "What is the name of the programming language used to create websites?",
                "options": ["Java", "Python", "C++", "HTML"],
                "answer": 3
            },
            {
                "question": "What is the name of the device used to input data into a computer?",
                "options": ["Keyboard", "Monitor", "Printer", "Mouse"],
                "answer": 3
            }
        ]
    elif topic == '3':
        # History quiz questions and answers
        questions = [
            {
                "question": "In what year did the American Revolutionary War begin?",
                "options": ["1776", "1812", "1861", "1945"],
                "answer": 0
            },
            {
                "question": "Which ancient civilization is known for building the Pyramids of Giza?",
                "options": ["Mesopotamia", "Indus Valley", "Ancient Greece", "Ancient Egypt"],
                "answer": 3
            },
            {
                "question": "What was the name of the first successful powered flight, which took place in 1903?",
                "options": ["The Wright Flyer", "The Spitfire", "The Concorde", "The Apollo 11"],
                "answer": 0
            }
        ]
    elif topic == '4':
        # General knowledge quiz questions and answers
        questions = [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            },
            {
                "question": "What is the name of the largest mammal on Earth?",
                "options": ["Elephant", "Hippopotamus", "Blue Whale", "Giraffe"],
                "answer": 2
            },
            {
                "question": "What is the capital city of Australia?",
                "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
                "answer": 3
            }
        ]
    else:
        return "Invalid topic selection."

    # Randomly select a question and display it to the user
    question = random.choice(questions)
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")

    # Get the user's answer
    user_answer = int(input("Enter your answer (1-4): "))

    # Check if the user's answer is correct
    if user_answer - 1 == question["answer"]:
        return "Correct!"
    else:
        return "Incorrect. The correct answer is: " + question["options"][question["answer"]]

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic_id, topic_name in topics.items():
        print(f"{topic_id}. {topic_name}")

    topic_choice = input("Enter the number of the topic (1-4): ")

    if topic_choice in topics:
        print("\nHere's a random fact or concept about", topics[topic_choice] + ":")
        print(get_random_fact(topic_choice))
        print("\nNow, let's test your knowledge with a quiz!")
        print(quiz(topic_choice))
    else:
        print("Invalid topic selection. Please try again.")

if __name__ == "__main__":
    main()
