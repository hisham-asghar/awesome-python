
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

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    api_key = "YOUR_API_KEY_HERE"
    url = topics[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data[0]['fact']
    else:
        return "Error fetching data. Please try again later."

# Function to display the multiple-choice quiz
def quiz(topic):
    # Fetch quiz questions and answers from a predefined database or an API
    questions_and_answers = {
        "Science": [
            {"question": "What is the chemical symbol for gold?", "answers": ["Au", "Ag", "Cu", "Fe"], "correct_answer": "Au"},
            {"question": "What is the largest planet in our solar system?", "answers": ["Earth", "Mars", "Jupiter", "Saturn"], "correct_answer": "Jupiter"},
            {"question": "What is the process of converting water into water vapor called?", "answers": ["Evaporation", "Condensation", "Precipitation", "Transpiration"], "correct_answer": "Evaporation"}
        ],
        "Technology": [
            {"question": "What is the primary function of a computer's CPU?", "answers": ["Data storage", "Network connectivity", "Graphical processing", "Computation"], "correct_answer": "Computation"},
            {"question": "What is the name of the first commercially successful web browser?", "answers": ["Internet Explorer", "Netscape Navigator", "Mozilla Firefox", "Google Chrome"], "correct_answer": "Netscape Navigator"},
            {"question": "What is the name of the programming language used to create websites?", "answers": ["Java", "Python", "C++", "HTML"], "correct_answer": "HTML"}
        ],
        # Add more questions and answers for other topics
    }

    # Select a random question from the chosen topic
    question_data = random.choice(questions_and_answers[topic])
    question = question_data["question"]
    answers = question_data["answers"]
    correct_answer = question_data["correct_answer"]

    # Display the question and answers
    print(question)
    for i, answer in enumerate(answers):
        print(f"{i+1}. {answer}")

    # Get the user's answer
    user_answer = input("Enter the number of the correct answer: ")

    # Check the user's answer and provide feedback
    if answers[int(user_answer)-1] == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")

# Main program loop
while True:
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")

    selected_topic = input("Enter your choice: ")

    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic}:")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

    print("\nDo you want to explore another topic? (y/n)")
    choice = input()
    if choice.lower() != "y":
        break

print("Thank you for using the Interactive Knowledge Booster. Have a great day!")
