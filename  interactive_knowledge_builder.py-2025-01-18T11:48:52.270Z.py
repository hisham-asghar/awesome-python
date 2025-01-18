
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

# Function to fetch a random fact or concept from the chosen topic
def get_random_fact(topic):
    api_key = "YOUR_API_KEY_HERE"
    url = topics[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data[0]["fact"]
    else:
        return "Sorry, we couldn't fetch a fact right now. Please try again later."

# Function to run the interactive quiz
def run_quiz(topic):
    api_key = "YOUR_API_KEY_HERE"
    url = topics[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        question = random.choice(data)
        choices = ["A", "B", "C", "D"]
        random.shuffle(choices)
        
        print(f"Question: {question['question']}")
        for choice in choices:
            print(f"{choice}) {question[f'answer_{choice.lower()}']}")
        
        user_answer = input("Enter your answer (A, B, C, or D): ").upper()
        
        if user_answer == question["correct_answer"].upper():
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {question['correct_answer']}.")
    else:
        print("Sorry, we couldn't fetch a quiz question right now. Please try again later.")

# Main function to run the interactive knowledge-building script
def main():
    print("Welcome to the Interactive Knowledge Builder!")
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
