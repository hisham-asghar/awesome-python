
import random
import requests
import json

# Define a dictionary of topics and their corresponding API endpoints
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Define a function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    api_key = "YOUR_API_KEY_HERE"
    url = topics[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    return data[0]['fact']

# Define a function to run the interactive quiz
def run_quiz(topic):
    # Fetch questions and answers from the selected topic
    api_key = "YOUR_API_KEY_HERE"
    url = topics[topic] + "?limit=5"
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)

    # Run the quiz
    score = 0
    for question in data:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer == question['answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score is {score} out of 5.")

# Main program loop
while True:
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    selected_topic = input("Enter your choice: ")

    if selected_topic in topics:
        print(f"Random fact about {selected_topic}:")
        print(get_random_fact(selected_topic))
        print("Let's test your knowledge!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

    continue_prompt = input("Do you want to try another topic? (y/n) ")
    if continue_prompt.lower() != 'y':
        break
