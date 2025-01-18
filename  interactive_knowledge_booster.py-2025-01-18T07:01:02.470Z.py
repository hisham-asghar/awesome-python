import random
import json
import requests

# Define topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The hottest planet in the solar system is Venus, not Mercury.',
            'The largest known prime number as of 2022 has over 23 million digits.'
        ],
        'quiz': [
            {
                'question': 'What is the main component of the Earth\'s atmosphere?',
                'options': ['Oxygen', 'Nitrogen', 'Carbon dioxide', 'Water vapor'],
                'answer': 1
            },
            {
                'question': 'What is the process by which plants convert light energy into chemical energy?',
                'options': ['Photosynthesis', 'Respiration', 'Osmosis', 'Transpiration'],
                'answer': 0
            },
            {
                'question': 'What is the name of the force that attracts objects with mass towards each other?',
                'options': ['Gravity', 'Friction', 'Magnetism', 'Electricity'],
                'answer': 0
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer virus, called \"Brain\", was created in 1986.',
            'The first commercial text message was sent in 1992.',
            'The World Wide Web was invented by Tim Berners-Lee in 1989.'
        ],
        'quiz': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 2
            },
            {
                'question': 'What is the name of the device that converts digital signals into analog signals?',
                'options': ['Modem', 'Router', 'Switch', 'Amplifier'],
                'answer': 0
            },
            {
                'question': 'What is the name of the process by which data is transmitted between computers over the internet?',
                'options': ['Streaming', 'Downloading', 'Uploading', 'Networking'],
                'answer': 3
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.',
            'The Silk Road was an ancient network of trade routes that connected the East and West from the 2nd century BCE to the 18th century CE.',
            'The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci between 1503 and 1519.'
        ],
        'quiz': [
            {
                'question': 'What was the name of the first successful powered flight, made by the Wright brothers in 1903?',
                'options': ['The Flyer', 'The Glider', 'The Biplane', 'The Monoplane'],
                'answer': 0
            },
            {
                'question': 'What was the name of the first atomic bomb dropped on Hiroshima, Japan in 1945?',
                'options': ['Little Boy', 'Fat Man', 'Trinity', 'Atomic Bomb'],
                'answer': 0
            },
            {
                'question': 'What was the name of the first successful moon landing mission, carried out by NASA in 1969?',
                'options': ['Apollo 8', 'Apollo 11', 'Apollo 13', 'Apollo 17'],
                'answer': 1
            }
        ]
    },
    'general': {
        'facts': [
            'The largest known prime number as of 2022 has over 23 million digits.',
            'The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.',
            'The largest known prime number as of 2022 has over 23 million digits.'
        ],
        'quiz': [
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
                'answer': 2
            },
            {
                'question': 'What is the capital city of Australia?',
                'options': ['Sydney', 'Melbourne', 'Brisbane', 'Canberra'],
                'answer': 3
            },
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 3
            }
        ]
    }
}

def get_random_fact(topic):
    return random.choice(topics[topic]['facts'])

def get_quiz_question(topic):
    quiz_question = random.choice(topics[topic]['quiz'])
    return quiz_question

def check_answer(topic, question_index, user_answer):
    correct_answer = topics[topic]['quiz'][question_index]['answer']
    return user_answer == correct_answer

def main():
    print('Welcome to the Interactive Knowledge Booster!')
    print('Please select a topic:')
    for topic in topics:
        print(f'- {topic.capitalize()}')

    selected_topic = input('Enter your choice: ').lower()

    if selected_topic not in topics:
        print('Invalid topic. Please try again.')
        return

    print(f'\nHere\'s a random fact about {selected_topic.capitalize()}:')
    print(get_random_fact(selected_topic))

    print('\nNow, let\'s test your knowledge with a quiz!')

    score = 0
    for i in range(3):
        quiz_question = get_quiz_question(selected_topic)
        print(f'\nQuestion {i+1}: {quiz_question["question"]}')
        for j, option in enumerate(quiz_question['options']):
            print(f'{j+1}. {option}')

        user_answer = int(input('Enter your answer (1-4): ')) - 1
        if check_answer(selected_topic, i, user_answer):
            print('Correct!')
            score += 1
        else:
            print('Incorrect. Better luck next time!')

    print(f'\nYour final score is {score} out of 3.')

if __name__ == '__main__':
    main()