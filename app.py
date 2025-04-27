from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    items = []
    return render_template('index.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)
