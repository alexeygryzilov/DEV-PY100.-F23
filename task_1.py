# TODO импортировать необходимые молули
import os
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as csv_file:
        data = csv.DictReader(csv_file)
        py_file = [row for row in data]

    with open(OUTPUT_FILENAME, 'w') as json_file:
        result = json.dump(py_file, json_file, indent=4)

    return result


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
