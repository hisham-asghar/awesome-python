
import random
import requests
import json

# Define the topics and their corresponding API endpoints
topics = {
    '1': 'Science',
    '2': 'Technology',
    '3': 'History',
    '4': 'General Knowledge'
}

def get_random_fact(topic):
    """
    Fetch a random fact or concept from the corresponding API endpoint.
    """
    if topic == '1':
        # Science API endpoint
        response = requests.get('https://api.api-ninjas.com/v1/science', headers={'X-Api-Key': 'YOUR_API_KEY'})
    elif topic == '2':
        # Technology API endpoint
        response = requests.get('https://api.api-ninjas.com/v1/technology', headers={'X-Api-Key': 'YOUR_API_KEY'})
    elif topic == '3':
        # History API endpoint
        response = requests.get('https://api.api-ninjas.com/v1/history', headers={'X-Api-Key': 'YOUR_API_KEY'})
    elif topic == '4':
        # General Knowledge API endpoint
        response = requests.get('https://api.api-ninjas.com/v1/trivia', headers={'X-Api-Key': 'YOUR_API_KEY'})
    else:
        return "Invalid topic selection."

    if response.status_code == 200:
        data = response.json()
        return data[0]['fact']
    else:
        return "Error fetching data."

def quiz(topic):
    """
    Provide a multiple-choice quiz for the selected topic.
    """
    if topic == '1':
        # Science quiz questions and answers
        questions = [
            {"question": "What is the chemical symbol for gold?", "answers": ["Au", "Ag", "Cu", "Fe"], "correct": 0},
            {"question": "What is the process by which plants convert sunlight into energy?", "answers": ["Respiration", "Photosynthesis", "Evaporation", "Transpiration"], "correct": 1},
            {"question": "What is the name of the closest planet to the Sun?", "answers": ["Venus", "Mars", "Mercury", "Earth"], "correct": 2}
        ]
    elif topic == '2':
        # Technology quiz questions and answers
        questions = [
            {"question": "What is the name of the first computer programmer?", "answers": ["Ada Lovelace", "Charles Babbage", "Alan Turing", "Steve Jobs"], "correct": 0},
            {"question": "What is the name of the operating system developed by Apple?", "answers": ["Windows", "Linux", "macOS", "Android"], "correct": 2},
            {"question": "What is the name of the programming language used to create websites?", "answers": ["Java", "Python", "C++", "HTML"], "correct": 3}
        ]
    elif topic == '3':
        # History quiz questions and answers
        questions = [
            {"question": "In what year did the American Civil War begin?", "answers": ["1861", "1865", "1914", "1939"], "correct": 0},
            {"question": "Who was the first president of the United States?", "answers": ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "James Madison"], "correct": 1},
            {"question": "What was the name of the first successful powered flight?", "answers": ["Wright Flyer", "Concorde", "Sputnik", "Apollo 11"], "correct": 0}
        ]
    elif topic == '4':
        # General Knowledge quiz questions and answers
        questions = [
            {"question": "What is the capital city of Australia?", "answers": ["Sydney", "Melbourne", "Brisbane", "Canberra"], "correct": 3},
            {"question": "What is the largest ocean on Earth?", "answers": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "correct": 3},
            {"question": "Who wrote the novel 'To Kill a Mockingbird'?", "answers": ["Ernest Hemingway", "F. Scott Fitzgerald", "Harper Lee", "Maya Angelou"], "correct": 2}
        ]
    else:
        return "Invalid topic selection."

    # Randomly select a question from the list
    question = random.choice(questions)

    # Print the question and answers
    print(question["question"])
    for i, answer in enumerate(question["answers"]):
        print(f"{i+1}. {answer}")

    # Get the user's answer
    user_answer = int(input("Enter your answer (1-4): "))

    # Check if the user's answer is correct
    if user_answer - 1 == question["correct"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is", question["answers"][question["correct"]])

def main():
    """
    Main function to display the menu and handle user interactions.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for key, value in topics.items():
        print(f"{key}. {value}")

    topic = input("Enter the number of the topic (1-4): ")

    if topic in topics:
        print(get_random_fact(topic))
        quiz(topic)
    else:
        print("Invalid topic selection.")

if __name__ == "__main__":
    main()
