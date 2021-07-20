from flask import Flask
from flask.globals import request
from flask.json import jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CORS_HEADERS'] = 'Content-Type'
from users import users

@cross_origin()

@app.route('/test')
def test():
    return jsonify({'response': 'exito'})
     
     
@app.route('/users')
def getUsers():
    return jsonify(users)

@app.route('/users/<string:username>')
def getUser(username):
    retorno = [user for user in users if user['username']== username]
    return jsonify(retorno)

@app.route('/users', methods=['POST'])
def addUser():
    newUser = {
         'userid': request.json['userid'], 
         'username': request.json['username'], 
         'password': request.json['password']
    }
    users.append(newUser)
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True, port=5000)