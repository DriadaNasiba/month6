from django.core.cache import cache
import random

CONFIRMATION_CODE_PREFIX = "confirm_code_"

def generate_code(user_id):

    code = str(random.randint(100000, 999999))  # 6-значный код
    cache_key = f"{CONFIRMATION_CODE_PREFIX}{user_id}"
    cache.set(cache_key, code, timeout=300)  # 5 минут
    return code

def get_code(user_id):
    return cache.get(f"{CONFIRMATION_CODE_PREFIX}{user_id}")

def delete_code(user_id):
    cache.delete(f"{CONFIRMATION_CODE_PREFIX}{user_id}")

def verify_code(user_id, code):
    real_code = get_code(user_id)
    if real_code and real_code == code:
        delete_code(user_id)  # удалить после использования
        return True
    return False
