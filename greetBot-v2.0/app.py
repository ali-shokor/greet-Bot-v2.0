from flask import Flask, redirect
from applications.phone_routes import phone_bp
from applications.robot_routes import robot_bp

app = Flask(__name__)
app.register_blueprint(phone_bp, url_prefix='/phone')
app.register_blueprint(robot_bp, url_prefix='/robot')

@app.route('/')
def home():
    return redirect('/phone')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
