from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/terminal/<os>')
def terminal(os):
    return render_template('terminal.html', os=os)

if __name__ == '__main__':
    app.run(debug=True)

