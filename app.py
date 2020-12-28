from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/status', methods = ['POST']) 
def return_status():
    return jsonify(str('Training Complete!'))


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
    #app.run(port=8080)
