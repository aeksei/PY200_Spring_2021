"""
    1. Реализовать класс JsonFileDriver, который будет описывать логику считывания (записи) элементов из (в) json файл.
    2. Реализовать класс SimpleFileDriver, который будет описывать логику считывания (записи) элементов из (в) файл.
    3. В блоке __main__ протестировать работу драйверов
"""

from typing import Sequence
from abc import ABC, abstractmethod
import json


class IStructureDriver(ABC):
    @abstractmethod
    def read(self) -> Sequence:
        """
        Считывает информацию из драйвера и возвращает её для объекта, использующего этот драйвер

        :return Последовательность элементов, считанная драйвером, для объекта
        """
        pass

    @abstractmethod
    def write(self, data: Sequence) -> None:
        """
        Получает информацию из объекта, использующего этот драйвер, и записывает её в драйвер

        :param data Последовательность элементов, полученная от объекта, для записи драйвером
        """
        pass


class JsonFileDriver(IStructureDriver):
    def __init__(self, filename):
        self.filename = filename

    def read(self) -> Sequence:
        with open(self.filename) as fp:
            return json.load(fp)

    def write(self, data: Sequence, indent=4) -> None:
        with open(self.filename, 'w') as fp:
            json.dump(data, fp, indent=indent)


class SimpleFileDriver(IStructureDriver):
    ...


if __name__ == '__main__':
    driver = JsonFileDriver('tmp.json')
    d = [1, 2, 3, 4, 5]
    driver.write(d)
    output = driver.read()

    assert d == output
