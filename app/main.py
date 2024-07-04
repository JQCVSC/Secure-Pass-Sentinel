from flask import Flask, request, jsonify, render_template
import re
import os

app = Flask(__name__)

# Load common passwords
common_passwords = set()
with open(os.path.join(os.path.dirname(__file__), 'common_passwords.txt'), 'r') as f:
    common_passwords = set(line.strip().lower() for line in f)

def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")

    # Check for numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one number")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include at least one special character")

    # Check if it's a common password
    if password.lower() in common_passwords:
        feedback.append("This is a commonly used password")
        score = max(0, score - 2)  # Penalize common passwords

    # Determine strength based on score
    if score <= 1:
        strength = "Very Weak"
    elif score == 2:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return {
        "strength": strength,
        "score": score,
        "feedback": feedback
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_password', methods=['POST'])
def check_password():
    password = request.json.get('password', '')
    result = check_password_strength(password)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)