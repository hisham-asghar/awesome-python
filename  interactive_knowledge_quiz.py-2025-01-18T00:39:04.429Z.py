import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The hottest temperature ever recorded on Earth was 154°F (68°C) in Death Valley, California.',
            'Cats have fewer toes on their back paws than their front paws.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the primary function of the human heart?',
                'options': ['Pumping blood', 'Digesting food', 'Producing hormones', 'Filtering waste'],
                'answer': 0
            },
            {
                'question': 'Which of these is the largest planet in our solar system?',
                'options': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
                'answer': 2
            },
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 0
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer mouse was invented in 1964 and had only one button.',
            'The first commercial email service was launched in 1971 by Ray Tomlinson.',
            'The world's first programmable computer was the ENIAC, completed in 1946.'
        ],
        'quiz_questions': [
            {
                'question': 'What does "RAM" stand for in computer terminology?',
                'options': ['Random Access Memory', 'Rapid Acceleration Mechanism', 'Rotational Acceleration Module', 'Rapid Analog Modulation'],
                'answer': 0
            },
            {
                'question': 'Which company developed the first commercial web browser?',
                'options': ['Microsoft', 'Apple', 'Netscape', 'Google'],
                'answer': 2
            },
            {
                'question': 'What is the primary function of a computer's CPU?',
                'options': ['Storing data', 'Displaying images', 'Processing information', 'Generating electricity'],
                'answer': 2
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The first successful powered flight took place on December 17, 1903, by the Wright brothers.',
            'The Eiffel Tower was built in 1889 as the entrance arch for the World's Fair.'
        ],
        'quiz_questions': [
            {
                'question': 'Which ancient civilization is known for building the Pyramids of Giza?',
                'options': ['Mesopotamia', 'Indus Valley', 'Ancient Egypt', 'Aztec'],
                'answer': 2
            },
            {
                'question': 'What was the name of the first successful American space mission to the Moon?',
                'options': ['Apollo 11', 'Gemini 7', 'Mercury 6', 'Sputnik 1'],
                'answer': 0
            },
            {
                'question': 'Which event is considered the start of World War I?',
                'options': ['The assassination of Archduke Franz Ferdinand', 'The bombing of Pearl Harbor', 'The Cuban Missile Crisis', 'The fall of the Berlin Wall'],
                'answer': 0
            }
        ]
    },
    'general_knowledge': {
        'facts': [
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.',
            'A group of porcupines is called a prickle.',
            'The first product to have a barcode was Wrigley's gum.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Pacific Ocean', 'Indian Ocean', 'Arctic Ocean'],
                'answer': 1
            },
            {
                'question': 'Which of these is not a primary color?',
                'options': ['Red', 'Blue', 'Green', 'Yellow'],
                'answer': 3
            },
            {
                'question': 'What is the rarest blood type?',
                'options': ['A', 'B', 'AB', 'O'],
                'answer': 2
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the specified topic.
    """
    facts = topics[topic]['facts']
    return random.choice(facts)

def get_quiz_question(topic):
    """
    Retrieves a random quiz question and its options from the specified topic.
    """
    quiz_questions = topics[topic]['quiz_questions']
    question = random.choice(quiz_questions)
    return question['question'], question['options'], question['answer']

def run_interactive_quiz():
    """
    Runs an interactive quiz for the user, allowing them to select a topic and answer multiple-choice questions.
    """
    print('Welcome to the Interactive Knowledge Quiz!')
    print('Please select a topic:')
    for topic in topics:
        print(f'- {topic.capitalize()}')

    selected_topic = input('Enter your choice: ').lower()
    if selected_topic not in topics:
        print('Invalid topic. Please try again.')
        return

    print(f'You have selected the {selected_topic.capitalize()} topic.')
    print('Here is a random fact:')
    print(get_random_fact(selected_topic))
    print()

    print('Now, let\'s test your knowledge with a quiz!')
    score = 0
    for _ in range(3):
        question, options, answer = get_quiz_question(selected_topic)
        print(question)
        for i, option in enumerate(options):
            print(f'{i+1}. {option}')
        user_answer = int(input('Enter your answer (1-4): '))
        if user_answer - 1 == answer:
            print('Correct!')
            score += 1
        else:
            print('Incorrect. Better luck next time!')
        print()

    print(f'Your final score is {score} out of 3.')

if __name__ == '__main__':
    run_interactive_quiz()