
import random
import requests
import json

# Define topics and their corresponding API endpoints
topics = {
    "Science": "https://api.api-ninjas.com/v1/facts?category=science",
    "Technology": "https://api.api-ninjas.com/v1/facts?category=technology",
    "History": "https://api.api-ninjas.com/v1/facts?category=history",
    "General Knowledge": "https://api.api-ninjas.com/v1/facts?category=general"
}

# API key for API-Ninjas
api_key = "YOUR_API_KEY_HERE"

def get_random_fact(topic):
    """
    Fetch a random fact from the specified topic using the API-Ninjas API.
    """
    url = topics[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    return data[0]['fact']

def quiz_question(topic):
    """
    Generate a multiple-choice quiz question for the specified topic.
    """
    # Fetch a random fact from the topic
    fact = get_random_fact(topic)
    
    # Generate multiple-choice options
    options = [fact]
    for i in range(3):
        other_topic = random.choice(list(topics.keys()))
        if other_topic != topic:
            options.append(get_random_fact(other_topic))
    random.shuffle(options)
    
    # Prompt the user with the question and options
    print(f"Question: What is the fact about {topic.lower()}?")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    
    # Get the user's answer
    while True:
        try:
            answer = int(input("Enter the number of the correct answer: "))
            if 1 <= answer <= 4:
                return options[answer-1] == fact
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    """
    Main function that displays the menu, handles user input, and runs the interactive quiz.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    
    # Display the menu of topics
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")
    
    while True:
        try:
            choice = int(input("Enter the number of the topic (or 0 to exit): "))
            if choice == 0:
                print("Goodbye!")
                break
            elif 1 <= choice <= len(topics):
                topic = list(topics.keys())[choice-1]
                print(f"\nFact about {topic}:")
                print(get_random_fact(topic))
                
                # Run the quiz
                if quiz_question(topic):
                    print("Correct!")
                else:
                    print("Incorrect. Better luck next time!")
                print()
            else:
                print("Invalid input. Please enter a number between 0 and", len(topics))
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
