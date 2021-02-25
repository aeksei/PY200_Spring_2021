"""
    1. Реализовать класс JsonFileDriver, который будет описывать логику считывания (записи) элементов из (в) json файл.
    2. Реализовать класс SimpleFileDriver, который будет описывать логику считывания (записи) элементов из (в) файл.
    3. В блоке __main__ протестировать работу драйверов
"""

from typing import Sequence
from abc import ABC, abstractmethod
import json
import csv
import random


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
    def __init__(self, json_filename):
        self.json_filename = json_filename

    def read(self) -> Sequence:
        with open(self.json_filename) as fp:
            return json.load(fp)

    def write(self, data: Sequence, indent=4) -> None:
        with open(self.json_filename, 'w') as fp:
            data = [value for value in data]
            json.dump(data, fp, indent=indent)


class SimpleFileDriver(IStructureDriver):
    def __init__(self, filename):
        self.filename = filename

    def read(self) -> Sequence:
        with open(self.filename) as fp:
            return [int(value) for value in fp]

    def write(self, data: Sequence) -> None:
        with open(self.filename, 'w') as fp:
            for value in data:
                fp.write(str(value) + '\n')


class CSVFileDriver(IStructureDriver):
    def __init__(self, filename):
        self.filename = filename

    def read(self) -> Sequence:
        with open(self.filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = [value for value in reader][0]
            return [int(value) for value in data]

    def write(self, data: Sequence) -> None:
        with open(self.filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([value for value in data])


if __name__ == '__main__':
    driver_json = JsonFileDriver('tmp.json')
    driver_txt = SimpleFileDriver('tmp.txt')
    driver_csv = CSVFileDriver('tmp.csv')
    d = [random.randint(-10, 10) for i in range(10)]
    driver_csv.write(d)
    driver_json.write(d)
    driver_txt.write(d)
    output_csv = driver_csv.read()
    output_json = driver_json.read()
    output_txt = driver_txt.read()
    print(output_csv)
    print(output_json)
    print(output_txt)

    assert d == output_csv and output_json and output_txt
