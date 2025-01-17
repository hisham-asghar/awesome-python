
import random
import requests
import json

def get_topic_content(topic):
    """
    Fetch topic-specific content from a public API or predefined database.
    """
    topics = {
        "science": "https://api.api-ninjas.com/v1/science",
        "technology": "https://api.api-ninjas.com/v1/technology",
        "history": "https://api.api-ninjas.com/v1/history",
        "general": "https://api.api-ninjas.com/v1/trivia"
    }
    
    if topic in topics:
        response = requests.get(topics[topic], headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
        if response.status_code == 200:
            return response.json()
        else:
            return None
    else:
        return None

def display_fact(topic, fact):
    """
    Display a random fact or concept from the chosen topic.
    """
    print(f"Here's a {topic} fact for you:")
    print(fact)

def quiz_question(topic, question, choices, answer):
    """
    Present a multiple-choice quiz question to the user.
    """
    print(question)
    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice}")
    
    user_answer = int(input("Enter your answer (1-4): "))
    if user_answer == answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {answer}.")

def main():
    """
    The main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Select a topic to get started:")
    
    topics = ["Science", "Technology", "History", "General Knowledge"]
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")
    
    user_topic = int(input("Enter the number of the topic (1-4): ")) - 1
    
    if user_topic < 0 or user_topic >= len(topics):
        print("Invalid topic selection. Exiting.")
        return
    
    topic_name = topics[user_topic].lower()
    topic_content = get_topic_content(topic_name)
    
    if topic_content:
        fact = random.choice(topic_content)
        display_fact(topics[user_topic], fact["fact"])
        
        quiz_question(
            topics[user_topic],
            fact["question"],
            fact["choices"],
            fact["answer"]
        )
    else:
        print("Failed to fetch content. Please try again later.")

if __name__ == "__main__":
    main()
