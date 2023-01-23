
import re
import logging


logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

if __name__ == "__main__":

    test_string = "+375 (29) 299-00-00"
    match = re.search(r"^\+\d{1,3}\s\(\d{2}\)\s\d{3}\-\d{2}\-\d{2}$", test_string)

    if match:
        logger.info(f"Found {match.group()}")
    else:
        logger.info("Didn't not found")
