#-*-coding:utf-8 -*-

import app.poet as poet
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
app=Flask(__name__) #__name__代表目前執行的模組
CORS(app)

@app.route("/test", methods=["GET"]) #函式的裝飾
def getResult():
    heading = '我'
    result = poet.get_hidden_poetry(heading)
    return jsonify(result)

@app.route('/predict', methods=["POST"])
def postInput():
    # 取得前端傳過來的數值
    insertValues = request.get_json()
    heading = insertValues['keyin']
    result = poet.get_hidden_poetry(heading)
    return jsonify(result)
