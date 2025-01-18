import random
import requests
import json

# Define the topics and their corresponding facts and quiz questions
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The Milky Way galaxy contains an estimated 100 to 400 billion stars.',
            'The first vaccine was developed in 1796 to protect against smallpox.'
        ],
        'quiz': [
            {
                'question': 'What is the main function of the human heart?',
                'options': ['To pump blood', 'To filter waste', 'To produce oxygen'],
                'answer': 0
            },
            {
                'question': 'What is the name of the closest planet to the Sun?',
                'options': ['Venus', 'Mars', 'Mercury'],
                'answer': 2
            },
            {
                'question': 'Who is credited with the invention of the telephone?',
                'options': ['Thomas Edison', 'Alexander Graham Bell', 'Nikola Tesla'],
                'answer': 1
            }
        ]
    },
    'technology': {
        'facts': [
            'The first commercial computer, the UNIVAC I, was delivered to the U.S. Census Bureau in 1951.',
            'The World Wide Web was invented by Tim Berners-Lee in 1989.',
            'The first mobile phone call was made by Martin Cooper of Motorola in 1973.'
        ],
        'quiz': [
            {
                'question': 'What is the name of the operating system developed by Apple Inc.?',
                'options': ['Windows', 'macOS', 'Linux'],
                'answer': 1
            },
            {
                'question': 'Which company is known for the creation of the Android operating system?',
                'options': ['Apple', 'Microsoft', 'Google'],
                'answer': 2
            },
            {
                'question': 'What is the name of the first programmable computer?',
                'options': ['ENIAC', 'UNIVAC I', 'Z1'],
                'answer': 0
            }
        ]
    },
    'history': {
        'facts': [
            'The Great Pyramid of Giza in Egypt is the oldest and largest of the three pyramids in the Giza pyramid complex.',
            'The Gutenberg Bible, printed in the 15th century, was the first major book printed in the West using movable type.',
            'The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci.'
        ],
        'quiz': [
            {
                'question': 'In what year did the American Civil War begin?',
                'options': ['1861', '1776', '1945'],
                'answer': 0
            },
            {
                'question': 'Which ancient civilization is known for its advanced mathematics and astronomy?',
                'options': ['Egyptians', 'Greeks', 'Mayans'],
                'answer': 1
            },
            {
                'question': 'Who is considered the father of modern history?',
                'options': ['Herodotus', 'Thucydides', 'Plutarch'],
                'answer': 0
            }
        ]
    },
    'general': {
        'facts': [
            'The largest organ in the human body is the skin.',
            'The tallest mammal is the giraffe, which can grow up to 6 meters (20 feet) tall.',
            'The world's largest desert is the Sahara, covering an area of about 3.6 million square miles.'
        ],
        'quiz': [
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Pacific Ocean', 'Indian Ocean'],
                'answer': 1
            },
            {
                'question': 'Which country is known as the Land of the Rising Sun?',
                'options': ['China', 'Japan', 'South Korea'],
                'answer': 1
            },
            {
                'question': 'What is the rarest blood type?',
                'options': ['A', 'B', 'AB', 'O'],
                'answer': 3
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
    quiz = topics[topic]['quiz']
    question = random.choice(quiz)
    return question

def run_quiz(topic):
    """
    Runs a quiz for the specified topic.
    """
    question = get_quiz_question(topic)
    print(question['question'])
    for i, option in enumerate(question['options']):
        print(f"{i+1}. {option}")
    
    user_answer = int(input("Enter your answer (1-3): "))
    if user_answer == question['answer'] + 1:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is", question['options'][question['answer']])

def main():
    """
    Main function to run the interactive knowledge script.
    """
    print("Welcome to the Interactive Knowledge Script!")
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