from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
	browser = webdriver.Chrome()

	browser.get("http://suninjuly.github.io/explicit_wait2.html")

	WebDriverWait(browser, 12).until(
	EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
	
	
	button1 = browser.find_element_by_id("book")
	button1.click()
	
	button2 = browser.find_element_by_id("solve")
	browser.execute_script("return arguments[0].scrollIntoView(true);", button2)


	num = browser.find_element_by_id("input_value").text
	sum = math.log(abs(12*math.sin(int(num))))

	input = browser.find_element_by_id("answer")
	input.send_keys(str(sum)) 
	
	button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
