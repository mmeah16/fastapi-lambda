from fastapi import FastAPI
from mangum import Mangum
import boto3
from db.dynamo import table

app = FastAPI()


@app.get("/")
async def root():
  return {"message": "Hello World"}

@app.get("/users")
async def get_users():
  response = table.scan()
  data = response["Items"]
  return data

handler = Mangum(app)

