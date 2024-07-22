﻿from flask import Flask, redirect,url_for
from CV.cv_routes import *
from info.info_routes import *
from ejemplos.suma_simple.ss_routes import *
from Demos.projectos_routes import *

app = Flask(__name__)
app.config['SECRET_KEY'] =  'Holacd'

@app.route('/')
def index():
    return redirect(url_for('cv.CV'))

#registro de blueprints
app.register_blueprint(cv) #carpeta de cv
app.register_blueprint(info) # Carpeta de información
app.register_blueprint(ss) # carpeta de ejemplos sumas simples
app.register_blueprint(projectos)# carpeta de proyectos

if __name__ == '__main__':
    app.run()