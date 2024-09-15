// script.js

// -------------------------
// Question Bank
// -------------------------
const QUESTION_BANK = [
    {
        "id": 1,
        "type": "theory",
        "question": "What’s your favorite way to spend a weekend?",
        "answer": ""
    },
    {
        "id": 2,
        "type": "theory",
        "question": "Do you enjoy trying new restaurants, or do you have a few go-tos?",
        "answer": ""
    },
    {
        "id": 3,
        "type": "theory",
        "question": "What type of music do you enjoy?",
        "answer": ""
    },
    {
        "id": 4,
        "type": "theory",
        "question": "Do you prefer mornings or evenings? Why?",
        "answer": ""
    },
    {
        "id": 5,
        "type": "theory",
        "question": "What’s the last book you read, and did you enjoy it?",
        "answer": ""
    },
    {
        "id": 6,
        "type": "theory",
        "question": "If you could travel anywhere in the world, where would you go and why?",
        "answer": ""
    },
    {
        "id": 7,
        "type": "theory",
        "question": "What’s your dream job and what attracts you to it?",
        "answer": ""
    },
    {
        "id": 8,
        "type": "theory",
        "question": "What’s your favorite movie or TV show, and what do you like about it?",
        "answer": ""
    },
    {
        "id": 9,
        "type": "theory",
        "question": "Do you like to stay active or prefer relaxing at home? Why?",
        "answer": ""
    },
    {
        "id": 10,
        "type": "theory",
        "question": "What’s a hobby you’ve always wanted to try and why?",
        "answer": ""
    },
    {
        "id": 11,
        "type": "theory",
        "question": "What’s your favorite holiday and why does it stand out to you?",
        "answer": ""
    },
    {
        "id": 12,
        "type": "theory",
        "question": "Do you enjoy spending time in nature? If so, what do you like to do?",
        "answer": ""
    },
    {
        "id": 13,
        "type": "theory",
        "question": "What’s something you’re really passionate about and why?",
        "answer": ""
    },
    {
        "id": 14,
        "type": "theory",
        "question": "What motivates you to get out of bed in the morning?",
        "answer": ""
    },
    {
        "id": 15,
        "type": "theory",
        "question": "What personal values guide your decision-making?",
        "answer": ""
    },
    {
        "id": 16,
        "type": "theory",
        "question": "How do you define success, both personally and professionally?",
        "answer": ""
    },
    {
        "id": 17,
        "type": "theory",
        "question": "What is a personal philosophy or motto you live by?",
        "answer": ""
    },
    {
        "id": 18,
        "type": "theory",
        "question": "What are three goals you want to accomplish in the next five years?",
        "answer": ""
    },
    {
        "id": 19,
        "type": "theory",
        "question": "What is your biggest dream or ambition in life?",
        "answer": ""
    },
    {
        "id": 20,
        "type": "theory",
        "question": "How do you plan to balance your personal and professional aspirations?",
        "answer": ""
    },
    {
        "id": 21,
        "type": "theory",
        "question": "What skill or hobby would you love to master but haven’t yet?",
        "answer": ""
    },
    {
        "id": 22,
        "type": "theory",
        "question": "If you had an extra hour each day, how would you spend it?",
        "answer": ""
    },
    {
        "id": 23,
        "type": "theory",
        "question": "What qualities do you value most in a friendship?",
        "answer": ""
    },
    {
        "id": 24,
        "type": "theory",
        "question": "How do you deal with stress and what are your coping mechanisms?",
        "answer": ""
    },
    {
        "id": 25,
        "type": "theory",
        "question": "What do you think is the most important quality a person can have?",
        "answer": ""
    },
    {
        "id": 26,
        "type": "theory",
        "question": "How do you stay motivated when working towards a long-term goal?",
        "answer": ""
    },
    {
        "id": 27,
        "type": "theory",
        "question": "If you could change one thing about the world, what would it be?",
        "answer": ""
    },
    {
        "id": 28,
        "type": "theory",
        "question": "What do you find most fulfilling in your daily life?",
        "answer": ""
    },
    {
        "id": 29,
        "type": "theory",
        "question": "What’s the best piece of advice you’ve ever received?",
        "answer": ""
    },
    {
        "id": 30,
        "type": "theory",
        "question": "What role does family play in your life?",
        "answer": ""
    },
    {
        "id": 31,
        "type": "theory",
        "question": "How do you like to spend a rainy day?",
        "answer": ""
    },
    {
        "id": 32,
        "type": "theory",
        "question": "What’s a cause or charity you care deeply about?",
        "answer": ""
    },
    {
        "id": 33,
        "type": "theory",
        "question": "If you could learn any language, which would it be and why?",
        "answer": ""
    },
    {
        "id": 34,
        "type": "theory",
        "question": "How would you describe your perfect vacation?",
        "answer": ""
    },
    {
        "id": 35,
        "type": "theory",
        "question": "What’s the most challenging thing you’ve done in your life?",
        "answer": ""
    },
    {
        "id": 36,
        "type": "multiple_choice",
        "question": "Do you prefer coffee or tea?",
        "options": ["Coffee", "Tea", "Neither"],
        "answer": ""
    },
    {
        "id": 37,
        "type": "multiple_choice",
        "question": "Are you more of an introvert or extrovert?",
        "options": ["Introvert", "Extrovert", "Ambivert"],
        "answer": ""
    },
    {
        "id": 38,
        "type": "multiple_choice",
        "question": "Do you like to cook or bake?",
        "options": ["Cook", "Bake", "Both", "Neither"],
        "answer": ""
    },
    {
        "id": 39,
        "type": "multiple_choice",
        "question": "Do you enjoy going to concerts or live events?",
        "options": ["Yes", "No", "Sometimes"],
        "answer": ""
    },
    {
        "id": 40,
        "type": "multiple_choice",
        "question": "Are you a morning person or a night owl?",
        "options": ["Morning person", "Night owl"],
        "answer": ""
    },
    {
        "id": 41,
        "type": "multiple_choice",
        "question": "Do you enjoy spending time in nature?",
        "options": ["Yes", "No", "Occasionally"],
        "answer": ""
    },
    {
        "id": 42,
        "type": "multiple_choice",
        "question": "Are you into any sports or outdoor activities?",
        "options": ["Yes", "No", "Sometimes"],
        "answer": ""
    },
    {
        "id": 43,
        "type": "multiple_choice",
        "question": "Do you prefer the beach or the mountains?",
        "options": ["Beach", "Mountains"],
        "answer": ""
    },
    {
        "id": 44,
        "type": "multiple_choice",
        "question": "Do you like to try new things or stick to what you know?",
        "options": ["Try new things", "Stick to what I know"],
        "answer": ""
    },
    {
        "id": 45,
        "type": "multiple_choice",
        "question": "Are you a cat or a dog person?",
        "options": ["Cat person", "Dog person", "Both", "Neither"],
        "answer": ""
    },
    {
        "id": 46,
        "type": "multiple_choice",
        "question": "Do you enjoy listening to podcasts?",
        "options": ["Yes", "No", "Occasionally"],
        "answer": ""
    },
    {
        "id": 47,
        "type": "multiple_choice",
        "question": "What’s your favorite type of movie?",
        "options": ["Comedy", "Drama", "Action", "Horror", "Romance"],
        "answer": ""
    },
    {
        "id": 48,
        "type": "multiple_choice",
        "question": "Do you prefer reading books or watching movies?",
        "options": ["Reading books", "Watching movies", "Both"],
        "answer": ""
    },
    {
        "id": 49,
        "type": "multiple_choice",
        "question": "How do you like to spend your free time?",
        "options": ["Relaxing", "Staying active", "Learning new things", "Socializing"],
        "answer": ""
    },
    {
        "id": 50,
        "type": "multiple_choice",
        "question": "Do you enjoy traveling?",
        "options": ["Yes", "No", "Sometimes"],
        "answer": ""
    }
]
;

