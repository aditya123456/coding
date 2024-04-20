import functools


def log_request(func):
    def wrapper(*args):
        method = args[0]
        print(method)
        print("HTTP request+"+method)
        result = func()
        print("HTTP request+")
        return result
    return wrapper

@log_request
def request_logger():
    print("request logged successfully")
    return "returned"

request_logger("GET")
