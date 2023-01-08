import numpy as np
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"),name="static")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.get('/add/{ma1}/{ma2}')
def add(ma1:str,ma2:str):
    c = json.loads(ma1)
    d = json.loads(ma2)
    print(type(c))
    mat1 = np.array(c)
    mat2 = np.array(d)
    res = np.add(mat1,mat2)
    data = res.tolist()
    return data

@app.get('/sub/{ma1}/{ma2}')
def subtract(ma1:str,ma2:str):
    c = json.loads(ma1)
    d = json.loads(ma2)
    mat1 = np.array(c)
    mat2 = np.array(d)
    res = np.subtract(mat1,mat2)
    data = res.tolist()
    return data

@app.get('/mmul/{ma1}/{ma2}')
def m_mul(ma1:str,ma2:str):
    c = json.loads(ma1)
    d = json.loads(ma2)
    mat1 = np.array(c)
    mat2 = np.array(d)
    res = np.dot(mat1,mat2)
    data = res.tolist()
    return data

@app.get('/smul/{n}/{ma2}')
def s_mul(n:str,ma2:str):
    a = int(n)
    c = json.loads(ma2)
    mat1 = np.array(c)
    res = np.multiply(a,mat1)
    data = res.tolist()
    return data

@app.get('/tr/{ma1}')
def transpose_(ma1:str):
    c = json.loads(ma1)
    mat1 = np.array(c)
    res = mat1.transpose()
    data = res.tolist()
    return data

@app.get('/inv/{ma1}')
def inverse(ma1:str):
    try:
        c = json.loads(ma1)
        mat1 = np.array(c)
        mat2 = np.linalg.inv(mat1)
        res = []
        for i in mat2:
            y = []
            for j in i:
                x = j.round(2)
                y.append(x)
            res.append(y)
            return res
    except np.linalg.LinAlgError:
        return "Singular Matrix"

@app.get('/det/{ma1}')
def det(ma1:str):
    c = json.loads(ma1)
    mat1 = np.array(c)
    res = np.linalg.det(mat1)
    res1 = res.tolist()
    return res1

@app.get('/co/{ma1}')
def cofactor(ma1:str):
    try:
        c = json.loads(ma1)
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
        return res1
    except np.linalg.LinAlgError:
        return "Singular Matrix"


@app.get('/ad/{ma1}')
def adjoint(ma1:str):
    try:
        c = json.loads(ma1)
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
        return res1
    except np.linalg.LinAlgError:
        return "Singular Matrix"