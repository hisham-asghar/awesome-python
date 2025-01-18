
import random
import requests
import json

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the specified topic using a public API.
    """
    api_url = {
        "science": "https://api.api-ninjas.com/v1/facts?category=science",
        "technology": "https://api.api-ninjas.com/v1/facts?category=technology",
        "history": "https://api.api-ninjas.com/v1/facts?category=history",
        "general": "https://api.api-ninjas.com/v1/facts?category=general"
    }
    
    headers = {'X-Api-Key': 'YOUR_API_KEY_HERE'}
    response = requests.get(api_url[topic], headers=headers)
    
    if response.status_code == 200:
        facts = json.loads(response.text)
        return random.choice(facts)['fact']
    else:
        return "Error fetching fact."

def quiz_question(topic):
    """
    Generates a multiple-choice quiz question for the specified topic.
    """
    quiz_data = {
        "science": [
            {
                "question": "What is the chemical symbol for gold?",
                "choices": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            },
            # Add more science quiz questions here
        ],
        "technology": [
            {
                "question": "What does the acronym 'CPU' stand for?",
                "choices": ["Central Processing Unit", "Computer Power Unit", "Central Power Unit", "Computer Processor Unit"],
                "answer": 0
            },
            # Add more technology quiz questions here
        ],
        "history": [
            {
                "question": "In what year did World War II end?",
                "choices": ["1945", "1939", "1942", "1950"],
                "answer": 0
            },
            # Add more history quiz questions here
        ],
        "general": [
            {
                "question": "What is the largest planet in our solar system?",
                "choices": ["Earth", "Mars", "Jupiter", "Saturn"],
                "answer": 2
            },
            # Add more general knowledge quiz questions here
        ]
    }
    
    question_data = random.choice(quiz_data[topic])
    return question_data

def main():
    """
    The main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")
    print("1. Science")
    print("2. Technology")
    print("3. History")
    print("4. General Knowledge")
    
    topic_choice = int(input("Enter the number of your choice: "))
    
    topics = ["science", "technology", "history", "general"]
    chosen_topic = topics[topic_choice - 1]
    
    print(f"\nYour chosen topic is: {chosen_topic.capitalize()}")
    print(get_random_fact(chosen_topic))
    
    quiz_data = quiz_question(chosen_topic)
    print("\nTime for a quiz!")
    print(quiz_data["question"])
    for i, choice in enumerate(quiz_data["choices"]):
        print(f"{i+1}. {choice}")
    
    user_answer = int(input("Enter the number of your answer: "))
    if user_answer == quiz_data["answer"] + 1:
        print("Correct!")
    else:
        print("Incorrect. Better luck next time!")

if __name__ == "__main__":
    main()
