from applications.robot_routes import robot_bp
from applications.phone_routes import phone_bp
from flask import Flask, redirect


app = Flask(__name__)

# Register blueprints with URL prefixes
app.register_blueprint(robot_bp, url_prefix='/robot')
app.register_blueprint(phone_bp, url_prefix='/phone')

@app.route('/')
def home():
    return redirect('/robot/')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
