from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def index():
    return {'data':'blog list'}

@app.get('/blog/{id}/comments')
def comments(id):
    return {'data':{'1', '2'}}


# dynamic routing
@app.get('/blog/{id}')
# fetchblogwith id = id
def songs(id:int):
    return {'data':id}

@app.get('/blog/city/{city}')
def location(city:str):
    return {'data':city}
