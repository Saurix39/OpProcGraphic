from flask import Flask, render_template, request
from modelo.ecuacion import Ecuacion

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def data():
    numVariables = int(request.form.get("numVariables"))
    numRestricciones = int(request.form.get("numRestricciones"))
    
    return render_template("data.html", restricciones = numRestricciones)

@app.route('/grafico', methods=['POST', 'GET'])
def graficar():

    print(dict(request.form))

    restricciones= [] #las restricciones por post
    puntosSoluci = [] #Puntos que conforman el area de solución en coordenadas
    # ciclo for que nos recorra las restricciones
    #for res in restricciones:
     #   for restri in restricciones
      #      append(res.puntCortEcua(restri))
    #restric = dict(request.form)
    restric = {'MinMax': 'min',
                'Fo': {"x1":"23","x2":"23"},
                'Restr': [
                            {"x1":"2","x2":"3","op":"<=","result":"3"},
                            {"x1":"3","x2":"3","op":">=","result":"5"}
                        ]
                }
    
    for rest in restric['Restr']:
        restriccion=Ecuacion(int(rest['x1']),int(rest['x2']),rest['op'],int(rest['result']))
        restricciones.append(restriccion)
    for rest in restricciones:
        for rest2 in restricciones:
            if rest != rest2:
                coord=rest.puntCortEcua(rest2)
                if coord not in puntosSoluci:
                    puntosSoluci.append(coord) 
    
    #request.form['rest'+i]
    '''
    ecua=Ecuacion(2,3,"<=",3)
    ecua2=Ecuacion(3,3,"<=",5)
    coordenada=ecua.puntCortEcua(ecua2)
    return f"<h1>({coordenada.x}, {coordenada.y} )</h1>"
    '''
    return render_template('metodo.html')

if __name__=="__main__":
    app.run(debug=True)
