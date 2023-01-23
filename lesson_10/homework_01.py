
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

result = 0
current = 1
s = int(input("Введите число: "))
q = s
m = int(input("Введите число: "))
while current <= m:
    result += s
    s = s * 10 + q
    current += 1
logger.info(result)


