from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
bp = Blueprint('homepage', __name__, url_prefix='/')

@bp.route('/index', methods=('GET', 'POST'))
def index():
    return render_template('index.html')
