import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_s17_modal_place_order(driver, subtests):
    driver.get("https://www.demoblaze.com/cart.html")
    wait = WebDriverWait(driver, 10)
    time.sleep(2)

    tombol_place_order = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']")))

    with subtests.test(msg="S17 [NEGATIF] - Membuka form dengan keranjang kosong"):
        tombol_place_order.click()
        
        modal_total = wait.until(EC.visibility_of_element_located((By.ID, "totalm"))).text
        assert modal_total != "Total: 0", "Bug: System allows placing an order with $0 empty cart!"
        
        # Close it if it incorrectly opened
        driver.find_element(By.XPATH, "//*[@id='orderModal']//button[text()='Close']").click()
        time.sleep(1)

    with subtests.test(msg="S17 [POSITIF] - Membuka form tagihan"):
        # Add an item to test positive flow
        driver.find_element(By.ID, "nava").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Samsung galaxy s6')]"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Add to cart']"))).click()
        wait.until(EC.alert_is_present()).accept()
        
        driver.find_element(By.ID, "cartur").click()
        time.sleep(2)
        
        driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
        modal_order = wait.until(EC.visibility_of_element_located((By.ID, "orderModal")))
        assert modal_order.is_displayed()