import requests
import streamlit as st


def get_tivaly_response(user_input):
    response=requests.post(
        "http://localhost:8000/openai-functions-agent/invoke",
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
    return response.json()

st.title("Welcome to Tivaly Search Api app")
user_input = st.text_input("Tell me about: ")
if user_input:
    response=get_tivaly_response(user_input)
    st.write(response)