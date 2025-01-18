
import random
import requests
import json

# Define topics and their corresponding API endpoints or data sources
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
    return data[0]

# Function to display the interactive quiz
def quiz(topic):
    # Fetch quiz questions and answers from the API or a predefined database
    api_key = "YOUR_API_KEY_HERE"
    url = topics[topic] + "/quiz"
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    quiz_data = response.json()

    # Loop through the quiz questions and get user input
    score = 0
    for question in quiz_data:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score is {score} out of {len(quiz_data)}.")

# Main function to run the interactive knowledge app
def main():
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    selected_topic = input("Enter your choice: ")

    if selected_topic in topics:
        fact = get_random_fact(selected_topic)
        print(f"\nHere's a random fact about {selected_topic.lower()}:")
        print(fact["fact"])
        print("\nNow, let's test your knowledge!")
        quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
