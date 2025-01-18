
import random
import requests
import json

# Define the topics and their corresponding APIs or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://opentdb.com/api.php?amount=1&type=multiple"
}

# Function to get a random fact or concept from the selected topic
def get_random_fact(topic):
    if topic == "General Knowledge":
        response = requests.get(topics[topic])
        data = response.json()
        fact = data["results"][0]["question"]
        return fact
    else:
        response = requests.get(topics[topic], headers={"X-Api-Key": "YOUR_API_KEY_HERE"})
        data = response.json()
        fact = random.choice(data)
        return fact

# Function to display the interactive quiz
def quiz(topic):
    if topic == "General Knowledge":
        response = requests.get(topics[topic])
        data = response.json()
        question = data["results"][0]["question"]
        correct_answer = data["results"][0]["correct_answer"]
        incorrect_answers = data["results"][0]["incorrect_answers"]
        answers = [correct_answer] + incorrect_answers
        random.shuffle(answers)
        print(f"Question: {question}")
        for i, answer in enumerate(answers):
            print(f"{i+1}. {answer}")
        user_answer = int(input("Enter the number of the correct answer: "))
        if answers[user_answer-1] == correct_answer:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {correct_answer}.")
    else:
        print("Sorry, interactive quizzes are not available for this topic yet.")

# Main function to display the menu and handle user input
def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"{topic}")
    selected_topic = input("Enter your choice: ")
    if selected_topic in topics:
        print(f"Here's a random fact about {selected_topic}:")
        print(get_random_fact(selected_topic))
        print("Let's test your knowledge!")
        quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
