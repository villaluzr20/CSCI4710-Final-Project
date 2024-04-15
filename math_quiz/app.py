from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
app.static_folder = 'static'

# Function to calculate the score
def calculate_score(user_answers, correct_answers):
    correct_count = 0
    total_questions = len(correct_answers)

    # Compare each user answer with the corresponding correct answer
    for user_answer, correct_answer in zip(user_answers, correct_answers):
        if user_answer == correct_answer:
            correct_count += 1

    # Calculate the score percentage
    score_percentage = (correct_count / total_questions) * 100

    return score_percentage

def get_addition_questions():
    questions = []
    correct_answers = []
    # Connect to the database
    with sqlite3.connect('quiz.db') as conn:
        cursor = conn.cursor()

        # Fetch questions from the database for addition
        cursor.execute("SELECT question, correct_answer FROM addition_questions")
        rows = cursor.fetchall()
        for row in rows:
            questions.append(row[0])
            correct_answers.append(row[1])

    # Return the questions fetched from the database
    return questions, correct_answers


# Function to fetch questions from the database
def get_subtraction_questions():
    questions = []
    correct_answers = []
    # Connect to the database
    with sqlite3.connect('quiz.db') as conn:
        cursor = conn.cursor()

        # Fetch questions from the database
        cursor.execute("SELECT question, correct_answer FROM subtraction_questions")
        rows = cursor.fetchall()
        for row in rows:
            questions.append(row[0])
            correct_answer = row[1]
            if isinstance(correct_answer, list):  # Check if the correct answer is a list
                correct_answer = correct_answer[0]  # Extract the first element of the list
            correct_answers.append(correct_answer)

    # Return the questions fetched from the database
    return questions, correct_answers

def get_multiplication_questions():
    questions = []
    correct_answers = []
    # Connect to the database
    with sqlite3.connect('quiz.db') as conn:
        cursor = conn.cursor()

        # Fetch questions from the database for multiplication
        cursor.execute("SELECT question, correct_answer FROM multiplication_questions")
        rows = cursor.fetchall()
        for row in rows:
            questions.append(row[0])
            correct_answers.append(row[1])

    # Return the questions fetched from the database
    return questions, correct_answers

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/study.html')
def study():
    return render_template('study.html')

@app.route('/test.html')
def test():
    return render_template('test.html')

@app.route('/addition.html', methods=['GET', 'POST'])
def addition():
    if request.method == 'POST':
        # Fetch questions and correct answers from the database
        questions, correct_answers = get_addition_questions()
        print("User Answers:", request.form.values())
        print("Correct Answers:", correct_answers)

        # Fetch user's answers from the form submission
        user_answers = [int(request.form.get(f'q{i}')) for i in range(1, len(correct_answers) + 1)]
        print("User Answers:", user_answers)

        # Calculate the score
        score = calculate_score(user_answers, correct_answers)

        # Provide feedback to the user based on the score
        if score >= 70:
            feedback_message = "Congratulations! You passed the test."
        else:
            feedback_message = "You need to study more. Try again later."

        # Render the template with the questions, feedback message, and score
        return render_template('addition.html', score=score, feedback_message=feedback_message)

    else:
        # Fetch questions from the database
        questions, _ = get_addition_questions()
        return render_template('addition.html', questions=questions)

@app.route('/subtraction.html', methods=['GET', 'POST'])
def subtraction():
    if request.method == 'POST':
        # Fetch questions and correct answers from the database
        questions, correct_answers = get_subtraction_questions()
        print("User Answers:", request.form.values())
        print("Correct Answers:", correct_answers)

        # Fetch user's answers from the form submission
        user_answers = [int(request.form.get(f'q{i}')) for i in range(1, len(correct_answers) + 1)]
        print("User Answers:", user_answers)

        # Calculate the score
        score = calculate_score(user_answers, correct_answers)

        # Provide feedback to the user based on the score
        if score >= 70:
            feedback_message = "Congratulations! You passed the test."
        else:
            feedback_message = "You need to study more. Try again later."

        # Render the template with the questions, feedback message, and score
        return render_template('subtraction.html', score=score, feedback_message=feedback_message)

    else:
        # Fetch questions from the database
        questions, _ = get_subtraction_questions()
        return render_template('subtraction.html', questions=questions)

@app.route('/multiplication.html', methods=['GET', 'POST'])
def multiplication():
    if request.method == 'POST':
        # Fetch questions and correct answers from the database
        questions, correct_answers = get_multiplication_questions()
        print("User Answers:", request.form.values())
        print("Correct Answers:", correct_answers)

        # Fetch user's answers from the form submission
        user_answers = [int(request.form.get(f'q{i}')) for i in range(1, len(correct_answers) + 1)]
        print("User Answers:", user_answers)

        # Calculate the score
        score = calculate_score(user_answers, correct_answers)

        # Provide feedback to the user based on the score
        if score >= 70:
            feedback_message = "Congratulations! You passed the test."
        else:
            feedback_message = "You need to study more. Try again later."

        # Render the template with the questions, feedback message, and score
        return render_template('multiplication.html', score=score, feedback_message=feedback_message)

    else:
        # Fetch questions from the database
        questions, _ = get_multiplication_questions()
        return render_template('multiplication.html', questions=questions)

@app.route('/division.html')
def division():
    return render_template('division.html')

if __name__ == '__main__':
    app.run(debug=True)
