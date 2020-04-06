from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
  
def calc(x):
    return str(math.log(math.fabs(12*math.sin(x))))  
  
try:

   
    
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
    text = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )
    button = browser.find_element_by_class_name('btn')
    button.click()
     
    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)
     
    y = calc(x)
    
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    
    button1 = browser.find_element_by_id('solve')
    button1.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
