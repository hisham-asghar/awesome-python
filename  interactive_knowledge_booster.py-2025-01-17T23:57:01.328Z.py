import random
import requests
import json

# Define the topics and their corresponding facts and quizzes
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The hottest planet in the solar system is Venus, not Mercury.',
            'The largest known prime number as of 2022 has 23 million digits.'
        ],
        'quizzes': [
            {
                'question': 'What is the name of the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Evaporation', 'Transpiration'],
                'answer': 'Photosynthesis'
            },
            {
                'question': 'Which scientist is known for developing the theory of relativity?',
                'options': ['Isaac Newton', 'Albert Einstein', 'Stephen Hawking', 'Marie Curie'],
                'answer': 'Albert Einstein'
            },
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer mouse was invented in 1964 by Douglas Engelbart.',
            'The largest hard drive ever produced had a capacity of 60 TB.',
            'The first commercial microprocessor was the Intel 4004, released in 1971.'
        ],
        'quizzes': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            },
            {
                'question': 'Which company is known for creating the Android operating system?',
                'options': ['Apple', 'Microsoft', 'Google', 'Samsung'],
                'answer': 'Google'
            },
            {
                'question': 'What is the name of the device that converts digital signals into analog signals?',
                'options': ['Modem', 'Printer', 'Scanner', 'Router'],
                'answer': 'Modem'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world.',
            'The Mona Lisa was painted by the Italian artist Leonardo da Vinci.',
            'The first successful powered flight was made by the Wright brothers in 1903.'
        ],
        'quizzes': [
            {
                'question': 'In what year did the American Civil War begin?',
                'options': ['1861', '1865', '1914', '1939'],
                'answer': '1861'
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Thomas Jefferson', 'Abraham Lincoln', 'George Washington', 'John Adams'],
                'answer': 'George Washington'
            },
            {
                'question': 'What was the name of the ancient Egyptian civilization that built the pyramids?',
                'options': ['Mesopotamia', 'Aztec', 'Inca', 'Ancient Egypt'],
                'answer': 'Ancient Egypt'
            }
        ]
    },
    'general_knowledge': {
        'facts': [
            'The largest ocean on Earth is the Pacific Ocean.',
            'The highest mountain in the world is Mount Everest.',
            'The longest river in the world is the Nile River.'
        ],
        'quizzes': [
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
                'answer': 'Jupiter'
            },
            {
                'question': 'What is the capital city of Australia?',
                'options': ['Sydney', 'Melbourne', 'Brisbane', 'Canberra'],
                'answer': 'Canberra'
            },
            {
                'question': 'What is the name of the largest mammal on Earth?',
                'options': ['Elephant', 'Whale', 'Giraffe', 'Hippopotamus'],
                'answer': 'Whale'
            }
        ]
    }
}

def get_random_fact(topic):
    facts = topics[topic]['facts']
    return random.choice(facts)

def get_random_quiz(topic):
    quizzes = topics[topic]['quizzes']
    quiz = random.choice(quizzes)
    return quiz

def run_quiz(quiz):
    print(quiz['question'])
    for i, option in enumerate(quiz['options']):
        print(f"{i+1}. {option}")
    
    user_answer = input("Enter the number of your answer: ")
    if quiz['options'][int(user_answer)-1] == quiz['answer']:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {quiz['answer']}")

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
        quiz = get_random_quiz(selected_topic)
        run_quiz(quiz)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()