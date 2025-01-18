import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The largest known prime number as of 2023 has 23,249,425 digits.',
            'The human body has around 60,000 miles of blood vessels.',
            'The first computer bug was a real moth trapped in a Harvard Mark II computer.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the first satellite launched into Earth\'s orbit?',
                'options': ['Sputnik 1', 'Explorer 1', 'Vanguard 1', 'Telstar 1'],
                'answer': 'Sputnik 1'
            },
            {
                'question': 'Which scientist is known for the theory of relativity?',
                'options': ['Isaac Newton', 'Albert Einstein', 'Stephen Hawking', 'Galileo Galilei'],
                'answer': 'Albert Einstein'
            },
            {
                'question': 'What is the name of the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Osmosis'],
                'answer': 'Photosynthesis'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer mouse was invented in 1964 and had only one button.',
            'The first commercial text message was sent on December 3, 1992.',
            'The first smartphone was the IBM Simon, released in 1992.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            },
            {
                'question': 'What is the name of the first web browser?',
                'options': ['Internet Explorer', 'Google Chrome', 'Mozilla Firefox', 'Mosaic'],
                'answer': 'Mosaic'
            },
            {
                'question': 'Which company developed the first commercially successful smartphone?',
                'options': ['Apple', 'Samsung', 'BlackBerry', 'Nokia'],
                'answer': 'BlackBerry'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Rosetta Stone, a key to deciphering ancient Egyptian hieroglyphics, was discovered in 1799.',
            'The first Olympic Games were held in 776 BC in Olympia, Greece.'
        ],
        'quiz_questions': [
            {
                'question': 'Which ancient civilization is known for its advanced mathematical and astronomical knowledge?',
                'options': ['Mesopotamia', 'Egypt', 'Greece', 'India'],
                'answer': 'Mesopotamia'
            },
            {
                'question': 'What was the name of the first permanent European settlement in North America?',
                'options': ['Jamestown', 'Plymouth Rock', 'St. Augustine', 'Quebec City'],
                'answer': 'St. Augustine'
            },
            {
                'question': 'Which event is considered the start of the American Civil War?',
                'options': ['The Battle of Gettysburg', 'The Emancipation Proclamation', 'The Assassination of Abraham Lincoln', 'The Attack on Fort Sumter'],
                'answer': 'The Attack on Fort Sumter'
            }
        ]
    },
    'general': {
        'facts': [
            'The largest known prime number as of 2023 has 23,249,425 digits.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.',
            'The first person convicted of speeding was Walter Arnold of East Peckham, Kent, UK, in 1896. He was fined 1 shilling for driving at 8 mph (13 km/h), which was the speed limit at the time.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 'Pacific Ocean'
            },
            {
                'question': 'What is the name of the largest moon of Saturn?',
                'options': ['Titan', 'Ganymede', 'Callisto', 'Europa'],
                'answer': 'Titan'
            },
            {
                'question': 'Who is the author of the Harry Potter book series?',
                'options': ['J.K. Rowling', 'J.R.R. Tolkien', 'Stephen King', 'George R.R. Martin'],
                'answer': 'J.K. Rowling'
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the selected topic.
    """
    return random.choice(topics[topic]['facts'])

def get_quiz_question(topic):
    """
    Retrieves a random quiz question from the selected topic.
    """
    question = random.choice(topics[topic]['quiz_questions'])
    return question

def run_quiz(topic):
    """
    Runs a quiz for the selected topic.
    """
    question = get_quiz_question(topic)
    print(question['question'])
    for i, option in enumerate(question['options']):
        print(f"{i+1}. {option}")
    
    while True:
        user_answer = input("Enter the number of your answer: ")
        if user_answer.isdigit() and int(user_answer) in range(1, len(question['options'])+1):
            if question['options'][int(user_answer)-1] == question['answer']:
                print("Correct!")
                return
            else:
                print("Incorrect. Please try again.")
        else:
            print("Invalid input. Please enter a number between 1 and", len(question['options']))

def main():
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    while True:
        selected_topic = input("Enter your choice: ").lower()
        if selected_topic in topics:
            print(f"Random fact about {selected_topic.capitalize()}:")
            print(get_random_fact(selected_topic))
            print("\nTime for a quiz!")
            run_quiz(selected_topic)
            break
        else:
            print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()