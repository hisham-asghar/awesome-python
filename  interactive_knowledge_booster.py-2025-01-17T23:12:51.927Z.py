
import random
import requests
import json

# Define topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# API key for API-Ninjas
api_key = "YOUR_API_KEY_HERE"

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the specified topic using the API.
    """
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]["fact"]

def quiz(topic):
    """
    Provides a multiple-choice quiz for the specified topic.
    """
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    
    # Select a random question and answers
    question = random.choice(data)
    correct_answer = question["answer"]
    answers = [correct_answer]
    
    # Generate 3 incorrect answers
    while len(answers) < 4:
        incorrect_answer = random.choice(data)["answer"]
        if incorrect_answer not in answers:
            answers.append(incorrect_answer)
    
    random.shuffle(answers)
    
    print(f"Question: {question['question']}")
    for i, answer in enumerate(answers):
        print(f"{i+1}. {answer}")
    
    user_answer = int(input("Enter the number of the correct answer: "))
    if answers[user_answer-1] == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")

def main():
    """
    Main function that displays the menu, allows the user to select a topic, and runs the corresponding quiz.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")
    
    topic_choice = int(input("Enter the number of the topic: "))
    selected_topic = list(topics.keys())[topic_choice-1]
    
    print(f"\nRandom fact about {selected_topic}: {get_random_fact(selected_topic)}")
    print("\nNow let's test your knowledge with a quiz!")
    quiz(selected_topic)

if __name__ == "__main__":
    main()
