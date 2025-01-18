
import random
import requests
import json

# Define the topics and their corresponding APIs or data sources
topics = {
    1: "Science",
    2: "Technology",
    3: "History",
    4: "General Knowledge"
}

def get_random_fact(topic):
    """
    Fetch a random fact or concept from the selected topic.
    """
    if topic == "Science":
        # Fetch a random science fact from an API
        response = requests.get("https://api.api-ninjas.com/v1/facts?category=science", headers={"X-Api-Key": "YOUR_API_KEY_HERE"})
        data = response.json()
        return data[0]["fact"]
    elif topic == "Technology":
        # Fetch a random technology fact from an API
        response = requests.get("https://api.api-ninjas.com/v1/facts?category=technology", headers={"X-Api-Key": "YOUR_API_KEY_HERE"})
        data = response.json()
        return data[0]["fact"]
    elif topic == "History":
        # Fetch a random history fact from a predefined database
        history_facts = [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first product to have a barcode was Wrigley's gum."
        ]
        return random.choice(history_facts)
    elif topic == "General Knowledge":
        # Fetch a random general knowledge fact from an API
        response = requests.get("https://api.api-ninjas.com/v1/facts?category=general", headers={"X-Api-Key": "YOUR_API_KEY_HERE"})
        data = response.json()
        return data[0]["fact"]
    else:
        return "Sorry, I don't have any facts for that topic."

def quiz(topic):
    """
    Provide a multiple-choice quiz for the selected topic.
    """
    if topic == "Science":
        # Fetch science quiz questions and answers from a predefined database
        quiz_data = [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "Which planet in our solar system is known as the 'Red Planet'?",
                "options": ["Mars", "Venus", "Jupiter", "Saturn"],
                "answer": "Mars"
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "options": ["Photosynthesis", "Respiration", "Transpiration", "Osmosis"],
                "answer": "Photosynthesis"
            }
        ]
    elif topic == "Technology":
        # Fetch technology quiz questions and answers from a predefined database
        quiz_data = [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "options": ["Java", "C++", "Python", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "Which company developed the first commercial graphical user interface (GUI)?",
                "options": ["Apple", "Microsoft", "IBM", "Xerox"],
                "answer": "Xerox"
            },
            {
                "question": "What is the name of the first web browser developed by Tim Berners-Lee?",
                "options": ["Mosaic", "Netscape Navigator", "Internet Explorer", "WorldWideWeb"],
                "answer": "WorldWideWeb"
            }
        ]
    elif topic == "History":
        # Fetch history quiz questions and answers from a predefined database
        quiz_data = [
            {
                "question": "Which ancient civilization is known for building the pyramids?",
                "options": ["Mesopotamia", "Indus Valley", "Aztec", "Ancient Egypt"],
                "answer": "Ancient Egypt"
            },
            {
                "question": "What was the name of the first successful powered flight by the Wright brothers?",
                "options": ["The Spirit of St. Louis", "The Flyer", "The Kitty Hawk", "The Wright Flyer"],
                "answer": "The Wright Flyer"
            },
            {
                "question": "Which event is considered the start of World War I?",
                "options": ["The assassination of Archduke Franz Ferdinand", "The bombing of Pearl Harbor", "The fall of the Berlin Wall", "The Cuban Missile Crisis"],
                "answer": "The assassination of Archduke Franz Ferdinand"
            }
        ]
    elif topic == "General Knowledge":
        # Fetch general knowledge quiz questions and answers from a predefined database
        quiz_data = [
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "What is the tallest mammal in the world?",
                "options": ["Elephant", "Giraffe", "Hippopotamus", "Rhinoceros"],
                "answer": "Giraffe"
            },
            {
                "question": "What is the capital city of Australia?",
                "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
                "answer": "Canberra"
            }
        ]
    else:
        return "Sorry, I don't have any quiz for that topic."

    # Randomly select a quiz question
    quiz_question = random.choice(quiz_data)

    # Get user input for the quiz
    print(quiz_question["question"])
    for i, option in enumerate(quiz_question["options"], start=1):
        print(f"{i}. {option}")
    user_answer = input("Enter your answer (1-4): ")

    # Check if the user's answer is correct
    if quiz_question["options"][int(user_answer) - 1] == quiz_question["answer"]:
        return "Correct!"
    else:
        return "Incorrect. The correct answer is: " + quiz_question["answer"]

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")

    for topic_id, topic_name in topics.items():
        print(f"{topic_id}. {topic_name}")

    user_choice = int(input("Enter the number of your chosen topic: "))

    if user_choice in topics:
        chosen_topic = topics[user_choice]
        print(f"\nYour chosen topic is: {chosen_topic}")

        # Get a random fact or concept for the selected topic
        random_fact = get_random_fact(chosen_topic)
        print(f"\nRandom {chosen_topic} fact: {random_fact}")

        # Provide a quiz for the selected topic
        quiz_result = quiz(chosen_topic)
        print(f"\n{quiz_result}")
    else:
        print("Invalid topic choice. Please try again.")

if __name__ == "__main__":
    main()
