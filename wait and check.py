from selenium.webdriver.chrome.webdriver import WebDriver
import execute2_js, download_file
import math, time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if __name__== "__main__":
    brw = execute2_js.open_page("http://suninjuly.github.io/explicit_wait2.html")
    brw.implicitly_wait(12)

    price = brw.find_element_by_id('price')

    btn = brw.find_element_by_id("book")
    WebDriverWait(brw,10).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    btn.click()
    
    x=brw.find_element_by_id('input_value').text
    x=int(x)
    rez = math.log(abs(12*math.sin(x)))

    pole = download_file.text_input(brw, "text", str(rez))
    btn = download_file.btn_click(brw, "#solve")
    time.sleep(5)
    brw.quit

