from flask import Blueprint, jsonify, render_template
from hardware import motors
import shared
import requests

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
    shared.robot_state["mode"] = "moving forward"
    return jsonify(status="ok", mode=shared.robot_state["mode"])

@phone_bp.route('/api/backward')
def move_backward():
    motors.backward()
    shared.robot_state["mode"] = "moving backward"
    return jsonify(status="ok", mode=shared.robot_state["mode"])

@phone_bp.route('/api/left')
def move_left():
    motors.left()
    shared.robot_state["mode"] = "turning left"
    return jsonify(status="ok", mode=shared.robot_state["mode"])

@phone_bp.route('/api/right')
def move_right():
    motors.right()
    shared.robot_state["mode"] = "turning right"
    return jsonify(status="ok", mode=shared.robot_state["mode"])

@phone_bp.route('/api/stop')
def stop_robot():
    motors.stop()
    shared.robot_state["mode"] = "idle"
    return jsonify(status="ok", mode=shared.robot_state["mode"])

# Correct route for starting greeting

@phone_bp.route('/api/start-talking')
def start_talking():
    motors.stop()
    robot_url = 'http://localhost:5000/robot/start_greeting'
    try:
        r = requests.get(robot_url, timeout=2)
        if r.json().get('status') == 'started':
            return jsonify(status="greeting_started", mode="talking")
        else:
            return jsonify(status="robot_busy", mode="busy")
    except Exception as e:
        print(f"Error triggering robot greeting: {e}")
        return jsonify(status="error", mode="error")

# New route to reset robot
@phone_bp.route('/api/reset', methods=['POST'])
def reset_robot():
    motors.stop()
    robot_url = 'http://localhost:5000/robot/reset'
    try:
        r = requests.post(robot_url, timeout=2)
        if r.json().get('status') == 'reset':
            shared.robot_state["mode"] = "idle"
            return jsonify(status="reset_done", mode="idle")
        else:
            return jsonify(status="reset_failed")
    except Exception as e:
        print(f"Error resetting robot: {e}")
        return jsonify(status="error")