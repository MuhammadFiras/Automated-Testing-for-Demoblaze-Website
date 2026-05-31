import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_s15_kalkulasi_total_cart(driver, subtests):
    driver.get("https://www.demoblaze.com/cart.html")
    wait = WebDriverWait(driver, 10)
    time.sleep(2)

    with subtests.test(msg="S15 [NEGATIF] - Menghitung total saat keranjang kosong"):
        total_harga = driver.find_element(By.ID, "totalp").text
        assert total_harga == "", "Bug: Total shows a value even when cart is empty!"

    with subtests.test(msg="S15 [POSITIF] - Menghitung total harga produk"):
        # Add an item to test calculation
        driver.find_element(By.ID, "nava").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Samsung galaxy s6')]"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Add to cart']"))).click()
        wait.until(EC.alert_is_present()).accept()
        
        driver.find_element(By.ID, "cartur").click()
        time.sleep(2)
        
        total_harga = driver.find_element(By.ID, "totalp").text
        assert int(total_harga) == 360 # Samsung S6 costs 360