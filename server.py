# import flask for serve
# import api blueprint
import flask
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import datetime

# Admin side api logic

# Register api logic
from route.users import user_blueprint
from route.login import login_blueprint
from route.job import job_blueprint
from route.shift import shift_blueprint
from route.income import income_blueprint
from route.expense import expense_blueprint


app = flask.Flask(__name__, template_folder='D:/D/Certification/Projects/Updated parking slot/public/', static_folder="static")

# Functions for tokenization
app.config["JWT_COOKIE_SECURE"] = False
app.config['JWT_SECRET_KEY'] = 'my_key'
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(hours=1)
jwt = JWTManager(app)

# Admin side api's


# Register api's 
app.register_blueprint(user_blueprint, url_prefix='/api')
app.register_blueprint(login_blueprint, url_prefix='/api')
app.register_blueprint(job_blueprint, url_prefix='/api')
app.register_blueprint(shift_blueprint, url_prefix='/api')
app.register_blueprint(income_blueprint, url_prefix='/api')
app.register_blueprint(expense_blueprint, url_prefix='/api')

#connect server
try:
    if (__name__ == "__main__"):
        app.run(debug=True) 

except Exception as err:
    print(err)