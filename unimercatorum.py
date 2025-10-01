from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def login_and_fetch_material(username, password):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://piattaforma.unimercatorum.it")

        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "loginbtn").click()

        time.sleep(3)  # Attendi il login

        driver.get("https://piattaforma.unimercatorum.it/materiali")
        time.sleep(2)

        materials = driver.find_elements(By.CLASS_NAME, "material-title")
        titles = [m.text for m in materials]

    except Exception as e:
        titles = [f"Errore: {str(e)}"]

    finally:
        driver.quit()

    return titles
