import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from nicegui_app.front import init

app = FastAPI()


@app.get("/")
def read_root():
    return RedirectResponse(url="/chuck")


init(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
