from flask import Flask, request, render_template
from flask_pymongo import PyMongo
from bson.json_util import loads, dumps

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost/pythonmongodb' 
mongo = PyMongo(app)

@app.route('/')
def index():
    return "Ruta principal, '/' introducir '/tabla' "

@app.route('/tabla')
def tabla():
    json = loads(dumps(mongo.db.nicob.find()))
    datos = []
    for i in json:
        datos.append([i['valor0'],i['valor1'],i['valor2'],i['valor3']])
    return render_template('index.html', datos = datos)

@app.route("/agregar", methods=['POST'])
def agregar():
    valor0 = request.json['valor0']
    valor1 = request.json['valor1']
    valor2 = request.json['valor2']    
    valor3 = request.json['valor3']
    if valor0 and valor1 and valor2 and valor3:
       id = mongo.db.nicob.insert({'valor0':valor0,'valor1':valor1,'valor2':valor2,'valor3':valor3})
    return "pdf agregado!"

if __name__ =="__main__":
    app.run(host='0.0.0.0', port=3000)
