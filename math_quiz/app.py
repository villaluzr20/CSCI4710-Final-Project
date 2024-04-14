from flask import Flask, render_template, request

app = Flask(__name__)

app.static_folder = 'static'

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/study.html')
def study():
    return render_template('study.html')

@app.route('/test.html')
def test():
    return render_template('test.html')

@app.route('/addition.html')
def addition():
    return render_template('addition.html')

@app.route('/subtraction.html')
def subtraction():
    return render_template('subtraction.html')

@app.route('/multiplication.html')
def multiplication():
    return render_template('multiplication.html')

@app.route('/division.html')
def division():
    return render_template('division.html')


# Place Database connection and setup code here


#@app.route('/study')
#def study():
    # Logic to fetch questions from database and pass them to template
    #return render_template('study.html', questions=questions)

#@app.route('/quiz', methods=['GET', 'POST'])
#def quiz():
    #if request.method == 'POST':
        # Logic to calculate score
        #return render_template('score.html', score=score)
    #else:
        # Logic to fetch questions from database and pass them to template
        #return render_template('quiz.html', questions=questions)

if __name__ == '__main__':
    app.run(debug=True)
