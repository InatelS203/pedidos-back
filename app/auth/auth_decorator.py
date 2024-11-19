import os
from functools import wraps
from flask import request, jsonify


def require_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        secret = request.headers.get("secret")
        if not secret or secret != os.getenv("API_SECRET"):
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)

    return decorated_function
