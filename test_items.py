import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_item(browser):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': "fr"})
    browser = webdriver.Chrome(options=options)
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    button = browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    assert button, "Кнопка не найдена"
    time.sleep(3)
