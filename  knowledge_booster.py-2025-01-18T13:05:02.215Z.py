import random
import requests
import json

def get_topic_menu():
    return {
        '1': 'Science',
        '2': 'Technology',
        '3': 'History',
        '4': 'General Knowledge'
    }

def get_science_fact():
    url = 'https://api.api-ninjas.com/v1/facts?category=science'
    response = requests.get(url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    if response.status_code == requests.codes.ok:
        fact = response.json()[0]['fact']
        return fact
    else:
        return 'Error fetching science fact.'

def get_tech_fact():
    url = 'https://api.api-ninjas.com/v1/facts?category=technology'
    response = requests.get(url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    if response.status_code == requests.codes.ok:
        fact = response.json()[0]['fact']
        return fact
    else:
        return 'Error fetching technology fact.'

def get_history_fact():
    url = 'https://api.api-ninjas.com/v1/facts?category=history'
    response = requests.get(url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    if response.status_code == requests.codes.ok:
        fact = response.json()[0]['fact']
        return fact
    else:
        return 'Error fetching history fact.'

def get_general_knowledge_fact():
    url = 'https://api.api-ninjas.com/v1/facts?category=general'
    response = requests.get(url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    if response.status_code == requests.codes.ok:
        fact = response.json()[0]['fact']
        return fact
    else:
        return 'Error fetching general knowledge fact.'

def get_quiz_questions(topic):
    quiz_questions = {
        'Science': [
            {'question': 'What is the chemical symbol for gold?', 'options': ['Au', 'Ag', 'Cu', 'Fe'], 'answer': 0},
            {'question': 'What is the largest planet in our solar system?', 'options': ['Earth', 'Mars', 'Jupiter', 'Saturn'], 'answer': 2},
            {'question': 'What is the process by which plants convert light energy into chemical energy?', 'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Evaporation'], 'answer': 0}
        ],
        'Technology': [
            {'question': 'What is the name of the first commercially successful web browser?', 'options': ['Firefox', 'Chrome', 'Internet Explorer', 'Mosaic'], 'answer': 3},
            {'question': 'What is the name of the programming language used to create the Python programming language?', 'options': ['C', 'Java', 'C++', 'C#'], 'answer': 0},
            {'question': 'What is the name of the device that converts digital signals into analog signals?', 'options': ['Modem', 'Router', 'Switch', 'Amplifier'], 'answer': 0}
        ],
        'History': [
            {'question': 'In what year did the American Civil War begin?', 'options': ['1861', '1865', '1914', '1939'], 'answer': 0},
            {'question': 'Who was the first president of the United States?', 'options': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'John Adams'], 'answer': 2},
            {'question': 'What was the name of the ancient Egyptian queen who was famous for her beauty?', 'options': ['Cleopatra', 'Nefertiti', 'Hatshepsut', 'Neferkare'], 'answer': 0}
        ],
        'General Knowledge': [
            {'question': 'What is the largest mammal in the world?', 'options': ['Elephant', 'Blue Whale', 'Sperm Whale', 'Hippopotamus'], 'answer': 1},
            {'question': 'What is the capital city of Australia?', 'options': ['Sydney', 'Melbourne', 'Brisbane', 'Canberra'], 'answer': 3},
            {'question': 'What is the name of the longest river in the world?', 'options': ['Amazon River', 'Nile River', 'Mississippi River', 'Yangtze River'], 'answer': 1}
        ]
    }
    return quiz_questions[topic]

def run_quiz(topic):
    quiz_questions = get_quiz_questions(topic)
    score = 0
    for question in quiz_questions:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer - 1 == question['answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score is {score} out of {len(quiz_questions)}.")

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    topic_menu = get_topic_menu()
    for key, value in topic_menu.items():
        print(f"{key}. {value}")
    
    topic_choice = input("Enter your choice (1-4): ")
    
    if topic_choice == '1':
        print("Random science fact:", get_science_fact())
        run_quiz('Science')
    elif topic_choice == '2':
        print("Random technology fact:", get_tech_fact())
        run_quiz('Technology')
    elif topic_choice == '3':
        print("Random history fact:", get_history_fact())
        run_quiz('History')
    elif topic_choice == '4':
        print("Random general knowledge fact:", get_general_knowledge_fact())
        run_quiz('General Knowledge')
    else:
        print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()