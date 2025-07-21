import asyncio
import os
import sys
import threading
from obs_websocket import app, ws
from consts import prompt_template
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from dotenv import load_dotenv
from obsws_python import ReqClient, events

load_dotenv(".env", override=True)

from browser_use.llm.google import ChatGoogle

from browser_use import Agent
from browser_use.browser import BrowserProfile, BrowserSession
from task_prompt import default_template

browser_profile = BrowserProfile()
browser_session = BrowserSession(browser_profile=browser_profile, cdp_url="http://localhost:9222")

def run_fastapi_server():
    """Function to run the FastAPI server in a separate thread"""
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8088)

async def agent_loop():
    """Main agent loop that runs the browser agent and controls OBS scenes"""
    while True:
        ws.set_current_program_scene("tradingVideo")
        # Sleep for 5 minutes (300 seconds)
        await asyncio.sleep(300)
        # ws.set_current_program_scene("mainScene")
        # agent = Agent(
        #     task=prompt_template,
        #     llm=ChatGoogle(model='gemini-2.0-flash', api_key=os.getenv("GOOGLE_API_KEY")),
        #     browser_session=browser_session,
        # )
        # await agent.run()
        
        # await browser_session.close()
        # input('Press Enter to close...')

async def main():
    """Main function that starts both the FastAPI server and agent loop"""
    # Start the FastAPI server in a separate thread
    server_thread = threading.Thread(target=run_fastapi_server, daemon=True)
    server_thread.start()
    
    print("FastAPI server started on http://0.0.0.0:8088")
    
    # Run the agent loop in the main thread
    await agent_loop()


if __name__ == '__main__':
	asyncio.run(main())
