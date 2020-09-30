from fastapi import FastAPI

app = FastAPI()

#domain where this api is hosted for example : localhost:5000/docs to see swagger documentation automagically generated.


@app.get("/")
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
def home(name string : 'Bryant'):
    return {"message":"Hello " + name}
=======
<<<<<<< HEAD
=======
>>>>>>> parent of e08c8ee... Update main.py
=======
>>>>>>> parent of e08c8ee... Update main.py
def home(name : string = 'world'):
    return {"message":"Hello {}".format(name)}
=======
def home():
    return {"message":"Hello World"}
>>>>>>> parent of dc0d802... Update main.py
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> parent of e08c8ee... Update main.py
=======
>>>>>>> parent of e08c8ee... Update main.py
=======
>>>>>>> parent of e08c8ee... Update main.py
