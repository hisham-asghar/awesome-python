
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

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    api_key = "YOUR_API_KEY_HERE"
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    return data[0]["fact"]

# Function to display the menu and get the user's topic selection
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    return input("Enter your choice: ")

# Function to run the quiz for the selected topic
def run_quiz(topic):
    print(f"\nLet's test your {topic.lower()} knowledge!")
    
    # Fetch quiz questions and answers from the API
    api_key = "YOUR_API_KEY_HERE"
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    
    # Shuffle the questions and answers
    quiz_data = random.sample(data, 3)
    
    # Run the quiz
    score = 0
    for question in quiz_data:
        print(f"\nQuestion: {question['question']}")
        for i, answer in enumerate(question["options"]):
            print(f"{i+1}. {answer}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", question["options"][question["answer"]-1])
    
    print(f"\nYour final score: {score} out of 3")

# Main function
def main():
    topic = display_menu()
    fact = get_random_fact(topic)
    print(f"\nHere's a random {topic.lower()} fact for you:")
    print(fact)
    run_quiz(topic)

if __name__ == "__main__":
    main()
