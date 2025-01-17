
import random
import requests
import json

# Define a dictionary of topics and their corresponding API endpoints or data sources
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
    data = response.json()
    return data[0]['fact']

# Define a function to display a multiple-choice quiz for the selected topic
def quiz(topic):
    api_key = "YOUR_API_KEY_HERE"
    url = topics[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    question = data[0]['question']
    choices = data[0]['choices']
    answer = data[0]['answer']
    print(f"Question: {question}")
    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice}")
    user_answer = int(input("Enter your answer (1-4): "))
    if choices[user_answer-1] == answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {answer}.")

# Main program loop
while True:
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    selected_topic = input("Enter your choice: ")
    if selected_topic in topics:
        print(f"Here's a random fact about {selected_topic}:")
        print(get_random_fact(selected_topic))
        print("Now, let's test your knowledge with a quiz!")
        quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")
    print("Would you like to explore another topic? (y/n)")
    if input().lower() != 'y':
        break
print("Thank you for using the Interactive Knowledge Booster!")
