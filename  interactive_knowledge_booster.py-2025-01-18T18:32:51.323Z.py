
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

# Function to display the menu and get user's choice
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic}")
    return input("Enter your choice: ")

# Function to fetch a random fact or concept from the chosen topic
def get_random_fact(topic):
    api_url = topics[topic]
    if topic == "General Knowledge":
        response = requests.get(api_url)
        data = response.json()
        return data["results"][0]["question"], data["results"][0]["correct_answer"], data["results"][0]["incorrect_answers"]
    else:
        headers = {"X-Api-Key": "YOUR_API_KEY_HERE"}
        response = requests.get(api_url, headers=headers)
        data = response.json()
        return data[0]["fact"]

# Function to run the quiz
def run_quiz(topic, fact, correct_answer, incorrect_answers):
    print(f"\nTest your knowledge on {topic}!")
    print(fact)

    # Shuffle the answers
    all_answers = [correct_answer] + incorrect_answers
    random.shuffle(all_answers)

    # Display the multiple-choice options
    for i, answer in enumerate(all_answers):
        print(f"{i+1}. {answer}")

    # Get the user's answer
    user_answer = input("Enter the number of the correct answer: ")

    # Check the answer and provide feedback
    if all_answers[int(user_answer) - 1] == correct_answer:
        print("Correct! Well done.")
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}")

# Main function
def main():
    topic = display_menu()
    if topic in topics:
        if topic == "General Knowledge":
            fact, correct_answer, incorrect_answers = get_random_fact(topic)
            run_quiz(topic, fact, correct_answer, incorrect_answers)
        else:
            fact = get_random_fact(topic)
            print(f"\nHere's a random fact about {topic}:\n{fact}")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
