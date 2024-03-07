# import flask for serve
# import api blueprint
import flask

# Admin side api logic
from admin_pannel.route.add_slot import add_slot_blueprint

# Register api logic
from route.car_process import car_park_blueprint
from route.users import user_blueprint
from route.slot_details import slot_details_blueprint


app = flask.Flask(__name__, template_folder='D:/D/Certification/Projects/Updated parking slot/public/', static_folder="static")

# Admin side api's
app.register_blueprint(add_slot_blueprint, url_prefix='/api')

# Register api's 
app.register_blueprint(user_blueprint, url_prefix='/api')
app.register_blueprint(car_park_blueprint, url_prefix='/api')
app.register_blueprint(slot_details_blueprint, url_prefix='/api')

#connect server
try:
    if (__name__ == "__main__"):
        app.run(debug=True) 

except Exception as err:
    print(err)