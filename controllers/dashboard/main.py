from flask import Blueprint, render_template, abort, request

dashboard_main = Blueprint('dashboard_main_router', __name__)

@dashboard_main.route('/', methods=['GET'])
def user_page():
    return render_template('dashboard/main.html')
