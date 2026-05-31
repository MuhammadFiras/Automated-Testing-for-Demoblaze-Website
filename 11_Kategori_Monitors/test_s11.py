import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_s11_kategori_monitors(driver, subtests):
    driver.get("https://www.demoblaze.com/")
    wait = WebDriverWait(driver, 10)

    # Klik kategori Monitors
    driver.find_element(By.XPATH, "//a[contains(text(), 'Monitors')]").click()
    time.sleep(2) # Jeda tunggu render produk

    halaman_sumber = driver.page_source

    with subtests.test(msg="S11 [POSITIF] - Memfilter daftar monitor"):
        # Pastikan produk Monitor ada di halaman
        assert "Apple monitor 24" in halaman_sumber

    with subtests.test(msg="S11 [NEGATIF] - Memastikan isolasi kategori (tanpa kebocoran)"):
        # Pastikan produk Laptop tidak bocor ke kategori Monitor
        assert "Sony vaio i5" not in halaman_sumber, "Bug: Laptop muncul di kategori Monitors!"