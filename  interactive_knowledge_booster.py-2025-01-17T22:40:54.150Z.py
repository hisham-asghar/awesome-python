
import random
import requests
import json

def get_random_fact(topic):
    """
    Fetches a random fact or concept from a predefined database for the given topic.
    """
    facts = {
        "science": [
            "The human body contains enough iron to make a 3-inch nail.",
            "The first product to have a barcode was Wrigley's gum.",
            "A group of porcupines is called a prickle."
        ],
        "technology": [
            "The first computer mouse was invented in 1964 and cost $15,000.",
            "The 'qwerty' keyboard layout was designed to slow down typists.",
            "The first text message was sent on December 3, 1992."
        ],
        "history": [
            "The Great Wall of China is the only man-made structure visible from space.",
            "The Roman emperor Caligula made his horse a senator.",
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off."
        ],
        "general": [
            "A group of puffins is called a 'circus'.",
            "Recycling one glass jar saves enough energy to power a computer for 25 minutes.",
            "The first product to have a barcode was Wrigley's gum."
        ]
    }
    return random.choice(facts[topic])

def quiz(topic):
    """
    Provides a multiple-choice quiz for the given topic, fetching questions and answers from a public API.
    """
    # Fetch questions and answers from a public API (e.g., Open Trivia Database)
    response = requests.get(f"https://opentdb.com/api.php?amount=1&category={topic_to_category[topic]}&type=multiple")
    data = response.json()
    question = data["results"][0]["question"]
    correct_answer = data["results"][0]["correct_answer"]
    incorrect_answers = data["results"][0]["incorrect_answers"]
    all_answers = [correct_answer] + incorrect_answers
    random.shuffle(all_answers)

    print(f"Question: {question}")
    for i, answer in enumerate(all_answers):
        print(f"{i+1}. {answer}")

    user_answer = int(input("Enter the number of the correct answer: "))
    if all_answers[user_answer - 1] == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}")

topic_to_category = {
    "science": 17,
    "technology": 18,
    "history": 23,
    "general": 9
}

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    print("1. Science")
    print("2. Technology")
    print("3. History")
    print("4. General Knowledge")

    user_choice = int(input("Enter the number of the topic (1-4): "))
    topics = ["science", "technology", "history", "general"]
    topic = topics[user_choice - 1]

    print(f"You've chosen the {topic} topic.")
    print(get_random_fact(topic))

    quiz(topic)

if __name__ == "__main__":
    main()
