from flask import Blueprint, redirect,render_template, request,url_for,flash

ss = Blueprint('ss',__name__,template_folder='templates')

@ss.route("/ss",methods=['GET'])
def SS():      
    return render_template('ss.html')
    
@ss.route("/operaciones",methods=['POST','GET'])
def Op():
    if request.method == 'POST':
        a = int(request.form['a'])
        b = int(request.form['b'])
        c = str(a+b)
        flash(f'La suma es: {c}', 'success')  # Mensaje de éxito
        return redirect(url_for('ss.SS',a=a,b=b,c=c))