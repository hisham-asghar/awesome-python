
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

# Function to fetch a random fact or concept from the chosen topic
def get_random_fact(topic):
    api_url = topics[topic]
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    
    if topic == "General Knowledge":
        data = response.json()["results"][0]
        fact = f"Question: {data['question']}\nAnswer: {data['correct_answer']}"
    else:
        data = response.json()[0]
        fact = data["fact"]
    
    return fact

# Function to run the interactive quiz
def run_quiz(topic):
    api_url = topics[topic]
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    
    if topic == "General Knowledge":
        data = response.json()["results"][0]
        question = data["question"]
        choices = data["incorrect_answers"] + [data["correct_answer"]]
        random.shuffle(choices)
        
        print(question)
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")
        
        user_answer = int(input("Enter your answer (1-4): "))
        if choices[user_answer-1] == data["correct_answer"]:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {data['correct_answer']}")
    else:
        print("Sorry, the quiz feature is not available for this topic yet.")

# Main function to run the interactive knowledge application
def run_knowledge_app():
    print("Welcome to the Interactive Knowledge App!")
    
    while True:
        print("\nPlease select a topic:")
        for topic in topics:
            print(f"- {topic}")
        
        chosen_topic = input("Enter your choice: ")
        
        if chosen_topic in topics:
            print(f"\nHere's a random fact about {chosen_topic}:")
            print(get_random_fact(chosen_topic))
            
            print("\nNow, let's test your knowledge!")
            run_quiz(chosen_topic)
        else:
            print("Invalid choice. Please try again.")

# Run the knowledge app
run_knowledge_app()
