from flask import Flask

# Custom..
import __init__
from config.router import Router

# Start the app..
app = Flask(__name__, template_folder=__init__.VIEWS_DIR)

# Confing start...
app.config.from_object(__init__)

Router.run(app)

if __name__ == '__main__':
    app.run(
        debug = True
    )
