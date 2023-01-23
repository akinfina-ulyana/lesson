"""
Создать генератор и/или итератор простой геометрической прогрессии
"""
from time import sleep
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def regular_generator():
    i = 2
    count = 0
    while count <= 5:
       i = i * 2
       sleep(1)
       count += 1
       yield i

my_gen = regular_generator()
while True:
   try:
       print(next(my_gen))
   except StopIteration:
       break


print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))

