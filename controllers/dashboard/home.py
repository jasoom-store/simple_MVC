from flask import Blueprint, render_template, abort, request

dashboard_home = Blueprint('dashboard_home_router', __name__)

@dashboard_home.route('/', methods=['GET'])
def user_page():
    return render_template('dashboard/home.html')
