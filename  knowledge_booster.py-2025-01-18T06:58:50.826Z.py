
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
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data[0]['fact']
    else:
        return "Error fetching data. Please try again later."

# Function to run the interactive quiz
def run_quiz(topic):
    api_key = "YOUR_API_KEY_HERE"
    url = topics[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        question = random.choice(data)['question']
        choices = [question['choice1'], question['choice2'], question['choice3'], question['choice4']]
        random.shuffle(choices)
        
        print(f"Question: {question['question']}")
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")
        
        user_answer = int(input("Enter your answer (1-4): "))
        if choices[user_answer-1] == question['answer']:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {question['answer']}")
    else:
        print("Error fetching data. Please try again later.")

# Main function
def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    
    for topic in topics:
        print(f"{topic}")
    
    selected_topic = input("Enter your choice: ")
    
    if selected_topic in topics:
        print(f"\nRandom fact about {selected_topic}:")
        print(get_random_fact(selected_topic))
        
        print("\nLet's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
