
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
    Fetch a random fact or concept from the selected topic.
    """
    if topic == '1':
        # Fetch a random science fact from an API or database
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=science', headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
        data = response.json()
        return data[0]['fact']
    elif topic == '2':
        # Fetch a random technology fact from an API or database
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=technology', headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
        data = response.json()
        return data[0]['fact']
    elif topic == '3':
        # Fetch a random history fact from an API or database
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=history', headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
        data = response.json()
        return data[0]['fact']
    elif topic == '4':
        # Fetch a random general knowledge fact from an API or database
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=general', headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
        data = response.json()
        return data[0]['fact']
    else:
        return "Invalid topic selected."

def quiz_question(topic):
    """
    Provide a multiple-choice quiz question for the selected topic.
    """
    if topic == '1':
        # Generate a science quiz question
        question = "What is the chemical symbol for gold?"
        options = ['Au', 'Ag', 'Cu', 'Fe']
        answer = 0
    elif topic == '2':
        # Generate a technology quiz question
        question = "What is the name of the first programmable computer?"
        options = ['ENIAC', 'Apple II', 'IBM PC', 'Commodore 64']
        answer = 0
    elif topic == '3':
        # Generate a history quiz question
        question = "Who was the first president of the United States?"
        options = ['Abraham Lincoln', 'George Washington', 'Thomas Jefferson', 'John Adams']
        answer = 1
    elif topic == '4':
        # Generate a general knowledge quiz question
        question = "What is the largest planet in our solar system?"
        options = ['Earth', 'Mars', 'Jupiter', 'Saturn']
        answer = 2
    else:
        return "Invalid topic selected."

    return {'question': question, 'options': options, 'answer': answer}

def main():
    """
    The main function that runs the interactive knowledge-building program.
    """
    print("Welcome to the Interactive Knowledge-Building Program!")
    print("Please select a topic:")
    for key, value in topics.items():
        print(f"{key}. {value}")

    topic = input("Enter the number of the topic you want to explore: ")

    print(f"\nYour selected topic is: {topics[topic]}")
    print(get_random_fact(topic))

    quiz_data = quiz_question(topic)
    if quiz_data != "Invalid topic selected.":
        print("\nTime for a quiz!")
        print(quiz_data['question'])
        for i, option in enumerate(quiz_data['options']):
            print(f"{i+1}. {option}")

        user_answer = int(input("Enter the number of the correct answer: "))
        if user_answer == quiz_data['answer'] + 1:
            print("Correct! You're a knowledge master.")
        else:
            print("Oops, that's not the right answer. Better luck next time!")

if __name__ == "__main__":
    main()
