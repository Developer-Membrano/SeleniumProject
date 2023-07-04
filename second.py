from selenium.webdriver.remote.webelement import WebElement

def validateInput():
    while True:
        user_input = input("Please enter your input: ")
        try:
            if isinstance(user_input, WebElement):
                break
        except TypeError:
            print("The input is neither a WebElement nor iterable.")
    
validateInput()