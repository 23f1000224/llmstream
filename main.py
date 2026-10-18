
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

ANSWER = {
    "A": {
        "text": "Report job-f66b8fd: café\nReady ✓",
        "complete": True,
        "error": None,
    },
    "B": {
        "text": "Partial job-f66b8fd",
        "complete": False,
        "error": None,
    },
    "C": {
        "text": "Draft job-f66b8fd",
        "complete": False,
        "error": "model unloaded",
    },
}


@app.get("/")
def get_answer():
    return JSONResponse(content=ANSWER)
