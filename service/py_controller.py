# coding=utf-8
import json
from flask import Flask, Response, request
from service.py_service import classify_message

app = Flask(__name__)


@app.route("/health")
def health():
    result = {'status': 'UP'}
    return Response(json.dumps(result), mimetype='application/json')


@app.route("/chat")
def chat():
    message = request.args.get("message")
    msg = classify_message(message)
    result = {"target": msg[0], "score": msg[1]}
    return Response(json.dumps(result), mimetype='application/json', )


app.run(port=3000, host='0.0.0.0')
