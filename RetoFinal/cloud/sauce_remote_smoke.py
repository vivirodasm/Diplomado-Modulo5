
import os
from selenium.webdriver.remote.client_config import ClientConfig

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait

username = os.environ["SAUCE_USERNAME"]
access_key = os.environ["SAUCE_ACCESS_KEY"]

options = Options()
options.browser_version = "latest"
options.platform_name = "Windows 11"
options.set_capability("sauce:options", {
    "name": "Reto Final Modulo 5 - Filtro Hogar",
    "tunnelName": "reto-final-modulo5",
    "build": "RetoFinal-Fase4",
})

url = "https://ondemand.us-west-1.saucelabs.com:443/wd/hub"

client_config = ClientConfig(
    remote_server_addr=url,
    username=username,
    password=access_key,
)

driver = None

try:
    driver = webdriver.Remote(
    command_executor=url,
    options=options,
    client_config=client_config,
)
    driver.get("http://127.0.0.1:3000")

    wait = WebDriverWait(driver, 30)

    wait.until(
        lambda d: len(d.find_elements(By.CSS_SELECTOR, "[data-testid='grid-productos'] .card")) == 24
    )

    filtro = wait.until(
        lambda d: d.find_element(By.CSS_SELECTOR, "[data-testid='filtro-categoria']")
    )
    Select(filtro).select_by_value("hogar")

    wait.until(
        lambda d: len(d.find_elements(By.CSS_SELECTOR, "[data-testid='grid-productos'] .card")) == 6
    )

    productos = driver.find_elements(
        By.CSS_SELECTOR, "[data-testid='grid-productos'] .card"
    )

    assert all(
        producto.get_attribute("data-categoria") == "hogar"
        for producto in productos
    ), "Se encontraron productos de otra categoria"

    print("PASSED: Sauce Labs - 6 productos de categoria Hogar")

    driver.execute_script(
        "sauce:job-result=passed"
    )

except Exception:
    if driver:
        driver.execute_script("sauce:job-result=failed")
    raise

finally:
    if driver:
        driver.quit()
