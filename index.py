from flask import Flask, render_template, request, redirect, url_for, flash, session
from modelo.ecuacion import Ecuacion
import numpy as np
from matplotlib import pyplot as plt
from modelo.coord import Coord
import json
import datetime

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
numRestricciones = 1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['POST', 'GET'])
def data():
    if request.method == 'POST':
        numVariables = int(request.form.get("numVariables"))
        session['numRes'] = int(request.form.get("numRestricciones"))    
        return render_template("data.html", restricciones = session['numRes'])
    else:
        flash(request.args.get("error"), "alert-danger")
        return render_template("data.html", restricciones = session['numRes'])

@app.route('/grafico', methods=['POST', 'GET'])
def grafico():
    #print(request.form.get('hidden-data'))

    data = json.loads(request.form.get('hidden-data'))
    

    func_obj = data.get('Funcion objetivo')
    min_max = data.get('Minmax')

    restricciones= [] #las restricciones por post
    puntosCorte = [] #Puntos que corte
    puntosSoli = [] #Puntos de solucion
    # ciclo for que nos recorra las restricciones

    restric = data.get('Restricciones')
    for rest in restric:
        restriccion=Ecuacion(float(rest['x1']),float(rest['x2']),rest['op'],float(rest['result']))
        restricciones.append(restriccion)
    puntosCorte.append(Coord(0,0))
    for rest in restricciones:
        if rest.puntCortX() is not None:
            puntosCorte.append(rest.puntCortX())
        if rest.puntCortY() is not None:
            puntosCorte.append(rest.puntCortY())
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
        return redirect(url_for('data', error = "El modelo no tiene solución"))
    min = float(func_obj['x1'])*puntosSoli[0].x + float(func_obj['x2'])*puntosSoli[0].y
    max = float(func_obj['x1'])*puntosSoli[0].x + float(func_obj['x2'])*puntosSoli[0].y
    punt_min = puntosSoli[0]
    punt_max = puntosSoli[0]
    for punt in puntosSoli:
        punto = round(float(func_obj['x1'])*punt.x + float(func_obj['x2'])*punt.y,2)
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
        if res.pedPositiv():
            x=[0,max_range_x]
            y=[res.resultado,((res.x*(-1))*(max_range_x)+res.resultado)/(res.y if res.y != 0 else 1)]
        elif res.puntCortX() is None:
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
    nombre='static/img/grafica'+str(datetime.datetime.now().timestamp())+'.png'
    plt.savefig(nombre)
    plt.close()
    #Estos son los datos que debe incluir la tabla
    datos_tabla=tabla(puntosSoli,func_obj, func_obj_ecua)

    return render_template('metodo.html', data_table = datos_tabla, restricciones= restricciones, fo = func_obj_ecua, nom=nombre, MaxMin= "Maximizar" if min_max == "max" else "Minimizar")

def tabla(puntSoli, func_obj, func_obj_ecua):
    data={}
    puntos=[]
    i=1
    for punt in puntSoli:
        valor = round(float(func_obj['x1'])*punt.x + float(func_obj['x2'])*punt.y,2)
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
