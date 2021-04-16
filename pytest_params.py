
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, math, pytest

#1) открываем один браузер
#2) вставляем значение времени
#3) жмем кнопку
#4) ждем появления ответа
#5) Сравниваем ответ
#6) если ошибка, тогда сохраняем его в строку
rezult = []

@pytest.fixture()
def open_browser ():
    brows = webdriver.Chrome()
    brows.implicitly_wait(10)
    yield brows
    brows.quit()

#

class TestAlien():
    @pytest.mark.parametrize('id',['236895','236896','236897', '236898', '236899', "236903", '236904', '236905'])
    def testlink(self, open_browser, id):
        self.link = f"https://stepik.org/lesson/{id}/step/1"
        open_browser.get(self.link)
        #time.sleep(10)
        self.textarea = open_browser.find_element_by_tag_name("textarea")
        self.textarea.send_keys(str(math.log(int(time.time()))))
        open_browser.find_element_by_class_name("submit-submission").click()
        self.rez = open_browser.find_element_by_css_selector(".smart-hints__feedback > pre.smart-hints__hint").text
        try:
            assert self.rez=="Correct", "Response is not correct"
        except:
            rezult.append(self.rez)

print(' '.join(rezult))