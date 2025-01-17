
import random
import requests
import json

def get_fact(topic):
    """
    Fetches a random fact or concept from the chosen topic using a public API.
    """
    api_url = {
        "science": "https://api.api-ninjas.com/v1/facts?category=science",
        "technology": "https://api.api-ninjas.com/v1/facts?category=technology",
        "history": "https://api.api-ninjas.com/v1/facts?category=history",
        "general": "https://api.api-ninjas.com/v1/facts?category=general"
    }
    
    headers = {'X-Api-Key': 'YOUR_API_KEY_HERE'}
    response = requests.get(api_url[topic], headers=headers)
    
    if response.status_code == 200:
        facts = json.loads(response.text)
        return random.choice(facts)['fact']
    else:
        return "Error fetching fact."

def quiz(topic):
    """
    Provides a multiple-choice quiz for the chosen topic using a predefined database.
    """
    quiz_data = {
        "science": [
            {
                "question": "What is the largest planet in our solar system?",
                "choices": ["Jupiter", "Saturn", "Uranus", "Neptune"],
                "answer": 0
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "choices": ["Photosynthesis", "Respiration", "Transpiration", "Evaporation"],
                "answer": 0
            }
        ],
        "technology": [
            {
                "question": "What is the name of the programming language created by Guido van Rossum?",
                "choices": ["Java", "C++", "Python", "Ruby"],
                "answer": 2
            },
            {
                "question": "What is the name of the first commercially successful web browser?",
                "choices": ["Internet Explorer", "Netscape Navigator", "Mozilla Firefox", "Google Chrome"],
                "answer": 1
            }
        ],
        "history": [
            {
                "question": "In what year did the United States declare its independence?",
                "choices": ["1776", "1789", "1812", "1865"],
                "answer": 0
            },
            {
                "question": "Who was the first president of the United States?",
                "choices": ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "John Adams"],
                "answer": 2
            }
        ],
        "general": [
            {
                "question": "What is the largest mammal on Earth?",
                "choices": ["Elephant", "Giraffe", "Blue Whale", "Hippopotamus"],
                "answer": 2
            },
            {
                "question": "What is the capital city of Australia?",
                "choices": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
                "answer": 3
            }
        ]
    }
    
    questions = random.sample(quiz_data[topic], 2)
    score = 0
    
    for question in questions:
        print(question['question'])
        for i, choice in enumerate(question['choices']):
            print(f"{i+1}. {choice}")
        
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer - 1 == question['answer']:
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
    print("4. General")
    
    topic_choice = int(input("Enter your choice (1-4): "))
    
    topics = ["science", "technology", "history", "general"]
    chosen_topic = topics[topic_choice - 1]
    
    print(f"\nHere's a random fact about {chosen_topic}:")
    print(get_fact(chosen_topic))
    
    print("\nNow let's test your knowledge with a quiz!")
    quiz(chosen_topic)

if __name__ == "__main__":
    main()
