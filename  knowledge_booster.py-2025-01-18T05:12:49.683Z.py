
import random
import requests
import json

# Define the topics and their corresponding APIs or data sources
topics = {
    "science": "https://api.api-ninjas.com/v1/science",
    "technology": "https://api.api-ninjas.com/v1/technology",
    "history": "https://api.api-ninjas.com/v1/history",
    "general_knowledge": "https://opentdb.com/api.php?amount=1&type=multiple"
}

# Function to fetch a random fact or concept from the selected topic
def get_fact(topic):
    api_url = topics[topic]
    
    if topic == "general_knowledge":
        response = requests.get(api_url)
        data = response.json()
        return data["results"][0]["question"], data["results"][0]["correct_answer"], data["results"][0]["incorrect_answers"]
    else:
        response = requests.get(api_url, headers={"X-Api-Key": "YOUR_API_KEY_HERE"})
        data = response.json()
        return data[0]["fact"]

# Function to run the interactive quiz
def run_quiz(topic):
    question, correct_answer, incorrect_answers = get_fact(topic)
    all_answers = [correct_answer] + incorrect_answers
    random.shuffle(all_answers)
    
    print(f"Topic: {topic.capitalize()}")
    print(f"Question: {question}")
    
    for i, answer in enumerate(all_answers):
        print(f"{i+1}. {answer}")
    
    user_answer = int(input("Enter the number of the correct answer: "))
    
    if all_answers[user_answer-1] == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}")

# Main function to display the menu and run the script
def main():
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    
    for topic in topics:
        print(f"{topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
