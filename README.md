This repository underlines the process in creating a FastAPI application and using AWS Lambda to deploy it.

**Pydantic Module Error**
There seems to be an issue with pydantic - "No module named 'pydantic_core._pydantic_core'", 
but this command:

pip3 install -r requirements.txt --platform manylinux2014_x86_64 --target=dependencies 
--implementation cp --python-version 3.10 --only-binary=:all: --upgrade openai

seems to work. So a workflow can be as such:

1. Create virtual environment 
    python3.10 -m venv venv
2. Install dependencies
    pip3 install fastapi uvicorn mangum
3. Add dependencies into requirments file
    pip3 freeze > requirements.txt 
4. Use workaround command 
    pip3 install -r requirements.txt --platform manylinux2014_x86_64 --target=dependencies --implementation cp --python-version 3.10 --only-binary=:all: --upgrade openai
5.  Load the dependencies into a zip file
    cd dependencies; zip ../aws_lambda_artifact.zip -r .
6. Add the main.py file into the zip file
    zip aws_lambda_artifact.zip -u main.py   
