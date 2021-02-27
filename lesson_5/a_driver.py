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
import yaml
import pickle


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

    def write(self, data: Sequence) -> None:
        with open(self.json_filename, 'w') as fp:
            data = [value for value in data]
            json.dump(data, fp, indent=4)


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
    def __init__(self, csv_filename):
        self.csv_filename = csv_filename

    def read(self) -> Sequence:
        with open(self.csv_filename, newline='') as fp:
            reader = csv.reader(fp)
            return [int(', '.join(row)) for row in reader]

    def write(self, data: Sequence) -> None:
        with open(self.csv_filename, 'w', newline='') as fp:
            writer = csv.writer(fp, delimiter='\n')
            writer.writerows([data])


class YamlFileDriver(IStructureDriver):
    def __init__(self, yaml_filename):
        self.yaml_filename = yaml_filename

    def read(self) -> Sequence:
        with open(self.yaml_filename) as fp:
            return yaml.load(fp, Loader=yaml.FullLoader)

    def write(self, data: Sequence) -> None:
        with open(self.yaml_filename, 'w') as fp:
            yaml.dump(data, fp)


class PickleFileDriver(IStructureDriver):
    def __init__(self, pickle_filename):
        self.pickle_filename = pickle_filename

    def read(self) -> Sequence:
        with open(self.pickle_filename, 'rb') as fp:
            return pickle.load(fp)

    def write(self, data: Sequence) -> None:
        with open(self.pickle_filename, 'wb') as fp:
            pickle.dump(data, fp, pickle.DEFAULT_PROTOCOL)


if __name__ == '__main__':
    # driver_json = JsonFileDriver('tmp.json')
    # driver_txt = SimpleFileDriver('tmp.txt')
    # driver_csv = CSVFileDriver('tmp.csv')
    # driver_yaml = YamlFileDriver('tmp.yaml')
    driver_pickle = PickleFileDriver('tmp.pickle')
    d = [random.randint(-10, 10) for i in range(10)]
    print(d)
    # driver_pickle.write(d)
    # driver_csv.write(d)
    # crazy_dict = dict({'string': None, 'int': 2, 555: True})
    # driver_json.write(crazy_dict)
    driver_pickle.write(d)
    # driver_txt.write(d)
    # driver_yaml.write(d)
    # output_csv = driver_csv.read()
    # output_json = driver_json.read()
    # output_txt = driver_txt.read()
    # output_yaml = driver_yaml.read()
    output_pickle = driver_pickle.read()
    # driver_csv.write(output_txt)
    # driver_json.write(output_txt)
    # driver_yaml.write(output_json)
    # print(output_csv)
    # print(output_json)
    # print(output_txt)
    # print(output_yaml)
    print(output_pickle)

    # assert d == output_csv and output_json and output_txt
