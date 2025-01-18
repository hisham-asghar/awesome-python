
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

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    if topic == "General Knowledge":
        response = requests.get(topics[topic])
        data = response.json()
        return data["results"][0]
    else:
        response = requests.get(topics[topic], headers={"X-Api-Key": "YOUR_API_KEY_HERE"})
        data = response.json()
        return random.choice(data)

# Function to display the menu and get user's topic selection
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for i, topic in enumerate(topics.keys()):
        print(f"{i+1}. {topic}")
    
    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if 1 <= choice <= len(topics):
                return list(topics.keys())[choice - 1]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to run the interactive quiz
def run_quiz(topic):
    if topic == "General Knowledge":
        response = requests.get(topics[topic])
        data = response.json()
        question = data["results"][0]["question"]
        correct_answer = data["results"][0]["correct_answer"]
        incorrect_answers = data["results"][0]["incorrect_answers"]
    else:
        fact = get_random_fact(topic)
        question = fact["question"]
        correct_answer = fact["answer"]
        incorrect_answers = [fact["incorrect1"], fact["incorrect2"], fact["incorrect3"]]
    
    answers = [correct_answer] + incorrect_answers
    random.shuffle(answers)
    
    print(f"Question: {question}")
    for i, answer in enumerate(answers):
        print(f"{i+1}. {answer}")
    
    while True:
        try:
            user_answer = int(input("Enter your answer (1-4): "))
            if 1 <= user_answer <= len(answers):
                if answers[user_answer - 1] == correct_answer:
                    print("Correct!")
                else:
                    print(f"Incorrect. The correct answer is: {correct_answer}")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main function to run the script
def main():
    topic = display_menu()
    fact_or_concept = get_random_fact(topic)
    print(f"\nHere's a {topic.lower()} fact or concept for you:")
    print(fact_or_concept)
    
    print("\nNow, let's test your knowledge!")
    run_quiz(topic)

if __name__ == "__main__":
    main()
