from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    with open('data.txt', 'r') as f:
        data = f.read()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
