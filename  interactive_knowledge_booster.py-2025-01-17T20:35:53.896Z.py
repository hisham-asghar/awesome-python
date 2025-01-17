
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
            "The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.",
            "A group of porcupines is called a prickle."
        ],
        "technology": [
            "The first computer bug was a real bug (a moth) trapped in a Harvard Mark II computer.",
            "The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.",
            "The term 'bug' was first used in computing in 1945 when a technician found a moth stuck in a Harvard Mark II computer."
        ],
        "history": [
            "The Great Wall of China is the only man-made structure visible from space.",
            "The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and raises the structure.",
            "The first person convicted of speeding was going 8 mph."
        ],
        "general": [
            "A group of porcupines is called a prickle.",
            "The first product to have a barcode was Wrigley's gum.",
            "The King of Hearts is the only king without a mustache on a standard playing card."
        ]
    }

    return random.choice(facts[topic])

def quiz(topic):
    """
    Provides a multiple-choice quiz for the given topic, using trivia data fetched from an API.
    """
    url = f"https://opentdb.com/api.php?amount=1&category={topic_to_category[topic]}&type=multiple"
    response = requests.get(url)
    data = response.json()
    question = data['results'][0]['question']
    correct_answer = data['results'][0]['correct_answer']
    incorrect_answers = data['results'][0]['incorrect_answers']
    all_answers = [correct_answer] + incorrect_answers
    random.shuffle(all_answers)

    print(f"Question: {question}")
    for i, answer in enumerate(all_answers):
        print(f"{i+1}. {answer}")

    user_answer = int(input("Enter the number of the correct answer: "))
    if all_answers[user_answer-1] == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}")

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

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    topic = "science"
elif choice == 2:
    topic = "technology"
elif choice == 3:
    topic = "history"
elif choice == 4:
    topic = "general"
else:
    print("Invalid choice. Exiting.")
    exit()

print(f"\nHere's a random fact about {topic}:")
print(get_random_fact(topic))

print("\nNow, let's test your knowledge with a quiz!")
quiz(topic)

print("\nThanks for using the Interactive Knowledge Booster!")
