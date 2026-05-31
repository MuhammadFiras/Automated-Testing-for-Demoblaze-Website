import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_s07_pengiriman_form_contact(driver, subtests):
    driver.get("https://www.demoblaze.com/")
    wait = WebDriverWait(driver, 10)

    # Open Contact Modal
    driver.find_element(By.XPATH, "//a[contains(text(), 'Contact')]").click()
    tombol_send = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='exampleModal']//button[text()='Send message']")))

    with subtests.test(msg="S07 [NEGATIF] - Mengirim pesan dengan form kosong"):
        tombol_send.click()
        
        alert = wait.until(EC.alert_is_present())
        # We expect the system to ask to fill out the form. 
        # If Demoblaze says "Thanks for the message!!" instead, this test will accurately fail to highlight the bug.
        assert alert.text != "Thanks for the message!!", "Bug found: System accepts empty contact forms!"
        alert.accept()

    with subtests.test(msg="S07 [POSITIF] - Mengirim pesan dengan form lengkap"):
        driver.find_element(By.ID, "recipient-email").send_keys("qa_test@email.com")
        driver.find_element(By.ID, "recipient-name").send_keys("QA Tester")
        driver.find_element(By.ID, "message-text").send_keys("Hello, this is an automated test message.")
        
        tombol_send.click()
        
        alert = wait.until(EC.alert_is_present())
        assert alert.text == "Thanks for the message!!"
        alert.accept()