This repository underlines the process in creating a FastAPI application and using AWS Lambda to deploy it.

**Pydantic Module Error**

There seems to be an issue with pydantic - "No module named 'pydantic_core.\_pydantic_core'",
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
5. Load the dependencies into a zip file
   cd dependencies; zip ../aws_lambda_artifact.zip -r .
6. Add the main.py file into the zip file
   zip aws_lambda_artifact.zip -u main.py

When modify the zip file that will be used as the Code for the LambdaFunction in our CFN template, we must include all dependencies, as well as the main.py file and our db folder which contains the dynamo.py file. In order to tackle this, run these commands:

1.(cd dependencies; zip -r ../aws_lambda_artifact_v5.zip .) && (cd db; zip -ru ../aws_lambda_artifact_v5.zip .) 2. zip aws_lambda_artifact_v4.zip -u db
3.zip -r aws_lambda_artifact_v5.zip main.py

Helpful tip:
When obtaining the amazon resource name (ARN) of our dynamo db, run this query:
aws dynamodb describe-table --table-name [TableName] --query "Table.TableArn"
where TableName is the name of the DynamoDB table we want the ARN for.
