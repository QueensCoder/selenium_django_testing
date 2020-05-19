from selenium import webdriver


try:
    browser = webdriver.Chrome()
    browser.get('https://www.google.com')
    # if google not in title will throw assertion error
    assert 'Google' in browser.title
    print(browser.title, '<><><><>')

finally:
    browser.quit()
