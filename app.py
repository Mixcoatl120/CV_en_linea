from flask import Flask, redirect,url_for
from CV.cv_routes import *

app = Flask(__name__)
app.config['SECRET_KEY'] =  'Hola'

@app.route('/')
def index():
    return redirect(url_for('cv.CV'))

#registro de blueprints
app.register_blueprint(cv) #carpeta de cv

if __name__ == '__main__':
    app.run()