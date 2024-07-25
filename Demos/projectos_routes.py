from flask import Blueprint, redirect,render_template, request,url_for,flash
from dbmodel import *

projectos = Blueprint('projectos',__name__,template_folder='templates')

@projectos.route("/Demo_producto")
def DP():      
    return render_template('Demo_producto.html')

@projectos.route("/Demo_tecnico")
def DT():
    return render_template("Demo_tecnico.html")

@projectos.route("/Demo_homenaje")
def DH():
    return render_template("Demo_homenaje.html")