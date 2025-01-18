import random
import requests
import json

# Define the topics and corresponding facts/quizzes
topics = {
    'science': {
        'facts': [
            'The human body has around 100 trillion cells.',
            'The first digital computer was the ENIAC, which was completed in 1946.',
            'The largest known prime number as of 2022 has 23,249,425 digits.'
        ],
        'quizzes': [
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            },
            {
                'question': 'Which scientist is famous for developing the theory of relativity?',
                'options': ['Isaac Newton', 'Albert Einstein', 'Stephen Hawking', 'Marie Curie'],
                'answer': 'Albert Einstein'
            },
            {
                'question': 'What is the name of the process by which plants convert sunlight into energy?',
                'options': ['Respiration', 'Photosynthesis', 'Combustion', 'Evaporation'],
                'answer': 'Photosynthesis'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first electronic digital computer, the ENIAC, was completed in 1946 and weighed 30 tons.',
            'The first commercial microprocessor was the Intel 4004, released in 1971.',
            'The World Wide Web was invented by Tim Berners-Lee in 1989.'
        ],
        'quizzes': [
            {
                'question': 'What does the acronym "CPU" stand for?',
                'options': ['Central Processing Unit', 'Computer Power Unit', 'Central Power Unit', 'Computer Processing Unit'],
                'answer': 'Central Processing Unit'
            },
            {
                'question': 'Which company developed the first commercially successful smartphone?',
                'options': ['Apple', 'Samsung', 'Nokia', 'BlackBerry'],
                'answer': 'BlackBerry'
            },
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.',
            'The Roman Empire lasted for over 400 years, from 27 BC to 476 AD.',
            'The Gutenberg Bible, printed in 1455, was the first major book printed in the West using movable metal type.'
        ],
        'quizzes': [
            {
                'question': 'Which ancient civilization is known for its advanced mathematics and calendar system?',
                'options': ['Egyptians', 'Greeks', 'Mayans', 'Mesopotamians'],
                'answer': 'Mayans'
            },
            {
                'question': 'What was the name of the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'Benjamin Franklin'],
                'answer': 'George Washington'
            },
            {
                'question': 'Which event is considered the start of World War I?',
                'options': ['Assassination of Archduke Franz Ferdinand', 'Sinking of the Lusitania', 'Treaty of Versailles', 'Invasion of Poland'],
                'answer': 'Assassination of Archduke Franz Ferdinand'
            }
        ]
    },
    'general': {
        'facts': [
            'The largest known prime number as of 2022 has 23,249,425 digits.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.',
            'The first person convicted of speeding was Walter Arnold of East Peckham, Kent, UK, in 1896. He was doing 8 mph in a 2 mph zone.'
        ],
        'quizzes': [
            {
                'question': 'What is the largest organ in the human body?',
                'options': ['Heart', 'Liver', 'Skin', 'Brain'],
                'answer': 'Skin'
            },
            {
                'question': 'What is the rarest blood type?',
                'options': ['A', 'B', 'AB', 'O'],
                'answer': 'AB'
            },
            {
                'question': 'What is the tallest mountain in the world?',
                'options': ['Mount Everest', 'K2', 'Kangchenjunga', 'Lhotse'],
                'answer': 'Mount Everest'
            }
        ]
    }
}

def get_random_fact(topic):
    return random.choice(topics[topic]['facts'])

def get_random_quiz(topic):
    quiz = random.choice(topics[topic]['quizzes'])
    return quiz

def run_quiz(quiz):
    print(quiz['question'])
    for i, option in enumerate(quiz['options']):
        print(f"{i+1}. {option}")
    
    user_answer = input("Enter your answer (1-4): ")
    if quiz['options'][int(user_answer) - 1] == quiz['answer']:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz['answer'])

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print("\nHere's a random fact about", selected_topic.capitalize() + ":")
        print(get_random_fact(selected_topic))
        
        print("\nNow, let's test your knowledge with a quiz!")
        quiz = get_random_quiz(selected_topic)
        run_quiz(quiz)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()