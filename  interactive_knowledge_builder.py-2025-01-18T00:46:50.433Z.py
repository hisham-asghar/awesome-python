
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
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]["fact"]

# Function to display the multiple-choice quiz question and get the user's answer
def quiz_question(topic):
    api_key = "YOUR_API_KEY_HERE"
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    question = data[0]["question"]
    choices = data[0]["choices"]
    correct_answer = data[0]["answer"]

    print(f"Question: {question}")
    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice}")

    user_answer = int(input("Enter your answer (1-4): "))
    if choices[user_answer-1] == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}")
        return False

# Main function to run the interactive knowledge-building script
def main():
    print("Welcome to the Interactive Knowledge-Building Script!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")

    selected_topic = input("Enter your topic choice: ")
    if selected_topic in topics:
        print(f"You've selected: {selected_topic}")
        print(get_random_fact(selected_topic))
        print("Let's test your knowledge with a quiz!")
        if quiz_question(selected_topic):
            print("Congratulations, you got the answer right!")
        else:
            print("Better luck next time!")
    else:
        print("Invalid topic choice. Please try again.")

if __name__ == "__main__":
    main()
