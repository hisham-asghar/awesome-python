
import random
import requests
import json

# Define the topics and their corresponding APIs or data sources
topics = {
    '1': 'Science',
    '2': 'Technology',
    '3': 'History',
    '4': 'General Knowledge'
}

# Function to display a random fact or concept from the selected topic
def display_fact(topic):
    if topic == '1':  # Science
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=science', headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    elif topic == '2':  # Technology
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=technology', headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    elif topic == '3':  # History
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=history', headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    elif topic == '4':  # General Knowledge
        response = requests.get('https://api.api-ninjas.com/v1/facts?category=general', headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    else:
        return "Invalid topic selection."

    if response.status_code == 200:
        facts = json.loads(response.text)
        random_fact = random.choice(facts)
        return random_fact['fact']
    else:
        return "Error fetching fact."

# Function to display the quiz questions and handle user responses
def quiz(topic):
    if topic == '1':  # Science
        questions = [
            {
                'question': 'What is the chemical symbol for gold?',
                'options': ['Au', 'Ag', 'Cu', 'Fe'],
                'answer': 'Au'
            },
            {
                'question': 'What is the largest planet in our solar system?',
                'options': ['Mars', 'Saturn', 'Jupiter', 'Neptune'],
                'answer': 'Jupiter'
            },
            {
                'question': 'What is the process by which plants convert sunlight into energy?',
                'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Evaporation'],
                'answer': 'Photosynthesis'
            }
        ]
    elif topic == '2':  # Technology
        questions = [
            {
                'question': 'What is the name of the programming language created by Guido van Rossum?',
                'options': ['Java', 'C++', 'Python', 'Ruby'],
                'answer': 'Python'
            },
            {
                'question': 'What is the name of the first commercially successful web browser?',
                'options': ['Netscape Navigator', 'Internet Explorer', 'Mozilla Firefox', 'Google Chrome'],
                'answer': 'Netscape Navigator'
            },
            {
                'question': 'What is the name of the technology that allows devices to communicate wirelessly?',
                'options': ['Bluetooth', 'Wi-Fi', 'Ethernet', 'Cellular'],
                'answer': 'Bluetooth'
            }
        ]
    elif topic == '3':  # History
        questions = [
            {
                'question': 'What year did the American Civil War begin?',
                'options': ['1861', '1865', '1775', '1914'],
                'answer': '1861'
            },
            {
                'question': 'Who was the first president of the United States?',
                'options': ['Abraham Lincoln', 'George Washington', 'Thomas Jefferson', 'John Adams'],
                'answer': 'George Washington'
            },
            {
                'question': 'What was the name of the ancient civilization that built the pyramids?',
                'options': ['Mesopotamia', 'Aztec', 'Inca', 'Ancient Egypt'],
                'answer': 'Ancient Egypt'
            }
        ]
    elif topic == '4':  # General Knowledge
        questions = [
            {
                'question': 'What is the largest ocean on Earth?',
                'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
                'answer': 'Pacific Ocean'
            },
            {
                'question': 'What is the tallest mammal in the world?',
                'options': ['African Elephant', 'Giraffe', 'Hippopotamus', 'Rhinoceros'],
                'answer': 'Giraffe'
            },
            {
                'question': 'What is the capital city of Australia?',
                'options': ['Sydney', 'Melbourne', 'Brisbane', 'Canberra'],
                'answer': 'Canberra'
            }
        ]
    else:
        return "Invalid topic selection."

    score = 0
    for question in questions:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i+1}. {option}")
        user_answer = input("Enter your answer (1-4): ")
        if user_answer == question['answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    return f"Your score: {score}/{len(questions)}"

# Main function to display the menu and handle user interactions
def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic_id, topic_name in topics.items():
        print(f"{topic_id}. {topic_name}")

    topic_choice = input("Enter the topic number (1-4): ")
    if topic_choice in topics:
        print(f"You selected: {topics[topic_choice]}")
        print(display_fact(topic_choice))
        print(quiz(topic_choice))
    else:
        print("Invalid topic selection. Please try again.")

if __name__ == "__main__":
    main()
