
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    '1': 'Science',
    '2': 'Technology',
    '3': 'History',
    '4': 'General Knowledge'
}

def get_random_fact(topic):
    """
    Fetch a random fact or concept for the given topic.
    """
    if topic == '1':
        # Fetch a random science fact from an API or database
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=science')
        facts = response.json()
        return random.choice(facts)['fact']
    elif topic == '2':
        # Fetch a random technology fact from an API or database
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=technology')
        facts = response.json()
        return random.choice(facts)['fact']
    elif topic == '3':
        # Fetch a random history fact from an API or database
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=history')
        facts = response.json()
        return random.choice(facts)['fact']
    elif topic == '4':
        # Fetch a random general knowledge fact from an API or database
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=general')
        facts = response.json()
        return random.choice(facts)['fact']
    else:
        return "Invalid topic selection."

def quiz(topic):
    """
    Provide a multiple-choice quiz for the given topic.
    """
    if topic == '1':
        # Science quiz questions and answers
        questions = [
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            },
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Osmosis'],
                'answer': 'Photosynthesis'
            },
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Jupiter', 'Saturn', 'Neptune', 'Uranus'],
                'answer': 'Jupiter'
            }
        ]
    elif topic == '2':
        # Technology quiz questions and answers
        questions = [
            {
                'question': 'What is the name of the first computer programming language?',
                'options': ['FORTRAN', 'COBOL', 'BASIC', 'Ada'],
                'answer': 'FORTRAN'
            },
            {
                'question': 'What is the name of the operating system developed by Apple?',
                'options': ['Windows', 'Linux', 'macOS', 'Android'],
                'answer': 'macOS'
            },
            {
                'question': 'What is the name of the first web browser?',
                'options': ['Mozilla', 'Internet Explorer', 'Netscape Navigator', 'CERN WorldWideWeb'],
                'answer': 'CERN WorldWideWeb'
            }
        ]
    elif topic == '3':
        # History quiz questions and answers
        questions = [
            {
                'question': 'What year was the Declaration of Independence signed?',
                'options': ['1776', '1789', '1812', '1865'],
                'answer': '1776'
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'John Adams'],
                'answer': 'George Washington'
            },
            {
                'question': 'What was the name of the first successful powered flight?',
                'options': ['Wright Flyer', 'Spitfire', 'Mustang', 'Concorde'],
                'answer': 'Wright Flyer'
            }
        ]
    elif topic == '4':
        # General knowledge quiz questions and answers
        questions = [
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 'Pacific Ocean'
            },
            {
                'question': 'What is the capital city of Australia?',
                'options': ['Sydney', 'Melbourne', 'Brisbane', 'Canberra'],
                'answer': 'Canberra'
            },
            {
                'question': 'Who wrote the novel "To Kill a Mockingbird"?',
                'options': ['Harper Lee', 'Ernest Hemingway', 'F. Scott Fitzgerald', 'Maya Angelou'],
                'answer': 'Harper Lee'
            }
        ]
    else:
        return "Invalid topic selection."

    # Randomly select a question from the list
    question = random.choice(questions)

    # Display the question and options
    print(question['question'])
    for i, option in enumerate(question['options'], start=1):
        print(f"{i}. {option}")

    # Get the user's answer
    user_answer = input("Enter the number of your answer: ")

    # Check if the user's answer is correct
    if user_answer == question['answer']:
        return "Correct!"
    else:
        return "Incorrect. The correct answer is: " + question['answer']

def main():
    """
    Main function to run the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for key, value in topics.items():
        print(f"{key}. {value}")

    topic_choice = input("Enter the number of the topic: ")

    if topic_choice in topics:
        print("\nHere's a random fact or concept about", topics[topic_choice] + ":")
        print(get_random_fact(topic_choice))
        print("\nNow, let's test your knowledge with a quiz!")
        print(quiz(topic_choice))
    else:
        print("Invalid topic selection. Please try again.")

if __name__ == "__main__":
    main()
