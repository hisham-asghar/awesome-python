
import random
import requests
import json

# Define the topics and their corresponding API endpoints
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Function to fetch a random fact or concept from the chosen topic
def get_random_fact(topic):
    api_url = topics[topic]
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    data = response.json()
    return data[0]['fact']

# Function to run the interactive quiz
def run_quiz(topic):
    print(f"Welcome to the {topic} quiz!")
    print("Answer the multiple-choice questions to test your knowledge.")

    # Fetch quiz questions and answers from the API
    api_url = topics[topic] + "?type=multiple"
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    data = response.json()

    score = 0
    for question in data:
        print(question['question'])
        for i, answer in enumerate(question['options']):
            print(f"{i+1}. {answer}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer == question['answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", question['options'][question['answer']-1])
    print(f"Your final score: {score}/{len(data)}")

# Main function to run the script
def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")

    chosen_topic = input("Enter your choice: ")
    if chosen_topic in topics:
        print("\nHere's a random fact or concept from the", chosen_topic, "topic:")
        print(get_random_fact(chosen_topic))
        print("\nNow, let's test your knowledge!")
        run_quiz(chosen_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
