from flask import Blueprint, render_template, jsonify
import shared
import pygame
import threading

robot_bp = Blueprint('robot', __name__, template_folder='../templates')

# Initialize pygame mixer
pygame.mixer.init()

def play_greeting_sequence():
    # Update shared state: show main page first
    shared.robot_state["mode"] = "greeting"
    shared.robot_state["step"] = "welcome_sound"
    shared.robot_state["show_video"] = False

    # Play the greeting sound
    pygame.mixer.music.load("static/sounds/greeting/welcome1.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(100)

    # Play the take card sound
    shared.robot_state["step"] = "card_sound"
    shared.robot_state["show_video"] = True
    pygame.mixer.music.load("static/sounds/card/takeYourCard.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(100)

    # After sounds finish, hide video, update shared state, and redirect to /robot/ui
    shared.robot_state["show_video"] = False
    shared.robot_state["mode"] = "idle"
    shared.robot_state["step"] = None

    # Redirect to the UI page (this is handled on the frontend based on robot state)
    shared.robot_state["mode"] = "idle"
    shared.robot_state["step"] = None

@robot_bp.route('/')
def main_page():
    return render_template('index.html')

@robot_bp.route('/status')
def robot_status():
    return jsonify(shared.robot_state)

@robot_bp.route('/start_greeting')
def start_greeting():
    if shared.robot_state.get("mode", "idle") == "idle":
        threading.Thread(target=play_greeting_sequence, daemon=True).start()
        return jsonify(status="started")
    else:
        return jsonify(status="busy")

@robot_bp.route('/ui')
def robot_ui():
    return render_template('ui.html')
