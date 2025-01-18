
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Function to get a random fact or concept from the selected topic
def get_random_fact(topic):
    try:
        url = topics[topic]
        response = requests.get(url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
        data = json.loads(response.text)
        return data[0]['fact']
    except:
        return "Sorry, we couldn't fetch a random fact for this topic. Please try again later."

# Function to display the quiz questions and get user's answers
def quiz(topic):
    try:
        url = topics[topic]
        response = requests.get(url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
        data = json.loads(response.text)
        
        # Select a random question and its options
        question = random.choice(data)
        options = [question['answer']] + question['incorrect_answers']
        random.shuffle(options)
        
        print(f"Question: {question['question']}")
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        
        user_answer = int(input("Enter your answer (1-4): "))
        if options[user_answer-1] == question['answer']:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {question['answer']}")
    except:
        print("Sorry, we couldn't fetch the quiz questions for this topic. Please try again later.")

# Main function to display the menu and handle user input
def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    
    for i, topic in enumerate(topics):
        print(f"{i+1}. {topic}")
    
    try:
        user_choice = int(input("Enter your choice (1-4): "))
        topic = list(topics.keys())[user_choice-1]
        
        print(f"\nRandom fact about {topic}:")
        print(get_random_fact(topic))
        
        print("\nNow, let's test your knowledge with a quiz!")
        quiz(topic)
    except:
        print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
