from flask import Blueprint, render_template, abort, request

home = Blueprint('home_router', __name__)

@home.route('/', methods=['GET'])
def user_page():
    return render_template('home.html')
