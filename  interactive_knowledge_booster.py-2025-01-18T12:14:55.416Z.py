
import random
import requests
import json

def get_fact(topic):
    """
    Fetches a random fact or concept from a predefined database for the given topic.
    """
    facts = {
        "science": [
            "The human body has around 60,000 miles of blood vessels.",
            "The sun is approximately 93 million miles away from the Earth.",
            "Bees have five eyes: two compound eyes and three simple eyes."
        ],
        "technology": [
            "The first computer mouse was invented in 1964 by Douglas Engelbart.",
            "The first programmable computer was the ENIAC, which was completed in 1946.",
            "The internet was initially created for military communication in the 1960s."
        ],
        "history": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza were built around 2560–2540 BC.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD."
        ],
        "general": [
            "The largest known prime number as of 2022 has 23 million digits.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "The first person convicted of speeding was Walter Arnold of East Peckham, Kent, UK, in 1896. He was fined 1 shilling for driving at 8 mph, exceeding the 2 mph speed limit."
        ]
    }
    return random.choice(facts[topic])

def quiz(topic):
    """
    Provides a multiple-choice quiz for the given topic, using trivia data fetched from an API.
    """
    # Fetch trivia data from an API (e.g., Open Trivia Database)
    response = requests.get(f"https://opentdb.com/api.php?amount=1&category={topic_ids[topic]}&type=multiple")
    data = response.json()["results"][0]

    # Prepare the quiz question and answers
    question = data["question"]
    answers = data["incorrect_answers"] + [data["correct_answer"]]
    random.shuffle(answers)

    # Display the quiz question and answers
    print(f"Question: {question}")
    for i, answer in enumerate(answers):
        print(f"{i+1}. {answer}")

    # Get the user's answer
    user_answer = int(input("Enter the number of the correct answer: "))
    if answers[user_answer-1] == data["correct_answer"]:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {data['correct_answer']}.")

# Topic IDs for the Open Trivia Database API
topic_ids = {
    "science": 17,
    "technology": 18,
    "history": 23,
    "general": 9
}

# Main program loop
while True:
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    print("1. Science")
    print("2. Technology")
    print("3. History")
    print("4. General Knowledge")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        topic = "science"
    elif choice == "2":
        topic = "technology"
    elif choice == "3":
        topic = "history"
    elif choice == "4":
        topic = "general"
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        continue

    print(f"\nHere's a random fact about {topic}:")
    print(get_fact(topic))

    print("\nNow, let's test your knowledge with a quiz!")
    quiz(topic)

    print("\nThank you for using the Interactive Knowledge Booster!")
    print("Have a great day!")
