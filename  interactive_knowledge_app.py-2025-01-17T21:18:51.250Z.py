
import random
import requests
import json

# Define topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.example.com/science",
    "Technology": "https://api.example.com/technology",
    "History": "https://api.example.com/history",
    "General Knowledge": "https://api.example.com/general"
}

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    api_url = topics[topic]
    response = requests.get(api_url)
    data = json.loads(response.text)
    return random.choice(data)

# Function to display a multiple-choice quiz question
def quiz_question(topic):
    api_url = topics[topic] + "/quiz"
    response = requests.get(api_url)
    data = json.loads(response.text)
    question = data["question"]
    choices = data["choices"]
    correct_answer = data["correct_answer"]

    print(f"Question: {question}")
    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice}")

    user_answer = int(input("Enter your answer (1-4): "))
    if choices[user_answer-1] == correct_answer:
        print("Correct!")
        return True
    else:
        print("Incorrect. The correct answer is:", correct_answer)
        return False

# Main function to run the interactive knowledge app
def main():
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")

    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")

    topic_choice = int(input("Enter your choice (1-4): "))
    selected_topic = list(topics.keys())[topic_choice-1]

    print(f"\nYou selected: {selected_topic}")
    print(get_random_fact(selected_topic))

    print("\nNow let's test your knowledge with a quiz!")
    score = 0
    for _ in range(3):
        if quiz_question(selected_topic):
            score += 1
    print(f"Your score: {score}/3")

if __name__ == "__main__":
    main()
