from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<int:edad>')
def index(edad):
    return render_template('index.html',edad=edad)

if __name__=="__main__":
    app.run(debug=True)