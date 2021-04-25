from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data/<int:numVariables>/<int:numRestricciones>')
def data(numVariables, numRestricciones):
    return render_template("data.html", restricciones = numRestricciones)


@app.route('/getData', methods=['POST'])
def getData():
    print(request.form.get('MinMax'))
    print(dict(request.form))
    print(type(request.form))
    return ""

if __name__=="__main__":
    app.run(debug=True)