from flask import Blueprint,render_template

info = Blueprint('info',__name__,template_folder='templates')

@info.route("/info")
def Info():
    return render_template('info.html')