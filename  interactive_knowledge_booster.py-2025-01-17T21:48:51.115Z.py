
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.example.com/science",
    "Technology": "https://api.example.com/technology",
    "History": "https://api.example.com/history",
    "General Knowledge": "https://api.example.com/general-knowledge"
}

# Function to display the menu and get the user's topic choice
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    
    while True:
        choice = input("Enter your choice: ").strip()
        if choice in topics:
            return choice
        else:
            print("Invalid choice. Please try again.")

# Function to fetch a random fact or concept from the chosen topic
def get_random_fact(topic):
    # Fetch data from the API or predefined database
    response = requests.get(topics[topic])
    data = json.loads(response.text)
    
    # Select a random fact or concept from the data
    facts = data["facts"]
    random_fact = random.choice(facts)
    
    return random_fact

# Function to display the multiple-choice quiz
def display_quiz(topic):
    # Fetch quiz questions and answers from the API or predefined database
    response = requests.get(topics[topic] + "/quiz")
    quiz_data = json.loads(response.text)
    
    score = 0
    for question, options, answer in zip(quiz_data["questions"], quiz_data["options"], quiz_data["answers"]):
        print(question)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        
        user_answer = int(input("Enter your answer: "))
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is", answer)
    
    print(f"Your final score is {score}/{len(quiz_data['questions'])}")

# Main function to run the interactive knowledge booster
def main():
    topic = display_menu()
    random_fact = get_random_fact(topic)
    print(f"Here's a random {topic.lower()} fact: {random_fact}")
    
    print("\nTime for a quiz!")
    display_quiz(topic)

if __name__ == "__main__":
    main()
