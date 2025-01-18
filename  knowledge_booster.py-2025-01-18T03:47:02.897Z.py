import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has over 60,000 miles of blood vessels.',
            'The hottest planet in the solar system is Venus, not Mercury.',
            'Chewing gum while peeling onions can help reduce tears.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the largest planet in our solar system?',
                'options': ['Jupiter', 'Saturn', 'Neptune', 'Uranus'],
                'answer': 0
            },
            {
                'question': 'Which element is the most abundant in the Earth\'s crust?',
                'options': ['Oxygen', 'Silicon', 'Aluminum', 'Iron'],
                'answer': 0
            },
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Evaporation', 'Combustion'],
                'answer': 0
            }
        ]
    },
    'technology': {
        'facts': [
            'The first electronic computer, ENIAC, weighed over 30 tons.',
            'The first commercial computer mouse was introduced in 1984.',
            'The first smartphone was the IBM Simon, released in 1992.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 2
            },
            {
                'question': 'What is the name of the popular search engine founded by Larry Page and Sergey Brin?',
                'options': ['Bing', 'Yahoo', 'Google', 'DuckDuckGo'],
                'answer': 2
            },
            {
                'question': 'What is the name of the social media platform that was launched in 2004 by Mark Zuckerberg?',
                'options': ['Twitter', 'Instagram', 'Facebook', 'Snapchat'],
                'answer': 2
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world.',
            'The Mona Lisa has no eyebrows, as it was the fashion in Renaissance Florence to shave them off.',
            'The first successful powered flight was made by the Wright brothers in 1903.'
        ],
        'quiz_questions': [
            {
                'question': 'Which ancient civilization is known for its pyramids?',
                'options': ['Aztec', 'Inca', 'Egyptian', 'Mesopotamian'],
                'answer': 2
            },
            {
                'question': 'What was the name of the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'Benjamin Franklin'],
                'answer': 2
            },
            {
                'question': 'Which event is considered the beginning of World War I?',
                'options': ['The assassination of Archduke Franz Ferdinand', 'The bombing of Pearl Harbor', 'The Cuban Missile Crisis', 'The fall of the Berlin Wall'],
                'answer': 0
            }
        ]
    },
    'general': {
        'facts': [
            'The largest known prime number as of 2021 has 23 million digits.',
            'The first person to circumnavigate the globe was Ferdinand Magellan, although he did not complete the journey himself.',
            'The Eiffel Tower can be 15 cm taller during the summer, as the iron heats up, expands, and raises the structure.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the largest organ in the human body?',
                'options': ['Heart', 'Liver', 'Skin', 'Lungs'],
                'answer': 2
            },
            {
                'question': 'What is the currency used in Japan?',
                'options': ['Yuan', 'Euro', 'Yen', 'Dollar'],
                'answer': 2
            },
            {
                'question': 'What is the name of the tallest mountain in the world?',
                'options': ['Mount Everest', 'K2', 'Kangchenjunga', 'Lhotse'],
                'answer': 0
            }
        ]
    }
}

def get_random_fact(topic):
    return random.choice(topics[topic]['facts'])

def get_quiz_question(topic):
    quiz_question = random.choice(topics[topic]['quiz_questions'])
    return quiz_question['question'], quiz_question['options'], quiz_question['answer']

def run_quiz(topic):
    score = 0
    num_questions = 3
    for _ in range(num_questions):
        question, options, answer = get_quiz_question(topic)
        print(question)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer - 1 == answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score is {score}/{num_questions}")

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Select a topic to get started:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    selected_topic = input("Enter your choice: ").lower()
    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()