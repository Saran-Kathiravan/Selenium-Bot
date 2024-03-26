from selenium.webdriver.common.by import By

def close_popup(self):
        try:
            no_button = self.find_element(By.CSS_SELECTOR,'button[aria-label="Dismiss sign-in info."]')
            no_button.click()
        except:
            # print('No element with this class name. Skipping ....')
                pass