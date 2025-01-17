
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/facts?category=science",
    "Technology": "https://api.api-ninjas.com/v1/facts?category=technology",
    "History": "https://api.api-ninjas.com/v1/facts?category=history",
    "General Knowledge": "https://api.api-ninjas.com/v1/facts?category=general"
}

# Function to fetch a random fact or concept from the chosen topic
def get_random_fact(topic):
    api_key = "YOUR_API_KEY_HERE"
    url = topics[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    return random.choice(data)['fact']

# Function to display the menu and get the user's topic choice
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    return input("Enter your choice: ")

# Function to run the interactive quiz
def run_quiz(topic):
    print(f"\nLet's test your {topic.lower()} knowledge!")
    
    # Fetch quiz questions and answers from a database or API
    quiz_data = fetch_quiz_data(topic)
    
    score = 0
    for question, options, answer in quiz_data:
        print(question)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if options[user_answer-1] == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {answer}")
    
    print(f"\nYour final score is: {score}/{len(quiz_data)}")

# Function to fetch quiz data from a database or API
def fetch_quiz_data(topic):
    # Replace this with your actual data fetching logic
    quiz_data = [
        ("What is the chemical symbol for gold?", ["Au", "Ag", "Cu", "Fe"], "Au"),
        ("Who invented the telephone?", ["Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Marie Curie"], "Alexander Graham Bell"),
        ("Which is the largest planet in our solar system?", ["Earth", "Mars", "Jupiter", "Saturn"], "Jupiter")
    ]
    return quiz_data

def main():
    topic = display_menu()
    fact = get_random_fact(topic)
    print(f"\nHere's a random {topic.lower()} fact for you:")
    print(fact)
    run_quiz(topic)

if __name__ == "__main__":
    main()
