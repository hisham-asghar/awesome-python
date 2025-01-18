
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
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for key, value in topics.items():
        print(f"{key}. {value}")
    return input("Enter your choice (1-4): ")

# Function to fetch a random fact or concept from the chosen topic
def get_random_fact(topic):
    # Fetch data from a public API or a predefined database
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

# Function to display a random fact or concept and an interactive quiz
def interactive_learning(topic):
    # Display a random fact or concept
    print(f"\nHere's a random {topic.lower()} fact or concept:")
    print(get_random_fact(topic))

    # Display a multiple-choice quiz
    print("\nNow, let's test your knowledge with a quiz!")
    if topic == "Science":
        questions = [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": 0
            },
            {
                "question": "Which planet in our solar system has the most moons?",
                "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
                "answer": 0
            },
            # Add more science-related questions here
        ]
    elif topic == "Technology":
        questions = [
            {
                "question": "What does 'HTML' stand for?",
                "options": ["Hyper Text Markup Language", "Hyperlink Text Markup Language", "Hyper Text Management Language", "Hyper Text Markup Limit"],
                "answer": 0
            },
            {
                "question": "Which company developed the Android operating system?",
                "options": ["Apple", "Microsoft", "Google", "Samsung"],
                "answer": 2
            },
            # Add more technology-related questions here
        ]
    elif topic == "History":
        questions = [
            {
                "question": "In what year did World War II end?",
                "options": ["1945", "1939", "1942", "1950"],
                "answer": 0
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "James Madison"],
                "answer": 2
            },
            # Add more history-related questions here
        ]
    elif topic == "General Knowledge":
        questions = [
            {
                "question": "What is the capital of Australia?",
                "options": ["Sydney", "Melbourne", "Canberra", "Brisbane"],
                "answer": 2
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "answer": 3
            },
            # Add more general knowledge questions here
        ]

    # Ask the user the quiz questions
    score = 0
    for question in questions:
        print(f"\n{question['question']}")
        for i, option in enumerate(question['options']):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer - 1 == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. Better luck next time!")

    print(f"\nYour final score is {score} out of {len(questions)}.")

# Main function to run the interactive knowledge booster
def main():
    user_choice = display_menu()
    if user_choice in topics:
        interactive_learning(topics[user_choice])
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
