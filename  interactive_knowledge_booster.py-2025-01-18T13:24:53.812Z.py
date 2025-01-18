
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

topic_apis = {
    '1': 'https://api.api-ninjas.com/v1/facts?category=science',
    '2': 'https://api.api-ninjas.com/v1/facts?category=technology',
    '3': 'https://api.api-ninjas.com/v1/facts?category=history',
    '4': 'https://api.api-ninjas.com/v1/facts?category=general'
}

# Define the API key
api_key = 'YOUR_API_KEY_HERE'

def get_random_fact(topic):
    """
    Fetch a random fact from the specified topic using the API.
    """
    url = topic_apis[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    return data[0]['fact']

def quiz(topic):
    """
    Provide a multiple-choice quiz for the specified topic.
    """
    url = topic_apis[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    
    # Select a random fact and generate multiple-choice options
    fact = data[random.randint(0, len(data) - 1)]['fact']
    options = [fact]
    for i in range(3):
        other_fact = data[random.randint(0, len(data) - 1)]['fact']
        if other_fact != fact:
            options.append(other_fact)
    random.shuffle(options)
    
    # Ask the user to select the correct option
    print(f'Which of the following is a fact about {topics[topic]}?')
    for i, option in enumerate(options):
        print(f'{i+1}. {option}')
    user_input = input('Enter the number of the correct answer: ')
    
    if options[int(user_input) - 1] == fact:
        print('Correct!')
    else:
        print(f'Incorrect. The correct answer is: {fact}')

def main():
    """
    Main function to display the menu and handle user input.
    """
    print('Welcome to the Interactive Knowledge Booster!')
    while True:
        print('\nSelect a topic:')
        for topic_id, topic_name in topics.items():
            print(f'{topic_id}. {topic_name}')
        print('5. Quit')
        
        user_input = input('Enter the number of the topic you want to explore: ')
        
        if user_input == '5':
            print('Goodbye!')
            break
        elif user_input in topics:
            print(f'\nHere is a random fact about {topics[user_input]}:')
            print(get_random_fact(user_input))
            print('\nNow, let\'s test your knowledge!')
            quiz(user_input)
        else:
            print('Invalid input. Please try again.')

if __name__ == '__main__':
    main()
