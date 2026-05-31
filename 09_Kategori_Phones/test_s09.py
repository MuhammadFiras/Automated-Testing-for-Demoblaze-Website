import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_s09_kategori_phones(driver, subtests):
    driver.get("https://www.demoblaze.com/")
    wait = WebDriverWait(driver, 10)

    # Klik kategori Phones
    driver.find_element(By.XPATH, "//a[contains(text(), 'Phones')]").click()
    time.sleep(2) # Wajib jeda agar data AJAX Demoblaze selesai dimuat

    # Ambil seluruh teks dari halaman web saat ini
    halaman_sumber = driver.page_source

    with subtests.test(msg="S09 [POSITIF] - Memfilter daftar smartphone"):
        # Pastikan produk smartphone (misal Samsung) ada di halaman
        assert "Samsung galaxy s6" in halaman_sumber

    with subtests.test(msg="S09 [NEGATIF] - Memastikan isolasi kategori (tanpa kebocoran)"):
        # Pastikan produk Laptop tidak bocor ke kategori HP
        assert "Sony vaio i5" not in halaman_sumber, "Bug: Laptop muncul di kategori Phones!"