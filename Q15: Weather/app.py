from flask import Flask, render_template
import random
app = Flask(__name__)
cities = {
    'New York': {'temperature': random.randint(60, 80), 'description': 'Sunny'},
    'London': {'temperature': random.randint(50, 70), 'description': 'Partly Cloudy'},
    'Tokyo': {'temperature': random.randint(65, 85), 'description': 'Rainy'},
    'Sydney': {'temperature': random.randint(70, 90), 'description': 'Clear'},
}
@app.route('/')
def index():
    return render_template('index.html', cities=cities)
if __name__ == '__main__':
    app.run(debug=True)
