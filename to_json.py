from functools import wraps
import json

def to_json(func):
    @wraps
    def wrapper(func):
        r = func()
        return json.dumps(r)
    return wrapper(func)


@to_json
def get_data():
    return {'data': 42}

get_data() # вернёт '{"data": 42}'