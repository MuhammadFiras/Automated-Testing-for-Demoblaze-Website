import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_s16_hapus_item_keranjang(driver, subtests):
    # Setup: Add an item first
    driver.get("https://www.demoblaze.com/")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Samsung galaxy s6')]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Add to cart']"))).click()
    wait.until(EC.alert_is_present()).accept()
    
    driver.find_element(By.ID, "cartur").click()
    time.sleep(2)

    with subtests.test(msg="S16 [POSITIF] - Menghapus produk dari tabel"):
        tombol_delete = driver.find_element(By.XPATH, "//a[text()='Delete']")
        tombol_delete.click()
        time.sleep(2) # Wait for deletion to process
        
        baris_produk = driver.find_elements(By.XPATH, "//tbody[@id='tbodyid']/tr")
        assert len(baris_produk) == 0

    with subtests.test(msg="S16 [NEGATIF] - Sinkronisasi UI setelah penghapusan"):
        driver.refresh() # Force reload the page
        time.sleep(2)
        
        baris_produk = driver.find_elements(By.XPATH, "//tbody[@id='tbodyid']/tr")
        assert len(baris_produk) == 0, "Bug: Deleted item reappeared after refresh!"