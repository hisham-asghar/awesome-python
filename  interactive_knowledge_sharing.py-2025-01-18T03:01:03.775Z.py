import random
import requests
import json

# Define the topics and their associated facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has over 600 muscles.',
            'The first digital computer was the ENIAC, which was completed in 1946.',
            'The largest known prime number as of 2022 has 23 million digits.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Hg'],
                'answer': 'Au'
            },
            {
                'question': 'What is the name of the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Osmosis'],
                'answer': 'Photosynthesis'
            },
            {
                'question': 'Which scientist is credited with developing the theory of relativity?',
                'options': ['Isaac Newton', 'Albert Einstein', 'Stephen Hawking', 'Galileo Galilei'],
                'answer': 'Albert Einstein'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.',
            'The internet was initially developed as a military project called ARPANET in the 1960s.',
            'The first smartphone, the IBM Simon, was introduced in 1992.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            },
            {
                'question': 'Which company is credited with creating the first commercially successful personal computer?',
                'options': ['Apple', 'IBM', 'Microsoft', 'Dell'],
                'answer': 'IBM'
            },
            {
                'question': 'What is the name of the process by which computers encode and decode data?',
                'options': ['Encryption', 'Compression', 'Rendering', 'Parsing'],
                'answer': 'Encryption'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The Mona Lisa was painted by Leonardo da Vinci between 1503 and 1519.',
            'The first Olympic Games were held in ancient Greece in 776 BC.'
        ],
        'quiz_questions': [
            {
                'question': 'Which ancient civilization is known for its pyramids?',
                'options': ['Mesopotamia', 'Indus Valley', 'Egypt', 'Maya'],
                'answer': 'Egypt'
            },
            {
                'question': 'What was the name of the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'John Adams'],
                'answer': 'George Washington'
            },
            {
                'question': 'What event marked the beginning of World War I?',
                'options': ['The assassination of Archduke Franz Ferdinand', 'The attack on Pearl Harbor', 'The dropping of the atomic bomb', 'The fall of the Berlin Wall'],
                'answer': 'The assassination of Archduke Franz Ferdinand'
            }
        ]
    },
    'general': {
        'facts': [
            'The largest known prime number as of 2022 has 23 million digits.',
            'The world's largest desert is Antarctica, which is a desert because of its low precipitation.',
            'The first commercial airline flight took place on January 1, 1914, between St. Petersburg and Tampa, Florida.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
                'answer': 'Jupiter'
            },
            {
                'question': 'What is the tallest mammal in the world?',
                'options': ['Elephant', 'Giraffe', 'Rhinoceros', 'Hippopotamus'],
                'answer': 'Giraffe'
            },
            {
                'question': 'What is the name of the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Arctic Ocean', 'Indian Ocean', 'Pacific Ocean'],
                'answer': 'Pacific Ocean'
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
    quiz_question = random.choice(topics[topic]['quiz_questions'])
    return quiz_question

def run_quiz(topic):
    """
    Runs a quiz for the selected topic.
    """
    quiz_question = get_quiz_question(topic)
    print(quiz_question['question'])
    for i, option in enumerate(quiz_question['options']):
        print(f"{i+1}. {option}")
    
    user_answer = input("Enter your answer (1-4): ")
    if quiz_question['options'][int(user_answer)-1] == quiz_question['answer']:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz_question['answer'])

def main():
    """
    Main function that runs the interactive knowledge-sharing program.
    """
    print("Welcome to the Interactive Knowledge-Sharing Program!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print("\nHere's a random fact about", selected_topic.capitalize() + ":")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()