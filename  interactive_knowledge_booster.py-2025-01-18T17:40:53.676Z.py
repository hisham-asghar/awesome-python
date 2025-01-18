
import random
import requests
import json

# Define the topics and their corresponding API endpoints
topics = {
    "Science": "https://api.api-ninjas.com/v1/randomfact?category=science",
    "Technology": "https://api.api-ninjas.com/v1/randomfact?category=technology",
    "History": "https://api.api-ninjas.com/v1/randomfact?category=history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Define the API key for the API-Ninjas service
api_key = "YOUR_API_KEY_HERE"

def get_random_fact(topic):
    """
    Fetch a random fact or trivia from the specified topic using the API-Ninjas service.
    """
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data["fact"] if topic != "General Knowledge" else data["question"]

def quiz(topic):
    """
    Provide a multiple-choice quiz for the specified topic.
    """
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    
    if topic != "General Knowledge":
        print(f"Random {topic.lower()} fact: {data['fact']}")
        print("Test your knowledge with a multiple-choice question!")
        print(data["question"])
        options = data["options"]
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        
        while True:
            user_answer = input("Enter the number of the correct answer: ")
            if user_answer.isdigit() and 1 <= int(user_answer) <= len(options):
                if int(user_answer) == data["correct_answer"]:
                    print("Correct!")
                else:
                    print("Incorrect. Better luck next time!")
                break
            else:
                print("Invalid input. Please try again.")
    else:
        print(f"Random general knowledge trivia: {data['question']}")
        print("Choose the correct answer:")
        options = data["options"]
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        
        while True:
            user_answer = input("Enter the number of the correct answer: ")
            if user_answer.isdigit() and 1 <= int(user_answer) <= len(options):
                if int(user_answer) == data["correct_answer"]:
                    print("Correct!")
                else:
                    print("Incorrect. Better luck next time!")
                break
            else:
                print("Invalid input. Please try again.")

def main():
    """
    Main function that displays the topic menu and runs the interactive quiz.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    
    while True:
        user_topic = input("Enter your choice (or 'q' to quit): ")
        if user_topic.lower() == 'q':
            print("Goodbye!")
            break
        elif user_topic in topics:
            quiz(user_topic)
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
