# -*- coding: UTF-8 -*-
from app import app

@app.route('/')
def index():
    return '你好!!'

if __name__=="__main__": #如果以主程式執行
    app.run(debug=False) #立刻啟動伺服器