import execute2_js, download_file
import math, time


brw = execute2_js.open_page(r"http://suninjuly.github.io/alert_accept.html")
btn = download_file.btn_click(brw, ".btn")
alert = brw.switch_to.alert
alert.accept()
time.sleep(1)
x = int(brw.find_element_by_id('input_value').text)
print(x)
rez = math.log(abs(12*math.sin(x)))
inp = download_file.text_input(brw, "text", str(rez))

btn = download_file.btn_click(brw, ".btn")

time.sleep(5)
brw.quit()
