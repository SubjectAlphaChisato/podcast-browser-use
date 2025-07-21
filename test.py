from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

opts = webdriver.ChromeOptions()
opts.add_experimental_option("debuggerAddress", "127.0.0.1:9222")  # same port
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=opts,
)

target_url = "https://axiom.trade/meme/4RAXtS5H48akD1q2oJnXEsWeB4XQBhGpKVugZCBgsN6Q"
driver.execute_script("window.open(arguments[0], '_blank');", target_url)
driver.switch_to.window(driver.window_handles[-1])  # last handle == new tab

# # (B)  ── OR: focus an **existing** tab that already has the URL open
# for handle in driver.window_handles:
#     driver.switch_to.window(handle)
#     if target_url in driver.current_url:
#         break            # we are now “on” that tab

# # Optional: also raise the tab to the top of the browser’s UI
# driver.execute_cdp_cmd("Page.bringToFront", {})      # Chrome / Edge only