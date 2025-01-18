
import random
import requests
import json

# Define topics and their corresponding API endpoints
topics = {
    "Science": "https://api.api-ninjas.com/v1/facts?category=science",
    "Technology": "https://api.api-ninjas.com/v1/facts?category=technology",
    "History": "https://api.api-ninjas.com/v1/facts?category=history",
    "General Knowledge": "https://api.api-ninjas.com/v1/facts?category=general"
}

# Function to display a random fact or concept from the chosen topic
def display_fact(topic):
    api_key = "YOUR_API_KEY_HERE"
    url = topics[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        facts = response.json()
        random_fact = random.choice(facts)
        print(f"Random fact about {topic}: {random_fact['fact']}")
    else:
        print("Error fetching facts. Please try again later.")

# Function to run the interactive quiz
def run_quiz(topic):
    # Fetch quiz questions and answers from a predefined database or API
    quiz_data = get_quiz_data(topic)
    
    score = 0
    for question, options, answer in quiz_data:
        print(question)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        
        user_answer = int(input("Enter your answer (1-4): "))
        if options[user_answer-1] == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {answer}")
    
    print(f"Your final score: {score}/{len(quiz_data)}")

# Function to get quiz data from a predefined database or API
def get_quiz_data(topic):
    # Implement the logic to fetch quiz data based on the topic
    # This can be done by querying a database or making an API call
    
    # Example quiz data for the "Science" topic
    if topic == "Science":
        return [
            ("What is the chemical symbol for gold?", ["Au", "Ag", "Cu", "Fe"], "Au"),
            ("What is the process by which plants convert sunlight into energy?", ["Respiration", "Photosynthesis", "Transpiration", "Evaporation"], "Photosynthesis"),
            ("What is the name of the force that attracts objects with mass?", ["Friction", "Gravity", "Electromagnetism", "Centrifugal"], "Gravity")
        ]
    
    # Implement similar logic for other topics
    return []

# Main function to run the interactive knowledge app
def main():
    print("Welcome to the Interactive Knowledge App!")
    
    while True:
        print("\nSelect a topic:")
        for topic in topics:
            print(f"- {topic}")
        
        chosen_topic = input("Enter your choice: ")
        if chosen_topic in topics:
            display_fact(chosen_topic)
            run_quiz(chosen_topic)
        else:
            print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
