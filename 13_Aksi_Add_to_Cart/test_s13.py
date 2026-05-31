import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException

def test_s13_aksi_add_to_cart(driver, subtests):
    driver.get("https://www.demoblaze.com/")
    wait = WebDriverWait(driver, 10)

    # Open a product detail page
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Samsung galaxy s6')]"))).click()
    tombol_add = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Add to cart']")))

    with subtests.test(msg="S13 [NEGATIF] - Mengabaikan alert konfirmasi"):
        tombol_add.click()
        wait.until(EC.alert_is_present())
        
        try:
            # Attempt to click the Home button while the alert is active
            driver.find_element(By.ID, "nava").click()
            assert False, "Bug: User can interact with background UI while alert is open!"
        except UnexpectedAlertPresentException:
            # This exception is exactly what we want (UI is blocked)
            assert True 

    with subtests.test(msg="S13 [POSITIF] - Menambahkan item ke keranjang"):
        alert = driver.switch_to.alert
        assert alert.text == "Product added"
        alert.accept()