
import random
import requests
import json

# API endpoints for fetching educational content
API_ENDPOINTS = {
    "science": "https://api.example.com/science",
    "technology": "https://api.example.com/technology",
    "history": "https://api.example.com/history",
    "general_knowledge": "https://api.example.com/general_knowledge"
}

# Function to fetch a random fact or concept from the API
def get_random_fact(topic):
    try:
        response = requests.get(API_ENDPOINTS[topic])
        data = json.loads(response.text)
        return random.choice(data["facts"])
    except:
        return "Sorry, there was an error fetching the information."

# Function to display the multiple-choice quiz
def quiz(topic):
    try:
        response = requests.get(API_ENDPOINTS[topic])
        data = json.loads(response.text)
        quiz_data = random.choice(data["quizzes"])
        
        print(quiz_data["question"])
        
        options = quiz_data["options"]
        random.shuffle(options)
        
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        
        user_answer = int(input("Enter your answer (1-4): "))
        
        if options[user_answer-1] == quiz_data["answer"]:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {quiz_data['answer']}")
    except:
        print("Sorry, there was an error fetching the quiz.")

# Main function to display the menu and handle user input
def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    
    for topic in API_ENDPOINTS.keys():
        print(f"{topic.upper()}")
    
    user_input = input("Enter your choice: ").lower()
    
    if user_input in API_ENDPOINTS.keys():
        print(f"\nHere's a random {user_input} fact or concept:")
        print(get_random_fact(user_input))
        
        print(f"\nNow let's test your {user_input} knowledge with a quiz!")
        quiz(user_input)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
