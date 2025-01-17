import random
import json
import requests

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The Milky Way galaxy contains an estimated 100-400 billion stars.',
            'The first successful vaccine was developed by Edward Jenner in 1796 to prevent smallpox.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the scientist who developed the first successful vaccine?',
                'options': ['Louis Pasteur', 'Alexander Fleming', 'Edward Jenner', 'Marie Curie'],
                'answer': 'Edward Jenner'
            },
            {
                'question': 'Approximately how many stars are in the Milky Way galaxy?',
                'options': ['10 million', '100 million', '100-400 billion', '1 trillion'],
                'answer': '100-400 billion'
            },
            {
                'question': 'How many miles of blood vessels are in the human body?',
                'options': ['10,000 miles', '30,000 miles', '60,000 miles', '100,000 miles'],
                'answer': '60,000 miles'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer mouse was invented by Douglas Engelbart in 1964.',
            'The internet was initially created as ARPANET in 1969 by the U.S. Department of Defense.',
            'The first smartphone was the IBM Simon, released in 1992.'
        ],
        'quiz_questions': [
            {
                'question': 'Who invented the first computer mouse?',
                'options': ['Steve Jobs', 'Bill Gates', 'Douglas Engelbart', 'Tim Berners-Lee'],
                'answer': 'Douglas Engelbart'
            },
            {
                'question': 'What was the original name of the internet?',
                'options': ['WWW', 'ARPANET', 'TCP/IP', 'HTTP'],
                'answer': 'ARPANET'
            },
            {
                'question': 'What was the first smartphone?',
                'options': ['iPhone', 'Android', 'Blackberry', 'IBM Simon'],
                'answer': 'IBM Simon'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The first Olympic Games were held in 776 BC in Olympia, Greece.',
            'The Mona Lisa was painted by Leonardo da Vinci between 1503 and 1519.'
        ],
        'quiz_questions': [
            {
                'question': 'How long is the Great Wall of China?',
                'options': ['5,000 miles', '10,000 miles', '13,000 miles', '20,000 miles'],
                'answer': '13,000 miles'
            },
            {
                'question': 'When were the first Olympic Games held?',
                'options': ['500 BC', '776 BC', '1896 AD', '2000 AD'],
                'answer': '776 BC'
            },
            {
                'question': 'Who painted the Mona Lisa?',
                'options': ['Michelangelo', 'Pablo Picasso', 'Vincent van Gogh', 'Leonardo da Vinci'],
                'answer': 'Leonardo da Vinci'
            }
        ]
    },
    'general_knowledge': {
        'facts': [
            'The largest organ in the human body is the skin.',
            'The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.',
            'The largest planet in our solar system is Jupiter.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the largest organ in the human body?',
                'options': ['Heart', 'Liver', 'Lungs', 'Skin'],
                'answer': 'Skin'
            },
            {
                'question': 'What is the tallest mammal?',
                'options': ['Elephant', 'Rhinoceros', 'Giraffe', 'Hippopotamus'],
                'answer': 'Giraffe'
            },
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Saturn', 'Jupiter', 'Neptune', 'Uranus'],
                'answer': 'Jupiter'
            }
        ]
    }
}

def get_random_fact(topic):
    facts = topics[topic]['facts']
    return random.choice(facts)

def quiz(topic):
    questions = topics[topic]['quiz_questions']
    score = 0
    for question in questions:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if question['options'][user_answer-1] == question['answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", question['answer'])
    print(f"Your final score is: {score}/{len(questions)}")

def main():
    print("Welcome to the Interactive Knowledge Builder!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    
    if selected_topic in topics:
        print(f"\nRandom fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nTime for a quiz!")
        quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()