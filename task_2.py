# TODO решите задачу

import os
import json

FILENAME = 'input.json'


def task() -> float:
    with open(FILENAME) as f:
        data = json.load(f)

        result = sum([dict_['score'] * dict_['weight'] for dict_ in data])
        return round(result, 3)


print(task())
