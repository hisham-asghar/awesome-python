
import random
import requests
import json

# Define topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The hottest planet in the solar system is Venus, not Mercury.',
            'The largest known prime number has over 23 million digits.'
        ],
        'quiz': [
            {
                'question': 'What is the name of the closest planet to the Sun?',
                'options': ['Venus', 'Earth', 'Mercury', 'Mars'],
                'answer': 'Mercury'
            },
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Fermentation'],
                'answer': 'Photosynthesis'
            },
            {
                'question': 'What is the name of the force that attracts objects with mass towards each other?',
                'options': ['Gravity', 'Friction', 'Magnetism', 'Electricity'],
                'answer': 'Gravity'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first electronic computer, ENIAC, was the size of a large room and weighed 30 tons.',
            'The first smartphone was the IBM Simon, released in 1992.',
            'The internet was originally called ARPANET and was created by the US Department of Defense.'
        ],
        'quiz': [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            },
            {
                'question': 'What is the name of the search engine created by Larry Page and Sergey Brin?',
                'options': ['Bing', 'Yahoo', 'Google', 'DuckDuckGo'],
                'answer': 'Google'
            },
            {
                'question': 'What is the name of the company that created the first personal computer, the Apple I?',
                'options': ['Microsoft', 'IBM', 'Apple', 'HP'],
                'answer': 'Apple'
            }
        ]
    },
    'history': {
        'facts': [
            'The first successful powered flight took place in 1903, piloted by the Wright brothers.',
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The ancient Egyptian civilization lasted for over 3,000 years.'
        ],
        'quiz': [
            {
                'question': 'What was the name of the first successful powered flight?',
                'options': ['The Wright Flyer', 'The Kitty Hawk', 'The Spirit of St. Louis', 'The Bleriot XI'],
                'answer': 'The Wright Flyer'
            },
            {
                'question': 'What was the name of the ancient Egyptian pharaoh who built the Great Pyramid of Giza?',
                'options': ['Cleopatra', 'Tutankhamun', 'Ramses II', 'Khufu'],
                'answer': 'Khufu'
            },
            {
                'question': 'What was the name of the first permanent English settlement in North America?',
                'options': ['Jamestown', 'Plymouth Colony', 'Massachusetts Bay Colony', 'New Amsterdam'],
                'answer': 'Jamestown'
            }
        ]
    },
    'general': {
        'facts': [
            'The largest known prime number has over 23 million digits.',
            'The tallest mammal is the giraffe, which can grow up to 18 feet tall.',
            'The world's largest desert is Antarctica, not the Sahara.'
        ],
        'quiz': [
            {
                'question': 'What is the name of the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Pacific Ocean', 'Indian Ocean', 'Arctic Ocean'],
                'answer': 'Pacific Ocean'
            },
            {
                'question': 'What is the name of the largest moon of Saturn?',
                'options': ['Titan', 'Ganymede', 'Callisto', 'Europa'],
                'answer': 'Titan'
            },
            {
                'question': 'What is the name of the largest country in the world by land area?',
                'options': ['Russia', 'Canada', 'China', 'United States'],
                'answer': 'Russia'
            }
        ]
    }
}

def get_random_fact(topic):
    """
    Retrieves a random fact from the specified topic.
    """
    return random.choice(topics[topic]['facts'])

def get_quiz_question(topic):
    """
    Retrieves a random quiz question from the specified topic.
    """
    return random.choice(topics[topic]['quiz'])

def run_quiz(topic):
    """
    Runs a quiz for the specified topic.
    """
    question = get_quiz_question(topic)
    print(f"Question: {question['question']}")
    for i, option in enumerate(question['options']):
        print(f"{i+1}. {option}")
    user_answer = input("Enter your answer (1-4): ")
    if user_answer.strip() == str(question['options'].index(question['answer']) + 1):
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {question['answer']}.")

def main():
    """
    Main function that runs the interactive knowledge-building script.
    """
    print("Welcome to the Interactive Knowledge Builder!")
    while True:
        print("\nSelect a topic:")
        for i, topic in enumerate(topics):
            print(f"{i+1}. {topic.capitalize()}")
        print("0. Exit")
        choice = input("Enter your choice (0-4): ")
        if choice == '0':
            print("Goodbye!")
            break
        elif int(choice) in range(1, len(topics) + 1):
            topic = list(topics)[int(choice) - 1]
            print(f"\nFact about {topic.capitalize()}: {get_random_fact(topic)}")
            run_quiz(topic)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
