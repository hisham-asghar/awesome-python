
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    "science": "https://api.api-ninjas.com/v1/science",
    "technology": "https://api.api-ninjas.com/v1/technology",
    "history": "https://api.api-ninjas.com/v1/history",
    "general_knowledge": "https://opentdb.com/api.php?amount=10&category=9&difficulty=medium&type=multiple"
}

# Function to get a random fact or concept from the selected topic
def get_random_fact(topic):
    api_url = topics[topic]
    
    if topic == "general_knowledge":
        response = requests.get(api_url)
        data = response.json()
        fact = data["results"][random.randint(0, 9)]["question"]
    else:
        headers = {"X-Api-Key": "YOUR_API_KEY_HERE"}
        response = requests.get(api_url, headers=headers)
        data = response.json()
        fact = data[random.randint(0, len(data) - 1)]["fact"]
    
    return fact

# Function to run the interactive quiz
def run_quiz(topic):
    api_url = topics[topic]
    
    if topic == "general_knowledge":
        response = requests.get(api_url)
        data = response.json()
        questions = data["results"]
        
        score = 0
        for question in questions:
            print(question["question"])
            for i, answer in enumerate(question["incorrect_answers"]):
                print(f"{i+1}. {answer}")
            print(f"{len(question['incorrect_answers'])+1}. {question['correct_answer']}")
            
            user_answer = int(input("Enter your answer (1-4): "))
            if user_answer == len(question["incorrect_answers"]) + 1:
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")
            print()
        
        print(f"Your final score is {score} out of {len(questions)}.")
    else:
        print("Sorry, the quiz feature is not available for the selected topic.")

# Main function to run the interactive knowledge app
def main():
    print("Welcome to the Interactive Knowledge App!")
    
    while True:
        print("\nSelect a topic:")
        for topic in topics:
            print(f"- {topic.capitalize()}")
        print("- Exit")
        
        user_input = input("Enter your choice: ").lower()
        
        if user_input == "exit":
            print("Goodbye!")
            break
        elif user_input in topics:
            fact = get_random_fact(user_input)
            print(f"\nRandom {user_input.capitalize()} fact: {fact}")
            
            run_quiz(user_input)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
