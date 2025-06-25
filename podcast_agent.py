import asyncio
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from dotenv import load_dotenv

load_dotenv(".env", override=True)

from langchain_google_genai import ChatGoogleGenerativeAI

from browser_use import Agent
from browser_use.browser import BrowserProfile, BrowserSession

browser_profile = BrowserProfile(
	# NOTE: you need to close your chrome browser - so that this can open your browser in debug mode
	executable_path='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
	headless=False,
)
browser_session = BrowserSession(browser_profile=browser_profile)

domain = "https://axiom.discover"
trade_path = "/trade"
pulse_path = "/pulse"

prompt_template = f"""
Go to https://axiom.trade
You will click login button through login
input email: {os.getenv("AXIOM_EMAIL")}
password: {os.getenv("AXIOM_PASSWORD")}
Then, click Login

You are an agent that go to {domain + trade_path} and browse the trade options. \
1. select top 5 newly creation meme coin
2. click on those 5 coins and check their pricing change
3. go to {domain + pulse_path} and check the 'New Pair', 'Final stretch' and 'Migrated' of those 5 coins
and repeat
"""

async def main():
	agent = Agent(
		task=prompt_template,
		llm=ChatGoogleGenerativeAI(model='gemini-2.0-flash', api_key=os.getenv("GOOGLE_API_KEY")),
		browser_session=browser_session,
	)

	await agent.run()
	#await browser_session.close()

	input('Press Enter to close...')


if __name__ == '__main__':
	asyncio.run(main())
