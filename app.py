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

if __name__ == '__main__':
    app.run(debug=True)
