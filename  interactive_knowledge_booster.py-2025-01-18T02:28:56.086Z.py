
import random
import requests
import json

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
    return input("Enter the number of your chosen topic: ")

# Function to fetch a random fact or concept for the selected topic
def get_random_fact(topic):
    # Fetch data from a public API or a predefined database
    if topic == "Science":
        response = requests.get("https://api.api-ninjas.com/v1/facts?category=science", headers={'X-Api-Key': 'YOUR_API_KEY'})
    elif topic == "Technology":
        response = requests.get("https://api.api-ninjas.com/v1/facts?category=technology", headers={'X-Api-Key': 'YOUR_API_KEY'})
    elif topic == "History":
        response = requests.get("https://api.api-ninjas.com/v1/facts?category=history", headers={'X-Api-Key': 'YOUR_API_KEY'})
    elif topic == "General Knowledge":
        response = requests.get("https://api.api-ninjas.com/v1/facts?category=general", headers={'X-Api-Key': 'YOUR_API_KEY'})
    else:
        return "Invalid topic selected."

    if response.status_code == 200:
        facts = json.loads(response.text)
        return random.choice(facts)["fact"]
    else:
        return "Error fetching data."

# Function to display the quiz and get user answers
def quiz(topic):
    # Fetch quiz questions and answers from a public API or a predefined database
    if topic == "Science":
        response = requests.get("https://api.api-ninjas.com/v1/trivia?category=science", headers={'X-Api-Key': 'YOUR_API_KEY'})
    elif topic == "Technology":
        response = requests.get("https://api.api-ninjas.com/v1/trivia?category=technology", headers={'X-Api-Key': 'YOUR_API_KEY'})
    elif topic == "History":
        response = requests.get("https://api.api-ninjas.com/v1/trivia?category=history", headers={'X-Api-Key': 'YOUR_API_KEY'})
    elif topic == "General Knowledge":
        response = requests.get("https://api.api-ninjas.com/v1/trivia?category=general", headers={'X-Api-Key': 'YOUR_API_KEY'})
    else:
        return "Invalid topic selected."

    if response.status_code == 200:
        questions = json.loads(response.text)
        score = 0
        for question in questions:
            print(question["question"])
            for option in question["options"]:
                print(f"- {option}")
            user_answer = input("Enter your answer: ")
            if user_answer.lower() == question["answer"].lower():
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer is: {question['answer']}")
        print(f"Your final score is: {score}/{len(questions)}")
    else:
        return "Error fetching quiz data."

# Main function to run the interactive knowledge booster
def main():
    topic_choice = display_menu()
    topic = topics.get(topic_choice, "Invalid topic")
    if topic != "Invalid topic":
        print(f"\nHere's a random fact about {topic}:")
        print(get_random_fact(topic))
        print(f"\nNow, let's test your {topic} knowledge with a quiz!")
        quiz(topic)
    else:
        print("Invalid topic selected. Please try again.")

if __name__ == "__main__":
    main()
