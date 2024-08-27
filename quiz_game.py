import random

class Question:
    def __init__(self, text, choices, correct_answer):
        self.text = text
        self.choices = choices
        self.correct_answer = correct_answer

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer

class QuizGame:
    def __init__(self):
        self.all_questions = [
            # Existing questions
            Question("What is the capital of Pakistan?", ["Islamabad", "Karachi", "Lahore", "Peshawar"], "Islamabad"),
            Question("Which river is the longest in Pakistan?", ["Indus River", "Jhelum River", "Chenab River", "Ravi River"], "Indus River"),
            Question("Who is the founder of Pakistan?", ["Muhammad Ali Jinnah", "Allama Iqbal", "Liaquat Ali Khan", "Fatima Jinnah"], "Muhammad Ali Jinnah"),
            Question("What is the highest mountain peak in Pakistan?", ["K2", "Nanga Parbat", "Rakaposhi", "Broad Peak"], "K2"),
            Question("Which city is known as the 'City of Gardens' in Pakistan?", ["Lahore", "Karachi", "Islamabad", "Peshawar"], "Lahore"),
            Question("Who was the first Prime Minister of Pakistan?", ["Liaquat Ali Khan", "Muhammad Ali Jinnah", "Khawaja Nazimuddin", "Ghulam Muhammad"], "Liaquat Ali Khan"),
            Question("What is the national animal of Pakistan?", ["Markhor", "Snow Leopard", "Lion", "Tiger"], "Markhor"),
            Question("Which province is the largest in Pakistan by area?", ["Balochistan", "Punjab", "Sindh", "Khyber Pakhtunkhwa"], "Balochistan"),
            Question("Who is the current Prime Minister of Pakistan?", ["Imran Khan", "Nawaz Sharif", "Shahbaz Sharif", "Asif Ali Zardari"], "Shahbaz Sharif"),
            Question("What is the national language of Pakistan?", ["Urdu", "English", "Punjabi", "Sindhi"], "Urdu"),

            # New general knowledge questions
            Question("What is the capital of Japan?", ["Tokyo", "Seoul", "Beijing", "Bangkok"], "Tokyo"),
            Question("Who wrote 'To Kill a Mockingbird'?", ["Harper Lee", "J.K. Rowling", "Ernest Hemingway", "Mark Twain"], "Harper Lee"),
            Question("Which planet is known as the 'Red Planet'?", ["Mars", "Venus", "Jupiter", "Saturn"], "Mars"),
            Question("What is the hardest natural substance on Earth?", ["Gold", "Iron", "Diamond", "Platinum"], "Diamond"),
            Question("Who painted the Sistine Chapel's ceiling?", ["Leonardo da Vinci", "Vincent van Gogh", "Michelangelo", "Raphael"], "Michelangelo"),
            Question("What is the smallest prime number?", ["0", "1", "2", "3"], "2"),
            Question("In which year did the Titanic sink?", ["1910", "1912", "1914", "1916"], "1912"),
            Question("Who developed the theory of relativity?", ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Niels Bohr"], "Albert Einstein"),
            Question("Which country is known as the Land of the Rising Sun?", ["China", "Japan", "South Korea", "Vietnam"], "Japan"),
            Question("What is the largest ocean on Earth?", ["Atlantic Ocean", "Indian Ocean", "Southern Ocean", "Pacific Ocean"], "Pacific Ocean"),
        ]
        self.current_questions = []  # To store the current set of questions
        self.score = 0

    def start_new_game(self):
        self.current_questions = random.sample(self.all_questions, 5)
        self.score = 0

    def play_web(self, user_answers):
        results = []
        for i, question in enumerate(self.current_questions):
            user_answer = user_answers.get(f'question_{i}', "").strip()
            if question.check_answer(user_answer):
                self.score += 1
                results.append(f"Question {i + 1}: Correct!")
            else:
                results.append(f"Question {i + 1}: Wrong! The correct answer is {question.correct_answer}")
        
        return results, self.score
