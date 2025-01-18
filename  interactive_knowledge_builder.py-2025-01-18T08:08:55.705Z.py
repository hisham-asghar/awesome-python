Here is the raw Python code extracted from the JSON:

```python
import random
import requests
import json

# API endpoint for fetching trivia data
TRIVIA_API_ENDPOINT = "https://opentdb.com/api.php?amount=1&type=multiple"

# Topics and their corresponding trivia categories
TOPICS = {
    "Science": 17,
    "Technology": 18,
    "History": 23,
    "General Knowledge": 9
}

def get_trivia_data(topic):
    """
    Fetch a random trivia question and answer from the OpenTDB API.
    """
    params = {
        "amount": 1,
        "category": TOPICS[topic],
        "type": "multiple"
    }
    response = requests.get(TRIVIA_API_ENDPOINT, params=params)
    return response.json()["results"][0]

def display_fact(topic, data):
    """
    Display a short explanation of the trivia fact or concept.
    """
    print(f"Here's a random {topic.lower()} fact or concept:")
    print(data["question"])
    print(f"Explanation: {data['correct_answer']}")

def quiz_question(data):
    """
    Present a multiple-choice quiz question to the user.
    """
    answers = data["incorrect_answers"] + [data["correct_answer"]]
    random.shuffle(answers)
    print("What is the correct answer?")
    for i, answer in enumerate(answers):
        print(f"{i+1}. {answer}")
    user_answer = int(input("Enter the number of your answer: "))
    if answers[user_answer-1] == data["correct_answer"]:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {data['correct_answer']}")

def main():
    """
    The main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")
    for topic in TOPICS:
        print(f"- {topic}")
    chosen_topic = input("Enter your choice: ")

    if chosen_topic in TOPICS:
        trivia_data = get_trivia_data(chosen_topic)
        display_fact(chosen_topic, trivia_data)
        quiz_question(trivia_data)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
