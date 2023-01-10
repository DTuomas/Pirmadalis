import logging
from datetime import date

siandien = date.today()

logging.basicConfig(
    level=logging.DEBUG, 
    filename=f'logs/debug_dalyba_{siandien.strftime("%Y%m%d")}.log',
    format="%(asctime)s:%(levelname)s:%(name)s:%(message)s",
)

def dalyba(a, b):
    padalinom = a / b
   # print(f"{a} / {b} = {padalinom}")
    logging.debug(f'vykdant funkcija {dalyba.__name__} buvo {a} padalinta is {b} ir gauta {padalinom}')
    return padalinom 

print(dalyba(11, 5))
print(dalyba(17, 5))
print(dalyba(11, 3))