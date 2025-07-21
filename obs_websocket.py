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
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

browser_session = BrowserSession(cdp_url="http://localhost:9222")

app = FastAPI()
# Create a single ReqClient instance
ws = ReqClient(host="localhost", port=4455, password="dreamfly")

def set_req_client(client):
    global ws
    ws = client


opts = webdriver.ChromeOptions()
opts.add_experimental_option("debuggerAddress", "127.0.0.1:9222")  # same port


@app.get("/buy_coin/{meme_id}")
async def buy_coin(meme_id: str):
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=opts,
    )
    if driver is not None and ws is not None:
        target_url = f'https://axiom.trade/meme/{meme_id}'
        driver.execute_script("window.open(arguments[0], '_blank');", target_url)
        driver.switch_to.window(driver.window_handles[-1])  # last handle == new tab
        ws.set_current_program_scene("mainScene")
        await asyncio.sleep(5)
        ws.set_current_program_scene("tradingVideo")
        return {"status": "done"}
    else:
        return {"status": "error", "message": "OBS WebSocket client not initialized"}

@app.get("/sell_coin")
async def sell_coin():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=opts,
    )
    if driver is not None and ws is not None:
        target_url = 'https://axiom.trade/portfolio'
        driver.execute_script("window.open(arguments[0], '_blank');", target_url)
        driver.switch_to.window(driver.window_handles[-1])  # last handle == new tab
        ws.set_current_program_scene("mainScene")
        await asyncio.sleep(5)
        ws.set_current_program_scene("tradingVideo")
        return {"status": "done"}
    else:
        return {"status": "error", "message": "OBS WebSocket client not initialized"}


