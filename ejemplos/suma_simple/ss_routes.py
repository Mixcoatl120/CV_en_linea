from flask import Blueprint, redirect,render_template, request,url_for,flash

ss = Blueprint('ss',__name__,template_folder='templates')

@ss.route("/ss",methods=['GET'])
def SS():      
    return render_template('ss.html')
    
@ss.route("/suma",methods=['POST','GET'])
def Op():
    if request.method == 'POST':
        a = float(request.form['a'])
        b = float(request.form['b'])
        flash(f'La suma de {a} y de {b} es de: {a+b}', 'success')  # Mensaje suma
        flash(f'La resta de {a} y de {b} es de: {a-b}', 'success') # mensaje resta
        flash(f'La Multiplicación de {a} y de {b} es de: {a*b}', 'success') # mensaje multiplicacion
        
        if b != 0:
            flash(f'La Divición de {a} y de {b} es de: {a/b}', 'success') # mensaje divicion
        else:
            flash(f'Lo siento pero no puedo dividir entre 0', 'success') # mensaje divicion
            
        return redirect(url_for('ss.SS',a=a,b=b))
   
