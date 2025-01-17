import random
import requests
import json

# Define topics and their corresponding API endpoints or data sources
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
        # Fetch science fact from an API or database
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=science')
        facts = response.json()
        return random.choice(facts)['fact']
    elif topic == '2':
        # Fetch technology fact from an API or database
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=technology')
        facts = response.json()
        return random.choice(facts)['fact']
    elif topic == '3':
        # Fetch history fact from an API or database
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=history')
        facts = response.json()
        return random.choice(facts)['fact']
    elif topic == '4':
        # Fetch general knowledge fact from an API or database
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=general')
        facts = response.json()
        return random.choice(facts)['fact']
    else:
        return 'Invalid topic selected.'

def quiz(topic):
    """
    Provide a multiple-choice quiz for the specified topic.
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
                'question': 'What is the process of converting water into steam called?',
                'options': ['Evaporation', 'Condensation', 'Boiling', 'Sublimation'],
                'answer': 'Boiling'
            },
            # Add more science quiz questions and answers
        ]
    elif topic == '2':
        # Technology quiz questions and answers
        questions = [
            {
                'question': 'What is the name of the first commercially successful web browser?',
                'options': ['Internet Explorer', 'Netscape Navigator', 'Mozilla Firefox', 'Google Chrome'],
                'answer': 'Netscape Navigator'
            },
            {
                'question': 'What is the name of the programming language used to create websites?',
                'options': ['Java', 'Python', 'C++', 'HTML'],
                'answer': 'HTML'
            },
            # Add more technology quiz questions and answers
        ]
    elif topic == '3':
        # History quiz questions and answers
        questions = [
            {
                'question': 'What year did the American Civil War begin?',
                'options': ['1861', '1865', '1914', '1939'],
                'answer': '1861'
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'John Adams'],
                'answer': 'George Washington'
            },
            # Add more history quiz questions and answers
        ]
    elif topic == '4':
        # General knowledge quiz questions and answers
        questions = [
            {
                'question': 'What is the capital city of Australia?',
                'options': ['Sydney', 'Melbourne', 'Brisbane', 'Canberra'],
                'answer': 'Canberra'
            },
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
                'answer': 'Jupiter'
            },
            # Add more general knowledge quiz questions and answers
        ]
    else:
        return 'Invalid topic selected.'

    # Select a random question from the list
    question = random.choice(questions)

    # Display the question and options
    print(question['question'])
    for i, option in enumerate(question['options']):
        print(f"{i+1}. {option}")

    # Get the user's answer
    user_answer = input("Enter your answer (1-4): ")

    # Check if the user's answer is correct
    if question['options'][int(user_answer)-1] == question['answer']:
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

    topic = input("Enter the number of the topic (1-4): ")

    print(f"You selected: {topics[topic]}")
    print(get_random_fact(topic))
    print(quiz(topic))

if __name__ == "__main__":
    main()