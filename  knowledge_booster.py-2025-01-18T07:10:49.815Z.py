
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    "1. Science": "https://api.sampleapis.com/science/facts",
    "2. Technology": "https://api.sampleapis.com/tech/facts",
    "3. History": "https://api.sampleapis.com/history/facts",
    "4. General Knowledge": "https://api.sampleapis.com/trivia/questions"
}

def get_random_fact(topic):
    """
    Fetch a random fact or concept from the specified topic.
    """
    try:
        response = requests.get(topics[topic])
        data = response.json()
        return random.choice(data)
    except (requests.exceptions.RequestException, KeyError):
        return "Sorry, we couldn't fetch a fact for that topic right now."

def quiz(topic):
    """
    Provide an interactive quiz for the specified topic.
    """
    try:
        response = requests.get(topics[topic])
        data = response.json()
        question = random.choice(data)
        print(question["question"])
        options = question["options"]
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter the number of the correct answer: "))
        if options[user_answer-1] == question["answer"]:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {question['answer']}")
    except (requests.exceptions.RequestException, KeyError, ValueError):
        print("Sorry, we couldn't load the quiz for that topic right now.")

def main():
    """
    Main function to run the interactive knowledge-building script.
    """
    print("Welcome to the Knowledge Booster!")
    print("Select a topic to get started:")
    for topic in topics:
        print(topic)

    selected_topic = input("Enter the number of the topic you'd like to explore: ")
    if selected_topic in topics:
        fact = get_random_fact(selected_topic)
        print(f"\nFact about {selected_topic.split('.')[1]}: {fact['fact']}")
        print("\nNow, let's test your knowledge!")
        quiz(selected_topic)
    else:
        print("Invalid topic selection. Please try again.")

if __name__ == "__main__":
    main()
