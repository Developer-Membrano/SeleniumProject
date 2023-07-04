from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook

def extract_data(url, search_query, output_file):
    driver = webdriver.Chrome()
    driver.get(url)
    wait = WebDriverWait(driver, 3)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "action")))

    SearchBox = driver.find_element(By.ID, "search")
    SearchBox.send_keys(search_query)
    SearchBox.send_keys(Keys.RETURN)

    wb = Workbook()
    # select the active worksheet
    ws = wb.active

    # define the output data
    header = ['Product Name', 'Price', 'Variety of Colors']
    data = []

    parentElements = driver.find_elements(By.CSS_SELECTOR, 'li.item')
    for productElement in parentElements:
        each_product_name = productElement.find_elements(By.CSS_SELECTOR, 'a.product-item-link')
        each_product_price = productElement.find_elements(By.CSS_SELECTOR, 'span.normal-price')
        each_product_size = productElement.find_elements(By.XPATH, '//*[@role="listbox"]')

        for productNameElement, priceElement, sizeOptions in zip(each_product_name, each_product_price, each_product_size):
            productName = productNameElement.text
            productPrice = priceElement.text
            
            sizes = sizeOptions.find_elements(By.CLASS_NAME, 'swatch-option')
            variety = ', '.join([size.get_attribute('aria-label') for size in sizes])
            data.append([productName, productPrice, variety])

    # write the header row
    ws.append(header)
    # write the data rows
    for row in data:
        ws.append(row)

    # save the workbook to a file
    wb.save(output_file)

    driver.quit()

extract_data("https://magento.softwaretestingboard.com/", "Men t-shirt", r'E:\Users\Angie Villalba\Documents\Kenny\Development\ProductExtracted.xlsx')