// -------------------------
// Selecting Last 47 Questions
// -------------------------
const TOTAL_QUESTIONS = 47;
const selectedQuestions = QUESTION_BANK.slice(-TOTAL_QUESTIONS);

// -------------------------
// State Variables
// -------------------------
let currentQuestionIndex = 0;
let userName = '';
let userAnswers = {};

// -------------------------
// DOM Elements
// -------------------------
const introScreen = document.getElementById('intro-screen');
const quizScreen = document.getElementById('quiz-screen');
const completionScreen = document.getElementById('completion-screen');

const startQuizBtn = document.getElementById('start-quiz-btn');
const usernameInput = document.getElementById('username');

const questionNumber = document.getElementById('question-number');
const questionText = document.getElementById('question-text');
const optionsContainer = document.getElementById('options-container');

const prevBtn = document.getElementById('prev-btn');
const nextBtn = document.getElementById('next-btn');
const submitBtn = document.getElementById('submit-btn');

const thankYouMessage = document.getElementById('thank-you-message');
const restartBtn = document.getElementById('restart-btn');

const progressBar = document.getElementById('progress-bar');

// -------------------------
// Event Listeners
// -------------------------
startQuizBtn.addEventListener('click', startQuiz);
prevBtn.addEventListener('click', showPreviousQuestion);
nextBtn.addEventListener('click', showNextQuestion);
submitBtn.addEventListener('click', submitQuiz);
restartBtn.addEventListener('click', restartQuiz);

