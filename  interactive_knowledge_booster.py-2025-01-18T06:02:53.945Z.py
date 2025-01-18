
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://opentdb.com/api.php?amount=10&type=multiple"
}

# Function to display the menu and get user input
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    
    while True:
        user_input = input("Enter your choice (or 'q' to quit): ").strip()
        if user_input.lower() == 'q':
            print("Goodbye!")
            return None
        if user_input in topics:
            return user_input
        print("Invalid choice. Please try again.")

# Function to fetch and display a random fact or concept
def display_random_fact(topic):
    api_url = topics[topic]
    
    if topic == "General Knowledge":
        response = requests.get(api_url)
        data = response.json()
        question = data["results"][0]["question"]
        correct_answer = data["results"][0]["correct_answer"]
        incorrect_answers = data["results"][0]["incorrect_answers"]
        
        print(f"Question: {question}")
        print(f"Correct answer: {correct_answer}")
        print(f"Incorrect answers: {', '.join(incorrect_answers)}")
    else:
        response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
        data = response.json()
        random_fact = random.choice(data)
        print(f"Random {topic.lower()} fact: {random_fact['fact']}")

# Function to run the interactive quiz
def run_quiz(topic):
    api_url = topics[topic]
    
    if topic == "General Knowledge":
        response = requests.get(api_url)
        data = response.json()
        questions = data["results"]
        
        score = 0
        for question in questions:
            print(f"Question: {question['question']}")
            
            answers = question["incorrect_answers"] + [question["correct_answer"]]
            random.shuffle(answers)
            
            for i, answer in enumerate(answers):
                print(f"{i+1}. {answer}")
            
            user_answer = int(input("Enter your answer (1-4): "))
            if answers[user_answer-1] == question["correct_answer"]:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer is: {question['correct_answer']}")
        
        print(f"Your final score: {score} out of {len(questions)}")
    else:
        print("Quiz functionality is not available for this topic.")

# Main program loop
while True:
    selected_topic = display_menu()
    if selected_topic is None:
        break
    
    display_random_fact(selected_topic)
    print()
    
    run_quiz(selected_topic)
    print()
