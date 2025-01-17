
import random
import requests
import json

# Define topics and their corresponding API endpoints
topics = {
    '1': 'Science',
    '2': 'Technology',
    '3': 'History',
    '4': 'General Knowledge'
}

api_endpoints = {
    'Science': 'https://api.api-ninjas.com/v1/facts?category=science',
    'Technology': 'https://api.api-ninjas.com/v1/facts?category=technology',
    'History': 'https://api.api-ninjas.com/v1/facts?category=history',
    'General Knowledge': 'https://api.api-ninjas.com/v1/facts?category=general'
}

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    api_key = 'your_api_key_here'
    url = api_endpoints[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    return random.choice(data)['fact']

# Function to display the multiple-choice quiz
def quiz(topic):
    # Fetch quiz questions and answers from a predefined database or API
    questions = {
        'Science': [
            {'question': 'What is the chemical symbol for gold?', 'answers': ['Au', 'Ag', 'Cu', 'Fe'], 'correct': 0},
            {'question': 'What is the largest planet in our solar system?', 'answers': ['Mars', 'Jupiter', 'Saturn', 'Neptune'], 'correct': 1},
            {'question': 'What is the process of converting water into water vapor called?', 'answers': ['Condensation', 'Evaporation', 'Precipitation', 'Transpiration'], 'correct': 1}
        ],
        # Add more questions for other topics
    }

    # Select a random question from the chosen topic
    question = random.choice(questions[topic])

    # Display the question and answers
    print(question['question'])
    for i, answer in enumerate(question['answers']):
        print(f"{i+1}. {answer}")

    # Get the user's answer
    user_answer = int(input("Enter your answer (1-4): "))

    # Check if the user's answer is correct
    if user_answer - 1 == question['correct']:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", question['answers'][question['correct']])

# Main function
def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Select a topic:")
    for key, topic in topics.items():
        print(f"{key}. {topic}")

    # Get the user's topic choice
    choice = input("Enter the number of the topic (1-4): ")

    if choice in topics:
        topic = topics[choice]
        print(f"\nYou selected: {topic}")
        print(get_random_fact(topic))
        print("\nNow let's test your knowledge!")
        quiz(topic)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
