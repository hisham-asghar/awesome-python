
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    "science": "https://api.api-ninjas.com/v1/facts?category=science",
    "technology": "https://api.api-ninjas.com/v1/facts?category=technology",
    "history": "https://api.api-ninjas.com/v1/facts?category=history",
    "general": "https://api.api-ninjas.com/v1/facts?category=general"
}

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    API_KEY = "YOUR_API_KEY_HERE"
    url = topics[topic]
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        facts = json.loads(response.text)
        return random.choice(facts)['fact']
    else:
        return "Failed to fetch data. Please try again later."

# Function to display the multiple-choice quiz
def quiz(topic):
    # Fetch quiz questions and answers from a predefined database or API
    quiz_data = get_quiz_data(topic)
    
    score = 0
    for question, choices, answer in quiz_data:
        print(question)
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", choices[answer-1])
    print(f"Your final score: {score}/{len(quiz_data)}")

# Function to get quiz data for the selected topic
def get_quiz_data(topic):
    # Implement logic to fetch quiz data from a predefined database or API
    # Return a list of tuples containing (question, choices, answer_index)
    quiz_data = []
    if topic == "science":
        quiz_data = [
            ("What is the chemical symbol for gold?", ["Au", "Ag", "Cu", "Fe"], 1),
            ("What is the largest planet in our solar system?", ["Mars", "Jupiter", "Saturn", "Uranus"], 2),
            ("What is the process by which plants convert sunlight into energy?", ["Photosynthesis", "Respiration", "Transpiration", "Evaporation"], 1)
        ]
    elif topic == "technology":
        quiz_data = [
            ("What is the full form of CPU?", ["Central Processing Unit", "Computer Processing Unit", "Centralized Processor Unit", "Computer Power Unit"], 1),
            ("Which company developed the first commercially successful smartphone?", ["Apple", "Samsung", "BlackBerry", "Nokia"], 3),
            ("What is the name of the programming language created by Guido van Rossum?", ["Java", "C++", "Python", "Ruby"], 3)
        ]
    # Add more quiz data for other topics
    return quiz_data

# Main function to run the interactive learning script
def main():
    print("Welcome to the Interactive Learning Script!")
    print("Please select a topic:")
    for topic in topics:
        print(f"{topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
