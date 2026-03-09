from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from concurrent.futures import ThreadPoolExecutor

USERNAME = "adityatawade_m81z7A"
ACCESS_KEY = "a6BgJqW7YyqrzfqJHRbq"

URL = "https://elpais.com/opinion/"

configs = [
    {"browser": "Chrome", "os": "Windows", "osVersion": "10"},
    {"browser": "Firefox", "os": "Windows", "osVersion": "10"},
    {"browser": "Edge", "os": "Windows", "osVersion": "11"},
    {"browser": "Chrome", "os": "OS X", "osVersion": "Ventura"},
    {"browser": "Firefox", "os": "OS X", "osVersion": "Ventura"}
]


def run_test(config):

    options = Options()

    options.set_capability("browserName", config["browser"])
    options.set_capability("browserVersion", "latest")

    options.set_capability("bstack:options", {
        "os": config["os"],
        "osVersion": config["osVersion"],
        "sessionName": "BrowserStack Parallel Assignment Test"
    })

    driver = webdriver.Remote(
        command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub",
        options=options
    )

    driver.get(URL)

    print("Opened:", driver.title)

    driver.quit()


with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(run_test, configs)