from types import TracebackType
from typing import Type
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time
import booking.constants as const

class Booking(webdriver.Firefox):
    def __init__(self,driver_path=r"C:\Users\saran\Downloads\Firefox_Selenium",teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ["PATH"]+=self.driver_path
        super(Booking,self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()
    
    def __exit__(self, exc_type: type[BaseException] | None, exc: BaseException | None, traceback: TracebackType | None):
            if self.teardown:
                self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def close_popup(self):
        try:
            no_button = self.find_element(By.CSS_SELECTOR,'button[aria-label="Dismiss sign-in info."]')
            no_button.click()
        except:
            print('No element with this class name. Skipping ....')

    def check_currency(self,currency=None):
        currency_element=self.find_element(By.CSS_SELECTOR,'button[data-testid="header-currency-picker-trigger"]')
        currency_span = currency_element.find_element(By.CLASS_NAME,"e4adce92df")
        currency_text=currency_span.text
        if currency_text==currency:
            return True
        else:
            return False

    
    def change_currency(self,currency=None):
        currency_element=self.find_element(By.CSS_SELECTOR,'button[data-testid="header-currency-picker-trigger"]')
        currency_element.click()
        currency_button = self.find_element(By.XPATH,"//button[.//div[text()='" + currency + "']]")
        currency_button.click()


    
    def select_destination(self,destination=None): 
        search_field=self.find_element(By.NAME,"ss")
        search_field.clear()
        search_field.send_keys(destination)

        time.sleep(1)
        
        first_result=self.find_element(By.ID,"autocomplete-result-0")
        first_result.click()

       


