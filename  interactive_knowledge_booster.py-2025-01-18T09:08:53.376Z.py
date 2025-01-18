
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

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    # Fetch data from a public API or a predefined database
    if topic == "Science":
        response = requests.get("https://api.api-ninjas.com/v1/facts?category=science", headers={"X-Api-Key": "YOUR_API_KEY"})
    elif topic == "Technology":
        response = requests.get("https://api.api-ninjas.com/v1/facts?category=technology", headers={"X-Api-Key": "YOUR_API_KEY"})
    elif topic == "History":
        response = requests.get("https://api.api-ninjas.com/v1/facts?category=history", headers={"X-Api-Key": "YOUR_API_KEY"})
    elif topic == "General Knowledge":
        response = requests.get("https://api.api-ninjas.com/v1/facts?category=general", headers={"X-Api-Key": "YOUR_API_KEY"})
    else:
        return "Invalid topic selected."

    if response.status_code == 200:
        facts = response.json()
        random_fact = random.choice(facts)
        return random_fact["fact"]
    else:
        return "Error fetching data."

# Function to display a random fact or concept and run an interactive quiz
def run_interactive_session():
    topic_choice = display_menu()
    topic = topics.get(topic_choice, "Invalid choice")
    if topic != "Invalid choice":
        print(f"\nYour chosen topic is: {topic}")
        random_fact = get_random_fact(topic)
        print(f"\nHere's a random fact or concept about {topic}:\n{random_fact}")

        # Run an interactive quiz
        print("\nTime to test your knowledge!")
        if topic == "Science":
            quiz_questions = [
                {"question": "What is the chemical symbol for gold?", "options": ["Au", "Ag", "Cu", "Fe"], "answer": 0},
                {"question": "What is the process of converting water into water vapor called?", "options": ["Evaporation", "Condensation", "Precipitation", "Transpiration"], "answer": 0},
                {"question": "What is the name of the largest planet in our solar system?", "options": ["Mars", "Jupiter", "Saturn", "Neptune"], "answer": 1}
            ]
        # Add more quiz questions for other topics
        else:
            print("Sorry, no quiz available for this topic yet.")

        for question in quiz_questions:
            print(question["question"])
            for i, option in enumerate(question["options"]):
                print(f"{i+1}. {option}")
            user_answer = int(input("Enter your answer (1-4): ")) - 1
            if user_answer == question["answer"]:
                print("Correct!")
            else:
                print("Incorrect. The correct answer is:", question["options"][question["answer"]])
    else:
        print("Invalid topic selected. Please try again.")

# Run the interactive session
run_interactive_session()
