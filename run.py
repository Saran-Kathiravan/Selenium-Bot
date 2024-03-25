from booking.booking import Booking
import time

currency="INR"
destination="Chennai"
adults=5

check_in_date='2024-04-05'
check_out_date='2024-04-20'

with Booking() as bot:
    bot.land_first_page()
    bot.close_popup()
    time.sleep(2)
    inr=bot.check_currency(currency)
    if not inr:
        bot.change_currency(currency)
    bot.select_destination(destination)
    bot.select_dates(check_in_date,check_out_date)
    bot.number_of_occupants(adults)
    bot.click_search()

    