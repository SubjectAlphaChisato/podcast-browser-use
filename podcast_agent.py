import asyncio
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from dotenv import load_dotenv
from obsws_python import ReqClient, events

ws = ReqClient(host="localhost", port=4455, password="dreamfly")

load_dotenv(".env", override=True)

from browser_use.llm.google import ChatGoogle

from browser_use import Agent
from browser_use.browser import BrowserProfile, BrowserSession
from task_prompt import default_template
browser_profile = BrowserProfile(
	# NOTE: you need to close your chrome browser - so that this can open your browser in debug mode
	executable_path='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
	headless=False,
)
browser_session = BrowserSession(browser_profile=browser_profile)

domain = "https://axiom.trade"
trade_path = "/discover"
pulse_path = "/pulse"

prompt_template = f"""
Go to {domain}

You are an agent that go to {domain + trade_path} and browse the trade options. \
1. select top 5 newly creation meme coin
2. click on those 5 coins ONE BY ONE and check their pricing change
3. go to {domain + pulse_path} and check the 'New Pair', 'Final stretch' and 'Migrated' of these 5 coins one by one
"""

portfolio_prompt = f"""
Go to {domain}

you will go to https://axiom.trade/portfolio to check portfolio
"""

async def main():
	while True:
		ws.set_current_program_scene("mainScene")
		agent = Agent(
			task=prompt_template,
			llm=ChatGoogle(model='gemini-2.0-flash', api_key=os.getenv("GOOGLE_API_KEY")),
			browser_session=browser_session,
		)
		await agent.run()
		ws.set_current_program_scene("tradingVideo")
		await asyncio.sleep(300)  # Sleep for 5 minutes (300 seconds)

		# await browser_session.close()

		# input('Press Enter to close...')


if __name__ == '__main__':
	asyncio.run(main())
