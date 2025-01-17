Here is the raw Python code extracted from the JSON:

```python
import random
import requests
import json

# Define topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/randomfact?category=science",
    "Technology": "https://api.api-ninjas.com/v1/randomfact?category=technology",
    "History": "https://api.api-ninjas.com/v1/randomfact?category=history",
    "General Knowledge": "https://opentdb.com/api.php?amount=1&type=multiple"
}

# Function to get a random fact or concept from the selected topic
def get_random_fact(topic):
    api_key = "YOUR_API_KEY_HERE"  # Replace with your API key
    
    if topic == "General Knowledge":
        response = requests.get(topics[topic])
        data = response.json()
        return data["results"][0]["question"], data["results"][0]["correct_answer"], data["results"][0]["incorrect_answers"]
    else:
        headers = {"X-Api-Key": api_key}
        response = requests.get(topics[topic], headers=headers)
        return response.json()["fact"]

# Function to run the interactive quiz
def run_quiz(topic):
    fact, correct_answer, incorrect_answers = get_random_fact(topic)
    print(f"Topic: {topic}")
    print(f"Fact or Concept: {fact}")
    
    # Combine correct and incorrect answers
    all_answers = [correct_answer] + incorrect_answers
    random.shuffle(all_answers)
    
    # Ask the user to select the correct answer
    print("Multiple Choice:")
    for i, answer in enumerate(all_answers):
        print(f"{i+1}. {answer}")
    
    user_answer = input("Enter the number of the correct answer: ")
    
    if all_answers[int(user_answer) - 1] == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}")

# Main function to display the menu and run the script
def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    
    for topic in topics:
        print(f"{topic}")
    
    selected_topic = input("Enter your choice: ")
    
    if selected_topic in topics:
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
