from flask import Blueprint, render_template
from hardware import motors
import shared

phone_bp = Blueprint('phone', __name__, template_folder='../templates')

@phone_bp.before_app_first_request
def setup_motors():
    motors.init_motors()

@phone_bp.route('/')
def control_ui():
    return render_template('control.html')

@phone_bp.route('/api/forward')
def move_forward():
    motors.forward()
    return 'Moving forward'

@phone_bp.route('/api/backward')
def move_backward():
    motors.backward()
    return 'Moving backward'

@phone_bp.route('/api/left')
def move_left():
    motors.left()
    return 'Turning left'

@phone_bp.route('/api/right')
def move_right():
    motors.right()
    return 'Turning right'

@phone_bp.route('/api/stop')
def stop_robot():
    motors.stop()
    return 'Stopped'

@phone_bp.route('/api/start-talking')
def start_talking():
    motors.stop()
    shared.robot_state["mode"] = "talking"
    return 'Started talking'
