Here is the raw Python code extracted from the JSON:

```python
import random
import requests
import json

# Define the available topics
topics = {
    "1": "Science",
    "2": "Technology",
    "3": "History",
    "4": "General Knowledge"
}

# Function to display the menu and get user's topic choice
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for key, value in topics.items():
        print(f"{key}. {value}")
    return input("Enter your choice (1-4): ")

# Function to fetch a random fact or concept for the chosen topic
def get_random_fact(topic):
    # Fetch data from a public API or predefined database
    if topic == "Science":
        response = requests.get("https://api.api-ninjas.com/v1/facts?category=science")
    elif topic == "Technology":
        response = requests.get("https://api.api-ninjas.com/v1/facts?category=technology")
    elif topic == "History":
        response = requests.get("https://api.api-ninjas.com/v1/facts?category=history")
    elif topic == "General Knowledge":
        response = requests.get("https://api.api-ninjas.com/v1/facts?category=general")

    if response.status_code == 200:
        facts = response.json()
        return random.choice(facts)["fact"]
    else:
        return "Sorry, there was an error fetching the fact."

# Function to display the quiz and get user's answer
def quiz(topic):
    # Fetch quiz questions and answers from a public API or predefined database
    if topic == "Science":
        response = requests.get("https://opentdb.com/api.php?amount=1&category=17&difficulty=easy&type=multiple")
    elif topic == "Technology":
        response = requests.get("https://opentdb.com/api.php?amount=1&category=18&difficulty=easy&type=multiple")
    elif topic == "History":
        response = requests.get("https://opentdb.com/api.php?amount=1&category=23&difficulty=easy&type=multiple")
    elif topic == "General Knowledge":
        response = requests.get("https://opentdb.com/api.php?amount=1&category=9&difficulty=easy&type=multiple")

    if response.status_code == 200:
        question = response.json()["results"][0]["question"]
        correct_answer = response.json()["results"][0]["correct_answer"]
        incorrect_answers = response.json()["results"][0]["incorrect_answers"]
        all_answers = [correct_answer] + incorrect_answers
        random.shuffle(all_answers)

        print(f"Question: {question}")
        for i, answer in enumerate(all_answers):
            print(f"{i+1}. {answer}")

        user_answer = input("Enter the number of the correct answer: ")
        if all_answers[int(user_answer) - 1] == correct_answer:
            return "Correct!"
        else:
            return f"Incorrect. The correct answer is: {correct_answer}"
    else:
        return "Sorry, there was an error fetching the quiz."

# Main function to run the script
def main():
    topic_choice = display_menu()
    topic = topics[topic_choice]
    print(f"\nYour chosen topic is: {topic}")

    print("\nHere's a random fact or concept about the topic:")
    print(get_random_fact(topic))

    print("\nNow, let's test your knowledge with a quiz!")
    print(quiz(topic))

if __name__ == "__main__":
    main()
