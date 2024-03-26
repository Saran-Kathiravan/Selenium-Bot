from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from booking.popup_closer import close_popup
import time


class BookingFilter:

    def __init__(self,driver:WebDriver):
        self.driver=driver

    def apply_star_rating(self,*star_value):    

        star_filration_box=self.driver.find_element(By.XPATH, '//div[div/h3[text()="Property rating"]]')
        star_elements=star_filration_box.find_elements(By.CSS_SELECTOR,'[data-filters-item]')

        for star in star_value: 
            for star_element in star_elements:
                if str(star_element.get_attribute('data-filters-item')) == str(f'class:class={star}'):
                    # print(star)
                    star_element.click()
                    close_popup(self)

    def sort_bt_price(self):
        time.sleep(2)
        sort_by=self.driver.find_element(By.CSS_SELECTOR,'button[data-testid="sorters-dropdown-trigger"]')
        sort_by.click()
        lower_price=self.driver.find_element(By.CSS_SELECTOR,'button[data-id="price"]')
        lower_price.click()