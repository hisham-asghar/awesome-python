
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
    Fetch a random fact or concept from the specified topic.
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
    Provide a multiple-choice quiz for the specified topic.
    """
    if topic == '1':
        # Fetch science quiz questions and answers from an API or database
        response = requests.get('https://opentdb.com/api.php?amount=1&category=17&difficulty=easy&type=multiple')
        quiz_data = response.json()['results'][0]
        question = quiz_data['question']
        choices = quiz_data['incorrect_answers'] + [quiz_data['correct_answer']]
        random.shuffle(choices)
        print(f"Question: {question}")
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")
        user_answer = input("Enter your answer (1-4): ")
        if choices[int(user_answer) - 1] == quiz_data['correct_answer']:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {quiz_data['correct_answer']}")
    elif topic == '2':
        # Fetch technology quiz questions and answers from an API or database
        response = requests.get('https://opentdb.com/api.php?amount=1&category=18&difficulty=easy&type=multiple')
        quiz_data = response.json()['results'][0]
        question = quiz_data['question']
        choices = quiz_data['incorrect_answers'] + [quiz_data['correct_answer']]
        random.shuffle(choices)
        print(f"Question: {question}")
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")
        user_answer = input("Enter your answer (1-4): ")
        if choices[int(user_answer) - 1] == quiz_data['correct_answer']:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {quiz_data['correct_answer']}")
    elif topic == '3':
        # Fetch history quiz questions and answers from an API or database
        response = requests.get('https://opentdb.com/api.php?amount=1&category=23&difficulty=easy&type=multiple')
        quiz_data = response.json()['results'][0]
        question = quiz_data['question']
        choices = quiz_data['incorrect_answers'] + [quiz_data['correct_answer']]
        random.shuffle(choices)
        print(f"Question: {question}")
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")
        user_answer = input("Enter your answer (1-4): ")
        if choices[int(user_answer) - 1] == quiz_data['correct_answer']:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {quiz_data['correct_answer']}")
    elif topic == '4':
        # Fetch general knowledge quiz questions and answers from an API or database
        response = requests.get('https://opentdb.com/api.php?amount=1&category=9&difficulty=easy&type=multiple')
        quiz_data = response.json()['results'][0]
        question = quiz_data['question']
        choices = quiz_data['incorrect_answers'] + [quiz_data['correct_answer']]
        random.shuffle(choices)
        print(f"Question: {question}")
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")
        user_answer = input("Enter your answer (1-4): ")
        if choices[int(user_answer) - 1] == quiz_data['correct_answer']:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {quiz_data['correct_answer']}")
    else:
        print("Invalid topic selection.")

def main():
    """
    Main function to run the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")
    for key, value in topics.items():
        print(f"{key}. {value}")
    topic = input("Enter the number of the topic (1-4): ")

    print(f"\nRandom fact about {topics[topic]}:")
    print(get_random_fact(topic))

    print("\nNow let's test your knowledge with a quiz!")
    quiz(topic)

if __name__ == "__main__":
    main()
