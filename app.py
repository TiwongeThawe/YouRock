from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import random
import string

app = Flask(__name__)

CORS(app)  # Allow PHP to fetch data from Flask

def generate_password(length, use_uppercase, use_numbers, use_specials):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_specials:
        characters += "!@#$%^&*()-_=+"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    length = int(data.get('length', 12))
    use_uppercase = data.get('uppercase', False)
    use_numbers = data.get('numbers', False)
    use_specials = data.get('specials', False)
    
    password = generate_password(length, use_uppercase, use_numbers, use_specials)
    return jsonify({"password": password})

@app.route('/generate-password', methods=['GET'])
def get_password():
    length = request.args.get('length', default=12, type=int)
    password = generate()
    return jsonify({"password": password})



if __name__ == '__main__':
    app.run(debug=True)