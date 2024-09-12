# api_rate_limiter.py
import time
from functools import wraps

def rate_limiter(max_calls, period):
    def decorator(func):
        calls = []
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal calls
            now = time.time()
            calls = [call for call in calls if now - call < period]
            if len(calls) >= max_calls:
                wait_time = period - (now - calls[0])
                print(f"Rate limit exceeded. Waiting for {wait_time:.2f} seconds.")
                time.sleep(wait_time)
            calls.append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limiter(max_calls=5, period=10)
def api_call():
    print("API call made")

if __name__ == "__main__":
    for _ in range(10):
        api_call()
        time.sleep(1)
