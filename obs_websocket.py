import asyncio
import threading
from fastapi import FastAPI, Request
from obsws_python import ReqClient, events
from browser_use import Agent
from consts import portfolio_prompt
from browser_use.llm.google import ChatGoogle
from browser_use.browser import BrowserProfile, BrowserSession
from task_prompt import default_template
import os

browser_session = BrowserSession(cdp_url="http://localhost:9222")

app = FastAPI()
# Create a single ReqClient instance
ws = ReqClient(host="localhost", port=4455, password="dreamfly")

def set_req_client(client):
    global ws
    ws = client


@app.get("/trade")
async def trade():
    if ws is not None:
        ws.set_current_program_scene("mainScene")
        agent = Agent(
            task=portfolio_prompt,
            llm=ChatGoogle(model='gemini-2.0-flash', api_key=os.getenv("GOOGLE_API_KEY")),
            browser_session=browser_session,
        )
        await agent.run()
        await asyncio.sleep(10)
        ws.set_current_program_scene("mainScene")
        return {"status": "done"}
    else:
        return {"status": "error", "message": "OBS WebSocket client not initialized"}


