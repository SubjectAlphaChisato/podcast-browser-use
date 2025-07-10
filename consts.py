DOMAIN = "https://axiom.trade"
TRADE_PATH = "/discover"
PULSE_PATH = "/pulse"

prompt_template = f"""
Go to {DOMAIN}

You are an agent that go to {DOMAIN + TRADE_PATH} and browse the trade options. \
1. select top 5 newly creation meme coin
2. click on those 5 coins ONE BY ONE and check their pricing change
3. go to {DOMAIN + PULSE_PATH} and check the 'New Pair', 'Final stretch' and 'Migrated' of these 5 coins one by one
"""

portfolio_prompt = f"""
Go to {DOMAIN}

you will go to {DOMAIN}/portfolio to check portfolio
"""