
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://opentdb.com/api.php?amount=1&type=multiple"
}

# Define the API key for the API-Ninjas endpoints
api_key = "YOUR_API_KEY_HERE"

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the selected topic.
    """
    if topic in topics:
        url = topics[topic]
        headers = {"X-Api-Key": api_key}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if topic == "General Knowledge":
                return data["results"][0]["question"], data["results"][0]["correct_answer"], data["results"][0]["incorrect_answers"]
            else:
                return data[0]["fact"]
        else:
            return "Error fetching data. Please try again later."
    else:
        return "Invalid topic. Please select a valid topic."

def quiz(topic):
    """
    Provides an interactive quiz for the selected topic.
    """
    fact, correct_answer, incorrect_answers = get_random_fact(topic)
    print(fact)
    
    # Combine the correct and incorrect answers in a random order
    all_answers = [correct_answer] + incorrect_answers
    random.shuffle(all_answers)
    
    # Ask the user to select the correct answer
    print("Choose the correct answer:")
    for i, answer in enumerate(all_answers):
        print(f"{i+1}. {answer}")
    
    user_answer = input("Enter the number of the correct answer: ")
    
    if all_answers[int(user_answer)-1] == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}")

def main():
    """
    Main function that displays the menu and handles user input.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    
    for topic in topics:
        print(f"{topic}")
    
    selected_topic = input("Enter your choice: ")
    
    quiz(selected_topic)

if __name__ == "__main__":
    main()
