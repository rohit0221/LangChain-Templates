from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


# Edit this to add the chain you want to add
from pirate_speak.chain import chain as pirate_speak_chain

add_routes(app, pirate_speak_chain, path="/pirate-speak")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
