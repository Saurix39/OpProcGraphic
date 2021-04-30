from flask import Flask, render_template, request
from modelo.ecuacion import Ecuacion
import numpy as np
from matplotlib import pyplot as plt
import json

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

    func_obj = json.loads(request.form.get('Fo'))
    min_max = request.form.get('MinMax')
    restricciones= [] #las restricciones por post
    puntosCorte = [] #Puntos que corte
    puntosSoli = [] #Puntos de solucion
    # ciclo for que nos recorra las restricciones

    restric = json.loads(request.form.get('Restr'))
    for rest in restric:
        restriccion=Ecuacion(float(rest['x1']),float(rest['x2']),rest['op'],float(rest['result']))
        restricciones.append(restriccion)
    for rest in restricciones:
        for rest2 in restricciones:
            if rest != rest2:
                coord=rest.puntCortEcua(rest2)
                if coord is not None:
                    if coord not in puntosCorte:
                        puntosCorte.append(coord) 
    
    for punt in puntosCorte:
        if punt.coord_restric(restricciones):
            puntosSoli.append(punt)
            
    if len(puntosSoli) == 0:
        return "Mateo retorne un template o mensaje que diga que no hay puntos de solucion c:"
    min = int(func_obj['x1'])*puntosSoli[0].x + int(func_obj['x2'])*puntosSoli[0].y
    max = int(func_obj['x1'])*puntosSoli[0].x + int(func_obj['x2'])*puntosSoli[0].y
    punt_min = puntosSoli[0]
    punt_max = puntosSoli[0]
    for punt in puntosSoli:
        punto = int(func_obj['x1'])*punt.x + int(func_obj['x2'])*punt.y
        if punto < min:
            min = punto
            punt_min = punt
        elif punto > max:
            max = punto
            punt_max = punt
    
    max_range_x = 0
    max_range_y = 0
    for res in restricciones:
        if res.puntCortX() is not None and res.puntCortX().x > max_range_x:
            max_range_x = res.puntCortX().x
        if res.puntCortY() is not None and res.puntCortY().y > max_range_y:
            max_range_y = res.puntCortY().y
    
    legend = []
    plt.grid()
    for res in restricciones:
        if res.puntCortX() is None:
            x = [0, max_range_x]
            y = [res.puntCortY().y, res.puntCortY().y]
        elif res.puntCortY() is None:
            x = [res.puntCortX().x, res.puntCortX().x]
            y = [0, max_range_y]
        else:    
            x = [res.puntCortX().x, res.puntCortY().x]
            y = [res.puntCortX().y, res.puntCortY().y]
        legend.append(res.__str__())
        plt.plot(x,y)
    
    
    for solu in puntosSoli:
        plt.plot(solu.x, solu.y, marker="o", color="black")
    
    if min_max == "min":
        func_obj_ecua = Ecuacion(float(func_obj['x1']), float(func_obj['x2']), "=", min)
    elif min_max == "max":
        func_obj_ecua = Ecuacion(float(func_obj['x1']), float(func_obj['x2']), "=", max)
    
    f_o_x = [func_obj_ecua.puntCortX().x, func_obj_ecua.puntCortY().x]
    f_o_y = [func_obj_ecua.puntCortX().y, func_obj_ecua.puntCortY().y]
    plt.plot(f_o_x,f_o_y, color="black")
    legend.append("FO: "+func_obj_ecua.__str__())

    plt.legend(legend,shadow=True, title="Restricciones", framealpha=0.5)
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.savefig('static/img/grafica.png')
    plt.clf()
    #Estos son los datos que debe incluir la tabla
    datos_tabla=tabla(puntosSoli,func_obj, func_obj_ecua)
    return render_template('metodo.html')

def tabla(puntSoli, func_obj, func_obj_ecua):
    data={}
    puntos=[]
    i=1
    for punt in puntSoli:
        valor = int(func_obj['x1'])*punt.x + int(func_obj['x2'])*punt.y
        dicpunt={
            'Punto':f'{i}',
            'Coordenada X (X1)':f'{punt.x}',
            'Coordenada Y (X2)':f'{punt.y}',
            'Valor de la función objetivo (Z)':f'{valor}',
            'Solu': 1 if valor == func_obj_ecua.resultado else 0
            }
        puntos.append(dicpunt)
        i+=1
    data['puntos']=puntos
    return data

if __name__=="__main__":
    app.run(debug=True)
