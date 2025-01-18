
import random
import requests
import json

# Define topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://opentdb.com/api.php?amount=10&category=9&difficulty=medium&type=multiple"
}

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    url = topics[topic]
    response = requests.get(url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    data = response.json()
    
    if topic == "General Knowledge":
        return data["results"][random.randint(0, 9)]["question"], data["results"][random.randint(0, 9)]["correct_answer"], data["results"][random.randint(0, 9)]["incorrect_answers"]
    else:
        return data[random.randint(0, len(data) - 1)]["fact"]

# Function to run the interactive quiz
def run_quiz(topic):
    question, correct_answer, incorrect_answers = get_random_fact(topic)
    
    print(f"Question: {question}")
    
    # Shuffle the answers
    answers = [correct_answer] + incorrect_answers
    random.shuffle(answers)
    
    # Display the multiple-choice options
    for i, answer in enumerate(answers):
        print(f"{i+1}. {answer}")
    
    user_answer = int(input("Enter your answer (1-4): "))
    
    if answers[user_answer - 1] == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}")

# Main function to run the interactive knowledge app
def main():
    print("Welcome to the Interactive Knowledge App!")
    
    while True:
        print("\nSelect a topic:")
        for topic in topics:
            print(f"- {topic}")
        
        selected_topic = input("Enter your choice: ")
        
        if selected_topic in topics:
            fact = get_random_fact(selected_topic)
            print(f"\nHere's a {selected_topic.lower()} fact or concept: {fact}")
            
            run_quiz(selected_topic)
            
            continue_app = input("\nDo you want to explore another topic? (y/n) ")
            if continue_app.lower() != 'y':
                break
        else:
            print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
