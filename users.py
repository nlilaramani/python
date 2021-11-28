from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
bp = Blueprint('users', __name__, url_prefix='/users')
@bp.route('/register')
def register_user():
	return "register user"