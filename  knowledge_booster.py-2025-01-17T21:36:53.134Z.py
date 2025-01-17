
import random
import requests
import json

# Define the topics and their corresponding API endpoints
topics = {
    "Science": "https://api.publicapis.org/entries?category=science",
    "Technology": "https://api.publicapis.org/entries?category=technology",
    "History": "https://api.publicapis.org/entries?category=history",
    "General Knowledge": "https://api.publicapis.org/entries?category=general"
}

def get_random_fact(topic):
    """
    Fetches a random fact or concept from the chosen topic using a public API.
    """
    api_url = topics[topic]
    response = requests.get(api_url)
    data = json.loads(response.text)
    random_fact = random.choice(data['entries'])
    return random_fact['Description']

def quiz_question(topic):
    """
    Generates a multiple-choice quiz question for the chosen topic.
    """
    api_url = topics[topic]
    response = requests.get(api_url)
    data = json.loads(response.text)
    random_entry = random.choice(data['entries'])
    
    # Generate 4 multiple-choice options
    options = [random_entry['Description']]
    for i in range(3):
        other_entry = random.choice(data['entries'])
        while other_entry['Description'] in options:
            other_entry = random.choice(data['entries'])
        options.append(other_entry['Description'])
    random.shuffle(options)
    
    return {
        "question": random_entry['API'],
        "options": options,
        "answer": random_entry['Description']
    }

def main():
    """
    The main function that interacts with the user.
    """
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    
    # Display the topic menu
    for topic in topics:
        print(f"- {topic}")
    
    selected_topic = input("Enter your choice: ")
    
    if selected_topic in topics:
        # Display a random fact or concept
        random_fact = get_random_fact(selected_topic)
        print(f"\nHere's a random {selected_topic.lower()} fact or concept:")
        print(random_fact)
        
        # Quiz the user
        quiz_data = quiz_question(selected_topic)
        print(f"\nTest your knowledge with this {selected_topic.lower()} quiz question:")
        print(quiz_data['question'])
        for i, option in enumerate(quiz_data['options']):
            print(f"{i+1}. {option}")
        
        user_answer = input("Enter the number of the correct answer: ")
        if quiz_data['options'][int(user_answer)-1] == quiz_data['answer']:
            print("Correct! You're a knowledge master.")
        else:
            print(f"Oops, the correct answer is: {quiz_data['answer']}")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
