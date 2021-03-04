"""
Реализовать паттерн "Адаптер".

    1. Для NumpyAdapter и DictAdapter реализовать метод index, который будет производить поиск поиск элемента.
"""

from typing import Any, Union

import numpy as np


class ServerClass:
    """
    Код на стороне сервера менять не можем.
    Сервер выполняет вычисления очень быстро, поэтому все операции делаем на нем.
    """

    @staticmethod
    def find(data: Union[list, 'NumpyAdapter', dict], value: Any) -> int:
        """
        Сервер умеет вызывать только один метод index у объекта.

        :param data: Объект, в котором производится поиск
        :param value: Значение, индекс которого необходимо найти
        :return: Индекс искомого элемента

        :raise ValueError: f"{value} is not in {object_class_name}"
        """
        return data.index(value)


class NumpyAdapter:
    def __init__(self, np_array: np.ndarray):
        self.np_array = np_array

    def index(self, value: Any) -> int:
        """Делаем для numpy массива возможность работы с методом index"""
        for i, np_value in enumerate(self.np_array):
            if np_value == value:
                return i


class DictAdapter(dict):
    def __init__(self, dict_: dict):
        super().__init__()
        self.dict_ = dict_

    def index(self, value: Any) -> int:
        for key in self.dict_:
            if self.dict_[key] == value:
                return key


if __name__ == '__main__':
    server = ServerClass()

    list_ = [0, 1, 2, 3]
    print(server.find(list_, 1))

    numpy_adapter = NumpyAdapter(np.array(list_))
    print(server.find(numpy_adapter, 1))

    dict_adapter = DictAdapter({i: i for i in list_})
    print(dict_adapter)
    print(server.find(dict_adapter, 1))
