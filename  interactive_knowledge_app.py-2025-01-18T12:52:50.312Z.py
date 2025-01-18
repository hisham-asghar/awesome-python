
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.example.com/science",
    "Technology": "https://api.example.com/technology",
    "History": "https://api.example.com/history",
    "General Knowledge": "https://api.example.com/general_knowledge"
}

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the specified topic.
    """
    try:
        response = requests.get(topics[topic])
        data = json.loads(response.text)
        return random.choice(data)
    except:
        return "Sorry, we couldn't fetch a fact for that topic right now."

def quiz_question(topic):
    """
    Provides a multiple-choice quiz question for the specified topic.
    """
    try:
        response = requests.get(topics[topic] + "/quiz")
        data = json.loads(response.text)
        question = data["question"]
        choices = data["choices"]
        correct_answer = data["correct_answer"]
        
        print(question)
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")
        
        user_answer = int(input("Enter the number of your answer: "))
        if choices[user_answer-1] == correct_answer:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}")
    except:
        print("Sorry, we couldn't load a quiz question for that topic right now.")

def main():
    """
    The main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    
    while True:
        print("\nSelect a topic:")
        for topic in topics:
            print(f"- {topic}")
        
        selected_topic = input("Enter your choice: ")
        if selected_topic in topics:
            print(f"\nHere's a random fact about {selected_topic}:")
            print(get_random_fact(selected_topic))
            
            print("\nNow, let's test your knowledge!")
            quiz_question(selected_topic)
        else:
            print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
