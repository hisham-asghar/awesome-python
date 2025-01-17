
import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The Mona Lisa has no eyebrows. It was the fashion in Renaissance Florence to shave them off.',
            'The first product to have a barcode was Wrigley's gum.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Osmosis'],
                'answer': 'Photosynthesis'
            },
            {
                'question': 'Which scientist is known for developing the theory of relativity?',
                'options': ['Isaac Newton', 'Albert Einstein', 'Stephen Hawking', 'Galileo Galilei'],
                'answer': 'Albert Einstein'
            },
            {
                'question': 'What is the name of the largest planet in our solar system?',
                'options': ['Mars', 'Jupiter', 'Saturn', 'Venus'],
                'answer': 'Jupiter'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first electric car was built in Scotland in 1837.',
            'The first text message was sent on December 3, 1992.',
            'The first smartphone was the IBM Simon, released in 1992.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the software that allows computers to communicate with each other?',
                'options': ['Operating system', 'Web browser', 'Internet', 'Network protocol'],
                'answer': 'Network protocol'
            },
            {
                'question': 'Which company is known for creating the popular search engine Google?',
                'options': ['Apple', 'Microsoft', 'Amazon', 'Alphabet'],
                'answer': 'Alphabet'
            },
            {
                'question': 'What is the name of the process that allows computers to learn and improve from experience without being explicitly programmed?',
                'options': ['Artificial intelligence', 'Machine learning', 'Data mining', 'Natural language processing'],
                'answer': 'Machine learning'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The first computer bug was a real moth found trapped in a Harvard Mark II computer in 1947.',
            'The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and raises the structure.'
        ],
        'quiz_questions': [
            {
                'question': 'Which ancient civilization is known for building the pyramids?',
                'options': ['Mesopotamia', 'Indus Valley', 'Egypt', 'Aztec'],
                'answer': 'Egypt'
            },
            {
                'question': 'What was the name of the first successful powered flight, made by the Wright brothers?',
                'options': ['The Flyer', 'The Glider', 'The Biplane', 'The Monoplane'],
                'answer': 'The Flyer'
            },
            {
                'question': 'Which event marked the beginning of World War II?',
                'options': ['The assassination of Archduke Franz Ferdinand', 'The bombing of Pearl Harbor', 'The fall of the Berlin Wall', 'The Cuban Missile Crisis'],
                'answer': 'The assassination of Archduke Franz Ferdinand'
            }
        ]
    },
    'general': {
        'facts': [
            'The first product to have a barcode was Wrigley's gum.',
            'Apples are more effective at waking you up in the morning than coffee.',
            'The first person convicted of speeding was going 8 mph.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the largest organ in the human body?',
                'options': ['Heart', 'Liver', 'Skin', 'Brain'],
                'answer': 'Skin'
            },
            {
                'question': 'What is the name of the tallest land animal?',
                'options': ['Elephant', 'Giraffe', 'Rhinoceros', 'Hippopotamus'],
                'answer': 'Giraffe'
            },
            {
                'question': 'Which country is known as the "Land of the Rising Sun"?',
                'options': ['China', 'Japan', 'South Korea', 'India'],
                'answer': 'Japan'
            }
        ]
    }
}

def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    return input("Enter your choice: ").lower()

def display_fact(topic):
    fact = random.choice(topics[topic]['facts'])
    print(f"Here's a random fact about {topic.capitalize()}:")
    print(fact)

def quiz(topic):
    print(f"Let's test your {topic.capitalize()} knowledge!")
    score = 0
    for question in topics[topic]['quiz_questions']:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i+1}. {option}")
        user_answer = input("Enter your answer (1-4): ")
        if question['options'][int(user_answer)-1] == question['answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your score: {score}/{len(topics[topic]['quiz_questions'])}")

def main():
    topic = display_menu()
    display_fact(topic)
    quiz(topic)

if __name__ == "__main__":
    main()
