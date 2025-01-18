Here is the raw Python code without any additional commentary:

```python
import random
import requests
import json

TOPICS = {
    "Science": "https://api.api-ninjas.com/v1/randomfact?category=science",
    "Technology": "https://api.api-ninjas.com/v1/randomfact?category=technology",
    "History": "https://api.api-ninjas.com/v1/randomfact?category=history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

API_KEY = "YOUR_API_KEY_HERE"

def get_random_fact(topic):
    url = TOPICS[topic]
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["fact"]
    else:
        return "Sorry, we couldn't fetch a random fact. Please try again later."

def quiz(topic):
    url = TOPICS[topic]
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        trivia = response.json()
        score = 0
        for question in trivia:
            print(question["question"])
            options = question["options"]
            for i, option in enumerate(options):
                print(f"{i+1}. {option}")
            user_answer = int(input("Enter your answer (1-4): "))
            if options[user_answer-1] == question["answer"]:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer is: {question['answer']}")
        print(f"Your final score: {score}/{len(trivia)}")
    else:
        print("Sorry, we couldn't fetch the quiz questions. Please try again later.")

def main():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in TOPICS:
        print(f"- {topic}")

    selected_topic = input("Enter your choice: ")
    if selected_topic in TOPICS:
        print(f"Here's a random fact about {selected_topic}:")
        print(get_random_fact(selected_topic))
        print("\nNow, let's test your knowledge with a quiz!")
        quiz(selected_topic)
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    main()
