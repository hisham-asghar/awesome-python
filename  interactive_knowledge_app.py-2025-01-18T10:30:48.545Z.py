
import random
import requests
import json

# Define the topics and their corresponding API endpoints or database entries
topics = {
    "Science": "https://api.example.com/science",
    "Technology": "https://api.example.com/technology",
    "History": "https://api.example.com/history",
    "General Knowledge": "https://api.example.com/general"
}

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the specified topic using an API or database.
    """
    url = topics[topic]
    response = requests.get(url)
    data = json.loads(response.text)
    return random.choice(data)

def quiz_question(topic):
    """
    Generates a multiple-choice quiz question for the specified topic using an API or database.
    """
    url = topics[topic] + "/quiz"
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def main():
    """
    The main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")

    # Display the available topics
    for topic in topics:
        print(f"- {topic}")

    selected_topic = input("Enter your choice: ")

    if selected_topic in topics:
        # Fetch a random fact or concept from the selected topic
        fact = get_random_fact(selected_topic)
        print(f"\nHere's a random fact about {selected_topic}:")
        print(fact)

        # Generate a multiple-choice quiz question for the selected topic
        quiz = quiz_question(selected_topic)
        print("\nNow, let's test your knowledge with a quiz!")
        print(quiz["question"])
        for i, option in enumerate(quiz["options"]):
            print(f"{i+1}. {option}")

        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer == quiz["answer"]:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {quiz['answer']}.")

    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
