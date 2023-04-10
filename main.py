from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def index():
    return {'data':{'first':'Sujoy','last':'Gadha'}}


@app.get('/')
def abt():
    return {'data':'This is new page'}