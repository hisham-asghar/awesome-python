
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/facts?category=science",
    "Technology": "https://api.api-ninjas.com/v1/facts?category=technology",
    "History": "https://api.api-ninjas.com/v1/facts?category=history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Function to display the menu and get user's topic choice
def display_menu():
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    
    while True:
        choice = input("Enter your choice: ").title()
        if choice in topics:
            return choice
        else:
            print("Invalid choice. Please try again.")

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    api_url = topics[topic]
    response = requests.get(api_url, headers={"X-Api-Key": "YOUR_API_KEY_HERE"})
    
    if response.status_code == 200:
        data = response.json()
        if topic == "General Knowledge":
            return data[0]["question"], data[0]["answer"]
        else:
            return data[0]["fact"]
    else:
        return "Sorry, we couldn't fetch the information. Please try again later."

# Function to run the interactive quiz
def run_quiz(topic):
    print(f"\nLet's test your {topic} knowledge!")
    
    # Fetch the quiz questions and answers
    api_url = topics[topic]
    response = requests.get(api_url, headers={"X-Api-Key": "YOUR_API_KEY_HERE"})
    
    if response.status_code == 200:
        data = response.json()
        if topic == "General Knowledge":
            questions_answers = [(item["question"], item["answer"]) for item in data]
        else:
            questions_answers = [(f"What is the fact about {topic.lower()}?", item["fact"]) for item in data]
        
        # Shuffle the questions and answers
        random.shuffle(questions_answers)
        
        # Run the quiz
        score = 0
        for question, answer in questions_answers:
            print(f"\n{question}")
            user_answer = input("Your answer: ").lower()
            if user_answer == answer.lower():
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer is: {answer}")
        
        print(f"\nYour final score: {score}/{len(questions_answers)}")
    else:
        print("Sorry, we couldn't fetch the quiz questions. Please try again later.")

# Main function
def main():
    topic = display_menu()
    print(f"\nHere's a random fact about {topic}:")
    fact_or_question, answer = get_random_fact(topic)
    print(fact_or_question)
    
    run_quiz(topic)

if __name__ == "__main__":
    main()
