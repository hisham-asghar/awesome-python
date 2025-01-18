
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    "science": "https://api.api-ninjas.com/v1/science",
    "technology": "https://api.api-ninjas.com/v1/technology",
    "history": "https://api.api-ninjas.com/v1/history",
    "general_knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Replace with your API key
API_KEY = "your_api_key_here"

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the specified topic using the API.
    """
    url = topics[topic]
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]["fact"]

def quiz_question(topic):
    """
    Generates a multiple-choice quiz question for the specified topic using the API.
    """
    url = topics[topic]
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    question = data[0]["question"]
    options = data[0]["options"]
    answer = data[0]["answer"]
    return question, options, answer

def main():
    """
    The main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")

    # Display the topic menu
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic.capitalize()}")

    # Get user's topic choice
    choice = int(input("Enter the number of your chosen topic: "))
    selected_topic = list(topics.keys())[choice - 1]

    # Fetch and display a random fact or concept
    fact = get_random_fact(selected_topic)
    print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
    print(fact)

    # Run the quiz
    question, options, answer = quiz_question(selected_topic)
    print(f"\nNow, let's test your knowledge with a multiple-choice question:")
    print(question)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    user_answer = int(input("Enter the number of your answer: "))
    if options[user_answer - 1] == answer:
        print("Correct! You're a knowledge master.")
    else:
        print(f"Oops, the correct answer is '{answer}'.")

if __name__ == "__main__":
    main()
