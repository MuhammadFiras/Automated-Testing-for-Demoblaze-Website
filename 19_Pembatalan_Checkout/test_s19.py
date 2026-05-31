import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_s19_pembatalan_checkout(driver, subtests):
    driver.get("https://www.demoblaze.com/")
    wait = WebDriverWait(driver, 10)
    
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Samsung galaxy s6')]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Add to cart']"))).click()
    wait.until(EC.alert_is_present()).accept()
    driver.find_element(By.ID, "cartur").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
    
    tombol_close = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='orderModal']//button[text()='Close']")))

    with subtests.test(msg="S19 [POSITIF] - Menutup form tanpa transaksi"):
        driver.find_element(By.ID, "name").send_keys("Batal Beli")
        tombol_close.click()
        time.sleep(1)
        
        modal = driver.find_element(By.ID, "orderModal")
        assert not modal.is_displayed()

    with subtests.test(msg="S19 [NEGATIF] - Memeriksa keranjang setelah batal"):
        baris_produk = driver.find_elements(By.XPATH, "//tbody[@id='tbodyid']/tr")
        assert len(baris_produk) > 0 # Items should still be there