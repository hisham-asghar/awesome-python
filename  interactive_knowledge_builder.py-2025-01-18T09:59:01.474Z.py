import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The Milky Way galaxy contains an estimated 100 to 400 billion stars.',
            'The hottest temperature ever recorded on Earth was 154°F (68°C) in Death Valley, California.'
        ],
        'quiz_questions': [
            {
                'question': 'Which of the following is the largest organ in the human body?',
                'options': ['Skin', 'Liver', 'Heart', 'Lungs'],
                'answer': 'Skin'
            },
            {
                'question': 'What is the name of the closest star to Earth?',
                'options': ['Proxima Centauri', 'Betelgeuse', 'Sirius', 'Polaris'],
                'answer': 'Proxima Centauri'
            },
            {
                'question': 'Which element has the chemical symbol H?',
                'options': ['Helium', 'Hydrogen', 'Helium', 'Halogens'],
                'answer': 'Hydrogen'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first electronic computer, ENIAC, weighed 30 tons and took up 1,800 square feet of floor space.',
            'The first smartphone was the IBM Simon, released in 1992.',
            'The internet was originally called ARPANET, created by the U.S. Department of Defense in 1969.'
        ],
        'quiz_questions': [
            {
                'question': 'What does the acronym 'RAM' stand for?',
                'options': ['Random Access Memory', 'Read-only Memory', 'Rapid Access Memory', 'Robust Access Memory'],
                'answer': 'Random Access Memory'
            },
            {
                'question': 'Which company developed the first commercially successful smartphone?',
                'options': ['Apple', 'Samsung', 'BlackBerry', 'Nokia'],
                'answer': 'BlackBerry'
            },
            {
                'question': 'What was the original purpose of the internet?',
                'options': ['Communication', 'Entertainment', 'Military', 'Education'],
                'answer': 'Military'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.',
            'The first successful powered flight was made by the Wright brothers in 1903, lasting 12 seconds.'
        ],
        'quiz_questions': [
            {
                'question': 'In what year did the United States declare its independence?',
                'options': ['1776', '1787', '1492', '1865'],
                'answer': '1776'
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Thomas Jefferson', 'Abraham Lincoln', 'George Washington', 'Benjamin Franklin'],
                'answer': 'George Washington'
            },
            {
                'question': 'What was the name of the ancient Egyptian queen who was known for her beauty?',
                'options': ['Cleopatra', 'Nefertiti', 'Hatshepsut', 'Neferkare'],
                'answer': 'Cleopatra'
            }
        ]
    },
    'general_knowledge': {
        'facts': [
            'The largest known prime number as of 2022 has 23 million digits.',
            'The world's largest desert is Antarctica, not the Sahara.',
            'The first person convicted of speeding was going 8 mph.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the tallest building in the world?',
                'options': ['Burj Khalifa', 'Shanghai Tower', 'Abraj Al-Bait Clock Tower', 'One World Trade Center'],
                'answer': 'Burj Khalifa'
            },
            {
                'question': 'What is the rarest blood type?',
                'options': ['A-', 'B-', 'AB-', 'O-'],
                'answer': 'AB-'
            },
            {
                'question': 'Which planet in our solar system is known as the "Red Planet"?',
                'options': ['Mars', 'Jupiter', 'Venus', 'Saturn'],
                'answer': 'Mars'
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Returns a random fact from the given topic.
    """
    return random.choice(topics[topic]['facts'])

def get_quiz_question(topic):
    """
    Returns a random quiz question and its options from the given topic.
    """
    quiz_question = random.choice(topics[topic]['quiz_questions'])
    return quiz_question

def main():
    """
    The main function that runs the interactive knowledge-building script.
    """
    print('Welcome to the Interactive Knowledge Builder!')
    print('Please select a topic:')

    # Display the available topics
    for topic in topics:
        print(f'- {topic.capitalize()}')

    # Get the user's topic choice
    chosen_topic = input('Enter your choice: ').lower()

    if chosen_topic in topics:
        # Display a random fact from the chosen topic
        print(f'\nHere\'s a random fact about {chosen_topic.capitalize()}:')
        print(get_random_fact(chosen_topic))

        # Display a random quiz question from the chosen topic
        print('\nLet\'s test your knowledge with a quiz question!')
        quiz_question = get_quiz_question(chosen_topic)
        print(quiz_question['question'])
        for option in quiz_question['options']:
            print(f'- {option}')

        # Get the user's answer
        user_answer = input('Enter your answer: ')

        # Check the user's answer and provide feedback
        if user_answer.lower() == quiz_question['answer'].lower():
            print('Correct! You know your stuff.')
        else:
            print(f'Oops, the correct answer is "{quiz_question["answer"]}".')
    else:
        print(f'Sorry, "{chosen_topic.capitalize()}" is not a valid topic. Please try again.')

if __name__ == '__main__':
    main()