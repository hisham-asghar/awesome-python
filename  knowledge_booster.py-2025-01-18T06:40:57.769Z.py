
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

# Function to display the menu and get user's choice
def display_menu():
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    for key, value in topics.items():
        print(f"{key}. {value}")
    return input("Enter your choice (1-4): ")

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    # You can use public APIs or a predefined database to fetch the information
    # Here's an example using the 'requests' library to fetch data from an API
    if topic == "Science":
        response = requests.get("https://api.api-ninjas.com/v1/facts?category=science")
    elif topic == "Technology":
        response = requests.get("https://api.api-ninjas.com/v1/facts?category=technology")
    elif topic == "History":
        response = requests.get("https://api.api-ninjas.com/v1/facts?category=history")
    elif topic == "General Knowledge":
        response = requests.get("https://api.api-ninjas.com/v1/facts?category=general")
    
    if response.status_code == 200:
        facts = response.json()
        return random.choice(facts)["fact"]
    else:
        return "Sorry, we couldn't fetch a fact at the moment."

# Function to display a quiz for the selected topic
def display_quiz(topic):
    # You can create a database of multiple-choice questions for each topic
    # Here's an example using a predefined set of questions
    if topic == "Science":
        questions = [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "Which planet in our solar system is known as the 'Red Planet'?",
                "options": ["Mars", "Jupiter", "Saturn", "Venus"],
                "answer": "Mars"
            },
            # Add more science-related questions here
        ]
    elif topic == "Technology":
        questions = [
            {
                "question": "What does 'HTML' stand for?",
                "options": ["Hyper Text Markup Language", "Hyper Text Management Language", "Hyperlink Text Markup Language", "None of the above"],
                "answer": "Hyper Text Markup Language"
            },
            {
                "question": "Which company developed the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": "Google"
            },
            # Add more technology-related questions here
        ]
    elif topic == "History":
        questions = [
            {
                "question": "In what year did the American Civil War begin?",
                "options": ["1861", "1865", "1914", "1939"],
                "answer": "1861"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
                "answer": "George Washington"
            },
            # Add more history-related questions here
        ]
    elif topic == "General Knowledge":
        questions = [
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Earth", "Mars", "Jupiter", "Saturn"],
                "answer": "Jupiter"
            },
            {
                "question": "What is the currency used in Japan?",
                "options": ["Dollar", "Euro", "Yen", "Pound"],
                "answer": "Yen"
            },
            # Add more general knowledge questions here
        ]
    
    # Randomly select a question and display it to the user
    question = random.choice(questions)
    print(f"Question: {question['question']}")
    for i, option in enumerate(question['options'], start=1):
        print(f"{i}. {option}")
    
    # Get the user's answer and check if it's correct
    user_answer = input("Enter your answer (1-4): ")
    if question['options'][int(user_answer) - 1] == question['answer']:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {question['answer']}")

# Main function to run the knowledge booster
def run_knowledge_booster():
    while True:
        choice = display_menu()
        if choice in topics:
            topic = topics[choice]
            print(f"\nFact about {topic}:")
            print(get_random_fact(topic))
            print("\nNow, let's test your knowledge!")
            display_quiz(topic)
            print("\nThank you for using the Knowledge Booster!")
            break
        else:
            print("Invalid choice. Please try again.")

run_knowledge_booster()
