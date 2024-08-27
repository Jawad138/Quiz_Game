from flask import Flask, render_template, request, redirect, url_for
from quiz_game import QuizGame
import random

app = Flask(__name__)
game = QuizGame()

@app.route('/', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        user_answers = request.form
        results, score = game.play_web(user_answers)
        return render_template('results.html', results=results, score=score, total=len(game.current_questions))
    
    # Start a new game and get a fresh set of questions for each page load
    game.start_new_game()
    return render_template('quiz.html', questions=game.current_questions, enumerate=enumerate)

if __name__ == '__main__':
    app.run(debug=True)
