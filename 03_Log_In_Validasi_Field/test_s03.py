from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_s03_validasi_field_login(driver, subtests):
    driver.get("https://www.demoblaze.com/")
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.ID, "login2").click()
    tombol_login = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='logInModal']//button[text()='Log in']")))

    with subtests.test(msg="S03 [NEGATIF] - Login form kosong"):
        tombol_login.click()
        alert = wait.until(EC.alert_is_present())
        assert alert.text == "Please fill out Username and Password."
        alert.accept()

    with subtests.test(msg="S03 [POSITIF] - Login kredensial benar"):
        driver.find_element(By.ID, "loginusername").send_keys("test")
        driver.find_element(By.ID, "loginpassword").send_keys("test")
        tombol_login.click()
        
        welcome_text = wait.until(EC.visibility_of_element_located((By.ID, "nameofuser")))
        assert "Welcome test" in welcome_text.text