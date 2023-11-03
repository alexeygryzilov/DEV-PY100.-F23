# TODO написать функцию remove

from typing import Any


def remove(list_: list, item: Any) -> list:
    try:
        index = max(i[0] for i in enumerate(list_) if i[1] == item)
    except ValueError:
        return "Такого элемента в списке нет"
    else:
        if index < len(list_):
            return list_[:index] + list_[index + 1:]
        elif index == len(list_):
            return list_[:index]


print(remove([0, 1, 2, 0, 1, 2],

             0))  # [0, 1, 2, 1, 2]
print(remove([0, 1, 2], 0))  # [1, 2]
print(remove([0, 1, 2, 3, 4], 4))  # [0, 1, 2, 3]
