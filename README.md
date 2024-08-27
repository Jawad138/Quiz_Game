# Flask Quiz App

This is a web-based quiz application built using Flask, HTML, CSS, and JavaScript. The app presents users with a set of random questions, checks their answers, and provides a score upon completion. The project was developed as part of my internship at EcodeCamp, where I focused on enhancing my Python and web development skills.

## Features

- **Randomized Questions:** The app selects 5 random questions from a pool of pre-defined questions each time you play.
- **Multiple Choice Answers:** Each question comes with multiple choices, and users can select the correct answer.
- **Score Calculation:** After completing the quiz, the app calculates and displays the user's score.
- **Dynamic Feedback:** Immediate feedback on whether the selected answer is correct or incorrect.
- **Play Again Option:** Users can choose to retake the quiz, with a new set of random questions each time.
- **Responsive Design:** The app is designed to be responsive and works well on both desktop and mobile devices.

## Technologies Used

- **Flask:** A lightweight WSGI web application framework for Python.
- **HTML/CSS:** For structuring and styling the web pages.
- **JavaScript:** To handle dynamic interactions and validations.
- **Bootstrap:** For a responsive and modern design.
- **Git:** Version control to manage the project's codebase.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/username/flask-quiz-app.git
   cd flask-quiz-app
Create a virtual environment:

python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:

pip install -r requirements.txt

Run the application:

flask run
