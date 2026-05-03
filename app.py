from flask import Flask, request, jsonify
from flask_cors import CORS
from detector import detect_type
from knowledge import get_full_info

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Backend is running 🚀"

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    user_input = data.get("data")
    lang = data.get("language", "python")

    dtype = detect_type(user_input)
    definition, code, output, explanation = get_full_info(dtype, lang)

    return jsonify({
        "type": dtype,
        "definition": definition,
        "code": code,
        "output": output,
        "explanation": explanation
    })

if __name__ == '__main__':
    app.run(debug=True)