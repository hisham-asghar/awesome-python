
import random
import requests
import json

# Define topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://opentdb.com/api.php?amount=10&category=9&difficulty=medium&type=multiple"
}

# Function to get a random fact or concept from the selected topic
def get_random_fact(topic):
    if topic == "General Knowledge":
        response = requests.get(topics[topic])
        data = response.json()
        return data["results"][random.randint(0, 9)]
    else:
        response = requests.get(topics[topic], headers={"X-Api-Key": "YOUR_API_KEY_HERE"})
        data = response.json()
        return data[random.randint(0, len(data) - 1)]

# Function to run the interactive quiz
def run_quiz(topic):
    if topic == "General Knowledge":
        response = requests.get(topics[topic])
        data = response.json()
        for question in data["results"]:
            print(question["question"])
            answers = question["incorrect_answers"] + [question["correct_answer"]]
            random.shuffle(answers)
            for i, answer in enumerate(answers):
                print(f"{i+1}. {answer}")
            user_answer = int(input("Enter your answer (1-4): "))
            if answers[user_answer - 1] == question["correct_answer"]:
                print("Correct!")
            else:
                print(f"Incorrect. The correct answer is {question['correct_answer']}")
    else:
        print("Sorry, the quiz feature is not available for this topic yet.")

# Main function to display the menu and run the script
def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    selected_topic = input("Enter your choice: ")

    if selected_topic in topics:
        fact_or_concept = get_random_fact(selected_topic)
        print(f"\nHere's a random {selected_topic.lower()} fact or concept:")
        print(fact_or_concept)
        print("\nNow, let's test your knowledge!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
