from fastapi import FastAPI

app = FastAPI()

#domain where this api is hosted for example : localhost:5000/docs to see swagger documentation automagically generated.


@app.get("/")
<<<<<<< HEAD
def home(name : string = 'world'):
    return {"message":"Hello {}".format(name)}
=======
def home():
    return {"message":"Hello World"}
>>>>>>> parent of dc0d802... Update main.py
