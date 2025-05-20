from flask import Blueprint, render_template, jsonify
import shared
import pygame

robot_bp = Blueprint('robot', __name__, template_folder='../templates')

@robot_bp.route('/')
def robot_ui():
    return render_template('ui.html')

@robot_bp.route('/status')
def robot_status():
    return jsonify(mode=shared.robot_state.get("mode", "idle"))

@robot_bp.before_app_request
def check_and_play_greeting():
    if shared.robot_state.get("mode") == "talking":
        try:
            pygame.mixer.init()
            pygame.mixer.music.load("sounds/greeting/welcome1.wav")
            pygame.mixer.music.play()
            shared.robot_state["mode"] = "idle"
        except Exception as e:
            print("[SOUND ERROR]", e)
