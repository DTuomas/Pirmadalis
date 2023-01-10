import random
import math
skaicius = random.randint(1000, 9999)
print (skaicius, math.sqrt(skaicius))

from datetime import date
import calendar

print(calendar.isleap(skaicius))
print(f'siandien: {date.today()}')