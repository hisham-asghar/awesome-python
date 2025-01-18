
import random
import requests
import json

# Define the topics and their corresponding data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    url = topics[topic]
    response = requests.get(url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    data = response.json()
    return random.choice(data)

# Function to display a multiple-choice quiz for the selected topic
def quiz(topic):
    url = topics[topic]
    response = requests.get(url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    data = response.json()
    question = random.choice(data)
    choices = [question['fact']] + [random.choice(data)['fact'] for _ in range(3)]
    random.shuffle(choices)
    print(f"Question: {question['fact']}")
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")
    user_answer = int(input("Enter your answer (1-4): "))
    if choices[user_answer - 1] == question['fact']:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {question['fact']}")

# Main function to run the interactive knowledge booster
def main():
    print("Welcome to the Interactive Knowledge Booster!")
    while True:
        print("\nSelect a topic:")
        for i, topic in enumerate(topics, start=1):
            print(f"{i}. {topic}")
        print("5. Exit")
        choice = int(input("Enter your choice (1-5): "))
        if choice == 5:
            print("Goodbye!")
            break
        elif 1 <= choice <= 4:
            topic = list(topics.keys())[choice - 1]
            print(f"\nHere's a random fact or concept from the {topic} topic:")
            fact = get_random_fact(topic)
            print(fact['fact'])
            print("\nLet's test your knowledge!")
            quiz(topic)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
