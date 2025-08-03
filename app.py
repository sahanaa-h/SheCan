from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to fetch data

@app.route('/api/user')
def get_user_data():
    return jsonify({
        "name": "Sahana H",
        "referral_code": "sahana2025",
        "donations": 2000
    })

# ✅ Move this above the __main__ block
@app.route('/')
def home():
    return {"message": "Backend is running!"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
