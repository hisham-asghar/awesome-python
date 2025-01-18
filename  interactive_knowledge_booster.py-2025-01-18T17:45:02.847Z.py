import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The first digital computer, the ENIAC, was completed in 1946 and weighed 30 tons.',
            'The human body has over 600 muscles.',
            'The largest known prime number as of 2021 has 23 million digits.'
        ],
        'quiz': [
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            },
            {
                'question': 'What is the name of the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Osmosis'],
                'answer': 'Photosynthesis'
            },
            {
                'question': 'Which scientist is known for the theory of relativity?',
                'options': ['Isaac Newton', 'Albert Einstein', 'Galileo Galilei', 'Stephen Hawking'],
                'answer': 'Albert Einstein'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first electronic computer, ENIAC, had 17,468 vacuum tubes, 7,200 crystal diodes, 1,500 relays, 70,000 resistors, 10,000 capacitors, and around 5 million hand-soldered joints.',
            'The first commercial microprocessor was the Intel 4004, released in 1971.',
            'The first iPhone was released in 2007.'
        ],
        'quiz': [
            {
                'question': 'What does "HTML" stand for?',
                'options': ['Hyper Text Markup Language', 'Hyperlink Text Markup Language', 'Hyper Text Management Language', 'Hyperlink Text Management Language'],
                'answer': 'Hyper Text Markup Language'
            },
            {
                'question': 'Which company developed the Android operating system?',
                'options': ['Apple', 'Microsoft', 'Google', 'Samsung'],
                'answer': 'Google'
            },
            {
                'question': 'What is the name of the first computer virus?',
                'options': ['Morris Worm', 'ILOVEYOU', 'Melissa', 'Stuxnet'],
                'answer': 'Morris Worm'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.',
            'The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.',
            'The first successful powered flight took place on December 17, 1903, by the Wright brothers.'
        ],
        'quiz': [
            {
                'question': 'Which ancient civilization is known for its advanced mathematical and astronomical knowledge?',
                'options': ['Egyptians', 'Greeks', 'Mayans', 'Babylonians'],
                'answer': 'Babylonians'
            },
            {
                'question': 'What was the name of the first successful steamboat, developed by Robert Fulton in 1807?',
                'options': ['Clermont', 'Titanic', 'Mayflower', 'Nautilus'],
                'answer': 'Clermont'
            },
            {
                'question': 'Which event is considered the start of World War I?',
                'options': ['Assassination of Archduke Franz Ferdinand', 'Sinking of the Lusitania', 'Battle of the Somme', 'Invasion of Poland'],
                'answer': 'Assassination of Archduke Franz Ferdinand'
            }
        ]
    },
    'general': {
        'facts': [
            'The largest known snowflake was 15 inches wide and 8 inches thick, found in Montana in 1887.',
            'The first commercial airplane flight occurred on January 1, 1914, between St. Petersburg and Tampa, Florida.',
            'The largest known prime number as of 2021 has 23 million digits.'
        ],
        'quiz': [
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Pacific Ocean', 'Indian Ocean', 'Arctic Ocean'],
                'answer': 'Pacific Ocean'
            },
            {
                'question': 'Which country is known as the "Land of the Rising Sun"?',
                'options': ['China', 'Japan', 'South Korea', 'Thailand'],
                'answer': 'Japan'
            },
            {
                'question': 'What is the rarest blood type?',
                'options': ['A', 'B', 'AB', 'O'],
                'answer': 'AB'
            }
        ]
    }
}

def get_random_fact(topic):
    return random.choice(topics[topic]['facts'])

def get_quiz_question(topic):
    quiz_question = random.choice(topics[topic]['quiz'])
    return quiz_question

def run_quiz(topic):
    quiz_question = get_quiz_question(topic)
    print(quiz_question['question'])
    for i, option in enumerate(quiz_question['options']):
        print(f"{i+1}. {option}")
    
    user_answer = input("Enter your answer (1-4): ")
    if quiz_question['options'][int(user_answer) - 1] == quiz_question['answer']:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {quiz_question['answer']}.")

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print(f"Sorry, '{selected_topic}' is not a valid topic. Please try again.")

if __name__ == '__main__':
    main()