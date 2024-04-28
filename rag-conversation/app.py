from langserve.client import RemoteRunnable

runnable = RemoteRunnable("http://localhost:8000/openai-functions-agent")

input_data= {
    "input": "Tell me about Elon Musk in 10 words",
    "chat_history": [
    ]
  }

print(runnable.invoke(input_data))