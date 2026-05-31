import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_s01_validasi_sign_up(driver, subtests):
    driver.get("https://www.demoblaze.com/")
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.ID, "signin2").click()
    tombol_signup = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='signInModal']//button[text()='Sign up']")))

    with subtests.test(msg="S01 [NEGATIF] - Daftar form kosong"):
        tombol_signup.click()
        alert = wait.until(EC.alert_is_present())
        assert alert.text == "Please fill out Username and Password."
        alert.accept()

    with subtests.test(msg="S01 [POSITIF] - Daftar data benar"):
        username_unik = f"userqa_{int(time.time())}" 
        driver.find_element(By.ID, "sign-username").send_keys(username_unik)
        driver.find_element(By.ID, "sign-password").send_keys("password123")
        tombol_signup.click()
        
        alert = wait.until(EC.alert_is_present())
        assert alert.text == "Sign up successful."
        alert.accept()