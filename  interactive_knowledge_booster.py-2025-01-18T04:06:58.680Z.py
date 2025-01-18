
import random
import requests
import json

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the selected topic using a public API or a predefined database.
    """
    # Example using the 'uselessfacts' API
    if topic == 'science':
        url = 'https://uselessfacts.jsph.pl/api/v2/facts/random?category=science'
    elif topic == 'technology':
        url = 'https://uselessfacts.jsph.pl/api/v2/facts/random?category=technology'
    elif topic == 'history':
        url = 'https://uselessfacts.jsph.pl/api/v2/facts/random?category=history'
    else:
        url = 'https://uselessfacts.jsph.pl/api/v2/facts/random'

    response = requests.get(url)
    data = response.json()
    return data['text']

def quiz_question(topic):
    """
    Generates a multiple-choice quiz question for the selected topic.
    """
    # Example using predefined questions and answers
    if topic == 'science':
        questions = [
            {
                'question': 'What is the chemical symbol for gold?',
                'answers': ['Au', 'Ag', 'Cu', 'Fe'],
                'correct': 0
            },
            {
                'question': 'Which planet in our solar system has the most moons?',
                'answers': ['Jupiter', 'Saturn', 'Uranus', 'Neptune'],
                'correct': 0
            },
            # Add more science-related questions here
        ]
    elif topic == 'technology':
        questions = [
            {
                'question': 'What is the name of the first programmable computer?',
                'answers': ['ENIAC', 'UNIVAC', 'Analytical Engine', 'Z1'],
                'correct': 2
            },
            {
                'question': 'Which company developed the first commercially successful smartphone?',
                'answers': ['Apple', 'Samsung', 'BlackBerry', 'Nokia'],
                'correct': 2
            },
            # Add more technology-related questions here
        ]
    elif topic == 'history':
        questions = [
            {
                'question': 'In which year did World War II end?',
                'answers': ['1945', '1939', '1941', '1947'],
                'correct': 0
            },
            {
                'question': 'Who was the first president of the United States?',
                'answers': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'John Adams'],
                'correct': 2
            },
            # Add more history-related questions here
        ]
    else:
        questions = [
            {
                'question': 'What is the largest ocean on Earth?',
                'answers': ['Atlantic Ocean', 'Arctic Ocean', 'Indian Ocean', 'Pacific Ocean'],
                'correct': 3
            },
            {
                'question': 'What is the capital of Australia?',
                'answers': ['Sydney', 'Melbourne', 'Brisbane', 'Canberra'],
                'correct': 3
            },
            # Add more general knowledge questions here
        ]

    # Select a random question from the list
    question = random.choice(questions)
    return question

def main():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    print('1. Science')
    print('2. Technology')
    print('3. History')
    print('4. General Knowledge')

    topic_choice = input('Enter the number of your choice (1-4): ')

    if topic_choice == '1':
        topic = 'science'
    elif topic_choice == '2':
        topic = 'technology'
    elif topic_choice == '3':
        topic = 'history'
    else:
        topic = 'general'

    print(f'\nYour selected topic is: {topic.capitalize()}')
    print(f'Here is a random fact or concept about {topic}:')
    print(get_random_fact(topic))

    print('\nNow, let\'s test your knowledge with a quiz!')
    question = quiz_question(topic)
    print(question['question'])
    for i, answer in enumerate(question['answers']):
        print(f"{i+1}. {answer}")

    user_answer = int(input('Enter the number of your answer (1-4): '))
    if user_answer - 1 == question['correct']:
        print('Correct! You're a knowledge champion!')
    else:
        print('Oops, that's not the right answer. Better luck next time!')

    print('\nThank you for using the Interactive Knowledge Booster!')

if __name__ == '__main__':
    main()
