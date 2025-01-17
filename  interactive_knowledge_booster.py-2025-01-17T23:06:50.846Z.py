
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
    url = topics[topic]
    response = requests.get(url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    data = response.json()
    return data[0]['fact']

# Function to display the multiple-choice quiz
def quiz(topic):
    url = topics[topic]
    response = requests.get(url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    data = response.json()
    question = data[0]['question']
    answers = data[0]['options']
    correct_answer = data[0]['answer']

    print(f"Question: {question}")
    for i, answer in enumerate(answers):
        print(f"{i+1}. {answer}")

    user_answer = int(input("Enter your answer (1-4): "))
    if answers[user_answer-1] == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}")

# Main function
def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")

    selected_topic = input("Enter your choice: ")

    if selected_topic in topics:
        print(f"Random fact about {selected_topic.lower()}: {get_random_fact(selected_topic)}")
        print("Let's test your knowledge with a quiz!")
        quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
