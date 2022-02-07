from flask import Flask, jsonify, request
 
 
app = Flask(__name__)

#model

 
 
@app.route('/with_parameters')
def with_parameters():
    splWidth = float(request.args.get('splWidth'))
    # splLength = float(request.args.get('splLenght'))
    # ptlWidth = float(request.args.get('ptlWidth'))
    # ptlLength = float(request.args.get('ptlLength'))
    return jsonify("plantje")
 
 
 
if __name__ == '__main__':
    app.run()