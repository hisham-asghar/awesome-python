import random
import requests
import json

# Define the topics and associated facts/concepts
topics = {
    'science': [
        {'fact': 'The human body has around 37.2 trillion cells.', 'explanation': 'The human body is composed of trillions of cells, which are the basic building blocks of life. These cells work together to perform various functions and maintain the overall health of the body.'},
        {'fact': 'The fastest-spinning object created by humans is a neutron star, spinning at up to 716 times per second.', 'explanation': 'Neutron stars are the collapsed cores of massive stars that have exploded as supernovae. They are incredibly dense, with a teaspoon of neutron star material weighing over a billion tons on Earth.'},
        {'fact': 'The Milky Way galaxy contains an estimated 100 to 400 billion stars.', 'explanation': 'The Milky Way is the galaxy that contains our Solar System. It is a spiral galaxy with a central bulge and a rotating disk of gas, dust, and stars.'}
    ],
    'technology': [
        {'fact': 'The first computer virus, called \"Creeper\", was created in 1971.', 'explanation': 'The Creeper virus was an experimental self-replicating program that was designed to infect DEC PDP-10 computers running the TENEX operating system. It was not designed to be malicious, but rather to demonstrate the possibility of such a program.'},
        {'fact': 'The first commercial microprocessor, the Intel 4004, was released in 1971.', 'explanation': 'The Intel 4004 was a 4-bit central processing unit (CPU) released by Intel. It was the first commercially available microprocessor and was used in a variety of applications, including calculators and other electronic devices.'},
        {'fact': 'The first website was launched in 1991 by Tim Berners-Lee.', 'explanation': 'The first website was created by Tim Berners-Lee, a British computer scientist, at the CERN research institute in Switzerland. It was a simple website that provided information about the World Wide Web project and how to use it.'}
    ],
    'history': [
        {'fact': 'The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex.', 'explanation': 'The Great Pyramid of Giza is the oldest and largest of the three pyramids in the Giza pyramid complex, located in Egypt. It was built as a tomb for the Egyptian pharaoh Khufu (also known as Cheops) and is the only remaining wonder of the ancient world.'},
        {'fact': 'The Mona Lisa was painted by the Italian Renaissance artist Leonardo da Vinci between 1503 and 1519.', 'explanation': 'The Mona Lisa is a famous oil painting created by the Italian Renaissance artist Leonardo da Vinci. It depicts a half-length portrait of a woman whose mysterious smile has captivated viewers for centuries.'},
        {'fact': 'The Great Wall of China is the longest man-made structure in the world, stretching over 13,000 miles.', 'explanation': 'The Great Wall of China is a series of fortifications built in ancient China to protect the northern borders of the Chinese Empire against the raids and invasions of various nomadic groups. It is the longest man-made structure in the world, stretching over 13,000 miles.'}
    ],
    'general_knowledge': [
        {'fact': 'The largest organ in the human body is the skin.', 'explanation': 'The skin is the largest organ in the human body, covering the entire external surface and serving as a protective barrier against the environment. It is composed of multiple layers, including the epidermis, dermis, and subcutaneous tissue.'},
        {'fact': 'The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion caused by the heating of the iron.', 'explanation': 'The Eiffel Tower, a famous landmark in Paris, France, can actually grow in height during the summer months due to the thermal expansion of the iron used in its construction. The tower can become up to 15 centimeters (6 inches) taller as the metal heats up and expands.'},
        {'fact': 'The first product to have a barcode was Wrigley's gum.', 'explanation': 'The first product to have a barcode printed on its packaging was a pack of Wrigley's gum in 1974. Barcodes are a method of encoding product information into a machine-readable format, which revolutionized the way products are identified and tracked in stores and supply chains.'}
    ]
}

# Function to display the menu and get user's topic choice
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics.keys():
        print(f"- {topic.capitalize()}")
    
    while True:
        choice = input("Enter your choice (or 'exit' to quit): ").lower()
        if choice == 'exit':
            return None
        if choice in topics:
            return choice
        print("Invalid choice. Please try again.")

# Function to display a random fact and its explanation
def display_random_fact(topic):
    fact_info = random.choice(topics[topic])
    print(f"Random {topic.capitalize()} Fact: {fact_info['fact']}")
    print(f"Explanation: {fact_info['explanation']}")

# Function to run the interactive quiz
def run_quiz(topic):
    print(f"Welcome to the {topic.capitalize()} Quiz!")
    
    # Fetch quiz questions and answers from a public API or predefined database
    quiz_data = fetch_quiz_data(topic)
    
    score = 0
    for question in quiz_data:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i+1}. {option}")
        
        while True:
            try:
                user_answer = int(input("Enter your answer (1-4): "))
                if user_answer < 1 or user_answer > 4:
                    print("Invalid answer. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        if user_answer == question['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {question['answer']}.")
    
    print(f"Your final score is {score} out of {len(quiz_data)}.")

# Function to fetch quiz data from a public API or predefined database
def fetch_quiz_data(topic):
    # Implement logic to fetch quiz data based on the selected topic
    # This can be done by making an API call or retrieving data from a predefined database
    
    # For this example, let's use predefined quiz data
    quiz_data = [
        {
            'question': 'What is the largest planet in our solar system?',
            'options': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
            'answer': 3
        },
        {
            'question': 'What is the smallest planet in our solar system?',
            'options': ['Mercury', 'Venus', 'Mars', 'Earth'],
            'answer': 1
        },
        {
            'question': 'What is the process by which plants convert sunlight into energy?',
            'options': ['Photosynthesis', 'Respiration', 'Transpiration', 'Fermentation'],
            'answer': 1
        }
    ]
    
    return quiz_data

# Main function to run the script
def main():
    topic = display_menu()
    if topic:
        display_random_fact(topic)
        run_quiz(topic)

if __name__ == '__main__':
    main()