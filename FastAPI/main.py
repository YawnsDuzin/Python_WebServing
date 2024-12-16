from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hello World!"}

@app.get("/help")
async def help():
    return {"message" : "help World!"}