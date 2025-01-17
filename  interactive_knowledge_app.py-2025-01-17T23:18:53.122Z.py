
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
    '1': 'https://api.api-ninjas.com/v1/science?category=random',
    '2': 'https://api.api-ninjas.com/v1/technology?category=random',
    '3': 'https://api.api-ninjas.com/v1/history?category=random',
    '4': 'https://opentdb.com/api.php?amount=1&category=9&difficulty=medium&type=multiple'
}

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic_id):
    api_key = 'YOUR_API_KEY_HERE'
    url = api_endpoints[topic_id]
    headers = {'X-Api-Key': api_key}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        if topic_id == '4':
            return data['results'][0]['question'], data['results'][0]['correct_answer'], data['results'][0]['incorrect_answers']
        else:
            return data[0]['fact']
    except requests.exceptions.RequestException as e:
        print(f'Error fetching data: {e}')
        return None

# Function to run the interactive quiz
def run_quiz(topic_id):
    question, correct_answer, incorrect_answers = get_random_fact(topic_id)
    if question is None:
        return

    print(f'Question: {question}')

    # Shuffle the answers
    answers = [correct_answer] + incorrect_answers
    random.shuffle(answers)

    # Display the multiple-choice options
    for i, answer in enumerate(answers):
        print(f'{i+1}. {answer}')

    # Get user's answer
    user_answer = input('Enter your answer (1-4): ')

    if answers[int(user_answer) - 1] == correct_answer:
        print('Correct!')
    else:
        print(f'Incorrect. The correct answer is: {correct_answer}')

# Main function to run the interactive knowledge app
def main():
    print('Welcome to the Interactive Knowledge App!')

    while True:
        print('\nSelect a topic:')
        for topic_id, topic_name in topics.items():
            print(f'{topic_id}. {topic_name}')
        print('5. Exit')

        choice = input('Enter your choice (1-5): ')

        if choice == '5':
            print('Goodbye!')
            break

        if choice in topics:
            print(f'\nYou selected: {topics[choice]}')
            run_quiz(choice)
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
