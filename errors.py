from flask import (Flask, render_template, Blueprint,abort)
bp=Blueprint("/error",__name__,url_prefix="/error")
@bp.route("/401")
def error():
        abort(401)
@bp.route("/404")
def error1():
        abort(404)

@bp.errorhandler(404)
@bp.errorhandler(401)
def unauthorized(error):
	return render_template('unauthorized.html')
