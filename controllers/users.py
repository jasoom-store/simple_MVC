from flask import Blueprint, render_template, abort, request

users = Blueprint('users_router', __name__)

@users.route('/', methods=['GET'])
def user_page():
    return render_template('users.html')
