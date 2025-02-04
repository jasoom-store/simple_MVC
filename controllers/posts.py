from flask import Blueprint, render_template, abort, request

posts = Blueprint('posts_router', __name__)

@posts.route('/', methods=['GET'])
def user_page():
    return render_template('posts.html')
