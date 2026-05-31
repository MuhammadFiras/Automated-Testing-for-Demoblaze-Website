import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_s20_konfirmasi_pembelian(driver, subtests):
    driver.get("https://www.demoblaze.com/")
    wait = WebDriverWait(driver, 10)
    
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Samsung galaxy s6')]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Add to cart']"))).click()
    wait.until(EC.alert_is_present()).accept()
    driver.find_element(By.ID, "cartur").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[text()='Place Order']").click()

    with subtests.test(msg="S20 [POSITIF] - Menyelesaikan seluruh transaksi"):
        wait.until(EC.element_to_be_clickable((By.ID, "name"))).send_keys("Test User")
        driver.find_element(By.ID, "card").send_keys("1234567890")
        driver.find_element(By.XPATH, "//*[@id='orderModal']//button[text()='Purchase']").click()
        
        success_popup = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Thank you for your purchase!')]")))
        assert success_popup.is_displayed()
        
        # Click OK on SweetAlert to finish
        driver.find_element(By.XPATH, "//button[contains(text(), 'OK')]").click()
        time.sleep(2)

    with subtests.test(msg="S20 [NEGATIF] - Verifikasi keranjang setelah transaksi selesai"):
        driver.find_element(By.ID, "cartur").click()
        time.sleep(2)
        
        baris_produk = driver.find_elements(By.XPATH, "//tbody[@id='tbodyid']/tr")
        # A good system clears the cart. If it's > 0, we found a bug!
        assert len(baris_produk) == 0, "Bug: Cart is not empty after a successful purchase!"