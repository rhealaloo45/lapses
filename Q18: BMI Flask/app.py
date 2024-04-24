from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(weight, height):
    # Calculate BMI
    bmi = weight / (height ** 2)
    return round(bmi, 2)

@app.route('/', methods=['GET', 'POST'])
def bmi_calculator():
    if request.method == 'POST':
        # Get user input from the form
        weight = float(request.form['weight'])
        height = float(request.form['height'])

        # Calculate BMI
        bmi = calculate_bmi(weight, height)

        # Render template with BMI result
        return render_template('result.html', bmi=bmi)

    # Render the form template
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
