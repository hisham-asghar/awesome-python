
import random
import requests
import json

# Define the available topics
topics = {
    '1': 'Science',
    '2': 'Technology',
    '3': 'History',
    '4': 'General Knowledge'
}

# Define the API endpoints for each topic
api_endpoints = {
    'Science': 'https://api.api-ninjas.com/v1/science',
    'Technology': 'https://api.api-ninjas.com/v1/technology',
    'History': 'https://api.api-ninjas.com/v1/history',
    'General Knowledge': 'https://api.api-ninjas.com/v1/trivia'
}

# Define the API key
api_key = 'YOUR_API_KEY_HERE'

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the specified topic using the API.
    """
    url = api_endpoints[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    return data[0]['fact']

def quiz(topic):
    """
    Provides a multiple-choice quiz for the specified topic.
    """
    url = api_endpoints[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    question = random.choice(data)
    choices = [question['fact']]
    for i in range(3):
        choices.append(random.choice(data)['fact'])
    random.shuffle(choices)
    print(f"Question: {question['fact']}")
    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice}")
    user_answer = int(input("Enter your answer (1-4): "))
    if choices[user_answer-1] == question['fact']:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {question['fact']}")

def main():
    """
    Displays the topic menu, allows the user to select a topic, and then
    provides a random fact or concept and a multiple-choice quiz.
    """
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    for key, value in topics.items():
        print(f"{key}. {value}")
    topic_choice = input("Enter the number of the topic: ")
    topic = topics[topic_choice]
    print(f"You selected: {topic}")
    print(f"Random {topic} fact: {get_random_fact(topic)}")
    print("Now, let's test your knowledge with a quiz!")
    quiz(topic)

if __name__ == "__main__":
    main()
