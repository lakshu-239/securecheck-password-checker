import re

COMMON_PASSWORDS = {
    "password", "password123", "12345678",
    "qwerty123", "admin123", "welcome123",
    "iloveyou", "123456789", "abc123"
}


def check_password(password):
    score = 0
    feedback = []

    if not password:
        return {
            "score": 0,
            "strength": "No password entered",
            "feedback": ["Enter a password to begin."]
        }

    if password.lower() in COMMON_PASSWORDS:
        return {
            "score": 0,
            "strength": "Very Weak",
            "feedback": ["This is a commonly used password. Choose a unique one."]
        }

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 12 characters.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add an uppercase letter.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add a lowercase letter.")

    # Number check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Include a number.")

    # Special character check
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("Include a special character.")

    # Repeated character check
    if re.search(r"(.)\1{3,}", password):
        score -= 2
        feedback.append("Avoid repeating the same character.")

    # Sequential pattern check
    if re.search(
        r"(?:0123|1234|2345|3456|4567|5678|6789|abcd|qwer)",
        password.lower()
    ):
        score -= 1
        feedback.append("Avoid predictable sequences.")

    score = max(0, min(score, 6))

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    if not feedback:
        feedback.append("Good password structure! Keep it unique.")

    return {
        "score": score,
        "strength": strength,
        "feedback": feedback
    }
