
import random
import requests
import json

def get_random_fact(topic):
    """
    Fetches a random fact or concept from a predefined database for the given topic.
    """
    database = {
        "science": [
            "The human body has around 60,000 miles of blood vessels.",
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off."
        ],
        "technology": [
            "The first computer mouse was invented by Douglas Engelbart in 1964 and consisted of a wooden shell with two metal wheels.",
            "The first text message was sent on December 3, 1992, by software engineer Neil Papworth.",
            "The world's first webcam was used to monitor a coffee pot at the University of Cambridge in 1991."
        ],
        "history": [
            "The Magna Carta, signed in 1215, was one of the first documents to place limits on the power of the monarch.",
            "The Great Wall of China is the largest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza were built around 2560–2540 BC, and are the oldest and largest of the three main pyramids."
        ],
        "general_knowledge": [
            "The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and raises the structure.",
            "The first person convicted of speeding was Walter Arnold of East Peckham, Kent, UK, in 1896. He was fined 1 shilling for driving at 8 mph, exceeding the 2 mph speed limit.",
            "The first product to have a barcode was Wrigley's gum."
        ]
    }
    return random.choice(database[topic])

def quiz(topic):
    """
    Provides a multiple-choice quiz for the given topic, using real-time educational content or trivia from public APIs.
    """
    if topic == "science":
        # Fetch science trivia from an API
        response = requests.get("https://opentdb.com/api.php?amount=1&category=17&type=multiple")
        data = response.json()
        question = data["results"][0]["question"]
        choices = data["results"][0]["incorrect_answers"] + [data["results"][0]["correct_answer"]]
        random.shuffle(choices)
    elif topic == "technology":
        # Fetch technology trivia from an API
        response = requests.get("https://opentdb.com/api.php?amount=1&category=18&type=multiple")
        data = response.json()
        question = data["results"][0]["question"]
        choices = data["results"][0]["incorrect_answers"] + [data["results"][0]["correct_answer"]]
        random.shuffle(choices)
    elif topic == "history":
        # Fetch history trivia from an API
        response = requests.get("https://opentdb.com/api.php?amount=1&category=23&type=multiple")
        data = response.json()
        question = data["results"][0]["question"]
        choices = data["results"][0]["incorrect_answers"] + [data["results"][0]["correct_answer"]]
        random.shuffle(choices)
    elif topic == "general_knowledge":
        # Fetch general knowledge trivia from an API
        response = requests.get("https://opentdb.com/api.php?amount=1&category=9&type=multiple")
        data = response.json()
        question = data["results"][0]["question"]
        choices = data["results"][0]["incorrect_answers"] + [data["results"][0]["correct_answer"]]
        random.shuffle(choices)
    else:
        return "Invalid topic. Please choose from: science, technology, history, or general_knowledge."

    print(f"Question: {question}")
    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice}")

    user_answer = int(input("Enter your answer (1-4): "))
    if choices[user_answer - 1] == data["results"][0]["correct_answer"]:
        return "Correct!"
    else:
        return "Incorrect. The correct answer is: " + data["results"][0]["correct_answer"]

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    print("1. Science")
    print("2. Technology")
    print("3. History")
    print("4. General Knowledge")

    topic_choice = input("Enter the number of your chosen topic: ")

    if topic_choice == "1":
        topic = "science"
    elif topic_choice == "2":
        topic = "technology"
    elif topic_choice == "3":
        topic = "history"
    elif topic_choice == "4":
        topic = "general_knowledge"
    else:
        print("Invalid choice. Please try again.")
        return

    print("\nRandom fact about", topic, ":")
    print(get_random_fact(topic))

    print("\nNow let's test your knowledge with a quiz!")
    print(quiz(topic))

if __name__ == "__main__":
    main()
