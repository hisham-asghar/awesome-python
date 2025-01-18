
import random
import requests
import json

# Define topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.sampleapis.com/science/science",
    "Technology": "https://api.sampleapis.com/tech/tech",
    "History": "https://api.sampleapis.com/history/history",
    "General Knowledge": "https://api.sampleapis.com/generalknowledge/generalknowledge"
}

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the specified topic.
    """
    try:
        response = requests.get(topics[topic])
        data = json.loads(response.text)
        random_index = random.randint(0, len(data) - 1)
        return data[random_index]
    except (requests.exceptions.RequestException, KeyError, IndexError):
        return "Sorry, there was an error fetching the information."

def quiz(topic):
    """
    Provides an interactive quiz for the specified topic.
    """
    try:
        response = requests.get(topics[topic])
        data = json.loads(response.text)
        random_index = random.randint(0, len(data) - 1)
        question = data[random_index]["question"]
        options = data[random_index]["options"]
        answer = data[random_index]["answer"]

        print(f"Question: {question}")
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

        user_answer = int(input("Enter the number of the correct answer: "))
        if options[user_answer - 1] == answer:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {answer}")
    except (requests.exceptions.RequestException, KeyError, IndexError, ValueError):
        print("Sorry, there was an error running the quiz.")

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")

    for topic in topics:
        print(f"{topic}")

    selected_topic = input("Enter the topic you'd like to explore: ")

    if selected_topic in topics:
        fact = get_random_fact(selected_topic)
        print(f"\nFact about {selected_topic}: {fact['fact']}")

        quiz_choice = input("\nWould you like to take a quiz on this topic? (y/n) ")
        if quiz_choice.lower() == "y":
            quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
