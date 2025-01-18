import random
import requests
import json

# Dictionary to store topics and their facts/quizzes
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The largest known prime number as of 2022 has 23 million digits.',
            'A single lightning bolt contains enough energy to cook 100,000 pieces of toast.'
        ],
        'quizzes': [
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            },
            {
                'question': 'Which scientist is known for the theory of relativity?',
                'options': ['Isaac Newton', 'Albert Einstein', 'Stephen Hawking', 'Marie Curie'],
                'answer': 'Albert Einstein'
            },
            {
                'question': 'What is the largest organ in the human body?',
                'options': ['Heart', 'Brain', 'Liver', 'Skin'],
                'answer': 'Skin'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer bug was a real moth found trapped in a Harvard Mark II computer in 1947.',
            'The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.',
            'The largest hard drive ever made had a capacity of 5.25 gigabytes and was the size of a refrigerator.'
        ],
        'quizzes': [
            {
                'question': 'What does the term "URL" stand for?',
                'options': ['Uniform Resource Locator', 'Universal Resource Link', 'Unique Resource Location', 'Unified Resource Locator'],
                'answer': 'Uniform Resource Locator'
            },
            {
                'question': 'Which company developed the first commercially successful smartphone?',
                'options': ['Apple', 'Samsung', 'BlackBerry', 'Nokia'],
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
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The first successful powered flight took place on December 17, 1903, by the Wright brothers.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.'
        ],
        'quizzes': [
            {
                'question': 'Which ancient civilization built the pyramids?',
                'options': ['Greeks', 'Romans', 'Egyptians', 'Mayans'],
                'answer': 'Egyptians'
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'John Adams'],
                'answer': 'George Washington'
            },
            {
                'question': 'Which event marked the start of World War I?',
                'options': ['Assassination of Archduke Franz Ferdinand', 'Invasion of Poland', 'Attack on Pearl Harbor', 'Fall of the Berlin Wall'],
                'answer': 'Assassination of Archduke Franz Ferdinand'
            }
        ]
    },
    'general': {
        'facts': [
            'The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and rises.',
            'A group of flamingos is called a flamboyance.',
            'The first product to have a barcode was Wrigley's gum.'
        ],
        'quizzes': [
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Arctic Ocean', 'Pacific Ocean', 'Indian Ocean'],
                'answer': 'Pacific Ocean'
            },
            {
                'question': 'Which country is known as the "Land of the Rising Sun"?',
                'options': ['China', 'Japan', 'South Korea', 'Thailand'],
                'answer': 'Japan'
            },
            {
                'question': 'What is the name of the tallest mammal?',
                'options': ['Elephant', 'Giraffe', 'Rhinoceros', 'Hippopotamus'],
                'answer': 'Giraffe'
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

def get_random_quiz(topic):
    """
    Retrieves a random quiz from the specified topic.
    """
    quizzes = topics[topic]['quizzes']
    quiz = random.choice(quizzes)
    return quiz

def run_quiz(quiz):
    """
    Executes the quiz and returns the result.
    """
    print(quiz['question'])
    for i, option in enumerate(quiz['options']):
        print(f"{i+1}. {option}")
    
    user_answer = input("Enter your answer (1-4): ")
    if quiz['options'][int(user_answer) - 1] == quiz['answer']:
        return True
    else:
        return False

def main():
    """
    Main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    chosen_topic = input("Enter your choice: ").lower()
    
    if chosen_topic in topics:
        print(f"Here's a random fact about {chosen_topic.capitalize()}:")
        print(get_random_fact(chosen_topic))
        
        print(f"\nNow, let's test your knowledge with a quiz on {chosen_topic.capitalize()}:")
        quiz = get_random_quiz(chosen_topic)
        
        if run_quiz(quiz):
            print("Congratulations! You got the answer correct.")
        else:
            print("Oops, that's not the right answer. Better luck next time!")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()