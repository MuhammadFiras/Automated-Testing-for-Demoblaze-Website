import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_s10_kategori_laptops(driver, subtests):
    driver.get("https://www.demoblaze.com/")
    wait = WebDriverWait(driver, 10)

    # Klik kategori Laptops
    driver.find_element(By.XPATH, "//a[contains(text(), 'Laptops')]").click()
    time.sleep(2) # Jeda tunggu render produk

    halaman_sumber = driver.page_source

    with subtests.test(msg="S10 [POSITIF] - Memfilter daftar laptop"):
        # Pastikan produk Laptop ada di halaman
        assert "Sony vaio i5" in halaman_sumber

    with subtests.test(msg="S10 [NEGATIF] - Memastikan isolasi kategori (tanpa kebocoran)"):
        # Pastikan produk Smartphone tidak bocor ke kategori Laptop
        assert "Samsung galaxy s6" not in halaman_sumber, "Bug: HP muncul di kategori Laptops!"