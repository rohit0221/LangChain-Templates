import requests
import streamlit as st
import json


def extract_output_from_event_stream(event_stream):
    # Split the event stream into lines
    lines = event_stream.strip().split('\n')
    
    # Iterate over each line
    for line in lines:
        # Check if the line contains the "output" field
        if line.startswith("data:"):
            # Extract the JSON data from the line
            data_json = json.loads(line[5:])
            # Check if the "output" field exists
            if "output" in data_json:
                return data_json["output"]
# Example event stream
event_stream = """
event: metadata
data: {"run_id": "ce343be7-f011-41be-9fc8-5d5e9f20c097"}

event: data
data: {"output":"Visionary entrepreneur, SpaceX, Tesla, Neuralink, Boring Company, innovative thinker.","messages":[{"content":"Visionary entrepreneur, SpaceX, Tesla, Neuralink, Boring Company, innovative thinker.","additional_kwargs":{},"response_metadata":{},"type":"ai","name":null,"id":null,"example":false,"tool_calls":[],"invalid_tool_calls":[]}]}

event: end
"""

def get_tivaly_response(user_input):
    response=requests.post(
        "http://localhost:8000/openai-functions-agent/stream",
        json={
                "input": {
                    "input": user_input,
                    "chat_history": [
                    ]
                },
                "config": {},
                "kwargs": {}
                })
    #return response.json()['output']['content']
    return response.text
    


user_input = input("Enter a string: ")

response=get_tivaly_response(user_input)
output = extract_output_from_event_stream(response)
print(output)