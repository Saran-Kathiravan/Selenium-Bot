from booking.booking import Booking
import time

currency="INR"
destination="Chennai"

with Booking() as bot:
    bot.land_first_page()
    bot.close_popup()
    time.sleep(2)
    inr=bot.check_currency(currency)
    if not inr:
        bot.change_currency(currency)
    bot.select_destination(destination)
    