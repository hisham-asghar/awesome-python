import random
import requests
import json

# Define topics and associated facts/quizzes
topics = {
    'science': {
        'facts': [
            'The human body has around 60,000 miles of blood vessels.',
            'The hottest planet in the Solar System is Venus, not Mercury.',
            'A group of flamingos is called a flamboyance.'
        ],
        'quizzes': [
            {
                'question': 'What is the main function of the human heart?',
                'options': ['to pump blood', 'to filter waste', 'to produce hormones', 'to absorb oxygen'],
                'answer': 0
            },
            {
                'question': 'Which of these is not a state of matter?',
                'options': ['solid', 'liquid', 'gas', 'plasma', 'energy'],
                'answer': 4
            },
            {
                'question': 'What is the name of the largest moon of Saturn?',
                'options': ['Titan', 'Ganymede', 'Callisto', 'Io'],
                'answer': 0
            }
        ]
    },
    'technology': {
        'facts': [
            'The first computer virus, called \"Brain\", was created in 1986.',
            'The first smartphone was the IBM Simon, released in 1992.',
            'The largest hard drive ever produced had a capacity of 60 TB.'
        ],
        'quizzes': [
            {
                'question': 'What does "HTML" stand for?',
                'options': ['Hyper Text Markup Language', 'High-level Text Markup Language', 'Hyperlink Text Markup Language', 'Hyper Text Machine Language'],
                'answer': 0
            },
            {
                'question': 'Which company developed the Android operating system?',
                'options': ['Apple', 'Microsoft', 'Google', 'Samsung'],
                'answer': 2
            },
            {
                'question': 'What is the name of the programming language used to build websites?',
                'options': ['Java', 'Python', 'C++', 'JavaScript'],
                'answer': 3
            }
        ]
    },
    'history': {
        'facts': [
            'The first successful powered flight was made by the Wright brothers in 1903.',
            'The Great Wall of China is the longest man-made structure in the world.',
            'The Mona Lisa was painted by the famous artist Leonardo da Vinci.'
        ],
        'quizzes': [
            {
                'question': 'What year did the American Civil War begin?',
                'options': ['1861', '1865', '1914', '1939'],
                'answer': 0
            },
            {
                'question': 'Which ancient civilization built the Pyramids of Giza?',
                'options': ['Aztecs', 'Incas', 'Egyptians', 'Romans'],
                'answer': 2
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'John Adams'],
                'answer': 2
            }
        ]
    },
    'general': {
        'facts': [
            'The largest organ in the human body is the skin.',
            'A group of crows is called a murder.',
            'The largest mammal in the world is the blue whale.'
        ],
        'quizzes': [
            {
                'question': 'What is the tallest building in the world?',
                'options': ['Burj Khalifa', 'Empire State Building', 'Petronas Towers', 'Shanghai Tower'],
                'answer': 0
            },
            {
                'question': 'What is the name of the longest river in the world?',
                'options': ['Nile River', 'Amazon River', 'Mississippi River', 'Yangtze River'],
                'answer': 0
            },
            {
                'question': 'What is the currency used in Japan?',
                'options': ['Dollar', 'Euro', 'Yen', 'Pound'],
                'answer': 2
            }
        ]
    }
}

def get_random_fact(topic):
    return random.choice(topics[topic]['facts'])

def get_quiz(topic):
    quiz = random.choice(topics[topic]['quizzes'])
    return quiz

def run_quiz(quiz):
    print(quiz['question'])
    for i, option in enumerate(quiz['options']):
        print(f"{i+1}. {option}")
    
    user_answer = int(input("Enter your answer (1-4): ")) - 1
    if user_answer == quiz['answer']:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", quiz['options'][quiz['answer']])

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic.capitalize()}")
    
    chosen_topic = input("Enter your choice: ").lower()
    
    if chosen_topic in topics:
        print("\nHere's a random fact about", chosen_topic.capitalize() + ":")
        print(get_random_fact(chosen_topic))
        
        print("\nNow, let's test your knowledge with a quiz!")
        quiz = get_quiz(chosen_topic)
        run_quiz(quiz)
    else:
        print("Invalid topic. Please try again.")

if __name__ == '__main__':
    main()