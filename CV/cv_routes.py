from flask import Blueprint,render_template

cv = Blueprint('cv',__name__,template_folder='templates')

@cv.route("/cv")
def CV():
    return render_template('cv.html')