# Program that generates the report from the filtered data

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from booking.popup_closer import close_popup

class BookingReport:
    def __init__(self,box_section_element:WebElement):
        self.box_section_element = box_section_element
        self.deal_boxes=self.pull_deal_boxes()
        # print(len(self.deal_boxes))

    def pull_deal_boxes(self):
        return self.box_section_element.find_elements(By.CSS_SELECTOR,'div[data-testid="property-card"]')
    
    def pull_hotel_data(self):
        collection=[]

        for deal_box in self.deal_boxes:
            # Pull Hotel Name
            hotel=deal_box.find_element(By.CSS_SELECTOR,'div[data-testid="title"]')
            hotel_name=hotel.text
            # print(hotel_name)

            #Pull Hotel Price
            hotel_cost=deal_box.find_element(By.CSS_SELECTOR,'span[data-testid="price-and-discounted-price"]')
            hotel_price=hotel_cost.text

            #Pull Hotel Score
            try:
                hotel_mark=deal_box.find_element(By.CSS_SELECTOR,'div[class="a3b8729ab1 d86cee9b25"]')
                word=(hotel_mark.text).split('\n')
                hotel_rating=word[0]
            except NoSuchElementException:
                hotel_rating=None

            collection.append([hotel_name,hotel_price,hotel_rating])
            close_popup(self)
        
        return collection
            