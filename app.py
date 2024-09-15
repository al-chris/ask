import streamlit as st
import json

# Sample question bank
# In practice, you might load this from a JSON file or an API
QUESTION_BANK = [
    { 
        "id": 1,
        "type": "multiple_choice",
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    { 
        "id": 2,
        "type": "multiple_choice",
        "question": "Is the Earth round?",
        "options": ["True", "False"],
        "answer": "True"
    },
    { 
        "id": 3,
        "type": "multiple_choice",
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Jupiter", "Saturn", "Venus"],
        "answer": "Mars"
    },
    { 
        "id": 4,
        "type": "multiple_choice",
        "question": "What is the boiling point of water at sea level?",
        "options": ["100°C", "90°C", "50°C", "120°C"],
        "answer": "100°C"
    },
    {
        "id": 5,
        "type": "multiple_choice",
        "question": "Can humans breathe underwater unaided?",
        "options": ["True", "False"],
        "answer": "False"
    },
    { 
        "id": 6,
        "type": "multiple_choice",
        "question": "What is the chemical symbol for Gold?",
        "options": ["Au", "Ag", "Fe", "Pb"],
        "answer": "Au"
    },
    { 
        "id": 7,
        "type": "multiple_choice",
        "question": "Which language is used to create web pages?",
        "options": ["HTML", "Python", "Java", "C++"],
        "answer": "HTML"
    },
    { 
        "id": 8,
        "type": "multiple_choice",
        "question": "What is the square root of 64?",
        "options": ["8", "6", "7", "9"],
        "answer": "8"
    },
    { 
        "id": 9,
        "type": "multiple_choice",
        "question": "Is Mount Everest the tallest mountain in the world?",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "id": 10,
        "type": "multiple_choice",
        "question": "Who wrote 'Hamlet'?",
        "options": ["William Shakespeare", "Mark Twain", "Jane Austen", "Charles Dickens"],
        "answer": "William Shakespeare"
    },
    {
        "id": 11,
        "type": "multiple_choice",
        "question": "Is water an element?",
        "options": ["True", "False"],
        "answer": "False"
    },
    { 
        "id": 12,
        "type": "multiple_choice",
        "question": "Which is the smallest ocean in the world?",
        "options": ["Arctic Ocean", "Indian Ocean", "Atlantic Ocean", "Pacific Ocean"],
        "answer": "Arctic Ocean"
    },
    {
        "id": 13,
        "type": "multiple_choice",
        "question": "Which organ is responsible for pumping blood through the body?",
        "options": ["Heart", "Liver", "Lungs", "Kidneys"],
        "answer": "Heart"
    },
    {
        "id": 14,
        "type": "multiple_choice",
        "question": "Is the Great Wall of China visible from space?",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "id": 15,
        "type": "multiple_choice",
        "question": "What gas do plants absorb from the atmosphere?",
        "options": ["Carbon Dioxide", "Oxygen", "Nitrogen", "Hydrogen"],
        "answer": "Carbon Dioxide"
    },
    {
        "id": 16,
        "type": "multiple_choice",
        "question": "Does light travel faster than sound?",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "id": 17,
        "type": "multiple_choice",
        "question": "Which planet is closest to the Sun?",
        "options": ["Mercury", "Venus", "Earth", "Mars"],
        "answer": "Mercury"
    },
    {
        "id": 18,
        "type": "multiple_choice",
        "question": "Is ice less dense than water?",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "id": 19,
        "type": "multiple_choice",
        "question": "Which is the hardest natural substance on Earth?",
        "options": ["Diamond", "Gold", "Iron", "Quartz"],
        "answer": "Diamond"
    },
    {
        "id": 20,
        "type": "multiple_choice",
        "question": "Is Pluto classified as a planet?",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "id": 21,
        "type": "multiple_choice",
        "question": "What is the freezing point of water?",
        "options": ["0°C", "-10°C", "100°C", "32°C"],
        "answer": "0°C"
    },
    {
        "id": 22,
        "type": "multiple_choice",
        "question": "Do all mammals have backbones?",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "id": 23,
        "type": "multiple_choice",
        "question": "Which country is known as the Land of the Rising Sun?",
        "options": ["Japan", "China", "India", "Thailand"],
        "answer": "Japan"
    },
    {
        "id": 24,
        "type": "multiple_choice",
        "question": "Is helium heavier than air?",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "id": 25,
        "type": "multiple_choice",
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["Oxygen", "Osmium", "Oganesson", "Oxygenium"],
        "answer": "Oxygen"
    },
    {
        "id": 26,
        "type": "multiple_choice",
        "question": "Is the sun a star?",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "id": 27,
        "type": "multiple_choice",
        "question": "What is the hardest rock?",
        "options": ["Diamond", "Granite", "Marble", "Limestone"],
        "answer": "Diamond"
    },
    {
        "id": 28,
        "type": "multiple_choice",
        "question": "Is Venus the hottest planet in the solar system?",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "id": 29,
        "type": "multiple_choice",
        "question": "Which ocean is the largest?",
        "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
        "answer": "Pacific Ocean"
    },
    {
        "id": 30,
        "type": "multiple_choice",
        "question": "Is steel stronger than aluminum?",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "id": 31,
        "type": "multiple_choice",
        "question": "Who is known as the father of computers?",
        "options": ["Charles Babbage", "Alan Turing", "John Von Neumann", "Bill Gates"],
        "answer": "Charles Babbage"
    },
    {
        "id": 32,
        "type": "multiple_choice",
        "question": "Is the Moon a planet?",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "id": 33,
        "type": "multiple_choice",
        "question": "Which country has the largest population?",
        "options": ["China", "India", "USA", "Indonesia"],
        "answer": "China"
    },
    {
        "id": 34,
        "type": "multiple_choice",
        "question": "Is a tomato a fruit?",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "id": 35,
        "type": "multiple_choice",
        "question": "What is the chemical symbol for water?",
        "options": ["H2O", "O2", "CO2", "HO"],
        "answer": "H2O"
    },
    {
        "id": 36,
        "type": "multiple_choice",
        "question": "Is Australia a continent?",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "id": 37,
        "type": "multiple_choice",
        "question": "Which element is found in abundance in the Earth's crust?",
        "options": ["Oxygen", "Iron", "Silicon", "Carbon"],
        "answer": "Oxygen"
    },
    {
        "id": 38,
        "type": "multiple_choice",
        "question": "Is DNA the blueprint of life?",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "id": 39,
        "type": "multiple_choice",
        "question": "Which gas makes up the majority of Earth's atmosphere?",
        "options": ["Nitrogen", "Oxygen", "Carbon Dioxide", "Hydrogen"],
        "answer": "Nitrogen"
    },
    {
        "id": 40,
        "type": "multiple_choice",
        "question": "Is lead heavier than water?",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "id": 41,
        "type": "multiple_choice",
        "question": "Which galaxy is Earth located in?",
        "options": ["Milky Way", "Andromeda", "Whirlpool", "Triangulum"],
        "answer": "Milky Way"
    },
    {
        "id": 42,
        "type": "multiple_choice",
        "question": "Is the speed of light faster than the speed of sound?",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "id": 43,
        "type": "multiple_choice",
        "question": "What is the most common gas in the universe?",
        "options": ["Hydrogen", "Oxygen", "Helium", "Nitrogen"],
        "answer": "Hydrogen"
    },
    {
        "id": 44,
        "type": "multiple_choice",
        "question": "Is 24 hours a day caused by Earth's rotation?",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "id": 45,
        "type": "multiple_choice",
        "question": "Which is the longest river in the world?",
        "options": ["Nile", "Amazon", "Yangtze", "Mississippi"],
        "answer": "Nile"
    },
    {
        "id": 46,
        "type": "multiple_choice",
        "question": "Is sound faster in water than in air?",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "id": 47,
        "type": "multiple_choice",
        "question": "Which is the hottest planet in our solar system?",
        "options": ["Venus", "Mercury", "Mars", "Jupiter"],
        "answer": "Venus"
    },
    {
        "id": 48,
        "type": "multiple_choice",
        "question": "Is the atomic number of hydrogen 1?",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "id": 49,
        "type": "multiple_choice",
        "question": "Which country gifted the Statue of Liberty to the USA?",
        "options": ["France", "Germany", "UK", "Spain"],
        "answer": "France"
    },
    {
        "id": 50,
        "type": "multiple_choice",
        "question": "Is a bee a mammal?",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "id": 51,
        "type": "multiple_choice",
        "question": "Which is the smallest country in the world?",
        "options": ["Vatican City", "Monaco", "Nauru", "San Marino"],
        "answer": "Vatican City"
    },
    {
        "id": 52,
        "type": "multiple_choice",
        "question": "Is the chemical formula of salt NaCl?",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "id": 53,
        "type": "multiple_choice",
        "question": "Which animal is known as the 'Ship of the Desert'?",
        "options": ["Camel", "Elephant", "Horse", "Donkey"],
        "answer": "Camel"
    },
    {
        "id": 54,
        "type": "multiple_choice",
        "question": "Is water an insulator?",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "id": 55,
        "type": "multiple_choice",
        "question": "Which planet has rings around it?",
        "options": ["Saturn", "Mars", "Earth", "Venus"],
        "answer": "Saturn"
    },
    {
        "id": 56,
        "type": "multiple_choice",
        "question": "Is the Pacific Ocean the deepest ocean?",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "id": 57,
        "type": "multiple_choice",
        "question": "Which element is a liquid at room temperature?",
        "options": ["Mercury", "Gold", "Iron", "Lead"],
        "answer": "Mercury"
    },
    {
        "id": 58,
        "type": "multiple_choice",
        "question": "Is the Eiffel Tower in London?",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "id": 59,
        "type": "multiple_choice",
        "question": "Which is the largest planet in our solar system?",
        "options": ["Jupiter", "Saturn", "Neptune", "Earth"],
        "answer": "Jupiter"
    },
    {
        "id": 60,
        "type": "multiple_choice",
        "question": "Is copper a good conductor of electricity?",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "id": 61,
        "type": "multiple_choice",
        "question": "Which bird is the national bird of the USA?",
        "options": ["Bald Eagle", "Robin", "Sparrow", "Crow"],
        "answer": "Bald Eagle"
    },
    {
        "id": 62,
        "type": "multiple_choice",
        "question": "Is chocolate poisonous to dogs?",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "id": 63,
        "type": "multiple_choice",
        "question": "Which gas is used by plants during photosynthesis?",
        "options": ["Carbon Dioxide", "Oxygen", "Nitrogen", "Hydrogen"],
        "answer": "Carbon Dioxide"
    },
    {
        "id": 64,
        "type": "multiple_choice",
        "question": "Is the North Pole hotter than the South Pole?",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "id": 65,
        "type": "multiple_choice",
        "question": "Which metal is used in making light bulbs?",
        "options": ["Tungsten", "Copper", "Iron", "Aluminum"],
        "answer": "Tungsten"
    },
    {
        "id": 66,
        "type": "multiple_choice",
        "question": "Is gold more valuable than silver?",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "id": 67,
        "type": "multiple_choice",
        "question": "Which continent is the Sahara Desert located in?",
        "options": ["Africa", "Asia", "Australia", "Europe"],
        "answer": "Africa"
    },
    {
        "id": 68,
        "type": "multiple_choice",
        "question": "Is hydrogen the lightest element?",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "id": 69,
        "type": "multiple_choice",
        "question": "Which animal is known as the 'King of the Jungle'?",
        "options": ["Lion", "Tiger", "Elephant", "Giraffe"],
        "answer": "Lion"
    },
    {
        "id": 70,
        "type": "multiple_choice",
        "question": "Is the boiling point of water 100°C?",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "id": 71,
        "type": "multiple_choice",
        "question": "Which instrument measures earthquakes?",
        "options": ["Seismometer", "Barometer", "Thermometer", "Hygrometer"],
        "answer": "Seismometer"
    },
    {
        "id": 72,
        "type": "multiple_choice",
        "question": "Is a shark a mammal?",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "id": 73,
        "type": "multiple_choice",
        "question": "Which planet is known as the 'Evening Star'?",
        "options": ["Venus", "Mars", "Mercury", "Jupiter"],
        "answer": "Venus"
    },
    {
        "id": 74,
        "type": "multiple_choice",
        "question": "Is the Amazon rainforest the largest rainforest in the world?",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "id": 75,
        "type": "multiple_choice",
        "question": "Which part of the plant conducts photosynthesis?",
        "options": ["Leaf", "Root", "Stem", "Flower"],
        "answer": "Leaf"
    },
    {
        "id": 76,
        "type": "multiple_choice",
        "question": "Is an octopus a vertebrate?",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "id": 77,
        "type": "multiple_choice",
        "question": "Which vitamin is produced when a person is exposed to sunlight?",
        "options": ["Vitamin D", "Vitamin C", "Vitamin B", "Vitamin A"],
        "answer": "Vitamin D"
    },
    {
        "id": 78,
        "type": "multiple_choice",
        "question": "Is copper a metal?",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "id": 79,
        "type": "multiple_choice",
        "question": "Which mammal can fly?",
        "options": ["Bat", "Elephant", "Kangaroo", "Monkey"],
        "answer": "Bat"
    },
    {
        "id": 80,
        "type": "multiple_choice",
        "question": "Is honey a solid?",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "id": 81,
        "type": "multiple_choice",
        "question": "Which planet is known for its rings?",
        "options": ["Saturn", "Mars", "Jupiter", "Uranus"],
        "answer": "Saturn"
    },
    {
        "id": 82,
        "type": "multiple_choice",
        "question": "Is the capital of Australia Sydney?",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "id": 83,
        "type": "multiple_choice",
        "question": "Which gas do animals need to breathe?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "answer": "Oxygen"
    },
    {
        "id": 84,
        "type": "multiple_choice",
        "question": "Is Mars known as the 'Red Planet'?",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "id": 85,
        "type": "multiple_choice",
        "question": "Which organ pumps blood in the human body?",
        "options": ["Heart", "Liver", "Lungs", "Kidneys"],
        "answer": "Heart"
    },
    {
        "id": 86,
        "type": "multiple_choice",
        "question": "Is an elephant an amphibian?",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "id": 87,
        "type": "multiple_choice",
        "question": "Which planet is called the 'Blue Planet'?",
        "options": ["Earth", "Neptune", "Uranus", "Mars"],
        "answer": "Earth"
    },
    {
        "id": 88,
        "type": "multiple_choice",
        "question": "Is 0 a positive number?",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "id": 89,
        "type": "multiple_choice",
        "question": "Which animal is the largest mammal?",
        "options": ["Blue Whale", "Elephant", "Giraffe", "Hippo"],
        "answer": "Blue Whale"
    },
    {
        "id": 90,
        "type": "multiple_choice",
        "question": "Is oxygen necessary for human survival?",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "id": 91,
        "type": "multiple_choice",
        "question": "Which is the smallest unit of life?",
        "options": ["Cell", "Atom", "Molecule", "Organ"],
        "answer": "Cell"
    },
    {
        "id": 92,
        "type": "multiple_choice",
        "question": "Is the sun the center of the solar system?",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "id": 93,
        "type": "multiple_choice",
        "question": "Which is the strongest muscle in the human body?",
        "options": ["Tongue", "Heart", "Biceps", "Quadriceps"],
        "answer": "Tongue"
    },
    {
        "id": 94,
        "type": "multiple_choice",
        "question": "Is Pluto still classified as a planet?",
        "options": ["True", "False"],
        "answer": "False"
    },
    {
        "id": 95,
        "type": "multiple_choice",
        "question": "Which continent is known as the 'Dark Continent'?",
        "options": ["Africa", "Asia", "Europe", "Australia"],
        "answer": "Africa"
    },
    {
        "id": 96,
        "type": "multiple_choice",
        "question": "Is photosynthesis a process in plants?",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "id": 97,
        "type": "multiple_choice",
        "question": "Which planet is known as the 'Morning Star'?",
        "options": ["Venus", "Mars", "Mercury", "Jupiter"],
        "answer": "Venus"
    },
    {
        "id": 98,
        "type": "multiple_choice",
        "question": "Is the square root of 81 equal to 9?",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "id": 99,
        "type": "multiple_choice",
        "question": "Which is the largest land animal?",
        "options": ["Elephant", "Giraffe", "Rhino", "Hippo"],
        "answer": "Elephant"
    },
    {
        "id": 100,
        "type": "multiple_choice",
        "question": "Is the Atlantic Ocean larger than the Indian Ocean?",
        "options": ["True", "False"],
        "answer": "True"
    },
    {
        "id": 101,
        "type": "theory",
        "question": "Explain the process of photosynthesis in plants.",
        "answer": ""
    },
    {
        "id": 102,
        "type": "theory",
        "question": "Describe the main causes of global warming.",
        "answer": ""
    },
    {
        "id": 103,
        "type": "theory",
        "question": "What are the key differences between classical and quantum physics?",
        "answer": ""
    },
    {
        "id": 104,
        "type": "theory",
        "question": "Discuss the impact of technology on modern education.",
        "answer": ""
    },
    {
        "id": 105,
        "type": "theory",
        "question": "Outline the process of the water cycle.",
        "answer": ""
    },
    {
        "id": 106,
        "type": "theory",
        "question": "What are the fundamental rights mentioned in the Universal Declaration of Human Rights?",
        "answer": ""
    },
    {
        "id": 107,
        "type": "theory",
        "question": "Explain the theory of evolution by natural selection.",
        "answer": ""
    },
    {
        "id": 108,
        "type": "theory",
        "question": "Describe the structure and function of the human heart.",
        "answer": ""
    },
    {
        "id": 109,
        "type": "theory",
        "question": "What is the significance of the theory of relativity in modern physics?",
        "answer": ""
    },
    {
        "id": 110,
        "type": "theory",
        "question": "Discuss the economic and social impacts of unemployment in society.",
        "answer": ""
    }
]

# Function to initialize session state variables
def initialize_state():
    if 'name' not in st.session_state:
        st.session_state.name = ''
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'answers' not in st.session_state:
        st.session_state.answers = {}
    if 'question_order' not in st.session_state:
        # Select the last 47 questions from the question bank
        total_questions = len(QUESTION_BANK)
        if total_questions >= 47:
            st.session_state.question_order = list(range(total_questions - 47, total_questions))
        else:
            st.warning("Question bank does not contain enough questions.")
            st.session_state.question_order = list(range(total_questions))
    
# Function to load questions
def load_questions():
    # Fetch the selected questions based on question_order
    selected_questions = [QUESTION_BANK[i] for i in st.session_state.question_order]
    return selected_questions

# Initialize session state
initialize_state()

# Main application
def main():
    if st.session_state.name == '':
        intro_screen()
    elif st.session_state.current_question < 47:
        quiz_screen()
    else:
        completion_screen()

def intro_screen():
    st.title("Welcome to the Quiz App")
    name = st.text_input("Please enter your name:")
    if st.button("Start Quiz"):
        if name.strip() == '':
            st.warning("Please enter your name to proceed.")
        else:
            st.session_state.name = name.strip()

def quiz_screen():
    questions = load_questions()
    current_idx = st.session_state.current_question
    question = questions[current_idx]
    
    st.header(f"Question {current_idx + 1} of 47")
    st.write(question["question"])
    
    # Display input based on question type
    if question["type"] == "multiple_choice":
        options = question["options"]
        # Retrieve previously selected option if exists
        previous_answer = st.session_state.answers.get(question["id"], None)
        selected_option = st.radio("Select an option:", options, index=options.index(previous_answer) if previous_answer in options else 0, key=f"q_{current_idx}")
        st.session_state.answers[question["id"]] = selected_option
    elif question["type"] == "theory":
        # Retrieve previously entered answer if exists
        previous_answer = st.session_state.answers.get(question["id"], "")
        answer = st.text_area("Your Answer:", value=previous_answer, key=f"q_{current_idx}")
        st.session_state.answers[question["id"]] = answer
    
    # Navigation buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Previous"):
            if current_idx > 0:
                st.session_state.current_question -= 1
    with col2:
        if st.button("Next"):
            if current_idx < 46:
                st.session_state.current_question += 1
    with col3:
        if st.button("Submit Quiz"):
            if len(st.session_state.answers) < 47:
                st.warning("You have not answered all questions.")
            else:
                st.session_state.current_question = 47  # Move to completion screen

def completion_screen():
    st.title("Thank You for Participating!")
    st.write(f"Thank you, {st.session_state.name}, for completing the quiz.")
    # Optionally, you can display or process the answers here
    # For example, save to a database or display a summary
    # Reset the quiz for a new user
    if st.button("Restart Quiz"):
        st.session_state.name = ''
        st.session_state.current_question = 0
        st.session_state.answers = {}
        initialize_state()

if __name__ == "__main__":
    main()
