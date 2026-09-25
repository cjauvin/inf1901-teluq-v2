/**
 * Reusable Quiz Engine
 * Usage: new Quiz(containerId, questionsData)
 */
class Quiz {
    constructor(containerId, questions) {
        this.containerId = containerId;
        this.questions = questions;
        this.currentQuestion = 0;
        this.userAnswers = [];
        this.score = 0;
        this.answered = false;

        this.init();
    }

    init() {
        this.createQuizHTML();
        this.bindEvents();
        this.displayQuestion();
    }

    createQuizHTML() {
        const container = document.getElementById(this.containerId);
        container.innerHTML = `
            <div class="quiz-container">
                <div id="quiz-section-${this.containerId}">
                    <div class="question-counter">
                        Question <span id="current-question-${this.containerId}">1</span> sur ${this.questions.length}
                    </div>
                    <div class="question-container">
                        <div class="question-text" id="question-text-${this.containerId}"></div>
                        <div id="answers-container-${this.containerId}"></div>
                        <button class="quiz-button" id="action-button-${this.containerId}" disabled>Répondre</button>
                    </div>
                </div>

                <div id="results-section-${this.containerId}" class="results-container hidden" style="display: none;">
                    <div class="score-display">
                        Votre score: <span id="final-score-${this.containerId}"></span>/${this.questions.length}
                    </div>
                    <div class="recap-section">
                        <h3>Récapitulatif des questions</h3>
                        <div id="recap-container-${this.containerId}"></div>
                    </div>
                </div>
            </div>
        `;
    }

    bindEvents() {
        document.getElementById(`action-button-${this.containerId}`).addEventListener('click', () => {
            this.handleAnswer();
        });
    }

    displayQuestion() {
        const questionData = this.questions[this.currentQuestion];
        document.getElementById(`current-question-${this.containerId}`).textContent = this.currentQuestion + 1;
        document.getElementById(`question-text-${this.containerId}`).textContent = questionData.question;

        const answersContainer = document.getElementById(`answers-container-${this.containerId}`);
        answersContainer.innerHTML = '';

        questionData.answers.forEach((answer, index) => {
            const answerDiv = document.createElement('div');
            answerDiv.className = 'answer-option';
            answerDiv.innerHTML = `
                <input type="radio" name="answer-${this.containerId}" value="${index}" id="answer-${this.containerId}-${index}">
                <label for="answer-${this.containerId}-${index}">${answer}</label>
            `;
            answersContainer.appendChild(answerDiv);

            answerDiv.addEventListener('click', () => {
                document.getElementById(`answer-${this.containerId}-${index}`).checked = true;

                // Remove selected class from all options
                document.querySelectorAll(`#answers-container-${this.containerId} .answer-option`).forEach(opt => {
                    opt.classList.remove('selected');
                });

                // Add selected class to clicked option
                answerDiv.classList.add('selected');

                this.enableActionButton();
            });
        });

        document.getElementById(`action-button-${this.containerId}`).disabled = true;
        document.getElementById(`action-button-${this.containerId}`).textContent = 'Répondre';
        this.answered = false;
    }

    enableActionButton() {
        document.getElementById(`action-button-${this.containerId}`).disabled = false;
    }

    handleAnswer() {
        if (!this.answered) {
            const selectedAnswer = document.querySelector(`input[name="answer-${this.containerId}"]:checked`);
            if (selectedAnswer) {
                const userAnswer = parseInt(selectedAnswer.value);
                const correctAnswer = this.questions[this.currentQuestion].correct;

                this.userAnswers.push(userAnswer);

                if (userAnswer === correctAnswer) {
                    this.score++;
                }

                document.querySelectorAll(`#answers-container-${this.containerId} .answer-option`).forEach((option, index) => {
                    if (index === correctAnswer) {
                        option.classList.add('correct');
                    } else if (index === userAnswer && userAnswer !== correctAnswer) {
                        option.classList.add('incorrect');
                    }
                });

                document.getElementById(`action-button-${this.containerId}`).textContent = 'Question suivante';
                this.answered = true;

                if (this.currentQuestion === this.questions.length - 1) {
                    document.getElementById(`action-button-${this.containerId}`).textContent = 'Voir les résultats';
                }
            }
        } else {
            if (this.currentQuestion < this.questions.length - 1) {
                this.currentQuestion++;
                this.displayQuestion();
            } else {
                this.showResults();
            }
        }
    }

    showResults() {
        document.getElementById(`quiz-section-${this.containerId}`).classList.add('hidden');
        document.getElementById(`results-section-${this.containerId}`).style.display = 'block';
        document.getElementById(`results-section-${this.containerId}`).classList.remove('hidden');
        document.getElementById(`final-score-${this.containerId}`).textContent = this.score;

        const recapContainer = document.getElementById(`recap-container-${this.containerId}`);
        recapContainer.innerHTML = '';

        this.questions.forEach((question, index) => {
            const userAnswer = this.userAnswers[index];
            const correctAnswer = question.correct;
            const isCorrect = userAnswer === correctAnswer;

            const recapDiv = document.createElement('div');
            recapDiv.className = `recap-question ${isCorrect ? 'correct' : 'incorrect'}`;

            let answersHtml = '';
            question.answers.forEach((answer, answerIndex) => {
                let answerClass = '';
                if (answerIndex === correctAnswer) {
                    answerClass = 'correct-answer';
                } else if (answerIndex === userAnswer && !isCorrect) {
                    answerClass = 'user-incorrect';
                }

                answersHtml += `<div class="recap-answer ${answerClass}">${String.fromCharCode(97 + answerIndex)}. ${answer}</div>`;
            });

            recapDiv.innerHTML = `
                <div class="recap-question-text">Question ${index + 1}: ${question.question}</div>
                ${answersHtml}
            `;

            recapContainer.appendChild(recapDiv);
        });
    }
}