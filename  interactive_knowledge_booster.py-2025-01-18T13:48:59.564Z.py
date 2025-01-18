
import random
import requests
import json

# Define the topics and their corresponding API endpoints
topics = {
    '1': 'Science',
    '2': 'Technology',
    '3': 'History',
    '4': 'General Knowledge'
}

def get_random_fact(topic):
    """
    Fetch a random fact or concept from the corresponding API endpoint.
    """
    if topic == '1':
        # Science API endpoint
        url = 'https://api.api-ninjas.com/v1/facts?category=science'
    elif topic == '2':
        # Technology API endpoint
        url = 'https://api.api-ninjas.com/v1/facts?category=technology'
    elif topic == '3':
        # History API endpoint
        url = 'https://api.api-ninjas.com/v1/facts?category=history'
    elif topic == '4':
        # General Knowledge API endpoint
        url = 'https://api.api-ninjas.com/v1/facts?category=general'
    else:
        return 'Invalid topic selected.'

    response = requests.get(url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    if response.status_code == 200:
        facts = json.loads(response.text)
        return random.choice(facts)['fact']
    else:
        return 'Error fetching fact.'

def quiz(topic):
    """
    Provide a multiple-choice quiz for the selected topic.
    """
    if topic == '1':
        # Science quiz questions
        questions = [
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            },
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
                'answer': 'Jupiter'
            },
            # Add more science quiz questions here
        ]
    elif topic == '2':
        # Technology quiz questions
        questions = [
            {
                'question': 'What is the name of the first programmable computer?',
                'options': ['ENIAC', 'Apple I', 'IBM PC', 'Commodore 64'],
                'answer': 'ENIAC'
            },
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            },
            # Add more technology quiz questions here
        ]
    elif topic == '3':
        # History quiz questions
        questions = [
            {
                'question': 'What year did the American Revolutionary War begin?',
                'options': ['1776', '1812', '1861', '1914'],
                'answer': '1776'
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'John Adams'],
                'answer': 'George Washington'
            },
            # Add more history quiz questions here
        ]
    elif topic == '4':
        # General Knowledge quiz questions
        questions = [
            {
                'question': 'What is the capital city of Australia?',
                'options': ['Sydney', 'Melbourne', 'Brisbane', 'Canberra'],
                'answer': 'Canberra'
            },
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 'Pacific Ocean'
            },
            # Add more general knowledge quiz questions here
        ]
    else:
        return 'Invalid topic selected.'

    # Randomly select a question from the list
    question = random.choice(questions)

    # Display the question and options
    print(question['question'])
    for i, option in enumerate(question['options']):
        print(f"{i+1}. {option}")

    # Get the user's answer
    user_answer = input("Enter your answer (1-4): ")

    # Check if the user's answer is correct
    if user_answer == question['answer']:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {question['answer']}.")

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic_id, topic_name in topics.items():
        print(f"{topic_id}. {topic_name}")

    user_topic = input("Enter the topic number (1-4): ")

    print(f"You selected: {topics[user_topic]}")
    print(get_random_fact(user_topic))
    print()

    quiz(user_topic)

if __name__ == "__main__":
    main()
