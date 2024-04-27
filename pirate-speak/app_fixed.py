from langserve.client import RemoteRunnable

runnable = RemoteRunnable("http://localhost:8000/pirate-speak")

input_data= {
    "chat_history": [
    ],
    "text": "Hey there How Are you? How are things up with you?"
  }

print(runnable.invoke(input_data))


