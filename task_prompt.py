import os
domain = "https://axiom.discover"
trade_path = "/trade"
pulse_path = "/pulse"
default_template = f"""
Go to {domain}
You will click login button through login
input email: {os.getenv("AXIOM_EMAIL")}
password: {os.getenv("AXIOM_PASSWORD")}
Then, click Login

You are an agent that go to {domain + trade_path} and browse the trade options. \
1. select top 5 newly creation meme coin
2. click on those 5 coins ONE BY ONE and click the coin board to their pricing change
"""
