import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_s12_navigasi_detail_produk(driver, subtests):
    driver.get("https://www.demoblaze.com/")
    wait = WebDriverWait(driver, 10)

    # Tunggu sampai produk pertama muncul, lalu klik
    produk_pertama = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Samsung galaxy s6')]")))
    produk_pertama.click()

    with subtests.test(msg="S12 [POSITIF] - Membuka halaman spesifikasi produk"):
        # Verifikasi bahwa kita masuk ke halaman detail (ada tombol Add to cart)
        tombol_add_to_cart = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Add to cart')]")))
        assert tombol_add_to_cart.is_displayed()

    with subtests.test(msg="S12 [NEGATIF] - Navigasi paksa via tombol Back Browser"):
        # Perintahkan robot untuk menekan tombol 'Kembali' di browser
        driver.back()
        
        # Verifikasi bahwa sistem tidak rusak dan kembali memunculkan daftar kategori
        kategori_menu = wait.until(EC.visibility_of_element_located((By.ID, "cat")))
        assert kategori_menu.is_displayed(), "Bug: Sistem rusak setelah menekan tombol Back!"