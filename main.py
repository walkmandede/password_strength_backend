from flask import Flask, request, jsonify
from password_helper import proceed_password as prpwd
import joblib

# Load your trained model
model = joblib.load('password_strength_model.pkl')  # Make sure your model is saved as .pkl

# Initialize Flask app
app = Flask(__name__)

# Define the function to generate password score
def generate_password_score(password):
    each_x = prpwd(password)[1:-1]
    y_temp = model.predict([each_x])
    return y_temp[0]

# API route to classify password strength using GET method
@app.route('/classify_password', methods=['GET'])
def classify_password():
    # Get password from query parameters
    password = request.args.get('password')

    if not password:
        return jsonify({"error": "Password not provided"}), 400

    score = generate_password_score(password)
    
    # Convert the score to a standard Python float
    return jsonify({"password": password, "strength_score": float(score)})


if __name__ == '__main__':
    app.run(debug=True)