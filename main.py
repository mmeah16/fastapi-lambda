from fastapi import FastAPI
from mangum import Mangum


app = FastAPI()


@app.get("/")
async def root():
  return {"message": "Hello World"}

@app.get("/users")
async def get_users():
  return {"users" : "John Doe"}

handler = Mangum(app)

