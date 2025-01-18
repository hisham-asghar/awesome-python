
import random
import requests
import json

def get_trivia_data(topic):
    """
    Fetches trivia data for the given topic from a public API.
    """
    api_url = f"https://api.api-ninjas.com/v1/trivia?category={topic}"
    response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_fact(topic, fact):
    """
    Displays a short explanation of the given fact or concept.
    """
    print(f"Topic: {topic.capitalize()}")
    print(f"Fact: {fact['fact']}")
    print(f"Explanation: {fact['explanation']}")

def quiz(topic, questions):
    """
    Runs an interactive quiz for the user to test their knowledge.
    """
    score = 0
    for question in questions:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer == question['answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score: {score}/{len(questions)}")

def main():
    """
    Main function that displays the menu and runs the interactive knowledge session.
    """
    topics = ['science', 'technology', 'history', 'general']
    print("Welcome to the Interactive Knowledge Session!")
    while True:
        print("\nSelect a topic:")
        for i, topic in enumerate(topics):
            print(f"{i+1}. {topic.capitalize()}")
        print("5. Exit")
        choice = int(input("Enter your choice (1-5): "))
        if choice == 5:
            print("Goodbye!")
            break
        elif choice < 1 or choice > 4:
            print("Invalid choice. Please try again.")
        else:
            topic = topics[choice - 1]
            trivia_data = get_trivia_data(topic)
            if trivia_data:
                fact = random.choice(trivia_data)
                display_fact(topic, fact)
                quiz(topic, trivia_data)
            else:
                print("Failed to fetch trivia data. Please try again later.")

if __name__ == "__main__":
    main()
