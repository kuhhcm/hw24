from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook


chrome = webdriver.Chrome()
chrome.get('https://www.saucedemo.com/')

username = chrome.find_element(By.ID, 'user-name')
password = chrome.find_element(By.NAME, 'password')
username.send_keys('standard_user')
password.send_keys('secret_sauce')
login_button = chrome.find_element(By.NAME, 'login-button')
login_button.click()


wb = Workbook()
sheet = wb.active

sheet['A1'] = '№'
for i in range(2,7):
    sheet[f'A{i}'] = f'{i-1}'

sheet['B1'] = 'Name'
name = chrome.find_elements(By.CLASS_NAME,'inventory_item_name')
for j, name in enumerate(name, start=2):
    sheet[f'B{j}'] = name.text

sheet['C1'] = 'Description'
desc = chrome.find_elements(By.CLASS_NAME,'inventory_item_desc')
for l, desc in enumerate(desc, start=2):
        sheet[f'C{l}'] = desc.text

sheet['D1'] = 'Price'
price = chrome.find_elements(By.CLASS_NAME,'inventory_item_price')
for a, price in enumerate(price, start=2):
        sheet[f'D{a}'] = price.text


wb.save('lesson24.xlsx')