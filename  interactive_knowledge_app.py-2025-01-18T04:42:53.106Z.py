
import random
import requests
import json

# Define the topics and their corresponding API endpoints
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://opentdb.com/api.php?amount=1&type=multiple"
}

# Function to fetch a random fact or concept from the chosen topic
def get_random_fact(topic):
    if topic in topics:
        api_url = topics[topic]
        
        # Fetch data from the API
        if topic != "General Knowledge":
            response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'})
            data = response.json()
            fact = data[0]['fact']
        else:
            response = requests.get(api_url)
            data = response.json()
            fact = data['results'][0]['question']
        
        return fact
    else:
        return "Invalid topic. Please choose from the available topics."

# Function to run the interactive quiz
def run_quiz(topic):
    if topic in topics:
        api_url = topics[topic]
        
        # Fetch data from the API
        if topic != "General Knowledge":
            response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'})
            data = response.json()
            question = data[0]['fact']
            answer = data[0]['answer']
        else:
            response = requests.get(api_url)
            data = response.json()
            question = data['results'][0]['question']
            answer = data['results'][0]['correct_answer']
        
        # Display the question and get the user's answer
        user_answer = input(f"Question: {question}\nYour answer: ").lower()
        
        # Check if the user's answer is correct
        if user_answer == answer.lower():
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {answer}")
    else:
        print("Invalid topic. Please choose from the available topics.")

# Main function to run the interactive knowledge app
def main():
    print("Welcome to the Interactive Knowledge App!")
    
    while True:
        print("\nPlease select a topic:")
        for topic in topics:
            print(f"- {topic}")
        
        chosen_topic = input("Enter your choice: ")
        
        if chosen_topic in topics:
            print(f"\nHere's a random fact or concept about {chosen_topic}:")
            print(get_random_fact(chosen_topic))
            
            print("\nNow let's test your knowledge!")
            run_quiz(chosen_topic)
        else:
            print("Invalid topic. Please try again.")
        
        continue_app = input("\nDo you want to explore another topic? (y/n) ").lower()
        if continue_app != "y":
            print("\nThank you for using the Interactive Knowledge App. Goodbye!")
            break

if __name__ == "__main__":
    main()
