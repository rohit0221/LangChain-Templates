import requests

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

user_input = input("Enter a string: ")

print(get_pirate_response(user_input))