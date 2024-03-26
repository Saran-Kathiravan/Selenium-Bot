from booking.booking import Booking
import time
from booking.popup_closer import close_popup

currency="INR"
# destination="Chennai"
# adults=5

# check_in_date='2024-04-05'
# check_out_date='2024-04-20'

with Booking() as bot:
    bot.land_first_page()
    time.sleep(2)
    inr=bot.check_currency(currency)
    if not inr:
        bot.change_currency(currency)
    close_popup(bot)
    bot.select_destination(input("Please enter your destination:\n"))
    close_popup(bot)
    bot.check_availability()
    bot.select_dates(input("Enter check in date in yyyy-mm-dd format\n"),input("Enter check out date in yyyy-mm-dd format\n"))
    close_popup(bot)    
    bot.number_of_occupants(int(input("Enter number of adults:\n")))
    bot.click_search()
    close_popup(bot)
    bot.apply_filters()
    bot.report_results()

    