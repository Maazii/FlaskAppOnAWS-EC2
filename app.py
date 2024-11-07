from flask import Flask, request, jsonify
import time
import random
import string
from typing import Dict
import asyncio
from collections import deque

mockAIServer = Flask(__name__)

# Initiation of the queue instance
queue = deque()

# Basic function to generate alphanumerics for IDs
async def generate_random_string(size=6):
    myString = string.ascii_letters + string.digits
    randString = ''.join(random.choices(myString, k=size))
    return randString

# Function to create the JSON object absent of user input strictly for predictionID
async def nthPrediction():
    randomid = await generate_random_string()
    output = {"message": "Request Recevied. Processing Asynchronously.", "prediction_id": randomid}
    return output

# The Mock Model Predict function
async def mock_model_predict(input: str) -> Dict[str, str]:
    time.sleep(random.randint(10, 17)) # Simulate processing delay 
    result = str(random.randint(1000, 20000)) 
    output = {"input": input, "result": result} 
    return output

# Home Endpoint
@mockAIServer.route('/', methods=['GET', 'POST'])
async def index():
    return "Hello World!", 200

# Prediction Endpoint
@mockAIServer.route('/predict', methods=['GET', 'POST'])
async def prediction():
    if request.method == 'POST':
        pID = await nthPrediction()
        print(jsonify(pID))
        data = request.json # fetch data sent in the POST request
        predictionInput = data.get('input')
        result = await mock_model_predict(str(predictionInput))
        final = {"prediction_id": pID["prediction_id"], "input": result["input"], "result": result["result"]} 
        queue.append(final) # add the final object to the queue
        return result, 202

    else:
        return "Please use curl.", 200
    
# Dynamic Endpoint for accessing data about individual predictions
@mockAIServer.route('/predict/<predictionID>', methods=['GET'])
async def getnthPredictionInfo(predictionID):
    check1="prediction_id"
    check2="input"
    for obj in queue:
        if obj.get(check1) == str(predictionID):
            if check2 not in obj:
                return {"error": "Being processed"}, 404  
            return obj, 200
        else:
            continue
    return {"error": "ID not found"}, 404

# Display Whole Queue Endpoint   
@mockAIServer.route('/ViewAllPredictions', methods=['GET'])
async def getter():
    if not queue:
        return "No prediction history!"
    else:
        return list(queue)

if __name__ == '__main__':

    mockAIServer.run(host='0.0.0.0', debug=True, port=5000)