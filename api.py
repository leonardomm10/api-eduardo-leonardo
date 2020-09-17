#from flask_ngrok import run_with_ngrok
from flask import Flask, request, jsonify
#from flask_cors import CORS
import os
import math
import statistics

app = Flask(__name__)

#CORS(app)
#run_with_ngrok(app)

@app.route('/')
def root():
    return """
    <html>
        <body style="text-align:center">
            <hr>
            <h1>Links to access each function</h1>
            <hr>
            <br><br>
            <ul style="position: absolute; text-align: left; left: 45%;">
                <li><a href="/soma?var1=3&var2=3">Soma</a></li>
                <li><a href="/sub?var1=3&var2=3">Subtração</a></li>
                <li><a href="/multi?var1=3&var2=3">Multiplicação</a></li>
                <li><a href="/div?var1=3&var2=3">Divisão</a></li>
                <li><a href="/raiz?var1=4">Raiz quadrada</a></li>
                <li><a href="/pot?var1=2&var2=3">Potência</a></li>
                <li><a href="/mediaa?var1=2&var2=2&var3=4&var4=4">Media Aritimetica</a></li>
                <li><a href="/mediah?var1=2&var2=2&var3=4&var4=4">Media Harmonica</a></li>
                <li><a href="/moda?var1=1&var2=2&var3=4&var4=3&var5=4">Moda</a></li>
            </ul>
        </body>
    </html>
    """

@app.route('/soma', methods=['GET'])
def soma():

    value = request.args

    data = { "var1" : value["var1"], "var2" : value['var2']}
    
    soma = float(data['var1']) + float(data['var2'])
    result = jsonify(soma)
    return result

@app.route('/sub', methods=['GET'])
def subtracao():

    value = request.args

    data = { "var1" : value["var1"], "var2" : value['var2']}
    
    sub = float(data['var1']) - float(data['var2'])
    result = jsonify(sub)
    return result

@app.route('/div', methods=['GET'])
def divisao():

    value = request.args

    data = { "var1" : value["var1"], "var2" : value['var2']}
    
    div = float(data['var1']) / float(data['var2'])
    result = jsonify(div)
    return result

@app.route('/multi', methods=['GET'])
def multi():

    value = request.args

    data = { "var1" : value["var1"], "var2" : value['var2']}

    multi = float(data['var1']) * float(data['var2'])
    result = jsonify(multi)
    return result

@app.route('/raiz', methods=['GET'])
def raiz():

    value = request.args

    data = { "var1" : value["var1"]}
    
    raiz = math.sqrt(float(data['var1']))
    result = jsonify(raiz)
    return result

@app.route('/pot', methods=['GET'])
def pot():

    value = request.args

    data = { "var1" : value["var1"], "var2" : value['var2']}

    pot = float(data['var1']) ** float(data['var2'])
    result = jsonify(pot)
    return result

@app.route('/mediaa', methods=['GET'])
def mediaa():

    value = request.args

    data = { "var1" : value["var1"], "var2" : value['var2'], "var3" : value['var3'], "var4" : value['var4']}
    
    mediaa = (float(data['var1']) + float(data['var2']) + float(data['var3']) + float(data['var4'])) / 4
    result = jsonify(mediaa)
    return result

@app.route('/mediah', methods=['GET'])
def mediah():

    value = request.args

    data = { "var1" : value["var1"], "var2" : value['var2'], "var3" : value['var3'], "var4" : value['var4']}

    mediah = 4/ ((1/float(data['var1'])) + (1/float(data['var2'])) + (1/float(data['var3']))+ (1/float(data['var4'])))
    result = jsonify(mediah)
    return result

@app.route('/moda', methods=['GET'])
def moda():

    value = request.args

    data = { "var1" : value["var1"], "var2" : value['var2'], "var3" : value['var3'], "var4" : value['var4'], "var5" : value['var5']}
    lista = [data['var1'],data['var2'],data['var3'],data['var4'],data['var5']]

    try:
      moda = statistics.mode(lista)
      result = jsonify(moda)
      return result

    except:
      return "Mais de uma moda identificada"



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)