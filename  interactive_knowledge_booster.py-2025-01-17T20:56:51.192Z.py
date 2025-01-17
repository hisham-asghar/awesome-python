
import random
import requests
import json

# Define topics and their corresponding API endpoints
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Function to fetch a random fact or concept from the chosen topic
def get_random_fact(topic):
    api_key = "YOUR_API_KEY_HERE"  # Replace with your API key
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    return data[0]["fact"]

# Function to run the interactive quiz
def run_quiz(topic):
    api_key = "YOUR_API_KEY_HERE"  # Replace with your API key
    url = topics[topic] + "?amount=5"
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)

    score = 0
    for question in data:
        print(question["question"])
        print("A. " + question["options"][0])
        print("B. " + question["options"][1])
        print("C. " + question["options"][2])
        print("D. " + question["options"][3])
        user_answer = input("Enter your answer (A-D): ").upper()
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is " + question["answer"] + ".")
        print()

    print(f"Your final score is {score} out of 5.")

# Main function to run the program
def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")

    chosen_topic = input("Enter your choice: ")
    if chosen_topic in topics:
        print(f"\nHere's a random fact about {chosen_topic}:")
        print(get_random_fact(chosen_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(chosen_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
