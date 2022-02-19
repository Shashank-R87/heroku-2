from re import sub
import numpy as np
from flask import Flask
from flask import request, render_template
import ast

app = Flask(__name__)

@app.route('/add/<ma1>/<ma2>', methods=["GET", "POST"])
def add(ma1=None, ma2=None):
    c = ast.literal_eval(ma1)
    d = ast.literal_eval(ma2)
    mat1 = np.array(c)
    mat2 = np.array(d)
    res = np.add(mat1,mat2)
    res1 = res.tolist()
    return render_template("index.html",data = res1)

@app.route('/sub/<ma1>/<ma2>',methods =["GET","POST"])
def subtract(ma1 = None,ma2 = None):
    c = ast.literal_eval(ma1)
    d = ast.literal_eval(ma2)
    mat1 = np.array(c)
    mat2 = np.array(d)
    res = np.subtract(mat1,mat2)
    res1 = res.tolist()
    return render_template("index.html",data = res1)

@app.route('/mmul/<ma1>/<ma2>',methods =["GET","POST"])
def m_mul(ma1,ma2):
    c = ast.literal_eval(ma1)
    d = ast.literal_eval(ma2)
    mat1 = np.array(c)
    mat2 = np.array(d)
    res = np.dot(mat1,mat2,out=None)
    res1 = res.tolist()
    return render_template("index.html",data = res1)

@app.route('/smul/<n>/<ma2>',methods =["GET","POST"])
def s_mul(n,ma2):
    a = int(n)
    c = ast.literal_eval(ma2)
    mat1 = np.array(c)
    res = np.multiply(a,mat1)
    res1 = res.tolist()
    return render_template("index.html",data = res1)

@app.route('/tr/<ma1>',methods =["GET","POST"])
def transpose_(ma1):
    c = ast.literal_eval(ma1)
    mat1 = np.array(c)
    res = mat1.transpose()
    res1 = res.tolist()
    return render_template("index.html",data = res1)

@app.route('/inv/<ma1>',methods =["GET","POST"])
def inverse(ma1):
    c = ast.literal_eval(ma1)
    mat1 = np.array(c)
    mat2 = np.linalg.inv(mat1)
    res = []
    for i in mat2:
        y = []
        for j in i:
            x = j.round(2)
            y.append(x)
        res.append(y)
    return render_template("index.html",data = res)

@app.route('/det/<ma1>',methods =["GET","POST"])
def det(ma1):
    c = ast.literal_eval(ma1)
    mat1 = np.array(c)
    res = np.linalg.det(mat1)
    res1 = res.tolist()
    return render_template("index.html",data = res1)

@app.route('/co/<ma1>',methods =["GET","POST"])
def cofactor(ma1):
    c = ast.literal_eval(ma1)
    mat1 = np.array(c)
    determinant = np.linalg.det(mat1)
    adjoint = np.linalg.inv(mat1)*determinant
    cofactor = adjoint.transpose()
    res1 = []
    for i in cofactor:
        y = []
        for j in i:
            x = j.round(2)
            y.append(x)
        res1.append(y)
    return render_template("index.html",data = res1)

@app.route('/ad/<ma1>',methods =["GET","POST"])
def adjoint(ma1):
    c = ast.literal_eval(ma1)
    mat1 = np.array(c)
    determinant = np.linalg.det(mat1)
    adjoint = np.linalg.inv(mat1)*determinant
    res1 = []
    for i in adjoint:
        y = []
        for j in i:
            x = j.round(2)
            y.append(x)
        res1.append(y)
    return render_template("index.html",data = res1)
