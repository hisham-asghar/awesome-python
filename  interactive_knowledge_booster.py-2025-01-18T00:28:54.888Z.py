
import random
import requests
import json

# Define topics and their corresponding APIs or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://opentdb.com/api.php?amount=10&type=multiple"
}

# Function to get a random fact or concept from the selected topic
def get_random_fact(topic):
    if topic in ["Science", "Technology", "History"]:
        api_url = topics[topic]
        response = requests.get(api_url, headers={"X-Api-Key": "YOUR_API_KEY_HERE"})
        data = response.json()
        return data[0]["fact"]
    elif topic == "General Knowledge":
        api_url = topics[topic]
        response = requests.get(api_url)
        data = response.json()
        return data["results"][random.randint(0, 9)]["question"]

# Function to run the interactive quiz
def run_quiz(topic):
    if topic in ["Science", "Technology", "History"]:
        api_url = topics[topic]
        response = requests.get(api_url, headers={"X-Api-Key": "YOUR_API_KEY_HERE"})
        data = response.json()
        question = data[random.randint(0, len(data) - 1)]["fact"]
        choices = [data[random.randint(0, len(data) - 1)]["fact"] for _ in range(3)]
        choices.insert(random.randint(0, 3), question)
        random.shuffle(choices)
        print(f"Question: {question}")
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")
        user_answer = int(input("Enter your answer (1-4): "))
        if choices[user_answer - 1] == question:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", question)
    elif topic == "General Knowledge":
        api_url = topics[topic]
        response = requests.get(api_url)
        data = response.json()
        question = data["results"][random.randint(0, 9)]["question"]
        correct_answer = data["results"][random.randint(0, 9)]["correct_answer"]
        incorrect_answers = data["results"][random.randint(0, 9)]["incorrect_answers"]
        choices = [correct_answer] + incorrect_answers
        random.shuffle(choices)
        print(f"Question: {question}")
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")
        user_answer = int(input("Enter your answer (1-4): "))
        if choices[user_answer - 1] == correct_answer:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", correct_answer)

# Main function
def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    selected_topic = input("Enter your choice: ")

    if selected_topic in topics:
        print(f"\nHere's a random fact or concept from the {selected_topic} topic:")
        print(get_random_fact(selected_topic))
        print("\nLet's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
