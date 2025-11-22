from flask import Flask, request, jsonify
from flask_cors import CORS
from cryptography.fernet import Fernet
import base64
import hashlib

app = Flask(__name__)
CORS(app)

def generate_key(password: str) -> bytes:
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

@app.route('/api/encrypt', methods=['POST'])
def encrypt_message():
    data = request.json
    message = data.get("message")
    password = data.get("password")

    key = generate_key(password)
    cipher = Fernet(key)
    encrypted = cipher.encrypt(message.encode()).decode()

    return jsonify({"encrypted": encrypted})

@app.route('/api/decrypt', methods=['POST'])
def decrypt_message():
    data = request.json
    encrypted_text = data.get("encrypted")
    password = data.get("password")

    try:
        key = generate_key(password)
        cipher = Fernet(key)
        decrypted = cipher.decrypt(encrypted_text.encode()).decode()

        return jsonify({"decrypted": decrypted})
    except:
        return jsonify({"error": "Invalid password or corrupted text"}), 400

if __name__ == '__main__':
    app.run(debug=True)
