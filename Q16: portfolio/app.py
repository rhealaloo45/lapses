from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    profile = {
        'name': 'John Doe',
        'occupation': 'Web Developer',
        'about': 'I am a passionate web developer with expertise in HTML, CSS, JavaScript, and Python. I love creating responsive and user-friendly websites.',
        'profile_picture': 'profile_picture.jpg',
    }
    return render_template('index.html', profile=profile)
if __name__ == '__main__':
    app.run(debug=True)
