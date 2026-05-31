import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_s18_validasi_form_checkout(driver, subtests):
    driver.get("https://www.demoblaze.com/")
    wait = WebDriverWait(driver, 10)
    
    # Setup: Add item and go to checkout
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Samsung galaxy s6')]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Add to cart']"))).click()
    wait.until(EC.alert_is_present()).accept()
    driver.find_element(By.ID, "cartur").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
    
    tombol_purchase = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='orderModal']//button[text()='Purchase']")))

    with subtests.test(msg="S18 [NEGATIF] - Mengosongkan form checkout wajib"):
        tombol_purchase.click()
        alert = wait.until(EC.alert_is_present())
        assert alert.text == "Please fill out Name and Creditcard."
        alert.accept()

    with subtests.test(msg="S18 [POSITIF] - Mengisi form checkout wajib"):
        driver.find_element(By.ID, "name").send_keys("Test User")
        driver.find_element(By.ID, "card").send_keys("1234567890")
        tombol_purchase.click()
        
        # Verify success popup (SweetAlert)
        success_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".sa-success")))
        assert success_icon.is_displayed()