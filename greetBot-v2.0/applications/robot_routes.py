from flask import Blueprint, render_template, jsonify
import shared
import pygame
import threading
import time

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

    # Play the take card sound and show video
    shared.robot_state["step"] = "card_sound"
    shared.robot_state["show_video"] = True
    pygame.mixer.music.load("static/sounds/card/takeYourCard.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(100)

    # Add a small delay to ensure video plays completely
    time.sleep(1)

    # After sounds finish, hide video and prepare for UI redirect
    print("Greeting sequence finished, setting mode=show_ui and show_video=False")
    shared.robot_state["show_video"] = False
    shared.robot_state["mode"] = "show_ui"
    shared.robot_state["step"] = "redirect_to_ui"  # Add this step for better tracking

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
    # When UI page is accessed, reset the state to idle
    shared.robot_state["mode"] = "ui_active"
    shared.robot_state["step"] = None
    return render_template('ui.html')

# Add a reset route
@robot_bp.route('/reset', methods=['POST'])
def reset_robot():
    shared.robot_state["mode"] = "idle"
    shared.robot_state["show_video"] = False
    shared.robot_state["step"] = None
    return jsonify(status="reset")