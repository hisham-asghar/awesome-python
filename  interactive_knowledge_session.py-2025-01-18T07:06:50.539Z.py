
import random
import requests
import json

# Define the topics and their corresponding APIs or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/science?category={}",
    "Technology": "https://api.api-ninjas.com/v1/technology?category={}",
    "History": "https://api.api-ninjas.com/v1/history?topic={}",
    "General Knowledge": "https://opentdb.com/api.php?amount=1&category=9&type=multiple"
}

# Function to get a random fact or concept from the selected topic
def get_random_fact(topic):
    url = topics[topic]
    if topic == "General Knowledge":
        response = requests.get(url)
        data = response.json()
        return data["results"][0]["question"], data["results"][0]["correct_answer"], data["results"][0]["incorrect_answers"]
    else:
        category = random.choice(["physics", "chemistry", "biology", "astronomy"])
        response = requests.get(url.format(category))
        data = response.json()
        return data[0]["fact"]

# Function to run the interactive knowledge session
def run_knowledge_session():
    print("Welcome to the Interactive Knowledge Session!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")

    selected_topic = input("Enter your choice: ")

    if selected_topic in topics:
        fact_or_question, correct_answer, incorrect_answers = get_random_fact(selected_topic)
        print(f"\nHere's a {selected_topic} fact or concept:")
        print(fact_or_question)

        if selected_topic == "General Knowledge":
            print("\nChoose the correct answer:")
            all_answers = [correct_answer] + incorrect_answers
            random.shuffle(all_answers)
            for i, answer in enumerate(all_answers):
                print(f"{i+1}. {answer}")
            user_answer = int(input("Enter your answer (1-4): "))
            if all_answers[user_answer-1] == correct_answer:
                print("Correct!")
            else:
                print(f"Incorrect. The correct answer is: {correct_answer}")
        else:
            input("\nPress Enter to continue...")
    else:
        print("Invalid topic. Please try again.")

if __name__ == "__main__":
    run_knowledge_session()
