
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    "science": "https://api.example.com/science",
    "technology": "https://api.example.com/technology",
    "history": "https://api.example.com/history",
    "general_knowledge": "https://api.example.com/general_knowledge"
}

# Function to fetch a random fact or concept from the chosen topic
def get_random_fact(topic):
    try:
        # Fetch data from the corresponding API endpoint or data source
        response = requests.get(topics[topic])
        data = json.loads(response.text)
        
        # Select a random fact or concept from the data
        fact = random.choice(data["facts"])
        return fact
    except:
        return "Sorry, we couldn't fetch a fact for that topic right now."

# Function to display the multiple-choice quiz
def quiz(topic):
    try:
        # Fetch data from the corresponding API endpoint or data source
        response = requests.get(topics[topic])
        data = json.loads(response.text)
        
        # Select a random question and answers from the data
        question = random.choice(data["questions"])
        answers = question["answers"]
        
        # Shuffle the answers
        random.shuffle(answers)
        
        # Display the question and answers
        print(question["question"])
        for i, answer in enumerate(answers):
            print(f"{i+1}. {answer}")
        
        # Get the user's answer
        user_answer = int(input("Enter your answer (1-4): "))
        
        # Check if the user's answer is correct
        if answers[user_answer-1] == question["correct_answer"]:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {question['correct_answer']}")
    except:
        print("Sorry, we couldn't load the quiz for that topic right now.")

# Main function to run the program
def main():
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    
    # Display the available topics
    for topic in topics:
        print(f"{topic.capitalize()}")
    
    # Get the user's topic choice
    chosen_topic = input("Enter your choice: ").lower()
    
    if chosen_topic in topics:
        # Display a random fact or concept
        print(f"\nHere's a random fact about {chosen_topic.capitalize()}:")
        print(get_random_fact(chosen_topic))
        
        # Run the quiz
        print(f"\nNow, let's test your {chosen_topic.capitalize()} knowledge!")
        quiz(chosen_topic)
    else:
        print("Sorry, that's not a valid topic. Please try again.")

if __name__ == "__main__":
    main()
