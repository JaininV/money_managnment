# import flask for serve
# import api blueprint
import flask
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

# Admin side api logic

# Register api logic
from route.users import user_blueprint
from route.login import login_blueprint
from route.job import job_blueprint


app = flask.Flask(__name__, template_folder='D:/D/Certification/Projects/Updated parking slot/public/', static_folder="static")

# Functions for tokenization
app.config['JWT_SECRET_KEY'] = 'my_key'
jwt = JWTManager(app)

# Admin side api's


# Register api's 
app.register_blueprint(user_blueprint, url_prefix='/api')
app.register_blueprint(login_blueprint, url_prefix='/api')
app.register_blueprint(job_blueprint, url_prefix='/api')

#connect server
try:
    if (__name__ == "__main__"):
        app.run(debug=True) 

except Exception as err:
    print(err)