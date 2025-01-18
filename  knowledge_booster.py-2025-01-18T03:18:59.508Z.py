
import random
import requests
import json

def get_random_fact(topic):
    """Fetch a random fact or concept for the given topic using a public API."""
    api_url = {
        'science': 'https://api.api-ninjas.com/v1/facts?category=science',
        'technology': 'https://api.api-ninjas.com/v1/facts?category=technology',
        'history': 'https://api.api-ninjas.com/v1/facts?category=history',
        'general': 'https://api.api-ninjas.com/v1/facts?category=general'
    }
    
    headers = {'X-Api-Key': 'YOUR_API_KEY_HERE'}
    response = requests.get(api_url[topic], headers=headers)
    
    if response.status_code == 200:
        facts = json.loads(response.text)
        return random.choice(facts)['fact']
    else:
        return f"Error fetching {topic} fact: {response.status_code} - {response.text}"

def quiz(topic):
    """Provide a multiple-choice quiz for the given topic."""
    quiz_data = {
        'science': [
            {'question': 'What is the chemical symbol for gold?', 'answers': ['Au', 'Ag', 'Cu', 'Fe'], 'correct': 0},
            {'question': 'What is the largest planet in our solar system?', 'answers': ['Mars', 'Saturn', 'Jupiter', 'Neptune'], 'correct': 2},
            {'question': 'What is the process by which plants convert sunlight into energy?', 'answers': ['Photosynthesis', 'Respiration', 'Transpiration', 'Osmosis'], 'correct': 0}
        ],
        'technology': [
            {'question': 'What is the primary function of a computer processor (CPU)?', 'answers': ['Storing data', 'Displaying images', 'Processing information', 'Generating sound'], 'correct': 2},
            {'question': 'What is the name of the first commercially successful web browser?', 'answers': ['Internet Explorer', 'Google Chrome', 'Mozilla Firefox', 'Mosaic'], 'correct': 3},
            {'question': 'What is the name of the programming language used to create websites?', 'answers': ['Java', 'Python', 'C++', 'HTML'], 'correct': 3}
        ],
        'history': [
            {'question': 'What year was the Declaration of Independence signed?', 'answers': ['1776', '1789', '1812', '1865'], 'correct': 0},
            {'question': 'Who was the first president of the United States?', 'answers': ['Abraham Lincoln', 'Thomas Jefferson', 'George Washington', 'James Madison'], 'correct': 2},
            {'question': 'What was the name of the first successful powered flight?', 'answers': ['The Wright Flyer', 'The Kitty Hawk', 'The Biplane', 'The Glider'], 'correct': 0}
        ],
        'general': [
            {'question': 'What is the largest ocean on Earth?', 'answers': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'], 'correct': 3},
            {'question': 'What is the name of the tallest mammal?', 'answers': ['Elephant', 'Giraffe', 'Rhinoceros', 'Hippopotamus'], 'correct': 1},
            {'question': 'What is the capital city of Australia?', 'answers': ['Sydney', 'Melbourne', 'Brisbane', 'Canberra'], 'correct': 3}
        ]
    }
    
    questions = quiz_data[topic]
    score = 0
    
    for question in questions:
        print(question['question'])
        for i, answer in enumerate(question['answers']):
            print(f"{i+1}. {answer}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer - 1 == question['correct']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    
    print(f"Your final score: {score}/{len(questions)}")

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    print("1. Science")
    print("2. Technology")
    print("3. History")
    print("4. General Knowledge")
    
    topic_choice = int(input("Enter your choice (1-4): "))
    
    topics = ['science', 'technology', 'history', 'general']
    topic = topics[topic_choice - 1]
    
    print(f"You selected: {topic.capitalize()}")
    print(get_random_fact(topic))
    
    print("Now, let's test your knowledge with a quiz!")
    quiz(topic)

if __name__ == "__main__":
    main()
