Here is the raw Python code extracted from the JSON:

```python
import random
import json
import requests

# Define the available topics
topics = {
    "1": "Science",
    "2": "Technology",
    "3": "History",
    "4": "General Knowledge"
}

# Function to display the menu and get user input
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for key, value in topics.items():
        print(f"{key}. {value}")
    
    topic_choice = input("Enter your choice (1-4): ")
    return topic_choice

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    # Fetch data from a public API or a predefined database
    if topic == "Science":
        response = requests.get("https://api.api-ninjas.com/v1/facts?category=science")
        facts = response.json()
        return random.choice(facts)["fact"]
    elif topic == "Technology":
        response = requests.get("https://api.api-ninjas.com/v1/facts?category=technology")
        facts = response.json()
        return random.choice(facts)["fact"]
    elif topic == "History":
        response = requests.get("https://api.api-ninjas.com/v1/facts?category=history")
        facts = response.json()
        return random.choice(facts)["fact"]
    elif topic == "General Knowledge":
        response = requests.get("https://api.api-ninjas.com/v1/trivia")
        trivia = response.json()
        return random.choice(trivia)["question"]
    else:
        return "Sorry, that topic is not available."

# Function to display the quiz and get user answers
def quiz(topic):
    # Fetch quiz questions and answers from a public API or a predefined database
    if topic == "Science":
        response = requests.get("https://opentdb.com/api.php?amount=5&category=17&type=multiple")
        quiz_data = response.json()["results"]
    elif topic == "Technology":
        response = requests.get("https://opentdb.com/api.php?amount=5&category=18&type=multiple")
        quiz_data = response.json()["results"]
    elif topic == "History":
        response = requests.get("https://opentdb.com/api.php?amount=5&category=23&type=multiple")
        quiz_data = response.json()["results"]
    elif topic == "General Knowledge":
        response = requests.get("https://opentdb.com/api.php?amount=5&category=9&type=multiple")
        quiz_data = response.json()["results"]
    else:
        return "Sorry, that topic is not available."
    
    score = 0
    for question in quiz_data:
        print(question["question"])
        answers = question["incorrect_answers"] + [question["correct_answer"]]
        random.shuffle(answers)
        for i, answer in enumerate(answers):
            print(f"{i+1}. {answer}")
        user_answer = input("Enter your answer (1-4): ")
        if answers[int(user_answer) - 1] == question["correct_answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    
    print(f"Your final score is {score} out of 5.")

# Main function
def main():
    topic_choice = display_menu()
    if topic_choice in topics:
        selected_topic = topics[topic_choice]
        print(f"\nYou have selected the {selected_topic} topic.")
        
        # Display a random fact or concept
        random_fact = get_random_fact(selected_topic)
        print(f"\nHere's a random {selected_topic.lower()} fact or concept:\n{random_fact}")
        
        # Start the quiz
        print(f"\nNow, let's test your {selected_topic.lower()} knowledge with a quiz!")
        quiz(selected_topic)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
