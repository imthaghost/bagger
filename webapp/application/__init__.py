from application.controllers.home import home
from application.controllers.user_login import login_route
from application.controllers.email import email_route
from flask import Flask, request

app = Flask("digift", template_folder='application/templates',
            static_folder='application/static')

app.register_blueprint(home)
app.register_blueprint(login_route)
app.register_blueprint(email_route)

