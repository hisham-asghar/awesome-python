
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

# API key for API-Ninjas
api_key = "YOUR_API_KEY_HERE"

def get_random_fact(topic):
    """
    Fetch a random fact or concept from the specified topic using the API-Ninjas API.
    """
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = json.loads(response.text)
        return data[0]["fact"]
    else:
        return "Error: Could not fetch data from the API."

def quiz(topic):
    """
    Provide an interactive quiz for the user to test their knowledge on the selected topic.
    """
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = json.loads(response.text)
        question = random.choice(data)
        choices = [question["fact"]]
        
        # Generate three incorrect choices
        for i in range(3):
            incorrect_choice = random.choice(data)
            while incorrect_choice["fact"] in choices:
                incorrect_choice = random.choice(data)
            choices.append(incorrect_choice["fact"])
        
        random.shuffle(choices)
        
        print(f"Question: {question['fact']}")
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")
        
        user_answer = int(input("Enter the number of the correct answer: "))
        if choices[user_answer-1] == question["fact"]:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {question['fact']}")
    else:
        print("Error: Could not fetch data from the API.")

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    
    for topic in topics:
        print(f"{topic}")
    
    selected_topic = input("Enter your choice: ")
    
    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic}:")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge!")
        quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
