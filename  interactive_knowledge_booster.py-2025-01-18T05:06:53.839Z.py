
import random
import requests
import json

def get_random_fact(topic):
    """
    Fetches a random fact or concept from a predefined database for the given topic.
    """
    facts = {
        "science": [
            "The human body has around 60,000 miles of blood vessels.",
            "The sun is about 93 million miles away from the Earth.",
            "Bees can see ultraviolet light, which is invisible to the human eye."
        ],
        "technology": [
            "The first computer mouse was invented in 1964 and cost $25.",
            "The first commercial smartphone was the IBM Simon, released in 1992.",
            "The first digital camera was invented in 1975 and could only take black-and-white photos."
        ],
        "history": [
            "The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.",
            "The Pyramids of Giza were built around 2560–2540 BC, during the reign of Pharaoh Khufu.",
            "The Roman Empire lasted for over 400 years, from 27 BC to 476 AD."
        ],
        "general": [
            "Giraffes have the same number of vertebrae in their necks as humans do.",
            "Cats have fewer toes on their back paws than their front paws.",
            "The largest known prime number as of 2021 has 23 million digits."
        ]
    }
    return random.choice(facts[topic])

def quiz_question(topic):
    """
    Generates a multiple-choice quiz question for the given topic, using a public API.
    """
    api_url = f"https://opentdb.com/api.php?amount=1&category={topic_to_category[topic]}&type=multiple"
    response = requests.get(api_url)
    data = response.json()
    question = data["results"][0]["question"]
    choices = data["results"][0]["incorrect_answers"] + [data["results"][0]["correct_answer"]]
    random.shuffle(choices)
    return question, choices

def run_quiz(topic):
    """
    Runs an interactive quiz for the given topic, with multiple-choice questions.
    """
    score = 0
    for i in range(3):
        question, choices = quiz_question(topic)
        print(f"Question {i+1}: {question}")
        for j, choice in enumerate(choices):
            print(f"{j+1}. {choice}")
        user_answer = int(input("Enter your answer (1-4): "))
        if choices[user_answer-1] == data["results"][0]["correct_answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score is {score} out of 3.")

topic_to_category = {
    "science": 17,
    "technology": 18,
    "history": 23,
    "general": 9
}

print("Welcome to the Interactive Knowledge Booster!")
print("Please select a topic:")
print("1. Science")
print("2. Technology")
print("3. History")
print("4. General Knowledge")

user_choice = int(input("Enter your choice (1-4): "))
selected_topic = list(topic_to_category.keys())[user_choice - 1]

print(f"You have selected the '{selected_topic}' topic.")
print(get_random_fact(selected_topic))
print("Now, let's test your knowledge with a quiz!")
run_quiz(selected_topic)
