
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    "science": "https://api.sampleapis.com/science/facts",
    "technology": "https://api.sampleapis.com/technology/facts",
    "history": "https://api.sampleapis.com/history/facts",
    "general": "https://api.sampleapis.com/generalknowledge/facts"
}

def get_random_fact(topic):
    """
    Fetches a random fact from the specified topic.
    """
    try:
        response = requests.get(topics[topic])
        facts = json.loads(response.text)
        return random.choice(facts)
    except:
        return "Sorry, we couldn't fetch a fact for that topic right now."

def quiz(topic):
    """
    Provides a multiple-choice quiz for the specified topic.
    """
    try:
        response = requests.get(topics[topic])
        facts = json.loads(response.text)
        question = random.choice(facts)
        options = [question["fact"]] + [random.choice(facts)["fact"] for _ in range(3)]
        random.shuffle(options)
        
        print(f"Question: {question['fact']}")
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        
        while True:
            user_answer = input("Enter the number of the correct answer: ")
            if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
                if options[int(user_answer)-1] == question["fact"]:
                    print("Correct!")
                    return
                else:
                    print("Incorrect. Try again.")
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
    except:
        print("Sorry, we couldn't load the quiz for that topic right now.")

def main():
    print("Welcome to the Knowledge Booster!")
    print("Select a topic to get started:")
    
    while True:
        for i, topic in enumerate(topics):
            print(f"{i+1}. {topic.capitalize()}")
        print("5. Exit")
        
        user_choice = input("Enter your choice (1-5): ")
        if user_choice.isdigit() and 1 <= int(user_choice) <= 5:
            if int(user_choice) == 5:
                print("Goodbye!")
                break
            topic = list(topics.keys())[int(user_choice)-1]
            print(f"\nRandom {topic} fact: {get_random_fact(topic)}")
            quiz(topic)
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
