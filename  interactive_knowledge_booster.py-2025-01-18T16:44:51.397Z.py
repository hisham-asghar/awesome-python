
import random
import requests
import json

# Define topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://opentdb.com/api.php?amount=1&type=multiple"
}

# Function to get a random fact or concept from the selected topic
def get_random_fact(topic):
    if topic == "General Knowledge":
        response = requests.get(topics[topic])
        data = response.json()
        question = data["results"][0]["question"]
        correct_answer = data["results"][0]["correct_answer"]
        incorrect_answers = data["results"][0]["incorrect_answers"]
        return {"fact": f"Question: {question}", "answer": correct_answer, "options": incorrect_answers + [correct_answer]}
    else:
        response = requests.get(topics[topic], headers={"X-Api-Key": "your_api_key_here"})
        data = response.json()
        return {"fact": data[0]["fact"]}

# Function to run the interactive quiz
def run_quiz(topic):
    fact_data = get_random_fact(topic)
    print(fact_data["fact"])
    options = fact_data["options"]
    random.shuffle(options)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    user_answer = int(input("Enter the number of the correct answer: "))
    if options[user_answer-1] == fact_data["answer"]:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {fact_data['answer']}")

# Main function to run the script
def main():
    print("Welcome to the Interactive Knowledge Booster!")
    while True:
        print("\nSelect a topic:")
        for i, topic in enumerate(topics):
            print(f"{i+1}. {topic}")
        print("5. Quit")
        choice = int(input("Enter your choice (1-5): "))
        if choice == 5:
            print("Goodbye!")
            break
        elif 1 <= choice <= 4:
            topic = list(topics)[choice-1]
            print(f"\nYou selected: {topic}")
            fact_data = get_random_fact(topic)
            print(f"Fun fact: {fact_data['fact']}")
            run_quiz(topic)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
