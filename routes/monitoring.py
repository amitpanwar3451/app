from flask import render_template
from . import routes


@routes.route('/monitoring')
def monitoring():
      return render_template("monitoring.html")