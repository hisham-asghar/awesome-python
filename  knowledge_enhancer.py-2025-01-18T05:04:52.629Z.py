
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

api_key = 'YOUR_API_KEY_HERE'

def get_random_fact(topic):
    """
    Fetches a random fact from the corresponding API endpoint for the selected topic.
    """
    url = api_endpoints[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    
    if topic == '4':
        data = response.json()['results'][0]
        fact = f"Question: {data['question']}"
    else:
        data = response.json()[0]
        fact = data['fact']
    
    return fact

def quiz_question(topic):
    """
    Fetches a multiple-choice quiz question from the corresponding API endpoint for the selected topic.
    """
    url = api_endpoints[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = response.json()['results'][0]
    
    question = data['question']
    choices = data['incorrect_answers'] + [data['correct_answer']]
    random.shuffle(choices)
    
    return question, choices

def main():
    """
    The main function that runs the interactive knowledge-enhancing script.
    """
    print("Welcome to the Interactive Knowledge Enhancer!")
    print("Please select a topic:")
    
    for key, value in topics.items():
        print(f"{key}. {value}")
    
    topic_choice = input("Enter the number of the topic you want to explore: ")
    
    if topic_choice in topics:
        print(f"\nYou have selected: {topics[topic_choice]}")
        
        if topic_choice == '4':
            question, choices = quiz_question(topic_choice)
            print(question)
            for i, choice in enumerate(choices, start=1):
                print(f"{i}. {choice}")
            
            user_answer = input("Enter the number of the correct answer: ")
            if str(choices.index(data['correct_answer']) + 1) == user_answer:
                print("Correct!")
            else:
                print(f"Incorrect. The correct answer is {data['correct_answer']}")
        else:
            fact = get_random_fact(topic_choice)
            print(f"\nHere's a random fact about {topics[topic_choice]}:\n{fact}")
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
