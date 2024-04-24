from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        feedback = request.form['feedback']
        # Here you can do something with the feedback, such as store it in a database
        return 'Thank you for your feedback!'
if __name__ == '__main__':
    app.run(debug=True)
