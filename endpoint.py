from flask import Flask, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'use_your_key!'
jwt = JWTManager(app)

@app.route('/api/login', methods=['POST'])
def login():
    access_token = create_access_token(identity='username')
    return jsonify(access_token=access_token)

@app.route('/api/secure', methods=['GET'])
@jwt_required()
def secure_endpoint():
    return jsonify({'message': 'This is a safe endpoint'})

if __name__ == '__main__':
    app.run(debug=True)
