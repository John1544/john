from flask import Flask, render_template

app = Flask(__name__, template_folder='template')

@app.route('/')
def home():
    return render_template('home.html',)

@app.route('/login')
def login():
    return render_template('login.html',)

@app.route('/register')
def register():
    return render_template('register.html',)

@app.route('/profile')
def profile():
    return render_template('profile.html',)

if __name__ == '__main__':
    app.run(debug=True)