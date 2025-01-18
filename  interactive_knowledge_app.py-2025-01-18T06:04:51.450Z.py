
import random
import requests
import json

# Define topics and their corresponding API endpoints or data sources
TOPICS = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Function to get a random fact or concept from the selected topic
def get_random_fact(topic):
    api_url = TOPICS[topic]
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    
    if response.status_code == 200:
        data = response.json()
        return data[0]
    else:
        return None

# Function to display the fact or concept and ask the user to take a quiz
def display_and_quiz(fact):
    print(f"Did you know that {fact['fact']}?")
    
    # Generate multiple-choice questions
    options = [fact['answer']] + [random.choice(TOPICS.keys()) for _ in range(3)]
    random.shuffle(options)
    
    print("Which of the following is correct?")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    
    user_answer = input("Enter the number of your answer: ")
    
    if options[int(user_answer)-1] == fact['answer']:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {fact['answer']}.")

# Main function to run the interactive knowledge app
def run_knowledge_app():
    print("Welcome to the Interactive Knowledge App!")
    
    while True:
        print("\nSelect a topic:")
        for i, topic in enumerate(TOPICS.keys()):
            print(f"{i+1}. {topic}")
        
        topic_choice = input("Enter the number of your topic choice: ")
        
        try:
            topic = list(TOPICS.keys())[int(topic_choice)-1]
            fact = get_random_fact(topic)
            
            if fact:
                display_and_quiz(fact)
            else:
                print("Sorry, there was an error fetching the fact.")
        except (IndexError, ValueError):
            print("Invalid choice. Please try again.")
        
        continue_prompt = input("\nDo you want to explore another topic? (y/n) ")
        if continue_prompt.lower() != 'y':
            break

if __name__ == "__main__":
    run_knowledge_app()
