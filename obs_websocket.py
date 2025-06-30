import asyncio
from fastapi import FastAPI, Request
from obsws_python import ReqClient, events

app = FastAPI()
ws = ReqClient(host="localhost", port=4455, password="dreamfly")

@app.post("/webhook/{sceneName}")
async def interrupt(request: Request):
    sceneName = request.path_params.get("sceneName")
    ws.set_current_program_scene(sceneName)
    return {"status": "done"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8088)
