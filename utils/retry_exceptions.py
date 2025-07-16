import time
from functools import wraps
from services.app_logger import get_logger

logger = get_logger(__name__)

def retry(max_retries=10, delay=3, exception_types=(Exception,)):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except exception_types as e:
                    logger.warning(f'Retry Error: {e}, retrying in {delay} seconds...')
                    time.sleep(delay)
                    retries += 1

            raise Exception(f'Max retries reached ({max_retries}). Could not execute {func.__name__}.')

        return wrapper

    return decorator
