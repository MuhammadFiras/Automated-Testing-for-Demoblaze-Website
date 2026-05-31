from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_s06_fitur_log_out(driver, subtests):
    driver.get("https://www.demoblaze.com/")
    wait = WebDriverWait(driver, 10)

    with subtests.test(msg="S06 [NEGATIF] - Tombol logout tidak ada saat belum login"):
        # Check if the display property of the logout button is hidden
        logout_button = driver.find_element(By.ID, "logout2")
        assert not logout_button.is_displayed(), "Bug: Log out button is visible to guests!"

    with subtests.test(msg="S06 [POSITIF] - Mengakhiri sesi pengguna"):
        # We must log in first to test the log out functionality
        driver.find_element(By.ID, "login2").click()
        wait.until(EC.element_to_be_clickable((By.ID, "loginusername"))).send_keys("test")
        driver.find_element(By.ID, "loginpassword").send_keys("test")
        driver.find_element(By.XPATH, "//*[@id='logInModal']//button[text()='Log in']").click()
        
        # Wait until we are fully logged in
        wait.until(EC.visibility_of_element_located((By.ID, "nameofuser")))
        
        # Now perform the Log Out action
        driver.find_element(By.ID, "logout2").click()
        
        # Verify the Log In button reappears, proving the session ended
        login_button_navbar = wait.until(EC.visibility_of_element_located((By.ID, "login2")))
        assert login_button_navbar.is_displayed()