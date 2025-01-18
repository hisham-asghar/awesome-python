
import random
import requests
import json

# API endpoints for fetching educational content
API_ENDPOINTS = {
    'science': 'https://api.example.com/science',
    'technology': 'https://api.example.com/technology',
    'history': 'https://api.example.com/history',
    'general': 'https://api.example.com/general'
}

# Define quiz questions and answers
QUIZ_DATA = {
    'science': [
        {
            'question': 'What is the chemical symbol for gold?',
            'options': ['Au', 'Ag', 'Hg', 'Cu'],
            'answer': 'Au'
        },
        {
            'question': 'What is the largest planet in our solar system?',
            'options': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
            'answer': 'Jupiter'
        }
    ],
    'technology': [
        {
            'question': 'What is the primary function of a computer processor (CPU)?',
            'options': ['Storage', 'Input/Output', 'Processing', 'Networking'],
            'answer': 'Processing'
        },
        {
            'question': 'What is the name of the programming language created by Guido van Rossum?',
            'options': ['Java', 'C++', 'Python', 'Ruby'],
            'answer': 'Python'
        }
    ],
    'history': [
        {
            'question': 'In what year did the American Civil War begin?',
            'options': ['1861', '1865', '1776', '1945'],
            'answer': '1861'
        },
        {
            'question': 'Who was the first president of the United States?',
            'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'John Adams'],
            'answer': 'George Washington'
        }
    ],
    'general': [
        {
            'question': 'What is the largest ocean on Earth?',
            'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
            'answer': 'Pacific Ocean'
        },
        {
            'question': 'What is the capital city of Australia?',
            'options': ['Sydney', 'Melbourne', 'Brisbane', 'Canberra'],
            'answer': 'Canberra'
        }
    ]
}

def get_random_fact(topic):
    """
    Fetch a random fact or concept from the specified topic using an API.
    """
    try:
        response = requests.get(API_ENDPOINTS[topic])
        data = response.json()
        return random.choice(data)
    except (requests.exceptions.RequestException, KeyError):
        return 'Sorry, we couldn\'t fetch a random fact for that topic.'

def run_quiz(topic):
    """
    Run a quiz for the specified topic, with multiple-choice questions.
    """
    score = 0
    quiz_data = QUIZ_DATA[topic]
    for question in quiz_data:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i+1}. {option}")
        user_answer = input("Enter your answer (1-4): ")
        if question['options'][int(user_answer) - 1] == question['answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score is {score}/{len(quiz_data)}")

def main():
    """
    Main function to display the menu and handle user interactions.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in API_ENDPOINTS.keys():
        print(f"- {topic.capitalize()}")
    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in API_ENDPOINTS:
        print("\nHere's a random fact or concept about", selected_topic.capitalize() + ":")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
