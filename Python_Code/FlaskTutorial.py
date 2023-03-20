# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 22:07:48 2022

@author: Admin
"""

from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
   app.run()