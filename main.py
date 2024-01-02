from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
app = FastAPI()

app.mount("/static", StaticFiles(directory="static", html=True), "static")
@app.get("/", response_class=FileResponse)
async def root():
    return FileResponse("static/index.html")