// -------------------------
// Functions
// -------------------------

function startQuiz() {
    const name = usernameInput.value.trim();
    if (name === '') {
        alert('Please enter your name to proceed.');
        return;
    }
    userName = name;
    introScreen.classList.remove('active');
    quizScreen.classList.add('active');
    renderQuestion();
    updateProgressBar();
}

function renderQuestion() {
    const question = selectedQuestions[currentQuestionIndex];
    questionNumber.textContent = `Question ${currentQuestionIndex + 1} of ${TOTAL_QUESTIONS}`;
    questionText.textContent = question.question;
    optionsContainer.innerHTML = ''; // Clear previous options

    if (question.type === 'multiple_choice') {
        question.options.forEach((option, index) => {
            const optionId = `option-${index}`;
            const isChecked = userAnswers[question.id] === option;

            const optionHTML = `
                <div class="option">
                    <input type="radio" id="${optionId}" name="option" value="${option}" ${isChecked ? 'checked' : ''}>
                    <label for="${optionId}">${option}</label>
                </div>
            `;
            optionsContainer.insertAdjacentHTML('beforeend', optionHTML);
        });
    } else if (question.type === 'theory') {
        const previousAnswer = userAnswers[question.id] || '';
        const textareaHTML = `
            <textarea id="theory-answer" rows="5" placeholder="Type your answer here...">${previousAnswer}</textarea>
        `;
        optionsContainer.insertAdjacentHTML('beforeend', textareaHTML);
    }

    // Disable Previous button on first question
    prevBtn.disabled = currentQuestionIndex === 0;

    // Disable Next button on last question
    nextBtn.disabled = currentQuestionIndex === TOTAL_QUESTIONS - 1;
}

function showPreviousQuestion() {
    saveUserAnswer();
    if (currentQuestionIndex > 0) {
        currentQuestionIndex--;
        renderQuestion();
        updateProgressBar();
    }
}

function showNextQuestion() {
    saveUserAnswer();
    if (currentQuestionIndex < TOTAL_QUESTIONS - 1) {
        currentQuestionIndex++;
        renderQuestion();
        updateProgressBar();
    }
}

function saveUserAnswer() {
    const question = selectedQuestions[currentQuestionIndex];
    if (question.type === 'multiple_choice') {
        const selectedOption = document.querySelector('input[name="option"]:checked');
        if (selectedOption) {
            userAnswers[question.id] = selectedOption.value;
        }
    } else if (question.type === 'theory') {
        const theoryAnswer = document.getElementById('theory-answer').value.trim();
        userAnswers[question.id] = theoryAnswer;
    }
}

function submitQuiz() {
    saveUserAnswer();
    // Check if all questions are answered
    if (Object.keys(userAnswers).length < TOTAL_QUESTIONS) {
        const unanswered = TOTAL_QUESTIONS - Object.keys(userAnswers).length;
        const confirmSubmit = confirm(`You have ${unanswered} unanswered questions. Do you still want to submit?`);
        if (!confirmSubmit) {
            return;
        }
    }
    quizScreen.classList.remove('active');
    completionScreen.classList.add('active');
    thankYouMessage.textContent = `Thank you, ${userName}, for completing the quiz.`;
}

function restartQuiz() {
    // Reset all state variables
    currentQuestionIndex = 0;
    userName = '';
    userAnswers = {};

    // Reset UI
    completionScreen.classList.remove('active');
    introScreen.classList.add('active');
    usernameInput.value = '';
}

function updateProgressBar() {
    const progressPercentage = ((currentQuestionIndex + 1) / TOTAL_QUESTIONS) * 100;
    progressBar.style.width = `${progressPercentage}%`;
}
