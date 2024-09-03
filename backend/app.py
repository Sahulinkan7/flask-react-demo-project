from flask import Flask,jsonify
from flask_cors import CORS 

app=Flask(__name__)
CORS(app)

@app.route("/api/data",methods=['GET'])
def get_data():
    data={
        "message":"Hello from api endpoint",
        "name":"Linkan Kumar Sahu",
        "email":"sahulinkan7@gmail.com"
    }
    
    return jsonify(data)


if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)