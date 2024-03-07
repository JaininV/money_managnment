# import flask for serve
# import api blueprint
import flask

# Admin side api logic

# Register api logic
from route.users import user_blueprint


app = flask.Flask(__name__, template_folder='D:/D/Certification/Projects/Updated parking slot/public/', static_folder="static")

# Admin side api's

# Register api's 
app.register_blueprint(user_blueprint, url_prefix='/api')

#connect server
try:
    if (__name__ == "__main__"):
        app.run(debug=True) 

except Exception as err:
    print(err)