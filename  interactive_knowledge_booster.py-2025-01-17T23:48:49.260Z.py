
import random
import requests
import json

# Define the topics and their corresponding APIs or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/randomfact?category=science",
    "Technology": "https://api.api-ninjas.com/v1/randomfact?category=technology",
    "History": "https://api.api-ninjas.com/v1/randomfact?category=history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Function to get a random fact or trivia
def get_random_fact_or_trivia(topic):
    api_url = topics[topic]
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    data = response.json()
    return data["fact"] if topic != "General Knowledge" else data["question"]

# Function to display the menu and get user input
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    return input("Enter your choice: ")

# Function to run the quiz
def run_quiz(topic):
    fact_or_trivia = get_random_fact_or_trivia(topic)
    print(f"\n{topic} fact/trivia: {fact_or_trivia}")

    if topic == "General Knowledge":
        options = data["options"]
        print("Choose the correct answer:")
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer == data["correct_answer"]:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", options[data["correct_answer"]-1])
    else:
        input("Press Enter to continue...")

# Main function
def main():
    topic = display_menu()
    run_quiz(topic)

if __name__ == "__main__":
    main()
