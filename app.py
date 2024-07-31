# app.py
from flask import Flask, request, jsonify, render_template
from aes_encryption import encrypt, decrypt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt_route():
    data = request.get_json()
    encrypted = encrypt(data['plaintext'])
    return jsonify(encrypted)

@app.route('/decrypt', methods=['POST'])
def decrypt_route():
    data = request.get_json()
    decrypted = decrypt(data['iv'], data['ciphertext'])
    return jsonify({'plaintext': decrypted})

if __name__ == '__main__':
    app.run(debug=True)
