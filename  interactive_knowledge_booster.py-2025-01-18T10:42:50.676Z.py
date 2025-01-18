
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    api_key = "YOUR_API_KEY_HERE"
    url = topics[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]['fact']

# Function to display the multiple-choice quiz
def quiz(topic):
    # Fetch quiz questions and answers from the API or a predefined database
    api_key = "YOUR_API_KEY_HERE"
    url = topics[topic] + "/quiz"
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    quiz_data = response.json()

    score = 0
    for question in quiz_data:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer == question['answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is", question['answer'])
    print(f"Your score: {score}/{len(quiz_data)}")

# Main program loop
while True:
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    selected_topic = input("Enter your choice: ")

    if selected_topic in topics:
        print(f"\nRandom fact about {selected_topic}:")
        print(get_random_fact(selected_topic))
        print("\nNow let's test your knowledge!")
        quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

    print("\nDo you want to explore another topic? (y/n)")
    if input().lower() != 'y':
        break
