# Реализовать функцию которая возвращает дату недельной давности от текущего момента времени.
from datetime import datetime, timedelta


def week_ago():
    now = datetime.now()
    return now - timedelta(days=7)


print(f"The crime was done on {week_ago().strftime("%d.%m.%Y")} at {week_ago().strftime("%H:%M:%S")}")
