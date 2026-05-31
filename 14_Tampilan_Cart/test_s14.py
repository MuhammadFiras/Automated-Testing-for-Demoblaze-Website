import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_s14_tampilan_cart(driver, subtests):
    driver.get("https://www.demoblaze.com/")
    wait = WebDriverWait(driver, 10)

    with subtests.test(msg="S14 [NEGATIF] - Membuka keranjang dengan cache kosong"):
        driver.find_element(By.ID, "cartur").click()
        time.sleep(2) # Wait for AJAX cart render
        
        # Verify the table body has no product rows
        baris_produk = driver.find_elements(By.XPATH, "//tbody[@id='tbodyid']/tr")
        assert len(baris_produk) == 0

    with subtests.test(msg="S14 [POSITIF] - Memeriksa item yang dimasukkan"):
        driver.find_element(By.ID, "nava").click() # Go Home
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Samsung galaxy s6')]"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Add to cart']"))).click()
        wait.until(EC.alert_is_present()).accept()
        
        driver.find_element(By.ID, "cartur").click()
        time.sleep(2)
        
        baris_produk = driver.find_elements(By.XPATH, "//tbody[@id='tbodyid']/tr")
        assert len(baris_produk) > 0 # At least 1 item exists