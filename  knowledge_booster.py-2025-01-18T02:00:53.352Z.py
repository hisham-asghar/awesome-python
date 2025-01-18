
import random
import requests
import json

# Define topics and their corresponding API endpoints
topics = {
    '1': 'Science',
    '2': 'Technology',
    '3': 'History',
    '4': 'General Knowledge'
}

api_endpoints = {
    '1': 'https://api.api-ninjas.com/v1/facts?category=science',
    '2': 'https://api.api-ninjas.com/v1/facts?category=technology',
    '3': 'https://api.api-ninjas.com/v1/facts?category=history',
    '4': 'https://opentdb.com/api.php?amount=1&type=multiple'
}

# API key for API-Ninjas
api_key = 'YOUR_API_KEY_HERE'

def get_fact(topic):
    """
    Fetches a random fact or concept from the corresponding API endpoint.
    """
    url = api_endpoints[topic]
    headers = {'X-Api-Key': api_key}

    if topic == '4':
        response = requests.get(url)
        data = response.json()
        return data['results'][0]
    else:
        response = requests.get(url, headers=headers)
        data = response.json()
        return random.choice(data)

def quiz(topic):
    """
    Presents a multiple-choice quiz to the user based on the selected topic.
    """
    url = api_endpoints[topic]
    headers = {'X-Api-Key': api_key}

    if topic == '4':
        response = requests.get(url)
        data = response.json()
        question = data['results'][0]['question']
        correct_answer = data['results'][0]['correct_answer']
        incorrect_answers = data['results'][0]['incorrect_answers']
        answers = [correct_answer] + incorrect_answers
        random.shuffle(answers)

        print(f"Question: {question}")
        for i, answer in enumerate(answers):
            print(f"{i+1}. {answer}")

        user_answer = input("Enter the number of the correct answer: ")
        if answers[int(user_answer) - 1] == correct_answer:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {correct_answer}.")
    else:
        fact = get_fact(topic)
        print(f"Fact: {fact['fact']}")

def main():
    """
    Main function that displays the menu, gets user input, and calls the appropriate functions.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")

    for topic_id, topic_name in topics.items():
        print(f"{topic_id}. {topic_name}")

    user_choice = input("Enter the number of the topic: ")

    if user_choice in topics:
        print(f"You selected: {topics[user_choice]}")
        quiz(user_choice)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
