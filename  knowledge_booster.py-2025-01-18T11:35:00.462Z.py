
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has over 600 muscles.',
            'The largest known prime number has over 23 million digits.',
            'The first product to have a barcode was Wrigley's gum.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            },
            {
                'question': 'Which scientist is known for developing the theory of relativity?',
                'options': ['Isaac Newton', 'Albert Einstein', 'Stephen Hawking', 'Marie Curie'],
                'answer': 'Albert Einstein'
            },
            {
                'question': 'What is the name of the largest planet in our solar system?',
                'options': ['Saturn', 'Jupiter', 'Mars', 'Venus'],
                'answer': 'Jupiter'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer virus, called "Creeper," was created in 1971.',
            'The first commercial text message was sent on December 3, 1992.',
            'The first smartphone was the IBM Simon, released in 1992.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the operating system developed by Apple?',
                'options': ['Windows', 'Linux', 'macOS', 'Android'],
                'answer': 'macOS'
            },
            {
                'question': 'Which company created the popular search engine Google?',
                'options': ['Apple', 'Microsoft', 'Amazon', 'Alphabet'],
                'answer': 'Alphabet'
            },
            {
                'question': 'What is the name of the programming language that is known for its simplicity and readability?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The first successful powered flight took place on December 17, 1903, by the Wright brothers.',
            'The Mona Lisa was stolen from the Louvre in Paris in 1911 and was missing for two years.'
        ],
        'quiz_questions': [
            {
                'question': 'Which ancient civilization is known for its pyramids?',
                'options': ['Greek', 'Roman', 'Egyptian', 'Aztec'],
                'answer': 'Egyptian'
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'John Adams'],
                'answer': 'George Washington'
            },
            {
                'question': 'What was the name of the first successful manned space flight?',
                'options': ['Apollo 11', 'Sputnik 1', 'Vostok 1', 'Mercury-Redstone 3'],
                'answer': 'Vostok 1'
            }
        ]
    },
    'general': {
        'facts': [
            'The tallest mammal is the giraffe, which can grow up to 6 meters tall.',
            'The largest known prime number has over 23 million digits.',
            'The longest word in the English language is "pneumonoultramicroscopicsilicovolcanoconiosis."'
        ],
        'quiz_questions': [
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Arctic Ocean', 'Indian Ocean', 'Pacific Ocean'],
                'answer': 'Pacific Ocean'
            },
            {
                'question': 'Which country is known as the "Land of the Rising Sun"?',
                'options': ['China', 'Japan', 'Korea', 'Thailand'],
                'answer': 'Japan'
            },
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Saturn', 'Jupiter', 'Mars', 'Venus'],
                'answer': 'Jupiter'
            }
        ]
    }
}

def display_menu():
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")
    return input("Enter your choice: ").lower()

def display_fact(topic):
    fact = random.choice(topics[topic]['facts'])
    print(f"Here's a random fact about {topic.capitalize()}:")
    print(f"- {fact}")

def run_quiz(topic):
    print(f"Let's test your {topic.capitalize()} knowledge!")
    score = 0
    for question in topics[topic]['quiz_questions']:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i+1}. {option}")
        user_answer = input("Enter the number of your answer: ")
        if question['options'][int(user_answer) - 1] == question['answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", question['answer'])
    print(f"Your final score is: {score}/{len(topics[topic]['quiz_questions'])}")

def main():
    topic = display_menu()
    display_fact(topic)
    run_quiz(topic)

if __name__ == "__main__":
    main()
