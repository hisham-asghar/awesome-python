
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    '1': 'Science',
    '2': 'Technology',
    '3': 'History',
    '4': 'General Knowledge'
}

def get_random_fact(topic):
    """
    Fetch a random fact or concept from the chosen topic.
    """
    if topic == '1':
        # Fetch a random science fact from an API or database
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=science', headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
        data = response.json()
        return data[0]['fact']
    elif topic == '2':
        # Fetch a random technology fact from an API or database
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=technology', headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
        data = response.json()
        return data[0]['fact']
    elif topic == '3':
        # Fetch a random history fact from an API or database
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=history', headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
        data = response.json()
        return data[0]['fact']
    elif topic == '4':
        # Fetch a random general knowledge fact from an API or database
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=general', headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
        data = response.json()
        return data[0]['fact']
    else:
        return "Invalid topic selection."

def quiz(topic):
    """
    Provide a multiple-choice quiz for the chosen topic.
    """
    if topic == '1':
        # Fetch science-related quiz questions and answers from an API or database
        response = requests.get('https://api.api-ninjas.com/v1/trivia?category=science', headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
        data = response.json()
        question = data[0]['question']
        options = data[0]['options']
        answer = data[0]['answer']
    elif topic == '2':
        # Fetch technology-related quiz questions and answers from an API or database
        response = requests.get('https://api.api-ninjas.com/v1/trivia?category=technology', headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
        data = response.json()
        question = data[0]['question']
        options = data[0]['options']
        answer = data[0]['answer']
    elif topic == '3':
        # Fetch history-related quiz questions and answers from an API or database
        response = requests.get('https://api.api-ninjas.com/v1/trivia?category=history', headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
        data = response.json()
        question = data[0]['question']
        options = data[0]['options']
        answer = data[0]['answer']
    elif topic == '4':
        # Fetch general knowledge-related quiz questions and answers from an API or database
        response = requests.get('https://api.api-ninjas.com/v1/trivia?category=general', headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
        data = response.json()
        question = data[0]['question']
        options = data[0]['options']
        answer = data[0]['answer']
    else:
        return "Invalid topic selection."

    print(question)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    user_answer = input("Enter your answer (1-4): ")
    if user_answer == answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {answer}.")

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for key, value in topics.items():
        print(f"{key}. {value}")

    topic_choice = input("Enter the number of the topic (1-4): ")

    print(f"You selected: {topics[topic_choice]}")
    print(get_random_fact(topic_choice))
    print()
    quiz(topic_choice)

if __name__ == "__main__":
    main()
