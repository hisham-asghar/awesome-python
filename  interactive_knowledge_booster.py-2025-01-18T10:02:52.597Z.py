
import random
import requests
import json

# Define the topics and their corresponding API endpoints
topics = {
    '1. Science': 'https://api.api-ninjas.com/v1/facts?category=science',
    '2. Technology': 'https://api.api-ninjas.com/v1/facts?category=technology',
    '3. History': 'https://api.api-ninjas.com/v1/facts?category=history',
    '4. General Knowledge': 'https://api.api-ninjas.com/v1/trivia'
}

# API key for API-Ninjas
api_key = 'YOUR_API_KEY_HERE'

def get_fact(topic):
    """
    Fetches a random fact or trivia from the selected topic using the API-Ninjas API.
    """
    url = topics[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    
    if topic == '4. General Knowledge':
        return data[0]['question'], data[0]['answer']
    else:
        return data[0]['fact']

def quiz(topic):
    """
    Provides a multiple-choice quiz for the selected topic.
    """
    url = topics[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    
    if topic == '4. General Knowledge':
        question, answer = data[0]['question'], data[0]['answer']
        options = data[0]['options']
        print(question)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        
        user_answer = int(input("Enter your answer (1-4): "))
        if options[user_answer-1] == answer:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {answer}")
    else:
        fact = data[0]['fact']
        print(fact)
        
        # Add a multiple-choice quiz for the fact
        # (code omitted for brevity)

def main():
    """
    Main function that displays the menu, allows the user to select a topic, and provides the corresponding fact or quiz.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    
    for topic in topics:
        print(topic)
    
    choice = input("Enter the number of the topic (1-4): ")
    
    if choice == '1':
        fact = get_fact('1. Science')
        print(f"Random Science Fact: {fact}")
    elif choice == '2':
        fact = get_fact('2. Technology')
        print(f"Random Technology Fact: {fact}")
    elif choice == '3':
        fact = get_fact('3. History')
        print(f"Random History Fact: {fact}")
    elif choice == '4':
        quiz('4. General Knowledge')
    else:
        print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
