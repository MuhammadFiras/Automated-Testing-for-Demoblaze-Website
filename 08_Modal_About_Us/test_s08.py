import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_s08_modal_about_us(driver, subtests):
    driver.get("https://www.demoblaze.com/")
    wait = WebDriverWait(driver, 10)

    # Buka modal About Us
    driver.find_element(By.XPATH, "//a[contains(text(), 'About us')]").click()
    
    # Tunggu sampai modal dan video muncul
    video_modal = wait.until(EC.visibility_of_element_located((By.ID, "videoModal")))
    tombol_close = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='videoModal']//button[text()='Close']")))

    with subtests.test(msg="S08 [POSITIF] - Membuka dan memutar video profil"):
        # Kita memverifikasi bahwa modal benar-benar terbuka di layar
        assert video_modal.is_displayed()
        time.sleep(1) # Jeda menonton sebentar

    with subtests.test(msg="S08 [NEGATIF] - Menutup modal saat video berjalan"):
        tombol_close.click()
        time.sleep(1) # Tunggu animasi modal menutup
        
        # Verifikasi bahwa modal sudah benar-benar hilang dari layar
        assert not video_modal.is_displayed(), "Bug: Modal video gagal tertutup!"