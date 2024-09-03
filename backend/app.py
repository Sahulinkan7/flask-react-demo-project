from flask import Flask,jsonify

app=Flask(__name__)

@app.route("/api/data",methods=['GET'])
def get_data():
    data={
        "message":"Hello from api endpoint."
    }
    
    return jsonify(data)


if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)