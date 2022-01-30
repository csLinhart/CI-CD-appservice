from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import datetime

def timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def login (driver, user, password):
    driver.get('https://www.saucedemo.com/')
    driver.find_element_by_css_selector("input[id='user-name']").send_keys(user)
    driver.find_element_by_css_selector("input[id='password']").send_keys(password)
    driver.find_element_by_id("login-button").click()
    assert 'https://www.saucedemo.com/inventory.html' in driver.current_url
    print(timestamp() +' Loggged in with user: '+ user)

def add_cart(driver,n):
    acum = 0
    for i in range(n):
        element = "a[id='item_" + str(i) + "_title_link']"
        driver.find_element_by_css_selector(element).click()
        driver.find_element_by_css_selector("button.btn_primary.btn_inventory").click()
        product = driver.find_element_by_css_selector("div[class='inventory_details_name large_size']").text
        print(timestamp() + " " + product + " added to shopping cart!")
        driver.find_element_by_css_selector("button.inventory_details_back_button").click()
        acum +=1
    print(timestamp() +' '+ str(acum) + ' items were added to the shopping cart.')

def remove_cart(driver,n):
    acum = 0
    for i in range(n):
        element = "a[id='item_" + str(i) + "_title_link']"
        driver.find_element_by_css_selector(element).click()
        driver.find_element_by_css_selector("button.btn_secondary.btn_inventory").click()
        product = driver.find_element_by_css_selector("div[class='inventory_details_name large_size']").text
        print(timestamp() + " " + product + " removed from shopping cart!")
        driver.find_element_by_css_selector("button.inventory_details_back_button").click()
        acum += 1
    print(timestamp() +' '+ str(acum) + ' items were removed from the shopping cart.')

if __name__ == "__main__":
    print(timestamp() + 'Tests start...')
    options = ChromeOptions()
    options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)

    print(timestamp()+' Browser was launched. Navigating to the login page...')

    login(driver, 'standard_user', 'secret_sauce')
    add_cart(driver, 6)
    remove_cart(driver, 6)

    print(timestamp() + ' Selenium Tests were executed successfully!')