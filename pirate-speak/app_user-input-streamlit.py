import requests
import streamlit as st


def get_pirate_response(user_input):
    response=requests.post(
        "http://localhost:8000/pirate-speak/invoke",
        json={
                "input": {
                    "chat_history": [
                    ],
                    "text": user_input
                },
                "config": {},
                "kwargs": {}
                })
    return response.json()['output']['content']

st.title("Welcome to Pirate LangChain App⚓")
user_input = st.text_input("Enter a string: ")
if user_input:
    response=get_pirate_response(user_input)
    st.write(response)