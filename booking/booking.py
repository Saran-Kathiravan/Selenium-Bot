from types import TracebackType
from typing import Type
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time
from prettytable import PrettyTable

from selenium.common.exceptions import NoSuchElementException

from booking.booking_filters import BookingFilter
from booking.booking_report import BookingReport
import booking.constants as const
from booking.popup_closer import close_popup

class Booking(webdriver.Firefox):
    def __init__(self,driver_path=r"C:\Users\saran\Downloads\Firefox_Selenium",teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ["PATH"]+=self.driver_path
        super(Booking,self).__init__()
        self.maximize_window()
    
    def __exit__(self, exc_type: type[BaseException] | None, exc: BaseException | None, traceback: TracebackType | None):
            if self.teardown:
                self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

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
        currency_button = self.find_element(By.XPATH,"//button[.//div[text()='" +currency+ "']]")
        currency_button.click()


    
    def select_destination(self,destination=None): 
        search_field=self.find_element(By.NAME,"ss")
        search_field.clear()
        search_field.send_keys(destination)

        time.sleep(1)

        first_result=self.find_element(By.ID,"autocomplete-result-0")
        first_result.click()

        time.sleep(1)
        
    def check_availability(self):
        try:
            # Check if the div element with data-testid="searchbox-datepicker" exists
            searchbox_datepicker_div = self.find_element(By.XPATH,"//div[@data-testid='searchbox-datepicker']")
            # print("Div with data-testid='searchbox-datepicker' found on the page.")
        except NoSuchElementException:
            date_picker=self.find_element(By.XPATH,'//div[div[@data-testid="searchbox-dates-container"]]')
            date_picker.click()
        
        
    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(By.CSS_SELECTOR,'span[data-date="'+check_in_date+'"]')
        check_in_element.click()

        check_out_element = self.find_element(By.CSS_SELECTOR,'span[data-date="'+check_out_date+'"]')
        check_out_element.click()
    
    def number_of_occupants(self,adults):
        occupancy_button = self.find_element(By.CSS_SELECTOR,'button[data-testid="occupancy-config"]')
        occupancy_button.click()

        adult_division = self.find_element(By.XPATH,'//div[input[@id="group_adults"]]')        
        decrease_adults = adult_division.find_element(By.CLASS_NAME,"e91c91fa93")

        while True:

            decrease_adults.click()
            adult_input=self.find_element(By.CSS_SELECTOR,'input[id="group_adults"]')

            current_adults=adult_input.get_attribute('value')

            if int(current_adults)==1:
                break
            
        increase_adults=adult_division.find_element(By.CLASS_NAME,"f4d78af12a")

        for _ in range(adults-1):
            increase_adults.click()

    def click_search(self):
        search_button = self.find_element(By.CSS_SELECTOR,'button[type="submit"]')
        search_button.click()
        time.sleep(1)
    
    def apply_filters(self):
        filter=BookingFilter(driver=self)
        self.implicitly_wait(5)
        close_popup(self)
        filter.apply_star_rating(3,4,5)
        close_popup(self)
        filter.sort_bt_price()

    def report_results(self):
        hotel_boxes_section = self.find_element(By.CLASS_NAME,'d4924c9e74')
        report=BookingReport(hotel_boxes_section)

        table=PrettyTable(field_names=['Hotel Name','Price','Rating'])
        table.add_rows(report.pull_hotel_data())

        print(table)