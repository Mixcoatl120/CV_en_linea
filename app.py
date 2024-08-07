from flask import Flask, redirect,url_for
from CV.cv_routes import *
from info.info_routes import *
from Demos.projectos_routes import *
from dbmodel import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "Mixcoatl120"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres.bfmehanvxfbspoksbbai:Mixcoatl120.@aws-0-us-west-1.pooler.supabase.com/postgres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    return redirect(url_for('home.Home'))

#registro de blueprints
app.register_blueprint(home) #carpeta de cv
app.register_blueprint(info) # Carpeta de información
app.register_blueprint(projectos)# carpeta de proyectos

if __name__ == '__main__':
    app.run()