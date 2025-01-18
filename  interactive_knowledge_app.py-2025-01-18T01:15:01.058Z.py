import random
import json
import requests

# Define the topics and their associated facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The sun is about 93 million miles away from the Earth.',
            'Diamonds are the hardest known natural material on Earth.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the main component of the Earth\'s atmosphere?',
                'options': ['Nitrogen', 'Oxygen', 'Carbon dioxide', 'Argon'],
                'answer': 'Nitrogen'
            },
            {
                'question': 'Which organ in the human body produces insulin?',
                'options': ['Liver', 'Pancreas', 'Kidney', 'Thyroid'],
                'answer': 'Pancreas'
            },
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Osmosis'],
                'answer': 'Photosynthesis'
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer mouse was invented in 1964 by Douglas Engelbart.',
            'The first email was sent in 1971 by Ray Tomlinson.',
            'The World Wide Web was invented by Tim Berners-Lee in 1989.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the primary function of a CPU in a computer?',
                'options': ['Storing data', 'Displaying images', 'Processing information', 'Generating sound'],
                'answer': 'Processing information'
            },
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            },
            {
                'question': 'What is the purpose of a firewall in a computer network?',
                'options': ['To protect against unauthorized access', 'To increase internet speed', 'To store data', 'To connect devices'],
                'answer': 'To protect against unauthorized access'
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.',
            'The first Olympic Games were held in 776 BC in Olympia, Greece.',
            'The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci.'
        ],
        'quiz_questions': [
            {
                'question': 'In what year did the American Civil War begin?',
                'options': ['1861', '1776', '1945', '1939'],
                'answer': '1861'
            },
            {
                'question': 'Which ancient civilization is known for its pyramids?',
                'options': ['Greek', 'Roman', 'Egyptian', 'Mayan'],
                'answer': 'Egyptian'
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'George Washington', 'Thomas Jefferson', 'John Adams'],
                'answer': 'George Washington'
            }
        ]
    },
    'general': {
        'facts': [
            'The longest recorded flight of a chicken is 13 seconds.',
            'The first product to have a barcode was Wrigley's gum.',
            'The tallest mammal is the giraffe.'
        ],
        'quiz_questions': [
            {
                'question': 'What is the capital city of Australia?',
                'options': ['Sydney', 'Melbourne', 'Brisbane', 'Canberra'],
                'answer': 'Canberra'
            },
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Arctic Ocean', 'Indian Ocean', 'Pacific Ocean'],
                'answer': 'Pacific Ocean'
            },
            {
                'question': 'What is the name of the largest moon of Saturn?',
                'options': ['Titan', 'Callisto', 'Ganymede', 'Europa'],
                'answer': 'Titan'
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

def get_quiz_question(topic):
    """
    Retrieves a random quiz question and its options from the specified topic.
    """
    quiz_questions = topics[topic]['quiz_questions']
    question = random.choice(quiz_questions)
    return question

def run_quiz(topic):
    """
    Runs a quiz for the specified topic.
    """
    question = get_quiz_question(topic)
    print(question['question'])
    for i, option in enumerate(question['options']):
        print(f"{i+1}. {option}")
    user_answer = input("Enter your answer (1-4): ")
    if question['options'][int(user_answer)-1] == question['answer']:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {question['answer']}")

def main():
    """
    The main function that runs the interactive knowledge app.
    """
    print("Welcome to the Interactive Knowledge App!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")
    selected_topic = input("Enter your choice: ").lower()

    if selected_topic in topics:
        print(f"\nHere's a random fact about {selected_topic.capitalize()}:")
        print(get_random_fact(selected_topic))
        print("\nNow let's test your knowledge with a quiz!")
        run_quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()